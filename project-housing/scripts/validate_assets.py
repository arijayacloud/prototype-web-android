"""Lightweight consistency checks for the housing concept deliverables."""

import argparse
import json
import sys
from pathlib import Path
from zipfile import BadZipFile, ZipFile
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]


def validate_plans():
    errors = []
    data_path = ROOT / "plan_data.json"
    if not data_path.is_file():
        return ["Missing plan_data.json"]
    data = json.loads(data_path.read_text(encoding="utf-8"))
    width, depth = data["footprint_m"]["width"], data["footprint_m"]["depth"]
    for floor in data["floors"]:
        for room in floor["rooms"]:
            x, y, w, h = room["bounds_m"]
            if min(x, y, w, h) < 0 or x+w > width+1e-6 or y+h > depth+1e-6:
                errors.append(f"{floor['name']}: {room['name']} is outside the {width} × {depth} m footprint")
        path = ROOT / "assets" / f"floor-{floor['number']}.svg"
        if not path.is_file():
            errors.append(f"Missing {path.relative_to(ROOT)}")
        else:
            try:
                ElementTree.parse(path)
            except ElementTree.ParseError as exc:
                errors.append(f"Malformed {path.name}: {exc}")
            else:
                print(f"OK {path.relative_to(ROOT)} — parseable SVG")
    return errors


def validate_model():
    errors = []
    assets = ROOT / "assets"
    for name in ("house.blend",):
        path = assets / name
        magic = path.read_bytes()[:7] if path.is_file() else b""
        if not path.is_file() or not (magic.startswith(b"BLENDER") or magic.startswith(bytes.fromhex("28 b5 2f fd"))):
            errors.append(f"Missing or invalid Blender project: {path.relative_to(ROOT)}")
        else:
            print(f"OK {path.relative_to(ROOT)} — Blender project")
    for name in ("house.glb", "floor-1.glb", "floor-2.glb"):
        path = assets / name
        if not path.is_file():
            errors.append(f"Missing {path.relative_to(ROOT)}")
        else:
            header = path.read_bytes()[:12]
            if len(header) < 12 or header[:4] != b"glTF" or int.from_bytes(header[4:8], "little") != 2:
                errors.append(f"Invalid GLB header/version: {path.relative_to(ROOT)}")
            else:
                print(f"OK {path.relative_to(ROOT)} — GLB 2.0")
    for name in ("full-house.png", "floor-1.png", "floor-2.png"):
        path = assets / "renders" / name
        if not path.is_file() or not path.read_bytes().startswith(b"\x89PNG\r\n\x1a\n"):
            errors.append(f"Missing or invalid render: {path.relative_to(ROOT)}")
        else:
            print(f"OK {path.relative_to(ROOT)} — PNG render")
    return errors


def validate_web():
    path = ROOT / "index.html"
    if not path.is_file():
        return ["Missing index.html"]
    html = path.read_text(encoding="utf-8")
    required = ("mode-full", "mode-floor-1", "mode-floor-2", "GLTFLoader", "OrbitControls", "scene-wrap")
    errors = [f"index.html is missing expected viewer feature: {item}" for item in required if item not in html]
    if errors:
        return errors
    print("OK index.html — three presentation modes and WebGL viewer controls")
    return []


def validate_deck():
    path = ROOT / "output" / "presentasi-rumah-8x18.pptx"
    if not path.is_file():
        return ["Missing output/presentasi-rumah-8x18.pptx"]
    try:
        with ZipFile(path) as archive:
            slides = [n for n in archive.namelist() if n.startswith("ppt/slides/slide") and n.endswith(".xml")]
            if not (archive.testzip() is None):
                return ["PPTX archive integrity check failed"]
    except BadZipFile:
        return ["PPTX file is not a valid OOXML ZIP package"]
    if len(slides) != 6:
        return [f"Expected 6 slides, found {len(slides)}"]
    print(f"OK {path.relative_to(ROOT)} — valid OOXML presentation with {len(slides)} slides")
    return []


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--plans", action="store_true", help="validate floor plan data and SVGs")
    parser.add_argument("--model", action="store_true", help="validate Blender project, GLBs, and renders")
    parser.add_argument("--web", action="store_true", help="validate the interactive HTML viewer")
    parser.add_argument("--deck", action="store_true", help="validate the finished PPTX package")
    parser.add_argument("--all", action="store_true", help="validate every deliverable")
    args = parser.parse_args()
    run_all = args.all
    errors = []
    if args.plans or run_all:
        errors += validate_plans()
    if args.model or run_all:
        errors += validate_model()
    if args.web or run_all:
        errors += validate_web()
    if args.deck or run_all:
        errors += validate_deck()
    if not (args.plans or args.model or args.web or args.deck or run_all):
        errors.append("Choose a validation target, e.g. --plans or --all")
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Plan source and SVG checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Generate clean, presentation-ready SVG floor plans from plan_data.json."""

import json
from pathlib import Path
from xml.etree.ElementTree import Element, SubElement, register_namespace, tostring

ROOT = Path(__file__).resolve().parents[1]
SVG = "http://www.w3.org/2000/svg"
register_namespace("", SVG)
COLORS = ["#e7ddd0", "#dfe9e4", "#ece5d8", "#e4e1ed", "#dce7ed", "#efe1da"]


def el(parent, tag, attrs=None, text=None):
    node = SubElement(parent, f"{{{SVG}}}{tag}", attrs or {})
    if text is not None:
        node.text = str(text)
    return node


def draw_door(root, data, room, scale, left, top):
    x, y, w, h = room["bounds_m"]
    px, py, pw, ph = left+x*scale, top+y*scale, w*scale, h*scale
    size = data["width_m"]*scale
    offset = data["offset_m"]*scale
    wall = data["wall"]
    stroke = {"stroke":"#f7f4ed","stroke-width":"8","fill":"none","stroke-linecap":"square"}
    line = {"stroke":"#a46a4f","stroke-width":"3","fill":"none","stroke-linecap":"round"}
    arc = {"stroke":"#a46a4f","stroke-width":"2","fill":"none","stroke-dasharray":"5 4"}
    if wall == "front":
        hx, hy = px+offset, py
        ex, ey = hx, hy+size
        arc_start, arc_end = (hx+size,hy),(hx,hy+size)
        gap_a, gap_b = (hx, py), (hx+size, py)
    elif wall == "rear":
        hx, hy = px+offset, py+ph
        ex, ey = hx, hy-size
        arc_start, arc_end = (hx+size,hy),(hx,hy-size)
        gap_a, gap_b = (hx, py+ph), (hx+size, py+ph)
    elif wall == "left":
        hx, hy = px, py+offset
        ex, ey = hx+size, hy
        arc_start, arc_end = (hx,hy+size),(hx+size,hy)
        gap_a, gap_b = (px, hy), (px, hy+size)
    else:
        hx, hy = px+pw, py+offset
        ex, ey = hx-size, hy
        arc_start, arc_end = (hx,hy+size),(hx-size,hy)
        gap_a, gap_b = (px+pw, hy), (px+pw, hy+size)
    el(root, "line", {**stroke,"x1":f"{gap_a[0]:.1f}","y1":f"{gap_a[1]:.1f}","x2":f"{gap_b[0]:.1f}","y2":f"{gap_b[1]:.1f}"})
    el(root, "line", {**line,"x1":f"{hx:.1f}","y1":f"{hy:.1f}","x2":f"{ex:.1f}","y2":f"{ey:.1f}"})
    sweep = "1" if wall in ("front","right") else "0"
    el(root,"path",{**arc,"d":f"M {arc_start[0]:.1f} {arc_start[1]:.1f} A {size:.1f} {size:.1f} 0 0 {sweep} {arc_end[0]:.1f} {arc_end[1]:.1f}"})


def draw_stair_symbol(root, room, scale, left, top, direction):
    x,y,w,h=room["bounds_m"]
    px,py,pw,ph=left+x*scale,top+y*scale,w*scale,h*scale
    # Treads are drawn across the shorter axis so the flight reads as a staircase.
    if ph >= pw:
        for i in range(1,9):
            yy=py+ph*(.27+i*.075)
            el(root,"line",{"x1":f"{px+pw*.18:.1f}","y1":f"{yy:.1f}","x2":f"{px+pw*.82:.1f}","y2":f"{yy:.1f}","stroke":"#92775f","stroke-width":"2"})
        label="NAIK ↑" if direction.startswith("naik") else "TURUN ↓"
        el(root,"text",{"x":f"{px+pw/2:.1f}","y":f"{py+ph*.2:.1f}","text-anchor":"middle","font-family":"Arial,sans-serif","font-size":"14","font-weight":"700","fill":"#92775f"},label)
    else:
        for i in range(1,8):
            xx=px+pw*i/8
            el(root,"line",{"x1":f"{xx:.1f}","y1":f"{py+ph*.18:.1f}","x2":f"{xx:.1f}","y2":f"{py+ph*.82:.1f}","stroke":"#92775f","stroke-width":"2"})


def draw_fixture_symbol(root, room, scale, left, top):
    x,y,w,h=room["bounds_m"]
    px,py,pw,ph=left+x*scale,top+y*scale,w*scale,h*scale
    fixtures=" ".join(room.get("fixtures",[])).lower()
    ink="#89725c"
    if "ranjang" in fixtures or "bed" in fixtures:
        fw,fh=min(pw*.48,1.3*scale),min(ph*.36,1.45*scale)
        fx,fy=px+8,py+ph-fh-8
        el(root,"rect",{"x":f"{fx:.1f}","y":f"{fy:.1f}","width":f"{fw:.1f}","height":f"{fh:.1f}","rx":"5","fill":"#f5f0e6","stroke":ink,"stroke-width":"2"})
        el(root,"line",{"x1":f"{fx+fw*.12:.1f}","y1":f"{fy+fh*.23:.1f}","x2":f"{fx+fw*.88:.1f}","y2":f"{fy+fh*.23:.1f}","stroke":ink,"stroke-width":"2"})
        el(root,"rect",{"x":f"{fx+fw*.13:.1f}","y":f"{fy+fh*.04:.1f}","width":f"{fw*.3:.1f}","height":f"{fh*.15:.1f}","rx":"3","fill":"#e1e7e0","stroke":ink,"stroke-width":"1"})
        if "tingkat" in fixtures:
            el(root,"line",{"x1":f"{fx+fw*.08:.1f}","y1":f"{fy+fh*.51:.1f}","x2":f"{fx+fw*.92:.1f}","y2":f"{fy+fh*.51:.1f}","stroke":"#ae674b","stroke-width":"3"})
    elif "sofa" in fixtures:
        fw,fh=min(pw*.55,1.8*scale),min(ph*.2,.65*scale)
        el(root,"rect",{"x":f"{px+8:.1f}","y":f"{py+8:.1f}","width":f"{fw:.1f}","height":f"{fh:.1f}","rx":"5","fill":"#e1e7e0","stroke":ink,"stroke-width":"2"})
        el(root,"line",{"x1":f"{px+8:.1f}","y1":f"{py+fh*.62+8:.1f}","x2":f"{px+fw+8:.1f}","y2":f"{py+fh*.62+8:.1f}","stroke":ink,"stroke-width":"2"})
    elif any(k in fixtures for k in ("meja makan","meja kerja","counter","sink")):
        fw,fh=min(pw*.48,1.5*scale),min(ph*.22,.8*scale)
        el(root,"rect",{"x":f"{px+8:.1f}","y":f"{py+8:.1f}","width":f"{fw:.1f}","height":f"{fh:.1f}","rx":"3","fill":"#ede4d7","stroke":ink,"stroke-width":"2"})
        if "kerja" in fixtures:
            el(root,"circle",{"cx":f"{px+fw*.5+8:.1f}","cy":f"{py+fh+22:.1f}","r":"7","fill":"#e1e7e0","stroke":ink,"stroke-width":"2"})
    elif "toilet" in fixtures:
        el(root,"circle",{"cx":f"{px+pw*.78:.1f}","cy":f"{py+ph*.78:.1f}","r":"12","fill":"#e1e7e0","stroke":ink,"stroke-width":"2"})


def build_floor_svg(data, floor):
    width, depth = data["footprint_m"]["width"], data["footprint_m"]["depth"]
    scale, left, top = 82, 146, 192
    plan_w, plan_h = width * scale, depth * scale
    canvas_w, canvas_h = 1110, 1880
    root = Element(f"{{{SVG}}}svg", {"viewBox": f"0 0 {canvas_w} {canvas_h}", "width": str(canvas_w), "height": str(canvas_h)})
    el(root, "rect", {"width": str(canvas_w), "height": str(canvas_h), "fill": "#f7f4ed"})
    el(root, "text", {"x":"76","y":"81","font-family":"Arial,sans-serif","font-size":"25","letter-spacing":"4","fill":"#6c786d"}, "DESAIN ELEGAN  /  RUMAH KEKINIAN")
    el(root, "text", {"x":"76","y":"124","font-family":"Arial,sans-serif","font-size":"44","font-weight":"700","fill":"#26312d"}, floor["name"])
    el(root, "text", {"x":"76","y":"153","font-family":"Arial,sans-serif","font-size":"19","fill":"#68736c"}, floor["subtitle"])

    # Plan backdrop and room fills.
    el(root, "rect", {"x":str(left),"y":str(top),"width":str(plan_w),"height":str(plan_h),"fill":"#fffdf9","stroke":"#28312d","stroke-width":"10"})
    rooms = floor["rooms"]
    room_by_id={room["id"]:room for room in rooms}
    for i, room in enumerate(rooms):
        x, y, w, h = room["bounds_m"]
        px, py, pw, ph = left + x*scale, top + y*scale, w*scale, h*scale
        el(root, "rect", {"x":f"{px:.1f}","y":f"{py:.1f}","width":f"{pw:.1f}","height":f"{ph:.1f}","fill":COLORS[i%len(COLORS)],"fill-opacity":"0.68","stroke":"#46514b","stroke-width":"3"})
        draw_fixture_symbol(root,room,scale,left,top)
        # Room title uses two lines where needed; keep text centered and wrap to room bounds.
        words = room["name"].split()
        lines, line = [], ""
        max_chars = max(10, int(pw/14))
        for word in words:
            if line and len(line)+len(word)+1 > max_chars:
                lines.append(line); line = word
            else:
                line = (line + " " + word).strip()
        if line: lines.append(line)
        font = 16 if pw < 190 or ph < 155 else 18
        is_stairs=room["id"]==floor.get("stairs",{}).get("room_id")
        if is_stairs:
            lines=["Tangga"]
        start_y = (py + ph*.18) if is_stairs else py + ph/2 - ((len(lines)-1)*font*0.62)
        for j, label in enumerate(lines):
            el(root, "text", {"x":f"{px+pw/2:.1f}","y":f"{start_y+j*font*1.25:.1f}","text-anchor":"middle","font-family":"Arial,sans-serif","font-size":str(font),"font-weight":"700","fill":"#26312d"}, label)
        # Simple furniture cues, intentionally diagrammatic.
        furniture = room.get("fixtures", [])
        if furniture and "tangga" not in " ".join(furniture).lower():
            label = " · ".join(furniture[:2])
            el(root, "text", {"x":f"{px+pw/2:.1f}","y":f"{py+ph/2+len(lines)*font*.75+13:.1f}","text-anchor":"middle","font-family":"Arial,sans-serif","font-size":"12","fill":"#58645c"}, label)

    # Windows as teal ticks on perimeter, represented as distance along each edge.
    for window in floor.get("windows", []):
        wall, a, b = window["wall"], window["from_m"], window["to_m"]
        if wall in ("front", "rear"):
            y = top if wall == "front" else top+plan_h
            x1, x2 = left+a*scale, left+b*scale
            el(root, "line", {"x1":f"{x1:.1f}","y1":f"{y:.1f}","x2":f"{x2:.1f}","y2":f"{y:.1f}","stroke":"#4d9291","stroke-width":"10"})
        else:
            x = left if wall == "left" else left+plan_w
            y1, y2 = top+a*scale, top+b*scale
            el(root, "line", {"x1":f"{x:.1f}","y1":f"{y1:.1f}","x2":f"{x:.1f}","y2":f"{y2:.1f}","stroke":"#4d9291","stroke-width":"10"})

    for door in floor.get("doors", []):
        if door["room_id"] in room_by_id:
            draw_door(root,door,room_by_id[door["room_id"]],scale,left,top)
    stair_id=floor.get("stairs",{}).get("room_id")
    if stair_id in room_by_id:
        draw_stair_symbol(root,room_by_id[stair_id],scale,left,top,floor["stairs"]["direction"])

    # Front direction and dimensions.
    el(root, "text", {"x":str(left+plan_w/2),"y":str(top-15),"text-anchor":"middle","font-family":"Arial,sans-serif","font-size":"17","font-weight":"700","fill":"#b87353"}, "DEPAN / AKSES")
    el(root, "line", {"x1":str(left),"y1":str(top-5),"x2":str(left+plan_w),"y2":str(top-5),"stroke":"#26312d","stroke-width":"2"})
    el(root, "text", {"x":str(left+plan_w/2),"y":str(top+plan_h+38),"text-anchor":"middle","font-family":"Arial,sans-serif","font-size":"19","fill":"#26312d"}, "8 m")
    el(root, "text", {"x":str(left-20),"y":str(top+plan_h/2),"text-anchor":"middle","font-family":"Arial,sans-serif","font-size":"19","fill":"#26312d","transform":f"rotate(-90 {left-20} {top+plan_h/2})"}, "18 m")
    # Compact legend and caveat.
    ly = top+plan_h+88
    el(root, "line", {"x1":"77","y1":str(ly),"x2":"125","y2":str(ly),"stroke":"#4d9291","stroke-width":"9"})
    el(root, "text", {"x":"139","y":str(ly+6),"font-family":"Arial,sans-serif","font-size":"15","fill":"#58645c"}, "Jendela")
    el(root, "rect", {"x":"253","y":str(ly-10),"width":"27","height":"20","fill":"#e7ddd0","stroke":"#46514b","stroke-width":"2"})
    el(root, "text", {"x":"292","y":str(ly+6),"font-family":"Arial,sans-serif","font-size":"15","fill":"#58645c"}, "Pembagian ruang konseptual")
    bar_x, bar_w=664,5*scale
    el(root,"rect",{"x":str(bar_x),"y":str(ly-5),"width":str(bar_w/2),"height":"10","fill":"#26312d"})
    el(root,"rect",{"x":str(bar_x+bar_w/2),"y":str(ly-5),"width":str(bar_w/2),"height":"10","fill":"#fffdf9","stroke":"#26312d","stroke-width":"2"})
    el(root,"text",{"x":str(bar_x),"y":str(ly-13),"font-family":"Arial,sans-serif","font-size":"13","fill":"#58645c"},"0")
    el(root,"text",{"x":str(bar_x+bar_w),"y":str(ly-13),"text-anchor":"end","font-family":"Arial,sans-serif","font-size":"13","fill":"#58645c"},"5 m")
    el(root, "text", {"x":"77","y":str(ly+48),"font-family":"Arial,sans-serif","font-size":"14","fill":"#68736c"}, "Ukuran dan bukaan perkiraan. Konfirmasi kembali dengan survei lokasi dan perencana bangunan.")
    return tostring(root, encoding="unicode")


def main():
    data = json.loads((ROOT / "plan_data.json").read_text(encoding="utf-8"))
    out = ROOT / "assets"
    out.mkdir(parents=True, exist_ok=True)
    for floor in data["floors"]:
        path = out / f"floor-{floor['number']}.svg"
        path.write_text(build_floor_svg(data, floor), encoding="utf-8")
        print(f"Wrote {path}")


if __name__ == "__main__":
    main()

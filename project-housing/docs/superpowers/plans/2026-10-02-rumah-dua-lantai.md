# Rumah Dua Lantai 8 × 18 m Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver a concept package for a two-storey 8 × 18 m house with two floor plans, three interactive 3D presentation modes, Blender source/assets, and an Indonesian PowerPoint deck.

**Architecture:** Define the room layout once in structured project data. Generate labeled SVG floor plans and build the corresponding house geometry in a Blender Python script, separating floor, furniture, and roof collections so the web viewer can show full-house, open-top floor 1, and floor 2 views. The HTML viewer and PowerPoint use the same plan and render assets; a README records the assumptions and rebuild steps.

**Tech Stack:** Blender Python API for editable geometry and GLB export when Blender is installed; HTML/CSS/JavaScript with Three.js for the local interactive viewer; SVG and PNG for plans; Python-PPTX for the PowerPoint file; Python standard-library checks for asset links and file signatures.

**Spec:** `project-housing/docs/superpowers/specs/2026-10-02-rumah-dua-lantai-design.md`

## Global Constraints

- Use an 8 m frontage × 18 m depth conceptual footprint.
- Treat the attached sketch as the floor 1 reference and the user's text list as floor 2 requirements.
- Provide three modes: full house with roof, floor 1 open above, and floor 2 only.
- Label dimensions as conceptual estimates; do not present output as construction drawings.
- Save final deliverables under `project-housing` and write the page and deck in Indonesian.
- Keep roof geometry in a separate Blender collection so the viewer can hide it.

## Review Focus

- Ambiguous handwriting in the source floor 1 sketch: keep uncertain room names qualified and do not invent precise dimensions.
- Camera and floor visibility after changing modes: validate each of the three modes independently.
- Browser loading of GLB assets from a local HTML file: prefer a bundled data URI or document a local-server fallback if direct file access is blocked.
- Missing Blender installation: retain a runnable Blender build script and clearly report whether `.blend`/`.glb` generation could run in this environment.
- PowerPoint rendering and text overflow: render every slide to images and inspect title, plan, and model-image slides before delivery.

---

### Task 1: Create plan data and 2D floor plans

**Files:**
- Create: `project-housing/plan_data.json`
- Create: `project-housing/assets/floor-1.svg`
- Create: `project-housing/assets/floor-2.svg`
- Create: `project-housing/scripts/generate_plans.py`
- Create: `project-housing/scripts/validate_assets.py`

**Interfaces:**
- `generate_plans.py` reads `plan_data.json` and writes both SVG plans to `assets/`.
- Footprint and room rectangles are in meters; front edge is the 8 m side; room IDs/names and bounds are shared with Blender and the viewer.
- `validate_assets.py` will later check these files along with the HTML, GLB, and deck.

- [x] **Step 1: Define room layouts and labels** in `plan_data.json` using meter-based rectangles, room names, floor number, door openings, stairs, and basic fixtures. Use the sketch for floor 1 and the approved floor 2 list; mark uncertain names and estimated areas as conceptual.
- [x] **Step 2: Draw both floor plans** in `generate_plans.py` with scale, front marker, labels, wall outlines, door swings, windows, stairs, furniture silhouettes, and a scale bar. Emit legible SVG at presentation aspect ratio.
- [x] **Step 3: Generate and inspect plans** with `python scripts/generate_plans.py`; rasterize SVGs to PNG. Inspect generated plans and confirm geometry fits the 8 × 18 m boundary.
- [x] **Step 4: Validate plan source** with `python scripts/validate_assets.py --plans`; both SVGs are present and parseable.
- [x] **Step 5: Commit** the plan data, generator, and SVG plans.

### Task 2: Build the editable Blender model and web model asset

**Files:**
- Create: `project-housing/blender/build_house.py`
- Create: `project-housing/assets/house.glb` (generated when Blender is available)
- Create: `project-housing/assets/house.blend` (generated when Blender is available)
- Create: `project-housing/assets/renders/full-house.png`
- Create: `project-housing/assets/renders/floor-1.png`
- Create: `project-housing/assets/renders/floor-2.png`

**Interfaces:**
- The Blender script reads `plan_data.json` and creates named collections `Floor_1`, `Floor_2`, `Roof`, and `Furniture`.
- Export `house.glb` with floor and roof collections identifiable by stable object names (`F1_*`, `F2_*`, `Roof_*`).
- Render three matching views for use in the deck and as viewer fallbacks.

- [x] **Step 1: Check Blender availability**. No local command-line Blender was found; connected Blender MCP reported Blender 5.2.2 LTS.
- [x] **Step 2: Implement scene construction** in `build_house.py` from the shared room rectangles, using slabs, room partitions, stairs, furniture, and a detachable pitched roof.
- [x] **Step 3: Add task-specific furniture**: upper-floor bunk bed, main bedroom bed and attached toilet fixtures, shared toilet fixtures, work desk and shoe cabinet, dining table, pantry counters, and balcony railings.
- [x] **Step 4: Save and export** through Blender MCP. The project contains `house.blend`, a full `house.glb`, separate floor GLB variants, and three renders.
- [x] **Step 5: Validate model outputs** with `python scripts/validate_assets.py --model`; GLB headers and Blender/render files were confirmed.
- [x] **Step 6: Commit** the Blender source and generated assets that were successfully created.

### Task 3: Build the interactive house presentation page

**Files:**
- Create: `project-housing/index.html`
- Modify: `project-housing/scripts/validate_assets.py`

**Interfaces:**
- `index.html` loads `plan_data.json`, `assets/house.glb`, both SVG plans, and the three renders.
- Provide controls with IDs `mode-full`, `mode-floor-1`, and `mode-floor-2`; switching mode toggles named GLB objects and camera framing without reloading.
- On model load failure, show the corresponding render and a readable error message; do not display an empty viewport.

- [x] **Step 1: Create page structure and responsive styling** with a header, mode selector, 3D viewport, floor-plan panel, room summary, and visible concept-drawing note.
- [x] **Step 2: Implement 3D viewer** with orbit, zoom, and pan controls, camera framing, soft lighting, neutral materials, and a ground grid.
- [x] **Step 3: Implement three view states** using the full-house GLB and separate floor GLBs; each mode loads the intended geometry and frames the camera.
- [x] **Step 4: Connect the SVG plans and room summary** and keep desktop and phone layouts usable.
- [x] **Step 5: Verify browser behavior** in a local server. All modes and model loading were confirmed without browser console errors. A local server is required for GLB loading.
- [x] **Step 6: Commit** the HTML viewer and validation updates.

### Task 4: Create the Indonesian PowerPoint deck

**Files:**
- Create: `project-housing/presentasi-rumah-8x18.pptx`
- Create: `project-housing/scripts/build_presentation.py`

**Interfaces:**
- The deck consumes floor plan SVG/PNG and model renders from Tasks 1–2; do not redraw a conflicting layout in the deck.
- Use a clean warm-neutral architectural palette, clear Indonesian labels, and 16:9 slide size.

- [x] **Step 1: Load presentation visual guidance** and choose a slide structure for a residential concept proposal.
- [x] **Step 2: Build a concise 6-slide deck** with cover, room program, each floor plan, three model views, and development notes.
- [x] **Step 3: Add source images and typography** with consistent margins, warm neutral colors, and conceptual-drawing notes.
- [x] **Step 4: Export and render every slide** using the presentation workspace; inspect all six slides for layout and text fit.
- [x] **Step 5: Validate PPTX package** with `python scripts/validate_assets.py --deck`; the final file is a valid 6-slide OOXML presentation.
- [x] **Step 6: Commit** the deck and its builder script.

### Task 5: Document assumptions and deliver the project

**Files:**
- Create: `project-housing/README.md`
- Modify: `project-housing/scripts/validate_assets.py`

**Interfaces:**
- README links directly to `index.html`, the PPTX, the plans, and Blender source/assets.
- Final validator checks all referenced local assets exist and reports optional Blender-generated outputs accurately.

- [x] **Step 1: Write README** with opening instructions, Blender rebuild notes, deck contents, three viewer modes, footprint orientation, and assumptions.
- [x] **Step 2: Run final validation** with `python scripts/validate_assets.py --all`; all deliverable checks passed.
- [x] **Step 3: Review final output folder** for the page, plans, Blender files, renders, PPTX, and README.
- [x] **Step 4: Commit** final documentation and validator changes.

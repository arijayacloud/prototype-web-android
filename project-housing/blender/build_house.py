"""Build a conceptual two-storey 8 × 18 m house in Blender.

Run inside Blender (or through the Blender MCP) with plan_data.json beside the
project. Room boxes are intentionally diagrammatic and are not construction data.
"""
import json
import math
from pathlib import Path

import bpy
from mathutils import Vector

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "plan_data.json").read_text(encoding="utf-8"))
W = DATA["footprint_m"]["width"]
D = DATA["footprint_m"]["depth"]
FLOOR_Z = {1: 0.0, 2: 3.15}
WALL_H = 2.75
WALL_T = 0.16


def material(name, color, roughness=0.7, metallic=0.0):
    mat = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    mat.diffuse_color = (*color, 1.0)
    mat.use_nodes = True
    shader = next(n for n in mat.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
    shader.inputs["Base Color"].default_value = (*color, 1.0)
    shader.inputs["Roughness"].default_value = roughness
    shader.inputs["Metallic"].default_value = metallic
    return mat


MATS = {
    "plaster": material("Warm ivory plaster", (0.79, 0.75, 0.66)),
    "floor": material("Sandstone floor", (0.67, 0.62, 0.53)),
    "wood": material("Natural oak", (0.39, 0.24, 0.13)),
    "wood_light": material("Light oak", (0.66, 0.48, 0.29)),
    "sage": material("Muted sage", (0.34, 0.48, 0.39)),
    "roof": material("Terracotta roof", (0.37, 0.18, 0.12)),
    "glass": material("Blue green glass", (0.31, 0.59, 0.62), 0.2, 0.15),
    "white": material("Warm white", (0.89, 0.86, 0.79)),
    "dark": material("Charcoal details", (0.13, 0.16, 0.15)),
    "tile": material("Bathroom tile", (0.57, 0.69, 0.66)),
    "garden": material("Garden ground", (0.29, 0.38, 0.30)),
}


def collection(name, parent=None):
    col = bpy.data.collections.new(name)
    (parent or bpy.context.scene.collection).children.link(col)
    return col


def move_to(obj, col):
    for old in list(obj.users_collection):
        old.objects.unlink(obj)
    col.objects.link(obj)
    return obj


def box(name, location, dimensions, mat, col, bevel=0.03):
    bpy.ops.mesh.primitive_cube_add(size=1, location=location)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = dimensions
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    move_to(obj, col)
    if mat:
        obj.data.materials.append(mat)
    if bevel:
        mod = obj.modifiers.new("Soft edges", "BEVEL")
        mod.width = min(bevel, min(dimensions) * 0.24)
        mod.segments = 2
        obj.modifiers.new("Weighted corner normals", "WEIGHTED_NORMAL")
    return obj


def cyl(name, location, radius, depth, mat, col, vertices=20):
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=depth, location=location)
    obj = bpy.context.object
    obj.name = name
    move_to(obj, col)
    if mat:
        obj.data.materials.append(mat)
    return obj


def room_center(bounds):
    x, y, w, h = bounds
    return x + w / 2, y + h / 2


def floor_y(y):
    return y - D / 2


def panel_wall(name, a, b, z, height, mat, col, thickness=WALL_T):
    # End points in plan coordinates (front-left origin); convert to Blender XY.
    x1, y1 = a[0], floor_y(a[1])
    x2, y2 = b[0], floor_y(b[1])
    dx, dy = x2 - x1, y2 - y1
    length = math.hypot(dx, dy)
    obj = box(name, ((x1+x2)/2, (y1+y2)/2, z+height/2), (length, thickness if abs(dx)>abs(dy) else thickness, height), mat, col)
    if abs(dy) > abs(dx):
        obj.dimensions = (thickness, length, height)
    obj.location.z = z + height/2
    return obj


def make_furniture(floor, room, col):
    x, y, w, h = room["bounds_m"]
    cx, cy = room_center(room["bounds_m"])
    z = FLOOR_Z[floor] + 0.12
    cyb = floor_y(cy)
    room_id = room["id"]
    fx = min(1.35, max(0.85, w * 0.42))
    fy = min(2.0, max(0.65, h * 0.42))
    fixtures = " ".join(room.get("fixtures", [])).lower()
    if "ranjang" in fixtures or "bed" in fixtures:
        # beds align along the depth axis; a second mattress forms the bunk.
        bed_x, bed_y = min(1.55, max(1.05, w*0.52)), min(2.0, max(1.45, h*0.62))
        bx, by = x + min(0.35, w*.12) + bed_x/2, floor_y(y + min(.55,h*.15) + bed_y/2)
        box(f"{room_id}_Bed_Base", (bx, by, z+.22), (bed_x, bed_y, .42), MATS["wood"], col)
        box(f"{room_id}_Mattress", (bx, by, z+.47), (bed_x-.08, bed_y-.08, .13), MATS["white"], col)
        box(f"{room_id}_Pillow", (bx, by+bed_y*.34, z+.57), (bed_x*.60, .42, .10), MATS["white"], col)
        if "tingkat" in fixtures:
            box(f"{room_id}_Bunk_Upper", (bx, by, z+1.65), (bed_x, bed_y, .16), MATS["wood"], col)
            box(f"{room_id}_Bunk_Mattress", (bx, by, z+1.78), (bed_x-.08, bed_y-.08, .12), MATS["white"], col)
            for px in (bx-bed_x*.44, bx+bed_x*.44):
                box(f"{room_id}_Bunk_Post", (px, by, z+1.0), (.07,.07,1.8), MATS["wood"], col, .015)
    if "meja" in fixtures or "counter" in fixtures or "kabinet" in fixtures:
        width = min(1.8, max(.75,w*.58))
        box(f"{room_id}_Cabinet", (cx, floor_y(y+.34), z+.42), (width,.55,.84), MATS["wood_light"], col)
        box(f"{room_id}_Top", (cx, floor_y(y+.34), z+.88), (width+.04,.60,.08), MATS["dark"] if "kerja" in fixtures else MATS["white"], col)
        if "kerja" in fixtures:
            box(f"{room_id}_ChairSeat", (cx, floor_y(y+1.08), z+.50), (.48,.46,.12), MATS["sage"], col)
            box(f"{room_id}_ChairBack", (cx, floor_y(y+1.27), z+.82), (.48,.10,.58), MATS["sage"], col)
        if "makan" in fixtures:
            box(f"{room_id}_DiningTable", (cx, cyb, z+.78), (min(1.4,w*.64),min(1.5,h*.43),.10), MATS["wood"], col)
            for dx in (-.52,.52):
                for dy in (-.45,.45):
                    if min(1.4,w*.64)>1.2:
                        box(f"{room_id}_Chair", (cx+dx,cyb+dy,z+.42), (.32,.32,.08), MATS["sage"], col)
    if "toilet" in fixtures:
        cyl(f"{room_id}_Toilet_Bowl", (x+w*.72, floor_y(y+h*.62), z+.18), .22,.32,MATS["white"],col)
        box(f"{room_id}_Toilet_Tank", (x+w*.72,floor_y(y+h*.62)+.22,z+.48),(.39,.18,.48),MATS["white"],col)
        box(f"{room_id}_Vanity", (x+w*.3,floor_y(y+h*.75),z+.44),(.75,.42,.84),MATS["wood_light"],col)
        cyl(f"{room_id}_Sink", (x+w*.3,floor_y(y+h*.75),z+.88), .20,.06,MATS["white"],col)
    if "sofa" in fixtures:
        sofa_w, sofa_d = min(2.0,w*.6),.72
        box(f"{room_id}_Sofa", (cx,cyb,z+.36),(sofa_w,sofa_d,.55),MATS["sage"],col)
        box(f"{room_id}_Sofa_Back", (cx,cyb+sofa_d*.42,z+.72),(sofa_w,.16,.85),MATS["sage"],col)
        box(f"{room_id}_Coffee_Table", (cx,cyb-sofa_d*1.15,z+.42),(min(1.0,w*.35),.62,.12),MATS["wood_light"],col)
    if "tangga" in fixtures:
        for i in range(12):
            box(f"{room_id}_Step_{i+1:02d}",(x+w/2,floor_y(y+.32+i*.27),z+.12+i*.19),(min(1.45,w*.78),.34,.18),MATS["wood_light"],col,.01)


def create_house():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for col in list(bpy.data.collections):
        if col.name != "Collection":
            bpy.data.collections.remove(col)
    root = bpy.context.scene.collection
    floor_cols = {n: collection(f"Floor_{n}") for n in (1,2)}
    furniture_col = collection("Furniture")
    roof_col = collection("Roof")
    site_col = collection("Site")
    # Site and ground slab.
    box("Site_Ground", (W/2,0,-.28),(W+4,D+4,.45),MATS["garden"],site_col,.04)
    for floor in DATA["floors"]:
        n = floor["number"]
        base = FLOOR_Z[n]
        col = floor_cols[n]
        box(f"F{n}_Slab",(W/2,0,base),(W,D,.22),MATS["floor"],col,.025)
        # Open concept parapets keep room boundaries legible in all views.
        edges = set()
        for room in floor["rooms"]:
            if room["id"].endswith("circulation"):
                continue
            x,y,w,h = room["bounds_m"]
            corners = [((x,y),(x+w,y)),((x+w,y),(x+w,y+h)),((x+w,y+h),(x,y+h)),((x,y+h),(x,y))]
            for a,b in corners:
                key = tuple(sorted(((round(a[0],3),round(a[1],3)),(round(b[0],3),round(b[1],3)))))
                edges.add(key)
        for idx, edge in enumerate(sorted(edges)):
            a,b=edge
            boundary = (abs(a[0])<.01 and abs(b[0])<.01) or (abs(a[0]-W)<.01 and abs(b[0]-W)<.01) or (abs(a[1])<.01 and abs(b[1])<.01) or (abs(a[1]-D)<.01 and abs(b[1]-D)<.01)
            panel_wall(f"F{n}_Wall_{idx:03d}",a,b,base+.11,WALL_H if boundary else 1.12,MATS["plaster"],col)
        for room in floor["rooms"]:
            x,y,w,h = room["bounds_m"]
            if room["id"] in ("f1_teras","f2_balcony"):
                # glass balcony/terrace rail at the exposed front edge
                for seg in range(1,7):
                    px=x+w*seg/7
                    box(f"{room['id']}_Rail_{seg}",(px,floor_y(y),base+.52),(.04,.04,.82),MATS["dark"],col,.01)
                box(f"{room['id']}_Handrail",(x+w/2,floor_y(y),base+.96),(w,.07,.07),MATS["wood"],col,.015)
            make_furniture(n,room,furniture_col)
        # Floor 2 rests above the floor 1 walls, but remains a separately hideable layer.
    # Gable-like pitched roof as two broad planes represented with mesh triangles.
    y0,y1=-D/2-0.18,D/2+0.18
    z_eave=FLOOR_Z[2]+WALL_H
    z_ridge=z_eave+1.5
    for name, verts in [
        ("Roof_Slope_Left",[( -.45,y0,z_eave),(W/2,y0,z_ridge),(W/2,y1,z_ridge),(-.45,y1,z_eave)]),
        ("Roof_Slope_Right",[(W/2,y0,z_ridge),(W+.45,y0,z_eave),(W+.45,y1,z_eave),(W/2,y1,z_ridge)])
    ]:
        mesh=bpy.data.meshes.new(name+"Mesh"); mesh.from_pydata(verts,[],[(0,1,2,3)]); mesh.materials.append(MATS["roof"])
        obj=bpy.data.objects.new(name,mesh); roof_col.objects.link(obj)
        solid=obj.modifiers.new("Roof thickness","SOLIDIFY"); solid.thickness=.12
    # Camera and light for viewport/render.
    bpy.ops.object.camera_add(location=(18,-22,21))
    camera=bpy.context.object; camera.name="Presentation_Camera"; move_to(camera,site_col)
    direction=Vector((W/2,0,2.6))-camera.location
    camera.rotation_euler=direction.to_track_quat("-Z","Y").to_euler()
    camera.data.type="ORTHO"; camera.data.ortho_scale=24
    bpy.context.scene.camera=camera
    bpy.ops.object.light_add(type="AREA",location=(1,-9,19))
    key=bpy.context.object; key.name="Soft_Key"; key.data.energy=4200; key.data.shape="DISK"; key.data.size=12; move_to(key,site_col)
    key.rotation_euler=(math.radians(25),0,math.radians(-25))
    world=bpy.context.scene.world
    if world:
        world.color=(.45,.45,.45)
    scene=bpy.context.scene
    scene.render.resolution_x=1400; scene.render.resolution_y=1000; scene.render.resolution_percentage=100
    scene.render.film_transparent=False
    try:
        scene.render.engine="BLENDER_EEVEE_NEXT"
    except TypeError:
        pass
    scene.render.image_settings.file_format="PNG"
    # Save full editable scene. Variant GLBs are exported from the stable collection sets.
    out=ROOT/"assets"; (out/"renders").mkdir(parents=True,exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(out/"house.blend"))
    return scene, floor_cols, furniture_col, roof_col, site_col, out


def render_variant(scene, out, label, visible_floors, roof_visible):
    # Toggle floor and furniture objects based on name prefix; hide extras from the render.
    for obj in scene.objects:
        obj.hide_render=False
        if obj.name.startswith("F1_"):
            obj.hide_render=1 not in visible_floors
        elif obj.name.startswith("F2_"):
            obj.hide_render=2 not in visible_floors
        elif obj.name.startswith("Roof_"):
            obj.hide_render=not roof_visible
        elif obj.name.startswith("f1_"):
            obj.hide_render=1 not in visible_floors
        elif obj.name.startswith("f2_"):
            obj.hide_render=2 not in visible_floors
        elif obj.name in ("Site_Ground",):
            obj.hide_render=(label=="floor-2")
    scene.camera.data.ortho_scale = 23 if label=="floor-2" else 24
    scene.render.filepath=str(out/"renders"/(label+".png"))
    bpy.ops.render.render(write_still=True)


if __name__ == "__main__":
    scene, floors, furniture, roof, site, output = create_house()
    render_variant(scene, output, "full-house", {1,2}, True)
    render_variant(scene, output, "floor-1", {1}, False)
    render_variant(scene, output, "floor-2", {2}, False)
    print("Built editable Blender house model and three view renders.")

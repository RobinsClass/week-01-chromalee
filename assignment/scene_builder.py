"""
DIGM 131 - Assignment 1: Procedural Scene Builder
==================================================

OBJECTIVE:
    Build a simple 3D scene in Maya using Python scripting.
    You will practice using maya.cmds to create and position geometry,
    and learn to use descriptive variable names.

REQUIREMENTS:
    1. Create a ground plane (a large, flat polygon plane).
    2. Create at least 5 objects in your scene.
    3. Use at least 2 different primitive types (e.g., cubes AND spheres,
       or cylinders AND cones, etc.).
    4. Position every object using descriptive variable names
       (e.g., house_x, tree_height -- NOT x1, h).
    5. Add comments explaining what each section of your code does.

GRADING CRITERIA:
    - [20%] Ground plane is created and scaled appropriately.
    - [30%] At least 5 objects are created using at least 2 primitive types.
    - [25%] All positions/sizes use descriptive variable names.
    - [15%] Code is commented clearly and thoroughly.
    - [10%] Scene is visually coherent (objects are placed intentionally,
            not overlapping randomly).

TIPS:
    - Run this script from Maya's Script Editor (Python tab).
    - Use maya.cmds.polyCube(), maya.cmds.polySphere(), maya.cmds.polyCylinder(),
      maya.cmds.polyCone(), maya.cmds.polyPlane(), etc.
    - Use maya.cmds.move(x, y, z, objectName) to position objects.
    - Use maya.cmds.scale(x, y, z, objectName) to resize objects.
    - Use maya.cmds.rename(oldName, newName) to give objects meaningful names.
"""
#test
import maya.cmds as cmds

# ---------------------------------------------------------------------------
# Clear the scene so we start fresh each time the script runs.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.file(new=True, force=True)

# ---------------------------------------------------------------------------
# Ground Plane
# ---------------------------------------------------------------------------
# Descriptive variables for the ground plane dimensions and position.
ground_width = 50
ground_depth = 50
ground_y_position = 0

ground = cmds.polyPlane(
    name="ground_plane",
    width=ground_width,
    height=ground_depth,
    subdivisionsX=1,
    subdivisionsY=1,
)[0]
cmds.move(0, ground_y_position, 0, ground)

# ---------------------------------------------------------------------------
# Example Object 1 -- a simple building (cube)
# This is provided as an example. Study it, then add your own objects below.
# ---------------------------------------------------------------------------
building_width = 4
building_height = 6
building_depth = 4
building_x = -8
building_z = 5

building = cmds.polyCube(
    name="building_01",
    width=building_width,
    height=building_height,
    depth=building_depth,
)[0]
# Raise the building so its base sits on the ground plane.
cmds.move(building_x, building_height / 2.0, building_z, building)

# ---------------------------------------------------------------------------
# TODO: Add Object 2
# Create a second object using a DIFFERENT primitive type than the cube above.
# Remember to:
#   - Use descriptive variable names for size and position.
#   - Name the object meaningfully with the 'name' parameter or cmds.rename().
#   - Position it so it sits on the ground (not floating or buried).
tree1_trunk_height = 2
tree1_trunk_radius = 0.2
tree1_trunk_x = 3
tree1_trunk_z = 3

tree1_trunk = cmds.polyCylinder(
    name="tree1_trunk",
    height=tree1_trunk_height,
    radius=tree1_trunk_radius
)

cmds.move(tree1_trunk_x, tree1_trunk_height / 2, tree1_trunk_z, tree1_trunk)
#This command should make the trunk of the first tree which is just a cylinder, and the last command moves it

tree1_top_radius = 1
tree1_top_x = tree1_trunk_x
tree1_top_z = tree1_trunk_z
tree1_top_y = tree1_trunk_height + tree1_top_radius

tree1_top = cmds.polySphere(
    name="tree1_top",
    radius=tree1_top_radius
)

cmds.move(tree1_top_x, tree1_top_y, tree1_top_z, tree1_top)
#This command should make the top part of the tree. I set the coordinates so that it would line up with the trunk
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# TODO: Add Object 3
building2_width = 6
building2_height = 10
building2_depth = 5
building2_x = -8
building2_z = -2

building2 = cmds.polyCube(
    name="building_02",
    width=building2_width,
    height=building2_height,
    depth=building2_depth
)
cmds.move(building2_x, building2_height / 2, building2_z, building2)
#This command should make another building right next to the first one, but bigger
#I changed the variable names so that they have the same naming convention, but are different objects
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# TODO: Add Object 4
house_width = 2
house_height = 2
house_depth = 2
house_x = 4
house_z = 0

house = cmds.polyCube(
    name="house",
    width=house_width,
    height=house_height,
    depth=house_depth
)

cmds.move(house_x, house_height / 2, house_z, house)
#This is the base of a house, same as the buildings but smaller

roof_height = 1
roof_radius = 2
roof_x = house_x
roof_z = house_z
roof_y = house_height + (roof_height / 2)

roof = cmds.polyCone(
    name="house_roof",
    height=roof_height,
    radius=roof_radius
)

cmds.move(roof_x, roof_y, roof_z, roof)
#I used the technique for the tree top for the roof of the house
#I made a cone that had the same coordinates of the house base and adjusted the size accordingly
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# TODO: Add Object 5
building3_width = 3
building3_height = 8
building3_depth = 3
building3_x = 0
building3_z = -8

building3 = cmds.polyCube(
    name="building_03",
    width=building3_width,
    height=building3_height,
    depth=building3_depth
)
cmds.move(building3_x, building3_height / 2, building3_z, building3)

#This command makes another building but on the right side, not in the same line as the previous buildings
#Again, I changed the variable names so that they have the same naming convention, but are different objects
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# TODO (Optional): Add more objects to make your scene more interesting!
# Consider: trees, lamp posts, fences, vehicles, animals, etc.
sun_radius = 3
sun_x = 10
sun_y = 20
sun_z = -5

sun = cmds.polySphere(
    name="sun",
    radius=sun_radius
)

cmds.move(sun_x, sun_y, sun_z, sun)
#The y doesn't have to be changed, since the sun is not on the ground plane, thus I moved up
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Frame All -- so the whole scene is visible in the viewport.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.viewFit(allObjects=True)
print("Scene built successfully!")

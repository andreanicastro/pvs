import bpy
import os

tx = 0.0
ty = 0.0
tz = 4.0

rx = 0.0
ry = 0.0
rz = 0.0

fov = 50.0

pi = 3.14159265


def resetScene(context):
    scene = context.scene
    objs = bpy.data.objects
    for obj in objs:
        scene.objects.unlink(obj)
        objs.remove(obj)
   


def addCube():
    bpy.ops.mesh.primitive_cube_add()


def look_at(obj_camera, point):
    loc_camera = obj_camera.matrix_world.to_translation()
    
    direction = point - loc_camera
    #point the camera -Z and use its Y as up
    rot_quat = direction.to_track_quat('-Z', 'Y')
    
    # assume we're using euler rotation
    obj_camera.rotation_euler = rot_quat.to_euler()
    


resetScene(bpy.context)
addCube()

# import model 
# models_path = "tree/"
# models = "tree.blend"
# path = os.path.join(models_path, models)
# print(path)
# bpy.ops.wm.open_mainfile(filepath=path)


scene = bpy.data.scenes["Scene"]



# Set render resolution
scene.render.resolution_x = 640
scene.render.resolution_y = 480

#create camera
camera_loc = (10, 10, 0)
bpy.ops.object.camera_add(location= camera_loc)
bpy.data.cameras[0].name = 'Camera'
bpy.context.scene.camera = bpy.data.objects['Camera']

# Set camera fov in degrees
scene.camera.data.angle = fov*(pi/180.0)

#point the camera to the cube 
obj_camera = bpy.data.objects['Camera']
obj_cube = bpy.data.objects['Cube']
look_at(obj_camera, obj_cube.matrix_world.to_translation())




#chose image filename 
bpy.data.scenes['Scene'].render.filepath = 'img.png'

#render a single still image
bpy.ops.render.render(write_still = True)

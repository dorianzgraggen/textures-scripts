import bpy
import os

path_dir = bpy.context.scene.render.filepath #save for restore
basedir = os.path.dirname(bpy.data.filepath)
basedir = basedir + "/_Export_Tiles2/"
  
#for cam in [obj for obj in bpy.data.objects if obj.type == 'CAMERA']:
#    print("AAAAAA")
#    bpy.context.scene.camera = cam
#   
#    fn = os.path.join(basedir, cam.name)
#    print(fn)
#    bpy.context.scene.render.filepath = fn
#    bpy.ops.render.render(write_still=True)





TextureSphere = bpy.data.objects["TextureSphere"]

#NewMaterial = bpy.data.materials.get("Grass_01")

#if NewMaterial is not None:
#   TextureSphere.data.materials[0] = NewMaterial
   
renderAllCams = False
shouldRender = True   
   
for material in bpy.data.materials:
    print(material.name)
    TextureSphere.data.materials[0] = material
    
    for cam in [obj for obj in bpy.data.objects if obj.type == 'CAMERA']:
        print("AAAAAA ddddddd")
        
        shouldRender = True
        if renderAllCams == False and cam.name == "closeup":
            shouldRender = False
            
        if material.name == "_ExampleMaterial":
            shouldRender = False
        
        if shouldRender:
            bpy.context.scene.camera = cam
           
            fn = os.path.join(basedir, material.name + "_" + cam.name)
            print(fn)
            bpy.context.scene.render.filepath = fn
            bpy.ops.render.render(write_still=True)
            print("Rendered", material.name, cam.name)
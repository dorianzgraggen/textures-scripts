import bpy
import os

path_dir = bpy.context.scene.render.filepath #save for restore
baseDir = os.path.dirname(bpy.data.filepath)

textureDir =  "D:/Textures/2020/03_Tiles_II/Substance Designer/Upload"

textures = [dI for dI in os.listdir(textureDir) if os.path.isdir(os.path.join(textureDir, dI))]

print(textures)

baseMaterial = bpy.data.materials.get("_ExampleMaterial")
TextureSphere = bpy.data.objects["TextureSphere"]

list = textures 
   
resolution = 2;

# Using for loop 
for i in list: 
    print(i) 

def loadTexture(mapType, fileName, resolution):
    entirePath = textureDir + "/" + fileName + "/" + fileName + "_" + str(resolution) + "K_" + mapType + ".png"
    print(entirePath)
    image = bpy.data.images.load(entirePath)    
    return image

for j in textures:
    TextureSphere.data.materials[0] = baseMaterial.copy()
    bpy.context.object.active_material.name = j
    currentMaterial = bpy.data.materials[j]
    nodes = currentMaterial.node_tree.nodes

    baseColor = nodes.get("Base Color")
    baseColor.image = loadTexture("Base_Color", j, resolution)
    baseColor.image.colorspace_settings.name = 'sRGB'
    
    roughness = nodes.get("Roughness")
    roughness.image = loadTexture("Roughness", j, resolution)
    roughness.image.colorspace_settings.name = 'Non-Color'
    
    height = nodes.get("Height")
    height.image = loadTexture("Height", j, resolution)
    height.image.colorspace_settings.name = 'Non-Color'
    
    normal = nodes.get("Normal")
    normal.image = loadTexture("Normal", j, resolution)
    normal.image.colorspace_settings.name = 'Non-Color'
    
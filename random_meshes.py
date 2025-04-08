import random

import maya.cmds as cmds

def set_random_position(transform_node):
    tx = random.randint(-10, 10)
    ty = random.randint(-10, 10)
    tz = random.randint(-10, 10)
    
    cmds.setAttr(f"{transform_node}.translate", tx, ty, tz, type="double3")

def mesh_scatter(num_meshes, mesh_type="cube", size=1, variationSize=0):
    mesh_transforms = []
    valid_mesh_types = ["cube", "sphere", "cylinder", "prism"]
    is_random = mesh_type == "random"
    
    finalSize = size + variationSize
    
    for i in range(num_meshes):
        if variationSize > 0:
            variationSize = random.randrange(variationSize)
            finalSize = size + variationSize
        if is_random:
            mesh_type = random.choice(valid_mesh_types)
        if mesh_type == "sphere":
            transform_node = cmds.polySphere(radius=finalSize)[0]
        elif mesh_type == "cylinder":
            transform_node = cmds.polyCylinder(radius=finalSize, height=2*finalSize)[0]
        elif mesh_type == "prism":
            transform_node = cmds.polyPrism(sc=finalSize, sh=finalSize)[0]
        else:
            transform_node = cmds.polyCube(width=finalSize, depth=finalSize, height=finalSize)[0]
        
        set_random_position(transform_node)
        
        mesh_transforms.append(transform_node)
    
    cmds.group(mesh_transforms, name="scattered_meshes")
    

if __name__ == "__main__":
    cmds.file(new=True, force=True)
    
    mesh_scatter(20, mesh_type="random",size=2, variationSize=5)
    
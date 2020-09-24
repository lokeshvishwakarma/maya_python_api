import maya.api.OpenMaya as om

# create a transform node
transform_fn = om.MFnDagNode()
transform_obj = transform_fn.create('transform', 'pSphere1')

# create mesh node
mesh_fn = om.MFnDagNode()
mesh_obj = mesh_fn.create('mesh', 'pSphereShape1', transform_obj)

# create polysphere node
sphere_fn = om.MFnDependencyNode()
sphere_obj = sphere_fn.create('polySphere')

# find sphere node's output plug
src_plug = sphere_fn.findPlug('output', False)

# find mesh node's inMesh plug
dest_plug = mesh_fn.findPlug('inMesh', False)

# connect sphere node's output to mesh node's inMesh input
dg_mod = om.MDGModifier()
dg_mod.connect(src_plug, dest_plug)
dg_mod.doIt()

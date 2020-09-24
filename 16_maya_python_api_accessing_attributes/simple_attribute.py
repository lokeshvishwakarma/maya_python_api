# import maya.api.OpenMaya as om
import maya.api._OpenMaya_py2 as om

node_name = 'pSphere1'
attribute_name = 'translateY'  # Simple Attribute

selection = om.MSelectionList()
selection.add(node_name)

obj = selection.getDependNode(0)

if obj.hasFn(om.MFn.kTransform):
    transform_fn = om.MFnTransform(obj)
    plug = transform_fn.findPlug(attribute_name, False)

    attribute_value = plug.asDouble()
    print('{0}: {1}'.format(plug, attribute_value))

    plug.setDouble(2.0)
    print('{0}: {1}'.format(plug, attribute_value))

    # translation = transform_fn.translation(om.MSpace.kTransform)
    # translation[1] = 3.0
    # transform_fn.setTranslation(translation, om.MSpace.kTransform)

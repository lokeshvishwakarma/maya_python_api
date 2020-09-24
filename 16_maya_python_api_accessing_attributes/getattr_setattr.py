import maya.cmds as cmds

node_name = 'pSphere1'
attribute_name = 'translateY'
full_name = '{0}.{1}'.format(node_name, attribute_name)

# Get Attribute value
attribute_value = cmds.getAttr(full_name)
print('{0}: {1}'.format(full_name, attribute_value))

# Set Attribute value
cmds.setAttr(full_name, 1.0)
print('{0}: {1}'.format(full_name, attribute_value))

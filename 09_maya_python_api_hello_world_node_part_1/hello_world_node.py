import maya.api.OpenMaya as om
import maya.api.OpenMayaUI as omui
import maya.api.OpenMayaRender as omr
import maya.cmds as cmds


def maya_useNewAPI():
    """
    Tells Maya to use Maya API 2.0
    :return: None
    """
    pass


class HelloWorldNode(omui.MPxLocatorNode):
    """
    To register a node in Maya 4 things are required.
    1. Type Name
    2. Type ID
    3. Creator function
    4. Initialize function
    """
    # Used when file is saved to ascii format
    TYPE_NAME = 'helloworld'  # This is the name you would pass to createNode command to create a node

    # Used when file is saved to binary format
    TYPE_ID = om.MTypeId(0x0007F7F7)  # Must be a unique value in your Maya env

    # For development a range of 0 - 0x7ffff is available
    # For release a unique ID is to be assigned by Autodesk to avoid conflicts.

    DRAW_CLASSIFICATION = 'drawdb/geometry/helloworld'
    DRAW_REGISTRANT_ID = "HelloWorldNode"

    def __init__(self):
        super(HelloWorldNode, self).__init__()

    @classmethod
    def creator(cls):
        return HelloWorldNode()

    @classmethod
    def initialize(cls):
        """
        To initialize the attributes of this new node type
        """
       pass


class HelloWorldDrawOverride(omr.MPxDrawOverride):
    NAME = 'HelloWorldDrawOverride'

    def __init__(self, obj):
        super(HelloWorldDrawOverride, self).__init__(obj, None, False)

    def prepareForDraw(self, obj_path, camera_path, frame_context, old_data):
        """
        Is expected and must be implemented by any class that derive fro MPxDrawOverride
        :return:
        """
        pass

    def supportedDrawAPIs(self):
        """
        This method supports drawing using any of the drawing APIs
        :return: Constant
        """
        return omr.MRenderer.kAllDevices

    def hasUIDrawables(self):
        """
        :return: Bool
        """
        return True

    def addUIDrawables(self, obj_path, draw_manager, frame_context, data):
        """
        This method will be called whenever any update is required
        :return:
        """
        draw_manager.beginDrawable()
        draw_manager.text2d(om.MPoint(100, 100), "Hello World")  # Bottom Left corner
        draw_manager.endDrawable()

    @classmethod
    def creator(cls, obj):
        """
        :param obj: MObject
        :return:
        """
        return HelloWorldDrawOverride(obj)


def initializePlugin(plugin):
    """
    :param plugin: MObject: used to register the plugin using an MFnPlugin function set
    :return: None
    """
    vendor = 'Lokesh Vishwakarma'
    version = '1.0.0'
    api_version = 'Any'
    plugin_fn = om.MFnPlugin(plugin, vendor, version, api_version)
    # Register the node
    try:
        plugin_fn.registerNode(HelloWorldNode.TYPE_NAME,  # name of the node
                               HelloWorldNode.TYPE_ID,  # unique id that identifies node
                               HelloWorldNode.creator,  # function/method that returns new instance of class
                               HelloWorldNode.initialize,  # function/method that will initialize all attributes of node
                               om.MPxNode.kLocatorNode,  # type of node to be registered
                               HelloWorldNode.DRAW_CLASSIFICATION)  # draw-specific classification string (VP2.0)
        # 5th parameter is a constant that represents the type of node that is being registered.
        # Last parameter, only required if the node has a drawOverride.
    except:
        om.MGlobal.displayError('Failed to register Node: {0}'.format(HelloWorldNode.TYPE_NAME))

    # Register the DrawOverride
    try:
        omr.MDrawRegistry.registerDrawOverrideCreator(HelloWorldNode.DRAW_CLASSIFICATION,
                                                      # draw-specific classification
                                                      HelloWorldNode.DRAW_REGISTRANT_ID,
                                                      # unique name to identify registration
                                                      HelloWorldDrawOverride.creator
                                                      # function/method that returns new instance of class
                                                      )
    except:
        om.MGlobal.displayError('Failed to register DrawOverride: {0}'.format(HelloWorldDrawOverride.NAME))


def uninitializePlugin(plugin):
    """
    :param plugin: MObject: used to de-register the plugin using an MFnPlugin function set
    :return:
    """
    # Very important to de-register in reverse order of registration
    plugin_fn = om.MFnPlugin(plugin)
    # De-register DrawOverride
    try:
        omr.MDrawRegistry.deregisterDrawOverrideCreator(HelloWorldNode.DRAW_CLASSIFICATION,
                                                        HelloWorldNode.DRAW_REGISTRANT_ID)
    except:
        om.MGlobal.displayError('Failed to de-register DrawOverride: {0}'.format(HelloWorldDrawOverride.NAME))
    # De-register Node
    try:
        plugin_fn.deregisterNode(HelloWorldNode.TYPE_ID)
    except:
        om.MGlobal.displayError('Failed to de-register Node: {0}'.format(HelloWorldNode.TYPE_NAME))


if __name__ == '__main__':
    cmds.file(new=True, force=True)
    plugin_name = 'hello_world_node.py'  # plugin name is always the file name
    cmds.evalDeferred('if cmds.pluginInfo("{0}", q=True, loaded=True): cmds.unloadPlugin("{0}")'.format(plugin_name))
    cmds.evalDeferred('if not cmds.pluginInfo("{0}", q=True, loaded=True): cmds.loadPlugin("{0}")'.format(plugin_name))
    cmds.evalDeferred('cmds.createNode("helloworld")')

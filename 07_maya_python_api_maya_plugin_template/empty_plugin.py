import maya.api.OpenMaya as om
import maya.cmds as cmds


def maya_useNewAPI():
    """
    The presence of this function tells Maya that plugin produces, and
    expects to be passed, objects created using the Maya Python API 2.0
    :return: None
    """
    pass


def initializePlugin(plugin):
    """
    Entry point for a plugin. It is called once -- immediately after plugin is loaded.
    This function registers all of the commands, nodes, contexts, etc.
    It is required by all plugins.
    :param plugin: MObject used to register the plugin using an MFnPlugin function set
    """
    vendor = 'Lokesh Vishwakarma'
    version = '1.0.0'
    om.MFnPlugin(plugin, vendor, version)
    print('Hello World !!!')


def uninitializePlugin(plugin):
    """
    Exit point for a plugin. It is called once -- when plugin is unloaded.
    This function de-registers everything that was registered in the initializePlugin function.
    :param plugin: MObject used to de-register the plugin using an MFnPlugin function set
    """
    pass


if __name__ == '__main__':
    plugin_name = 'hello_world_cmd.py'  # plugin name is always the file name
    cmds.evalDeferred('if cmds.pluginInfo("{0}", q=True, loaded=True): cmds.unloadPlugin("{0}")'.format(plugin_name))
    cmds.evalDeferred('if not cmds.pluginInfo("{0}", q=True, loaded=True): cmds.loadPlugin("{0}")'.format(plugin_name))

import maya.api.OpenMaya as om
import maya.cmds as cmds


class HelloWorldCmd(om.MPxCommand):
    COMMAND_NAME = 'HelloWorld'

    def __init__(self):
        super(HelloWorldCmd, self).__init__()

    def doIt(self, args):
        """
        Required method for all commands. When one calls the command, maya runs the doIt() method
        :param args:
        :return:
        """
        print("Hello World !!")

    @classmethod
    def creator(cls):
        """
        This is the method provided to Maya when plugin is registered.
        And it is used to get an instance of this command.
        :return: HelloWorld
        """
        return HelloWorldCmd()


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
    :param plugin: MObject: used to register the plugin using an MFnPlugin function set
    """
    vendor = 'Lokesh Vishwakarma'
    version = '1.0.0'
    plugin_fn = om.MFnPlugin(plugin, vendor, version)
    try:
        plugin_fn.registerCommand(HelloWorldCmd.COMMAND_NAME, HelloWorldCmd.creator)
    except:
        om.MGlobal.displayError('Failed to register command: {0}'.format(HelloWorldCmd.COMMAND_NAME))


def uninitializePlugin(plugin):
    """
    Exit point for a plugin. It is called once -- when plugin is unloaded.
    This function de-registers everything that was registered in the initializePlugin function.
    :param plugin: MObject: used to de-register the plugin using an MFnPlugin function set
    """
    plugin_fn = om.MFnPlugin(plugin)
    try:
        plugin_fn.deregisterCommand(HelloWorldCmd.COMMAND_NAME)
    except:
        om.MGlobal.displayError('Failed to de-register command: {0}'.format(HelloWorldCmd.COMMAND_NAME))


if __name__ == '__main__':
    plugin_name = 'hello_world_cmd.py'  # plugin name is always the file name
    cmds.evalDeferred('if cmds.pluginInfo("{0}", q=True, loaded=True): cmds.unloadPlugin("{0}")'.format(plugin_name))
    cmds.evalDeferred('if not cmds.pluginInfo("{0}", q=True, loaded=True): cmds.loadPlugin("{0}")'.format(plugin_name))

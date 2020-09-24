# Python API 1.0 and 2.0 can coexist in the same script
# However, objects from API 1.0 and 2.0 are not interchangeable

from PySide2 import QtWidgets
from shiboken2 import wrapInstance

from maya.api.OpenMaya import MGlobal  # Python API 2.0
# from maya.api.OpenMayaUI import MQUtil
# from maya.OpenMaya import MGlobal # Python API 1.0
from maya.OpenMayaUI import MQtUtil


def maya_main_window():
    """
    Return s the Maya main window as a Python Object
    """
    main_window_ptr = MQtUtil.mainWindow()  # Python API 1.0
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)


class TestDialog(QtWidgets.QDialog):
    def __init__(self, parent=maya_main_window()):
        super(TestDialog, self).__init__(parent)
        button = QtWidgets.QPushButton('Print Error', self)
        button.clicked.connect(self.print_error)

    def print_error(self):
        MGlobal.displayError('Python API 2.0 Error')
        # MGlobal.displayError('Python API 1.0 Error')


if __name__ == '__main__':
    try:
        test_dialog.close()
        test_dialog.deleteLater()
    except:
        pass

    test_dialog = TestDialog()
    test_dialog.show()

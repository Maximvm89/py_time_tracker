'''

Initialize UI
'''
import sys

from PySide2 import QtCore
from PySide2 import QtUiTools
from PySide2.QtWidgets import QApplication, QDialog, QWidget


class TimeTrackingUI(QDialog):
    ui: QWidget

    def __init__(self, ui_path=None, parent=None):
        super(TimeTrackingUI, self).__init__(parent)

        # Remove the flag window
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        # Ui instance that will contain all the info of ui elements loeaded using init_ui reading the qt designer file
        self.ui = None
        self.init_ui(ui_path)

        self.ui.setWindowTitle("Time Tracking")
        self.ui.setFixedSize(600, 400)
        self.ui.windowFlags()

    def init_ui(self, ui_path=None):
        if not ui_path:
            ui_path = r'C:\Users\marco\Documents\Scripts\sandbox\docs\gray_hat\py_time_tracker\resources\tracking_task.ui'

        q_file = QtCore.QFile(ui_path)
        q_file.open(QtCore.QFile.ReadOnly)

        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(q_file, parentWidget=self)
        q_file.close()

    def create_layout(self):
        self.ui.layout().setContentsMargins(6, 6, 6, 6)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = TimeTrackingUI()
    gui.ui.show()

    sys.exit(app.exec_())

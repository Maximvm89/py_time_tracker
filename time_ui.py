'''

Initialize UI
'''
import operator
import sys
import threading

from PySide2 import QtCore
from PySide2 import QtUiTools
from PySide2.QtWidgets import *

import time_tracker


class TimeTrackModel(QtCore.QAbstractTableModel):
    def __init__(self, parent, custom_dict, header, *args):
        QtCore.QAbstractTableModel.__init__(self, parent, *args)
        self.custom_dict = custom_dict
        self.header = header

    # def index(self, row:int, column:int, parent:QtCore.QModelIndex=...) -> QtCore.QModelIndex:
    #     return self.custom_list[row][column]

    def rowCount(self, parent):
        return len(self.custom_dict)

    def columnCount(self, parent):
        return 2

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.header[col]
        return None

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != QtCore.Qt.DisplayRole:
            return None
        print(index.row())
        print(index.column())
        print(self.custom_dict[index.row()][index.column()])
        return self.custom_dict[index.row()][index.column()]


class TimeTrackingUI(QDialog):
    ui: QWidget

    def __init__(self, ui_path=None, parent=None):
        super(TimeTrackingUI, self).__init__(parent)

        # Remove the flag window
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        # Ui instance that will contain all the info of ui elements loeaded using init_ui reading the qt designer file
        self.ui = None
        self.time_tracker = time_tracker.TimeTracker()
        self.init_ui(ui_path)

        self.ui.setWindowTitle("Time Tracking")
        self.ui.setFixedSize(622, 251)
        self.create_connections()

    def create_connections(self):
        self.ui.pause_button.clicked.connect(self.pause_button_clicked)
        self.ui.stop_button.clicked.connect(self.stop_button_clicked)
        self.ui.start_button.clicked.connect(self.start_button_clicked)

    def pause_button_clicked(self):
        self.ui.lcdNumber.setStyleSheet("background-color:red;")
        self.time_tracker.stop_tracking_ui()
        pass

    def stop_button_clicked(self):
        self.ui.close()
        self.time_tracker.stop_tracking_ui()
        pass

    def start_button_clicked(self):
        # QLCDNumber
        self.ui.lcdNumber.setStyleSheet("background-color:green;")
        self.time_tracker.ui = self.ui
        t1 = threading.Thread(target=self.time_tracker.start_tracking_ui)
        t1.start()
        # self.time_tracker.start_tracking_ui("Test_ui")
        # self.ui.lcdNumber.

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
    app = QApplication()
    gui = TimeTrackingUI()
    # gui.show()
    gui.ui.show()

    sys.exit(app.exec_())

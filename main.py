from PyQt5 import QtWidgets        #Official Library
from radar_gui import Ui_MainWindow        #Custom Library
import sys        #Official Library


def main():
    app = QtWidgets.QApplication(sys.argv)
    osc_main_window = QtWidgets.QMainWindow()        #Instanitate a OscMainWindow class
    ui = Ui_MainWindow()
    ui.setupUi(osc_main_window)
    osc_main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()




from PyQt5.QtWidgets import QApplication
from view import *

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = Ui_Window()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


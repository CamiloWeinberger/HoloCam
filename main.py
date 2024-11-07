import sys
from PyQt6.QtWidgets import QApplication
from utils.init_program import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = windows()
    win.show()
    sys.exit(app.exec())
    

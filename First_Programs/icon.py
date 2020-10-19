# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    
    def initUI(self):
        self.setGeometry(300,300,300,220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))
        
        self.show()

def main():
    
    app = QApplication(sys.argv)
    
    ex = example()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
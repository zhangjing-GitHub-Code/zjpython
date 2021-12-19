import sys 
from PyQt5.QtWidgets import QWidget , QPushButton , QApplication
from PyQt5.QtCore import QCoreApplication 
apP = QApplication(sysargv) 
exp = QWidget()
qtn = QPushButton('退出 Q',exp)
qtn.resize(qtn.sizeHint())
qtn.clicked.connect(QCoreApplication.quit)
qtn.move(70,40)
exp.setGeometry (300,300,200,100)
exp.setWindowTitle('退出窗口')
exp.show ()
sysexit(apP.exec_())

from PyQt5 import QtCore, QtGui, QtWidgets
#from power_bar import PowerBar
from power_bar_v02 import PowerBar



app = QtWidgets.QApplication([])
volume = PowerBar()
volume.show()
app.exec_()

from PyQt5 import QtCore, QtGui, QtWidgets
from power_bar import PowerBar

"""def paintEvent(self, e):
    painter = QtGui.QPainter(self)
    brush = QtGui.QBrush()
    brush.setColor(QtGui.QColor('black'))
    brush.setStyle(Qt.SolidPattern)
    rect = QtCore.QRect(0, 0, painter.device().width(), painter.device().height())
    painter.fillRect(rect, brush)"""

app = QtWidgets.QApplication([])
volume = PowerBar()
volume.show()
app.exec_()

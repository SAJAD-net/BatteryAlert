# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SafeCharge.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import qdarkstyle
import psutil
import threading
import playsound
from notifypy import Notify


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 672)
        MainWindow.setMinimumSize(QtCore.QSize(450, 672))
        MainWindow.setMaximumSize(QtCore.QSize(450, 672))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./resources/BatteryAlert.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(180, 600, 89, 25))
        self.save_btn.setObjectName("save_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 30, 171, 40))
        self.label.setStyleSheet("font: 75 italic bold 20pt \"Ubuntu\";")
        self.label.setObjectName("label")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(140, 140, 51, 26))
        self.spinBox.setMinimum(70)
        self.spinBox.setMaximum(100)
        self.spinBox.setObjectName("spinBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 101, 41))
        self.label_2.setObjectName("label_2")
        self.alarm_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.alarm_checkbox.setGeometry(QtCore.QRect(20, 220, 92, 23))
        self.alarm_checkbox.setObjectName("alarm_checkbox")
        self.not_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.not_checkbox.setGeometry(QtCore.QRect(20, 190, 111, 23))
        self.not_checkbox.setObjectName("not_checkbox")
        self.statusl = QtWidgets.QLabel(self.centralwidget)
        self.statusl.setGeometry(QtCore.QRect(120, 510, 261, 20))
        self.statusl.setObjectName("statusl")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 510, 67, 21))
        self.label_4.setObjectName("label_4")
        self.label.raise_()
        self.save_btn.raise_()
        self.spinBox.raise_()
        self.label_2.raise_()
        self.alarm_checkbox.raise_()
        self.not_checkbox.raise_()
        self.statusl.raise_()
        self.label_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BatteryAlert"))
        self.save_btn.setText(_translate("MainWindow", "Save"))
        self.label.setText(_translate("MainWindow", "BatteryAlert"))
        self.label_2.setText(_translate("MainWindow", "Charge Level"))
        self.alarm_checkbox.setText(_translate("MainWindow", "Alarm"))
        self.not_checkbox.setText(_translate("MainWindow", "Notification"))
        self.statusl.setText(_translate("MainWindow", ""))
        self.label_4.setText(_translate("MainWindow", "Status"))
        
        self.save_btn.clicked.connect(self.save)
        
        
    def save(self):
        self.charge_level = self.spinBox.value()
        self.statusl.setText("Configuration successfully saved !")
        threading.Thread(target=self.alarm).start()


    def notification(self):
        notification = Notify()
        notification.title = "BatteryAlert"
        notification.message = f"Battery level reached {self.charge_level}"

        notification.send()	    
    
    
    def alarm(self):
        while True:
            battery_status = psutil.sensors_battery() 
            if battery_status.percent == self.charge_level:
                self.statusl.setText(f"Battery level reached {self.charge_level}")
                if self.not_checkbox.isChecked():
                    self.notification()	
                if self.alarm_checkbox.isChecked():
                    playsound.playsound("resources/alarm.mp3")
               
                break
		
		
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    batteryAlert = QtWidgets.QMainWindow()
    batteryAlert.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    ui = Ui_MainWindow()
    ui.setupUi(batteryAlert)
    batteryAlert.show()
    sys.exit(app.exec_())     
        
 

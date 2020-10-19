# -*- coding: utf-8 -*-

from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

now = QDate.currentDate()

print(now.toString(Qt.ISODate))
print(now.toString(Qt.DefaultLocaleLongDate))

date_time = QDateTime.currentDateTime()

print(date_time.toString())

time = QTime.currentTime()
 
print(time.toString(Qt.DefaultLocaleLongDate))
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QDateTime, Qt

now = QDateTime.currentDateTime()

print('Local Date Time : ', now.toString(Qt.ISODate))
print('Universal Date Time : ', now.toUTC().toString(Qt.ISODate))
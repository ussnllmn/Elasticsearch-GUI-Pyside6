# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'right_columnqTRRqG.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *

class Ui_RightColumn(object):
    def setupUi(self, RightColumn):
        if not RightColumn.objectName():
            RightColumn.setObjectName(u"RightColumn")
        RightColumn.resize(240, 544)
        self.main_pages_layout = QVBoxLayout(RightColumn)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.menus = QStackedWidget(RightColumn)
        self.menus.setObjectName(u"menus")
        self.menu_1 = QWidget()
        self.menu_1.setObjectName(u"menu_1")
        self.verticalLayout = QVBoxLayout(self.menu_1)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.row_1 = QWidget(self.menu_1)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setMinimumSize(QSize(0, 40))
        self.row_1.setMaximumSize(QSize(16777215, 40))
        self.row_1.setStyleSheet(u"border-top-style: solid;\n"
"border-bottom-style: solid;\n"
"border-width: 1px;\n"
"border-color: #2c313c;")
        self.horizontalLayout = QHBoxLayout(self.row_1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.ToggleNight_Icon = QFrame(self.row_1)
        self.ToggleNight_Icon.setObjectName(u"ToggleNight_Icon")
        self.ToggleNight_Icon.setMaximumSize(QSize(30, 40))
        self.ToggleNight_Icon.setFrameShape(QFrame.StyledPanel)
        self.ToggleNight_Icon.setFrameShadow(QFrame.Raised)
        self.ToggleNightmode_3 = QVBoxLayout(self.ToggleNight_Icon)
        self.ToggleNightmode_3.setSpacing(0)
        self.ToggleNightmode_3.setObjectName(u"ToggleNightmode_3")
        self.ToggleNightmode_3.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.ToggleNight_Icon)

        self.Nightmode = QLabel(self.row_1)
        self.Nightmode.setObjectName(u"Nightmode")

        self.horizontalLayout.addWidget(self.Nightmode)

        self.ToggleNight = QFrame(self.row_1)
        self.ToggleNight.setObjectName(u"ToggleNight")
        self.ToggleNight.setMaximumSize(QSize(60, 40))
        self.ToggleNight.setFrameShape(QFrame.StyledPanel)
        self.ToggleNight.setFrameShadow(QFrame.Raised)
        self.ToggleNightmode = QVBoxLayout(self.ToggleNight)
        self.ToggleNightmode.setSpacing(0)
        self.ToggleNightmode.setObjectName(u"ToggleNightmode")
        self.ToggleNightmode.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.ToggleNight)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QWidget(self.menu_1)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 40))
        self.row_2.setMaximumSize(QSize(16777215, 40))
        self.row_2.setStyleSheet(u"border-top-style: solid;\n"
"border-bottom-style: solid;\n"
"border-width: 1px;\n"
"border-color: #2c313c;")
        self.btn_3_layout = QVBoxLayout(self.row_2)
        self.btn_3_layout.setSpacing(0)
        self.btn_3_layout.setObjectName(u"btn_3_layout")
        self.btn_3_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.row_2)

        self.label_1 = QLabel(self.menu_1)
        self.label_1.setObjectName(u"label_1")
        font = QFont()
        font.setPointSize(16)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet(u"font-size: 16pt")
        self.label_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_1)

        self.menus.addWidget(self.menu_1)

        self.main_pages_layout.addWidget(self.menus)


        self.retranslateUi(RightColumn)

        self.menus.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(RightColumn)
    # setupUi

    def retranslateUi(self, RightColumn):
        RightColumn.setWindowTitle(QCoreApplication.translate("RightColumn", u"Form", None))
        self.Nightmode.setText(QCoreApplication.translate("RightColumn", u"Toggle Nightmode", None))
        self.label_1.setText(QCoreApplication.translate("RightColumn", u"Menu 1 - Right Menu", None))
    # retranslateUi


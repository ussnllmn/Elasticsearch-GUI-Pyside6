# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainfWlJer.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QStackedWidget,
    QTextBrowser, QTextEdit, QVBoxLayout, QWidget)
from .resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1306, 720)
        MainWindow.setMinimumSize(QSize(1280, 720))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-radius: 12px;\n"
"}\n"
"#response_json_frame_2 {	\n"
"	border: 2px solid #bd93f9;\n"
"}\n"
"#response_text_frame_2 {	\n"
"	border: 2px solid #bd93f9;\n"
"}\n"
"#client_text_frame {	\n"
"	border: 2px solid #bd93f9;\n"
"}\n"
"#result_frame {	\n"
"	border: 2px solid #bd93f9;\n"
"}\n"
"#health_frame {	\n"
"	border: 2px solid #bd93f9;\n"
"}\n"
"#indice_frame{	\n"
"	border: 2px solid #bd93f9;\n"
"}\n"
"#health_frame_2 {	\n"
"	border: 2px solid #bd93f9;\n"
"}\n"
"#indice_frame_2{	\n"
"	border: 2px solid #bd93f9;\n"
"}\n"
"#result_frame_2{	\n"
"	border: 2px solid #bd93f9;\n"
"}\n"
"#Danger_zone_frame{	\n"
"	border-radius: 5px;\n"
"	border: 2px solid #ff5555;\n"
"}\n"
"/*\n"
"#search_frame {	\n"
"	border: 2px solid #bd93f9;\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#info_frame {	\n"
"	border: 2px solid #bd93f9;\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#response_json_fra"
                        "me{\n"
"	border: 2px solid #bd93f9;\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#response_text_frame{\n"
"	border: 2px solid #bd93f9;\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"*/\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-top-left-radius: 12px;\n"
"	border-bottom-left-radius: 12px;\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/Elasticsearch.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px sol"
                        "id transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	border-bottom-left-radius: 12px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"	border-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	border-color:rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: l"
                        "eft center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/cil-user.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { backgroun"
                        "d-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
""
                        "#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-top-right-radius: 12px;\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); border-bottom-right-radius: 12px;}\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButt"
                        "on {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::sect"
                        "ion{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover "
                        "{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border"
                        "-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin"
                        ": 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* //////////////////////////////////////////////////////////////////////////////"
                        "///////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
""
                        "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* ///////////////////////////////"
                        "//////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
""
                        "    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59"
                        ", 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(9, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(73, 8, 160, 20))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(73, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_search = QPushButton(self.topMenu)
        self.btn_search.setObjectName(u"btn_search")
        sizePolicy.setHeightForWidth(self.btn_search.sizePolicy().hasHeightForWidth())
        self.btn_search.setSizePolicy(sizePolicy)
        self.btn_search.setMinimumSize(QSize(0, 45))
        self.btn_search.setFont(font)
        self.btn_search.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_search.setLayoutDirection(Qt.LeftToRight)
        self.btn_search.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-find-in-page.png);")

        self.verticalLayout_8.addWidget(self.btn_search)

        self.btn_document = QPushButton(self.topMenu)
        self.btn_document.setObjectName(u"btn_document")
        sizePolicy.setHeightForWidth(self.btn_document.sizePolicy().hasHeightForWidth())
        self.btn_document.setSizePolicy(sizePolicy)
        self.btn_document.setMinimumSize(QSize(0, 45))
        self.btn_document.setFont(font)
        self.btn_document.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_document.setLayoutDirection(Qt.LeftToRight)
        self.btn_document.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-description.png);")

        self.verticalLayout_8.addWidget(self.btn_document)

        self.btn_index = QPushButton(self.topMenu)
        self.btn_index.setObjectName(u"btn_index")
        sizePolicy.setHeightForWidth(self.btn_index.sizePolicy().hasHeightForWidth())
        self.btn_index.setSizePolicy(sizePolicy)
        self.btn_index.setMinimumSize(QSize(0, 45))
        self.btn_index.setFont(font)
        self.btn_index.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_index.setLayoutDirection(Qt.LeftToRight)
        self.btn_index.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-folder-open.png);")

        self.verticalLayout_8.addWidget(self.btn_index)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-user.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)

        self.Status_text = QLabel(self.leftBox)
        self.Status_text.setObjectName(u"Status_text")
        self.Status_text.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Status_text.setMargin(0)
        self.Status_text.setIndent(10)

        self.horizontalLayout_3.addWidget(self.Status_text)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setMaximumSize(QSize(16777215, 16777215))
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy2.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy2)
        self.stackedWidget.setMinimumSize(QSize(100, 0))
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image: url(:/images/images/images/Home.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.stackedWidget.addWidget(self.home)
        self.Search = QWidget()
        self.Search.setObjectName(u"Search")
        self.Search.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.Search)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_2 = QFrame(self.Search)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.info_frame_2 = QVBoxLayout()
        self.info_frame_2.setSpacing(0)
        self.info_frame_2.setObjectName(u"info_frame_2")
        self.info_frame_2.setContentsMargins(0, 0, -1, 0)
        self.search_frame = QFrame(self.row_2)
        self.search_frame.setObjectName(u"search_frame")
        self.search_frame.setMinimumSize(QSize(0, 0))
        self.search_frame.setFrameShape(QFrame.StyledPanel)
        self.search_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.search_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelBoxBlenderInstalation_3 = QLabel(self.search_frame)
        self.labelBoxBlenderInstalation_3.setObjectName(u"labelBoxBlenderInstalation_3")
        self.labelBoxBlenderInstalation_3.setFont(font)
        self.labelBoxBlenderInstalation_3.setStyleSheet(u"")

        self.gridLayout.addWidget(self.labelBoxBlenderInstalation_3, 6, 0, 1, 1)

        self.btn_search_doc = QPushButton(self.search_frame)
        self.btn_search_doc.setObjectName(u"btn_search_doc")
        self.btn_search_doc.setMinimumSize(QSize(150, 30))
        self.btn_search_doc.setFont(font)
        self.btn_search_doc.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_search_doc.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-magnifying-glass.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_search_doc.setIcon(icon3)

        self.gridLayout.addWidget(self.btn_search_doc, 4, 1, 1, 1)

        self.Index_combo = QComboBox(self.search_frame)
        self.Index_combo.addItem("")
        self.Index_combo.addItem("")
        self.Index_combo.addItem("")
        self.Index_combo.setObjectName(u"Index_combo")
        self.Index_combo.setFont(font)
        self.Index_combo.setAutoFillBackground(False)
        self.Index_combo.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.Index_combo.setIconSize(QSize(16, 16))
        self.Index_combo.setFrame(True)

        self.gridLayout.addWidget(self.Index_combo, 4, 0, 1, 1)

        self.Field_combo = QComboBox(self.search_frame)
        self.Field_combo.addItem("")
        self.Field_combo.addItem("")
        self.Field_combo.addItem("")
        self.Field_combo.addItem("")
        self.Field_combo.addItem("")
        self.Field_combo.addItem("")
        self.Field_combo.setObjectName(u"Field_combo")
        self.Field_combo.setFont(font)
        self.Field_combo.setAutoFillBackground(False)
        self.Field_combo.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.Field_combo.setIconSize(QSize(16, 16))
        self.Field_combo.setFrame(True)

        self.gridLayout.addWidget(self.Field_combo, 8, 0, 1, 1)

        self.Query_name = QLineEdit(self.search_frame)
        self.Query_name.setObjectName(u"Query_name")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Query_name.sizePolicy().hasHeightForWidth())
        self.Query_name.setSizePolicy(sizePolicy3)
        self.Query_name.setMinimumSize(QSize(0, 30))
        self.Query_name.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.Query_name, 8, 1, 1, 1)

        self.labelBoxBlenderInstalation_2 = QLabel(self.search_frame)
        self.labelBoxBlenderInstalation_2.setObjectName(u"labelBoxBlenderInstalation_2")
        self.labelBoxBlenderInstalation_2.setFont(font)
        self.labelBoxBlenderInstalation_2.setStyleSheet(u"")

        self.gridLayout.addWidget(self.labelBoxBlenderInstalation_2, 1, 0, 1, 1)

        self.labelBoxBlenderInstalation_4 = QLabel(self.search_frame)
        self.labelBoxBlenderInstalation_4.setObjectName(u"labelBoxBlenderInstalation_4")
        self.labelBoxBlenderInstalation_4.setFont(font)
        self.labelBoxBlenderInstalation_4.setStyleSheet(u"")

        self.gridLayout.addWidget(self.labelBoxBlenderInstalation_4, 6, 1, 1, 1)

        self.label_2 = QLabel(self.search_frame)
        self.label_2.setObjectName(u"label_2")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setItalic(False)
        font4.setUnderline(False)
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"font-weight: bold;\n"
"border-radius: 5px;\n"
"border: 2px solid #ff79c6;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)


        self.info_frame_2.addWidget(self.search_frame)

        self.info_frame = QFrame(self.row_2)
        self.info_frame.setObjectName(u"info_frame")
        sizePolicy3.setHeightForWidth(self.info_frame.sizePolicy().hasHeightForWidth())
        self.info_frame.setSizePolicy(sizePolicy3)
        self.info_frame.setMinimumSize(QSize(0, 0))
        self.info_frame.setStyleSheet(u"")
        self.info_frame.setFrameShape(QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.info_frame)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_3 = QLabel(self.info_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font4)
        self.label_3.setStyleSheet(u"font-weight: bold;\n"
"border-radius: 5px;\n"
"border: 2px solid #ff79c6;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_3)

        self.client_text_frame = QFrame(self.info_frame)
        self.client_text_frame.setObjectName(u"client_text_frame")
        self.client_text_frame.setFrameShape(QFrame.StyledPanel)
        self.client_text_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.client_text_frame)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.client_text = QTextBrowser(self.client_text_frame)
        self.client_text.setObjectName(u"client_text")
        self.client_text.setStyleSheet(u"")

        self.verticalLayout_23.addWidget(self.client_text)


        self.verticalLayout_17.addWidget(self.client_text_frame)


        self.info_frame_2.addWidget(self.info_frame)


        self.horizontalLayout_7.addLayout(self.info_frame_2)

        self.response_frame2 = QVBoxLayout()
        self.response_frame2.setSpacing(0)
        self.response_frame2.setObjectName(u"response_frame2")
        self.response_frame2.setContentsMargins(0, -1, -1, -1)
        self.response_json_frame = QFrame(self.row_2)
        self.response_json_frame.setObjectName(u"response_json_frame")
        self.response_json_frame.setFrameShape(QFrame.StyledPanel)
        self.response_json_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.response_json_frame)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_4 = QLabel(self.response_json_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"font-weight: bold;\n"
"border-radius: 5px;\n"
"border: 2px solid #ff79c6;")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_4)

        self.response_json_frame_2 = QFrame(self.response_json_frame)
        self.response_json_frame_2.setObjectName(u"response_json_frame_2")
        self.response_json_frame_2.setFrameShape(QFrame.StyledPanel)
        self.response_json_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.response_json_frame_2)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.response_json = QTextBrowser(self.response_json_frame_2)
        self.response_json.setObjectName(u"response_json")
        self.response_json.setStyleSheet(u"")

        self.verticalLayout_16.addWidget(self.response_json)


        self.verticalLayout_21.addWidget(self.response_json_frame_2)


        self.response_frame2.addWidget(self.response_json_frame)

        self.response_text_frame = QFrame(self.row_2)
        self.response_text_frame.setObjectName(u"response_text_frame")
        self.response_text_frame.setFrameShape(QFrame.StyledPanel)
        self.response_text_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.response_text_frame)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_5 = QLabel(self.response_text_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"font-weight: bold;\n"
"border-radius: 5px;\n"
"border: 2px solid #ff79c6;")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_5)

        self.response_text_frame_2 = QFrame(self.response_text_frame)
        self.response_text_frame_2.setObjectName(u"response_text_frame_2")
        self.response_text_frame_2.setFrameShape(QFrame.StyledPanel)
        self.response_text_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.response_text_frame_2)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.response_text = QTextBrowser(self.response_text_frame_2)
        self.response_text.setObjectName(u"response_text")
        self.response_text.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.response_text)


        self.verticalLayout_22.addWidget(self.response_text_frame_2)


        self.response_frame2.addWidget(self.response_text_frame)


        self.horizontalLayout_7.addLayout(self.response_frame2)


        self.verticalLayout_19.addLayout(self.horizontalLayout_7)


        self.verticalLayout.addWidget(self.row_2)

        self.stackedWidget.addWidget(self.Search)
        self.Document = QWidget()
        self.Document.setObjectName(u"Document")
        self.verticalLayout_20 = QVBoxLayout(self.Document)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(10, 10, 10, 10)
        self.row_3 = QFrame(self.Document)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.row_3)
        self.verticalLayout_24.setSpacing(5)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.info_frame_3 = QVBoxLayout()
        self.info_frame_3.setSpacing(0)
        self.info_frame_3.setObjectName(u"info_frame_3")
        self.info_frame_3.setContentsMargins(0, 0, -1, 0)
        self.search_frame_2 = QFrame(self.row_3)
        self.search_frame_2.setObjectName(u"search_frame_2")
        self.search_frame_2.setMinimumSize(QSize(0, 0))
        self.search_frame_2.setFrameShape(QFrame.StyledPanel)
        self.search_frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.search_frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Index_doc = QComboBox(self.search_frame_2)
        self.Index_doc.addItem("")
        self.Index_doc.addItem("")
        self.Index_doc.addItem("")
        self.Index_doc.setObjectName(u"Index_doc")
        self.Index_doc.setFont(font)
        self.Index_doc.setAutoFillBackground(False)
        self.Index_doc.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.Index_doc.setIconSize(QSize(16, 16))
        self.Index_doc.setFrame(True)

        self.gridLayout_2.addWidget(self.Index_doc, 4, 0, 1, 1)

        self.labelBoxBlenderInstalation_7 = QLabel(self.search_frame_2)
        self.labelBoxBlenderInstalation_7.setObjectName(u"labelBoxBlenderInstalation_7")
        self.labelBoxBlenderInstalation_7.setFont(font)
        self.labelBoxBlenderInstalation_7.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.labelBoxBlenderInstalation_7, 5, 1, 1, 1)

        self.btn_index_doc = QPushButton(self.search_frame_2)
        self.btn_index_doc.setObjectName(u"btn_index_doc")
        self.btn_index_doc.setMinimumSize(QSize(150, 30))
        self.btn_index_doc.setFont(font)
        self.btn_index_doc.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_index_doc.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_index_doc.setIcon(icon4)

        self.gridLayout_2.addWidget(self.btn_index_doc, 7, 0, 1, 2)

        self.labelBoxBlenderInstalation_5 = QLabel(self.search_frame_2)
        self.labelBoxBlenderInstalation_5.setObjectName(u"labelBoxBlenderInstalation_5")
        self.labelBoxBlenderInstalation_5.setFont(font)
        self.labelBoxBlenderInstalation_5.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.labelBoxBlenderInstalation_5, 5, 0, 1, 1)

        self.labelBoxBlenderInstalation_8 = QLabel(self.search_frame_2)
        self.labelBoxBlenderInstalation_8.setObjectName(u"labelBoxBlenderInstalation_8")
        self.labelBoxBlenderInstalation_8.setFont(font)
        self.labelBoxBlenderInstalation_8.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.labelBoxBlenderInstalation_8, 3, 1, 1, 1)

        self.label_6 = QLabel(self.search_frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font4)
        self.label_6.setStyleSheet(u"font-weight: bold;\n"
"border-radius: 5px;\n"
"border: 2px solid #ff79c6;")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 2)

        self.ID_index_doc = QLineEdit(self.search_frame_2)
        self.ID_index_doc.setObjectName(u"ID_index_doc")
        sizePolicy3.setHeightForWidth(self.ID_index_doc.sizePolicy().hasHeightForWidth())
        self.ID_index_doc.setSizePolicy(sizePolicy3)
        self.ID_index_doc.setMinimumSize(QSize(0, 34))
        self.ID_index_doc.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_2.addWidget(self.ID_index_doc, 4, 1, 1, 1)

        self.labelBoxBlenderInstalation_6 = QLabel(self.search_frame_2)
        self.labelBoxBlenderInstalation_6.setObjectName(u"labelBoxBlenderInstalation_6")
        self.labelBoxBlenderInstalation_6.setFont(font)
        self.labelBoxBlenderInstalation_6.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.labelBoxBlenderInstalation_6, 3, 0, 1, 1)

        self.Content_index_doc = QPlainTextEdit(self.search_frame_2)
        self.Content_index_doc.setObjectName(u"Content_index_doc")
        self.Content_index_doc.setMinimumSize(QSize(200, 40))
        self.Content_index_doc.setMaximumSize(QSize(16777215, 16777215))
        self.Content_index_doc.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_2.addWidget(self.Content_index_doc, 6, 1, 1, 1)

        self.Title_index_doc = QPlainTextEdit(self.search_frame_2)
        self.Title_index_doc.setObjectName(u"Title_index_doc")
        self.Title_index_doc.setMinimumSize(QSize(200, 40))
        self.Title_index_doc.setMaximumSize(QSize(16777215, 16777215))
        self.Title_index_doc.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_2.addWidget(self.Title_index_doc, 6, 0, 1, 1)


        self.info_frame_3.addWidget(self.search_frame_2)

        self.info_frame_4 = QFrame(self.row_3)
        self.info_frame_4.setObjectName(u"info_frame_4")
        sizePolicy3.setHeightForWidth(self.info_frame_4.sizePolicy().hasHeightForWidth())
        self.info_frame_4.setSizePolicy(sizePolicy3)
        self.info_frame_4.setMinimumSize(QSize(0, 0))
        self.info_frame_4.setStyleSheet(u"")
        self.info_frame_4.setFrameShape(QFrame.StyledPanel)
        self.info_frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.info_frame_4)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_7 = QLabel(self.info_frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet(u"font-weight: bold;\n"
"border-radius: 5px;\n"
"border: 2px solid #ff79c6;")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_7)

        self.indice_frame = QFrame(self.info_frame_4)
        self.indice_frame.setObjectName(u"indice_frame")
        self.indice_frame.setFrameShape(QFrame.StyledPanel)
        self.indice_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.indice_frame)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.Indices_text = QTextBrowser(self.indice_frame)
        self.Indices_text.setObjectName(u"Indices_text")
        self.Indices_text.setStyleSheet(u"")

        self.verticalLayout_26.addWidget(self.Indices_text)


        self.verticalLayout_25.addWidget(self.indice_frame)


        self.info_frame_3.addWidget(self.info_frame_4)


        self.horizontalLayout_8.addLayout(self.info_frame_3)

        self.response_frame2_2 = QVBoxLayout()
        self.response_frame2_2.setSpacing(0)
        self.response_frame2_2.setObjectName(u"response_frame2_2")
        self.response_frame2_2.setContentsMargins(0, -1, -1, -1)
        self.search_frame_4 = QFrame(self.row_3)
        self.search_frame_4.setObjectName(u"search_frame_4")
        self.search_frame_4.setMinimumSize(QSize(0, 0))
        self.search_frame_4.setFrameShape(QFrame.StyledPanel)
        self.search_frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.search_frame_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.labelBoxBlenderInstalation_9 = QLabel(self.search_frame_4)
        self.labelBoxBlenderInstalation_9.setObjectName(u"labelBoxBlenderInstalation_9")
        self.labelBoxBlenderInstalation_9.setFont(font)
        self.labelBoxBlenderInstalation_9.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.labelBoxBlenderInstalation_9, 1, 1, 1, 1)

        self.Delete_doc_id = QLineEdit(self.search_frame_4)
        self.Delete_doc_id.setObjectName(u"Delete_doc_id")
        sizePolicy3.setHeightForWidth(self.Delete_doc_id.sizePolicy().hasHeightForWidth())
        self.Delete_doc_id.setSizePolicy(sizePolicy3)
        self.Delete_doc_id.setMinimumSize(QSize(0, 34))
        self.Delete_doc_id.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_4.addWidget(self.Delete_doc_id, 2, 1, 1, 1)

        self.Delete_doc_name = QLineEdit(self.search_frame_4)
        self.Delete_doc_name.setObjectName(u"Delete_doc_name")
        sizePolicy3.setHeightForWidth(self.Delete_doc_name.sizePolicy().hasHeightForWidth())
        self.Delete_doc_name.setSizePolicy(sizePolicy3)
        self.Delete_doc_name.setMinimumSize(QSize(0, 34))
        self.Delete_doc_name.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_4.addWidget(self.Delete_doc_name, 2, 0, 1, 1)

        self.labelBoxBlenderInstalation_10 = QLabel(self.search_frame_4)
        self.labelBoxBlenderInstalation_10.setObjectName(u"labelBoxBlenderInstalation_10")
        self.labelBoxBlenderInstalation_10.setFont(font)
        self.labelBoxBlenderInstalation_10.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.labelBoxBlenderInstalation_10, 1, 0, 1, 1)

        self.btn_delete_doc_id = QPushButton(self.search_frame_4)
        self.btn_delete_doc_id.setObjectName(u"btn_delete_doc_id")
        self.btn_delete_doc_id.setMinimumSize(QSize(150, 30))
        self.btn_delete_doc_id.setFont(font)
        self.btn_delete_doc_id.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_delete_doc_id.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete_doc_id.setIcon(icon5)

        self.gridLayout_4.addWidget(self.btn_delete_doc_id, 3, 0, 1, 2)

        self.label_11 = QLabel(self.search_frame_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font4)
        self.label_11.setStyleSheet(u"font-weight: bold;\n"
"border-radius: 5px;\n"
"border: 2px solid #ff79c6;")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_11, 0, 0, 1, 2)


        self.response_frame2_2.addWidget(self.search_frame_4)

        self.response_text_frame_3 = QFrame(self.row_3)
        self.response_text_frame_3.setObjectName(u"response_text_frame_3")
        self.response_text_frame_3.setFrameShape(QFrame.StyledPanel)
        self.response_text_frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.response_text_frame_3)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_9 = QLabel(self.response_text_frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font4)
        self.label_9.setStyleSheet(u"font-weight: bold;\n"
"border-radius: 5px;\n"
"border: 2px solid #ff79c6;")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_9)

        self.result_frame = QFrame(self.response_text_frame_3)
        self.result_frame.setObjectName(u"result_frame")
        self.result_frame.setFrameShape(QFrame.StyledPanel)
        self.result_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.result_frame)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.Result_text = QTextEdit(self.result_frame)
        self.Result_text.setObjectName(u"Result_text")
        self.Result_text.setEnabled(True)
        self.Result_text.setMaximumSize(QSize(16777215, 16777215))
        self.Result_text.setReadOnly(True)

        self.verticalLayout_30.addWidget(self.Result_text)


        self.verticalLayout_29.addWidget(self.result_frame)


        self.response_frame2_2.addWidget(self.response_text_frame_3)


        self.horizontalLayout_8.addLayout(self.response_frame2_2)


        self.verticalLayout_24.addLayout(self.horizontalLayout_8)


        self.verticalLayout_20.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.Document)
        self.Index = QWidget()
        self.Index.setObjectName(u"Index")
        self.verticalLayout_38 = QVBoxLayout(self.Index)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(10, 10, 10, 10)
        self.row_4 = QFrame(self.Index)
        self.row_4.setObjectName(u"row_4")
        self.row_4.setMinimumSize(QSize(0, 150))
        self.row_4.setFrameShape(QFrame.StyledPanel)
        self.row_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.row_4)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, -1)
        self.info_frame_5 = QVBoxLayout()
        self.info_frame_5.setSpacing(0)
        self.info_frame_5.setObjectName(u"info_frame_5")
        self.info_frame_5.setContentsMargins(0, 0, -1, 0)
        self.search_frame_3 = QFrame(self.row_4)
        self.search_frame_3.setObjectName(u"search_frame_3")
        self.search_frame_3.setMinimumSize(QSize(0, 0))
        self.search_frame_3.setFrameShape(QFrame.StyledPanel)
        self.search_frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.search_frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btn_delete_index = QPushButton(self.search_frame_3)
        self.btn_delete_index.setObjectName(u"btn_delete_index")
        self.btn_delete_index.setMinimumSize(QSize(150, 30))
        self.btn_delete_index.setFont(font)
        self.btn_delete_index.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_delete_index.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete_index.setIcon(icon6)

        self.gridLayout_3.addWidget(self.btn_delete_index, 10, 1, 1, 1)

        self.labelBoxBlenderInstalation_16 = QLabel(self.search_frame_3)
        self.labelBoxBlenderInstalation_16.setObjectName(u"labelBoxBlenderInstalation_16")
        self.labelBoxBlenderInstalation_16.setFont(font)
        self.labelBoxBlenderInstalation_16.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.labelBoxBlenderInstalation_16, 9, 0, 1, 1)

        self.label_14 = QLabel(self.search_frame_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font4)
        self.label_14.setStyleSheet(u"font-weight: bold;\n"
"border-radius: 5px;\n"
"border: 2px solid #ff79c6;")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_14, 0, 0, 1, 2)

        self.Delete_index = QLineEdit(self.search_frame_3)
        self.Delete_index.setObjectName(u"Delete_index")
        sizePolicy3.setHeightForWidth(self.Delete_index.sizePolicy().hasHeightForWidth())
        self.Delete_index.setSizePolicy(sizePolicy3)
        self.Delete_index.setMinimumSize(QSize(0, 34))
        self.Delete_index.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_3.addWidget(self.Delete_index, 10, 0, 1, 1)

        self.btn_create_index = QPushButton(self.search_frame_3)
        self.btn_create_index.setObjectName(u"btn_create_index")
        self.btn_create_index.setMinimumSize(QSize(150, 30))
        self.btn_create_index.setFont(font)
        self.btn_create_index.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_create_index.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/cil-cloud-upload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_create_index.setIcon(icon7)

        self.gridLayout_3.addWidget(self.btn_create_index, 2, 1, 1, 1)

        self.Create_index = QLineEdit(self.search_frame_3)
        self.Create_index.setObjectName(u"Create_index")
        sizePolicy3.setHeightForWidth(self.Create_index.sizePolicy().hasHeightForWidth())
        self.Create_index.setSizePolicy(sizePolicy3)
        self.Create_index.setMinimumSize(QSize(0, 30))
        self.Create_index.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_3.addWidget(self.Create_index, 2, 0, 1, 1)

        self.labelBoxBlenderInstalation_15 = QLabel(self.search_frame_3)
        self.labelBoxBlenderInstalation_15.setObjectName(u"labelBoxBlenderInstalation_15")
        self.labelBoxBlenderInstalation_15.setFont(font)
        self.labelBoxBlenderInstalation_15.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.labelBoxBlenderInstalation_15, 1, 0, 1, 1)

        self.label_13 = QLabel(self.search_frame_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font4)
        self.label_13.setStyleSheet(u"font-weight: bold;\n"
"border-radius: 5px;\n"
"border: 2px solid #ff79c6;")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_13, 5, 0, 1, 2)


        self.info_frame_5.addWidget(self.search_frame_3)

        self.info_frame_6 = QFrame(self.row_4)
        self.info_frame_6.setObjectName(u"info_frame_6")
        sizePolicy3.setHeightForWidth(self.info_frame_6.sizePolicy().hasHeightForWidth())
        self.info_frame_6.setSizePolicy(sizePolicy3)
        self.info_frame_6.setMinimumSize(QSize(0, 0))
        self.info_frame_6.setStyleSheet(u"")
        self.info_frame_6.setFrameShape(QFrame.StyledPanel)
        self.info_frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.info_frame_6)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_19 = QLabel(self.info_frame_6)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font4)
        self.label_19.setStyleSheet(u"font-weight: bold;\n"
"border-radius: 5px;\n"
"border: 2px solid #ff79c6;")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_19)

        self.indice_frame_2 = QFrame(self.info_frame_6)
        self.indice_frame_2.setObjectName(u"indice_frame_2")
        self.indice_frame_2.setFrameShape(QFrame.StyledPanel)
        self.indice_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.indice_frame_2)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.Indices_text_2 = QTextBrowser(self.indice_frame_2)
        self.Indices_text_2.setObjectName(u"Indices_text_2")
        self.Indices_text_2.setStyleSheet(u"")

        self.verticalLayout_37.addWidget(self.Indices_text_2)


        self.verticalLayout_32.addWidget(self.indice_frame_2)

        self.Danger_zone_frame = QFrame(self.info_frame_6)
        self.Danger_zone_frame.setObjectName(u"Danger_zone_frame")
        self.Danger_zone_frame.setMinimumSize(QSize(0, 0))
        self.Danger_zone_frame.setFrameShape(QFrame.StyledPanel)
        self.Danger_zone_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.Danger_zone_frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.Password_del_all = QLineEdit(self.Danger_zone_frame)
        self.Password_del_all.setObjectName(u"Password_del_all")
        sizePolicy3.setHeightForWidth(self.Password_del_all.sizePolicy().hasHeightForWidth())
        self.Password_del_all.setSizePolicy(sizePolicy3)
        self.Password_del_all.setMinimumSize(QSize(0, 30))
        self.Password_del_all.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.Password_del_all.setEchoMode(QLineEdit.Password)

        self.gridLayout_5.addWidget(self.Password_del_all, 2, 0, 1, 1)

        self.btn_del_all = QPushButton(self.Danger_zone_frame)
        self.btn_del_all.setObjectName(u"btn_del_all")
        self.btn_del_all.setMinimumSize(QSize(150, 30))
        self.btn_del_all.setFont(font)
        self.btn_del_all.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_del_all.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"color: #ff5555;\n"
"")

        self.gridLayout_5.addWidget(self.btn_del_all, 2, 1, 1, 1)

        self.labelBoxBlenderInstalation_22 = QLabel(self.Danger_zone_frame)
        self.labelBoxBlenderInstalation_22.setObjectName(u"labelBoxBlenderInstalation_22")
        self.labelBoxBlenderInstalation_22.setFont(font)
        self.labelBoxBlenderInstalation_22.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.labelBoxBlenderInstalation_22, 1, 0, 1, 1)

        self.label_20 = QLabel(self.Danger_zone_frame)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font4)
        self.label_20.setStyleSheet(u"font-weight: bold;\n"
"border-radius: 5px;\n"
"border: 2px solid #ff5555;")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_20, 0, 0, 1, 2)


        self.verticalLayout_32.addWidget(self.Danger_zone_frame)


        self.info_frame_5.addWidget(self.info_frame_6)


        self.horizontalLayout_9.addLayout(self.info_frame_5)

        self.response_frame2_3 = QVBoxLayout()
        self.response_frame2_3.setSpacing(0)
        self.response_frame2_3.setObjectName(u"response_frame2_3")
        self.response_frame2_3.setContentsMargins(0, -1, -1, -1)
        self.response_json_frame_4 = QFrame(self.row_4)
        self.response_json_frame_4.setObjectName(u"response_json_frame_4")
        self.response_json_frame_4.setFrameShape(QFrame.StyledPanel)
        self.response_json_frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.response_json_frame_4)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_17 = QLabel(self.response_json_frame_4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font4)
        self.label_17.setStyleSheet(u"font-weight: bold;\n"
"border-radius: 5px;\n"
"border: 2px solid #ff79c6;")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.label_17)

        self.result_frame_2 = QFrame(self.response_json_frame_4)
        self.result_frame_2.setObjectName(u"result_frame_2")
        self.result_frame_2.setFrameShape(QFrame.StyledPanel)
        self.result_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.result_frame_2)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.Result_text_2 = QTextEdit(self.result_frame_2)
        self.Result_text_2.setObjectName(u"Result_text_2")
        self.Result_text_2.setEnabled(True)
        self.Result_text_2.setMaximumSize(QSize(16777215, 16777215))
        self.Result_text_2.setReadOnly(True)

        self.verticalLayout_33.addWidget(self.Result_text_2)


        self.verticalLayout_34.addWidget(self.result_frame_2)


        self.response_frame2_3.addWidget(self.response_json_frame_4)

        self.response_text_frame_4 = QFrame(self.row_4)
        self.response_text_frame_4.setObjectName(u"response_text_frame_4")
        self.response_text_frame_4.setFrameShape(QFrame.StyledPanel)
        self.response_text_frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.response_text_frame_4)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_18 = QLabel(self.response_text_frame_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font4)
        self.label_18.setStyleSheet(u"font-weight: bold;\n"
"border-radius: 5px;\n"
"border: 2px solid #ff79c6;")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_36.addWidget(self.label_18)

        self.health_frame_2 = QFrame(self.response_text_frame_4)
        self.health_frame_2.setObjectName(u"health_frame_2")
        self.health_frame_2.setFrameShape(QFrame.StyledPanel)
        self.health_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.health_frame_2)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.Health_text_2 = QTextBrowser(self.health_frame_2)
        self.Health_text_2.setObjectName(u"Health_text_2")
        self.Health_text_2.setStyleSheet(u"")

        self.verticalLayout_35.addWidget(self.Health_text_2)


        self.verticalLayout_36.addWidget(self.health_frame_2)


        self.response_frame2_3.addWidget(self.response_text_frame_4)


        self.horizontalLayout_9.addLayout(self.response_frame2_3)


        self.verticalLayout_31.addLayout(self.horizontalLayout_9)


        self.verticalLayout_38.addWidget(self.row_4)

        self.stackedWidget.addWidget(self.Index)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font5 = QFont()
        font5.setBold(False)
        font5.setItalic(False)
        self.creditsLabel.setFont(font5)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)
        QWidget.setTabOrder(self.minimizeAppBtn, self.maximizeRestoreAppBtn)
        QWidget.setTabOrder(self.maximizeRestoreAppBtn, self.client_text)
        QWidget.setTabOrder(self.client_text, self.Title_index_doc)
        QWidget.setTabOrder(self.Title_index_doc, self.btn_index_doc)
        QWidget.setTabOrder(self.btn_index_doc, self.response_json)
        QWidget.setTabOrder(self.response_json, self.response_text)
        QWidget.setTabOrder(self.response_text, self.Content_index_doc)
        QWidget.setTabOrder(self.Content_index_doc, self.Result_text)
        QWidget.setTabOrder(self.Result_text, self.Index_combo)
        QWidget.setTabOrder(self.Index_combo, self.Field_combo)
        QWidget.setTabOrder(self.Field_combo, self.btn_document)
        QWidget.setTabOrder(self.btn_document, self.Indices_text)
        QWidget.setTabOrder(self.Indices_text, self.btn_search)
        QWidget.setTabOrder(self.btn_search, self.btn_index)
        QWidget.setTabOrder(self.btn_index, self.closeAppBtn)
        QWidget.setTabOrder(self.closeAppBtn, self.toggleButton)
        QWidget.setTabOrder(self.toggleButton, self.btn_home)
        QWidget.setTabOrder(self.btn_home, self.Query_name)
        QWidget.setTabOrder(self.Query_name, self.btn_search_doc)
        QWidget.setTabOrder(self.btn_search_doc, self.toggleLeftBox)
        QWidget.setTabOrder(self.toggleLeftBox, self.extraCloseColumnBtn)
        QWidget.setTabOrder(self.extraCloseColumnBtn, self.textEdit)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"Elasticsearch", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Covid-19 Information ", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.btn_document.setText(QCoreApplication.translate("MainWindow", u"Document", None))
        self.btn_index.setText(QCoreApplication.translate("MainWindow", u"Index", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Info", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Elasticsearch for Covid-19 Information Application</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This application use elasticsearch to search about Covid-19 Information for Information Storage and Web Search assignment in 1/2564</p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-i"
                        "ndent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: <br />Kridsanapong Buathongjun</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Elasticsearch for Covid-19 Information Application", None))
        self.Status_text.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.labelBoxBlenderInstalation_3.setText(QCoreApplication.translate("MainWindow", u"Field name here..", None))
        self.btn_search_doc.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.Index_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"test-covid", None))
        self.Index_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"test1", None))
        self.Index_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"covid-19", None))

        self.Field_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"Title", None))
        self.Field_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Content", None))
        self.Field_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"firstname", None))
        self.Field_combo.setItemText(3, QCoreApplication.translate("MainWindow", u"lastname", None))
        self.Field_combo.setItemText(4, QCoreApplication.translate("MainWindow", u"age", None))
        self.Field_combo.setItemText(5, QCoreApplication.translate("MainWindow", u"gender", None))

        self.Query_name.setText("")
        self.Query_name.setPlaceholderText("")
        self.labelBoxBlenderInstalation_2.setText(QCoreApplication.translate("MainWindow", u"Index Name", None))
        self.labelBoxBlenderInstalation_4.setText(QCoreApplication.translate("MainWindow", u"Query match here..", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Search document", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Client info", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Response in json format", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Response in txt format", None))
        self.Index_doc.setItemText(0, QCoreApplication.translate("MainWindow", u"test-covid", None))
        self.Index_doc.setItemText(1, QCoreApplication.translate("MainWindow", u"test1", None))
        self.Index_doc.setItemText(2, QCoreApplication.translate("MainWindow", u"test2", None))

        self.labelBoxBlenderInstalation_7.setText(QCoreApplication.translate("MainWindow", u"Content", None))
        self.btn_index_doc.setText(QCoreApplication.translate("MainWindow", u"Index document", None))
        self.labelBoxBlenderInstalation_5.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.labelBoxBlenderInstalation_8.setText(QCoreApplication.translate("MainWindow", u"Type ID create", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Create or Update document", None))
        self.ID_index_doc.setText("")
        self.ID_index_doc.setPlaceholderText("")
        self.labelBoxBlenderInstalation_6.setText(QCoreApplication.translate("MainWindow", u"Index name", None))
        self.Title_index_doc.setPlainText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Indices info", None))
        self.labelBoxBlenderInstalation_9.setText(QCoreApplication.translate("MainWindow", u"Type ID to delete.", None))
        self.Delete_doc_id.setText("")
        self.Delete_doc_id.setPlaceholderText("")
        self.Delete_doc_name.setText("")
        self.Delete_doc_name.setPlaceholderText("")
        self.labelBoxBlenderInstalation_10.setText(QCoreApplication.translate("MainWindow", u"Index name", None))
        self.btn_delete_doc_id.setText(QCoreApplication.translate("MainWindow", u"Delete document", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Delete document", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Result", None))
        self.btn_delete_index.setText(QCoreApplication.translate("MainWindow", u"Delete Index", None))
        self.labelBoxBlenderInstalation_16.setText(QCoreApplication.translate("MainWindow", u"Type index to delete.", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Create Index", None))
        self.Delete_index.setText("")
        self.Delete_index.setPlaceholderText("")
        self.btn_create_index.setText(QCoreApplication.translate("MainWindow", u"Create Index", None))
        self.Create_index.setText("")
        self.Create_index.setPlaceholderText("")
        self.labelBoxBlenderInstalation_15.setText(QCoreApplication.translate("MainWindow", u"Type new create index.", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Delete Index", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Indices info", None))
        self.Password_del_all.setText("")
        self.Password_del_all.setPlaceholderText("")
        self.btn_del_all.setText(QCoreApplication.translate("MainWindow", u"Delete All", None))
        self.labelBoxBlenderInstalation_22.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Delete ALL", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Result", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Cluster health", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Kridsanapong Buathongjun", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.5", None))
    # retranslateUi


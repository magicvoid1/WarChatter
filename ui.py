# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warchatter.ui'
#
# Created: Thu Oct 20 16:37:59 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(808, 609)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 0, 791, 561))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page_login = QtGui.QWidget()
        self.page_login.setObjectName(_fromUtf8("page_login"))
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.page_login)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 781, 531))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_5.addWidget(self.label_3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_title = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.label_title.setObjectName(_fromUtf8("label_title"))
        self.verticalLayout_6.addWidget(self.label_title)
        self.input_username = QtGui.QLineEdit(self.verticalLayoutWidget_4)
        self.input_username.setObjectName(_fromUtf8("input_username"))
        self.verticalLayout_6.addWidget(self.input_username)
        self.input_password = QtGui.QLineEdit(self.verticalLayoutWidget_4)
        self.input_password.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.input_password.setEchoMode(QtGui.QLineEdit.Password)
        self.input_password.setObjectName(_fromUtf8("input_password"))
        self.verticalLayout_6.addWidget(self.input_password)
        self.input_server = QtGui.QLineEdit(self.verticalLayoutWidget_4)
        self.input_server.setObjectName(_fromUtf8("input_server"))
        self.verticalLayout_6.addWidget(self.input_server)
        self.input_channel = QtGui.QLineEdit(self.verticalLayoutWidget_4)
        self.input_channel.setObjectName(_fromUtf8("input_channel"))
        self.verticalLayout_6.addWidget(self.input_channel)
        self.input_client_tag = QtGui.QLineEdit(self.verticalLayoutWidget_4)
        self.input_client_tag.setObjectName(_fromUtf8("input_client_tag"))
        self.verticalLayout_6.addWidget(self.input_client_tag)
        self.button_login = QtGui.QPushButton(self.verticalLayoutWidget_4)
        self.button_login.setObjectName(_fromUtf8("button_login"))
        self.verticalLayout_6.addWidget(self.button_login)
        self.label_status_msg = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.label_status_msg.setText(_fromUtf8(""))
        self.label_status_msg.setObjectName(_fromUtf8("label_status_msg"))
        self.verticalLayout_6.addWidget(self.label_status_msg)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.stackedWidget.addWidget(self.page_login)
        self.page_chat = QtGui.QWidget()
        self.page_chat.setObjectName(_fromUtf8("page_chat"))
        self.verticalLayoutWidget = QtGui.QWidget(self.page_chat)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 781, 541))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_warchatter = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_warchatter.setObjectName(_fromUtf8("label_warchatter"))
        self.horizontalLayout.addWidget(self.label_warchatter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_channel = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_channel.setObjectName(_fromUtf8("label_channel"))
        self.verticalLayout.addWidget(self.label_channel)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.button_channel = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_channel.setObjectName(_fromUtf8("button_channel"))
        self.verticalLayout_9.addWidget(self.button_channel)
        self.button_create = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_create.setEnabled(False)
        self.button_create.setObjectName(_fromUtf8("button_create"))
        self.verticalLayout_9.addWidget(self.button_create)
        self.button_join = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_join.setEnabled(True)
        self.button_join.setObjectName(_fromUtf8("button_join"))
        self.verticalLayout_9.addWidget(self.button_join)
        self.button_ladder = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_ladder.setEnabled(False)
        self.button_ladder.setObjectName(_fromUtf8("button_ladder"))
        self.verticalLayout_9.addWidget(self.button_ladder)
        self.button_quit = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_quit.setObjectName(_fromUtf8("button_quit"))
        self.verticalLayout_9.addWidget(self.button_quit)
        self.horizontalLayout_3.addLayout(self.verticalLayout_9)
        self.textedit_chat = QtGui.QTextBrowser(self.verticalLayoutWidget)
        self.textedit_chat.setAutoFillBackground(False)
        self.textedit_chat.setOpenExternalLinks(True)
        self.textedit_chat.setObjectName(_fromUtf8("textedit_chat"))
        self.horizontalLayout_3.addWidget(self.textedit_chat)
        self.list_users = QtGui.QListWidget(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_users.sizePolicy().hasHeightForWidth())
        self.list_users.setSizePolicy(sizePolicy)
        self.list_users.setMinimumSize(QtCore.QSize(175, 0))
        self.list_users.setMaximumSize(QtCore.QSize(175, 16777215))
        self.list_users.setStyleSheet(_fromUtf8("background-color: gray\n"
""))
        self.list_users.setObjectName(_fromUtf8("list_users"))
        self.horizontalLayout_3.addWidget(self.list_users)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.input_msg = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.input_msg.setObjectName(_fromUtf8("input_msg"))
        self.horizontalLayout_4.addWidget(self.input_msg)
        self.button_send = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_send.setObjectName(_fromUtf8("button_send"))
        self.horizontalLayout_4.addWidget(self.button_send)
        self.button_whisper = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_whisper.setObjectName(_fromUtf8("button_whisper"))
        self.horizontalLayout_4.addWidget(self.button_whisper)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.stackedWidget.addWidget(self.page_chat)
        self.page_games = QtGui.QWidget()
        self.page_games.setObjectName(_fromUtf8("page_games"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.page_games)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 781, 541))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_10.setMargin(0)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout_10.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_13 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_5.addWidget(self.label_13)
        self.verticalLayout_10.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.horizontalLayout_22 = QtGui.QHBoxLayout()
        self.horizontalLayout_22.setObjectName(_fromUtf8("horizontalLayout_22"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.combo_game_type = QtGui.QComboBox(self.verticalLayoutWidget_3)
        self.combo_game_type.setObjectName(_fromUtf8("combo_game_type"))
        self.combo_game_type.addItem(_fromUtf8(""))
        self.combo_game_type.addItem(_fromUtf8(""))
        self.combo_game_type.addItem(_fromUtf8(""))
        self.combo_game_type.addItem(_fromUtf8(""))
        self.combo_game_type.addItem(_fromUtf8(""))
        self.combo_game_type.addItem(_fromUtf8(""))
        self.combo_game_type.addItem(_fromUtf8(""))
        self.combo_game_type.addItem(_fromUtf8(""))
        self.verticalLayout_8.addWidget(self.combo_game_type)
        self.verticalLayout_14 = QtGui.QVBoxLayout()
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.list_games = QtGui.QListWidget(self.verticalLayoutWidget_3)
        self.list_games.setObjectName(_fromUtf8("list_games"))
        self.verticalLayout_14.addWidget(self.list_games)
        self.verticalLayout_8.addLayout(self.verticalLayout_14)
        self.horizontalLayout_22.addLayout(self.verticalLayout_8)
        self.horizontalLayout_21.addLayout(self.horizontalLayout_22)
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.label_14 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.verticalLayout_11.addWidget(self.label_14)
        self.lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout_11.addWidget(self.lineEdit)
        self.label_15 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.verticalLayout_11.addWidget(self.label_15)
        self.lineEdit_2 = QtGui.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.verticalLayout_11.addWidget(self.lineEdit_2)
        self.textedit_game_info = QtGui.QTextBrowser(self.verticalLayoutWidget_3)
        self.textedit_game_info.setObjectName(_fromUtf8("textedit_game_info"))
        self.verticalLayout_11.addWidget(self.textedit_game_info)
        self.horizontalLayout_21.addLayout(self.verticalLayout_11)
        self.verticalLayout_10.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.button_send_13 = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.button_send_13.setEnabled(False)
        self.button_send_13.setObjectName(_fromUtf8("button_send_13"))
        self.horizontalLayout_7.addWidget(self.button_send_13)
        self.button_cancel_games = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.button_cancel_games.setObjectName(_fromUtf8("button_cancel_games"))
        self.horizontalLayout_7.addWidget(self.button_cancel_games)
        self.verticalLayout_10.addLayout(self.horizontalLayout_7)
        self.stackedWidget.addWidget(self.page_games)
        self.page_profile = QtGui.QWidget()
        self.page_profile.setObjectName(_fromUtf8("page_profile"))
        self.verticalLayoutWidget_5 = QtGui.QWidget(self.page_profile)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(0, 20, 781, 541))
        self.verticalLayoutWidget_5.setObjectName(_fromUtf8("verticalLayoutWidget_5"))
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_12.setMargin(0)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_8.addWidget(self.label_4)
        self.verticalLayout_12.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.verticalLayout_13 = QtGui.QVBoxLayout()
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_11.addWidget(self.label)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem5)
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_11.addWidget(self.label_5)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem6)
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_11.addWidget(self.label_6)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem7)
        self.verticalLayout_13.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.texredit_name = QtGui.QTextEdit(self.verticalLayoutWidget_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.texredit_name.sizePolicy().hasHeightForWidth())
        self.texredit_name.setSizePolicy(sizePolicy)
        self.texredit_name.setMaximumSize(QtCore.QSize(200, 25))
        self.texredit_name.setReadOnly(True)
        self.texredit_name.setObjectName(_fromUtf8("texredit_name"))
        self.horizontalLayout_15.addWidget(self.texredit_name)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem8)
        self.textedit_sex = QtGui.QTextEdit(self.verticalLayoutWidget_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textedit_sex.sizePolicy().hasHeightForWidth())
        self.textedit_sex.setSizePolicy(sizePolicy)
        self.textedit_sex.setMaximumSize(QtCore.QSize(100, 25))
        self.textedit_sex.setReadOnly(True)
        self.textedit_sex.setObjectName(_fromUtf8("textedit_sex"))
        self.horizontalLayout_15.addWidget(self.textedit_sex)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem9)
        self.textedit_age = QtGui.QTextEdit(self.verticalLayoutWidget_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textedit_age.sizePolicy().hasHeightForWidth())
        self.textedit_age.setSizePolicy(sizePolicy)
        self.textedit_age.setMaximumSize(QtCore.QSize(100, 25))
        self.textedit_age.setReadOnly(True)
        self.textedit_age.setObjectName(_fromUtf8("textedit_age"))
        self.horizontalLayout_15.addWidget(self.textedit_age)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem10)
        self.verticalLayout_13.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_7 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_13.addWidget(self.label_7)
        self.verticalLayout_13.addLayout(self.horizontalLayout_13)
        self.textedit_location = QtGui.QTextBrowser(self.verticalLayoutWidget_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textedit_location.sizePolicy().hasHeightForWidth())
        self.textedit_location.setSizePolicy(sizePolicy)
        self.textedit_location.setMinimumSize(QtCore.QSize(0, 0))
        self.textedit_location.setMaximumSize(QtCore.QSize(16777215, 25))
        self.textedit_location.setObjectName(_fromUtf8("textedit_location"))
        self.verticalLayout_13.addWidget(self.textedit_location)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_8 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_12.addWidget(self.label_8)
        self.verticalLayout_13.addLayout(self.horizontalLayout_12)
        self.textedit_description = QtGui.QTextBrowser(self.verticalLayoutWidget_5)
        self.textedit_description.setObjectName(_fromUtf8("textedit_description"))
        self.verticalLayout_13.addWidget(self.textedit_description)
        spacerItem11 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem11)
        self.horizontalLayout_9.addLayout(self.verticalLayout_13)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.textedit_stats = QtGui.QTextBrowser(self.verticalLayoutWidget_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textedit_stats.sizePolicy().hasHeightForWidth())
        self.textedit_stats.setSizePolicy(sizePolicy)
        self.textedit_stats.setSizeIncrement(QtCore.QSize(0, 0))
        self.textedit_stats.setObjectName(_fromUtf8("textedit_stats"))
        self.verticalLayout_3.addWidget(self.textedit_stats)
        self.horizontalLayout_9.addLayout(self.verticalLayout_3)
        self.verticalLayout_12.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem12)
        self.button_ok_profile = QtGui.QPushButton(self.verticalLayoutWidget_5)
        self.button_ok_profile.setEnabled(False)
        self.button_ok_profile.setObjectName(_fromUtf8("button_ok_profile"))
        self.horizontalLayout_10.addWidget(self.button_ok_profile)
        self.button_cancel_profile = QtGui.QPushButton(self.verticalLayoutWidget_5)
        self.button_cancel_profile.setObjectName(_fromUtf8("button_cancel_profile"))
        self.horizontalLayout_10.addWidget(self.button_cancel_profile)
        self.verticalLayout_12.addLayout(self.horizontalLayout_10)
        self.stackedWidget.addWidget(self.page_profile)
        self.page_channels = QtGui.QWidget()
        self.page_channels.setObjectName(_fromUtf8("page_channels"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.page_channels)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 20, 781, 541))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.label_warchatter_2 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_warchatter_2.setObjectName(_fromUtf8("label_warchatter_2"))
        self.horizontalLayout_16.addWidget(self.label_warchatter_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_9 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_4.addWidget(self.label_9)
        self.list_channels = QtGui.QListWidget(self.verticalLayoutWidget_2)
        self.list_channels.setObjectName(_fromUtf8("list_channels"))
        self.verticalLayout_4.addWidget(self.list_channels)
        self.horizontalLayout_19.addLayout(self.verticalLayout_4)
        self.horizontalLayout_17.addLayout(self.horizontalLayout_19)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_10 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_7.addWidget(self.label_10)
        spacerItem13 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem13)
        self.label_11 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_7.addWidget(self.label_11)
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.label_12 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_20.addWidget(self.label_12)
        self.input_channel_2 = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.input_channel_2.setObjectName(_fromUtf8("input_channel_2"))
        self.horizontalLayout_20.addWidget(self.input_channel_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_20)
        spacerItem14 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem14)
        self.horizontalLayout_17.addLayout(self.verticalLayout_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        spacerItem15 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem15)
        self.button_ok_channel = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.button_ok_channel.setObjectName(_fromUtf8("button_ok_channel"))
        self.horizontalLayout_18.addWidget(self.button_ok_channel)
        self.button_cancel_channel = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.button_cancel_channel.setObjectName(_fromUtf8("button_cancel_channel"))
        self.horizontalLayout_18.addWidget(self.button_cancel_channel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_18)
        self.stackedWidget.addWidget(self.page_channels)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/warchatter/warchatter.png\"/></p></body></html>", None))
        self.label_title.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">PvPGN Login Info</span></p></body></html>", None))
        self.input_username.setPlaceholderText(_translate("MainWindow", "Username", None))
        self.input_password.setPlaceholderText(_translate("MainWindow", "Password", None))
        self.input_server.setText(_translate("MainWindow", "server.war2.ru", None))
        self.input_server.setPlaceholderText(_translate("MainWindow", "Server", None))
        self.input_channel.setText(_translate("MainWindow", "War2BNE", None))
        self.input_channel.setPlaceholderText(_translate("MainWindow", "Channel", None))
        self.input_client_tag.setText(_translate("MainWindow", "W2BN", None))
        self.input_client_tag.setPlaceholderText(_translate("MainWindow", "Game Tag", None))
        self.button_login.setText(_translate("MainWindow", "Login", None))
        self.label_warchatter.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/warchatter/warchatter.png\"/></p></body></html>", None))
        self.label_channel.setText(_translate("MainWindow", "TextLabel", None))
        self.button_channel.setText(_translate("MainWindow", "Channel", None))
        self.button_create.setText(_translate("MainWindow", "Create", None))
        self.button_join.setText(_translate("MainWindow", "Join", None))
        self.button_ladder.setText(_translate("MainWindow", "Ladder", None))
        self.button_quit.setText(_translate("MainWindow", "Quit", None))
        self.textedit_chat.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\" bgcolor=\"#000000\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.button_send.setText(_translate("MainWindow", "Send", None))
        self.button_whisper.setText(_translate("MainWindow", "Whisper", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/warchatter/warchatter.png\"/></p></body></html>", None))
        self.label_13.setText(_translate("MainWindow", "Join Game", None))
        self.combo_game_type.setItemText(0, _translate("MainWindow", "Show All", None))
        self.combo_game_type.setItemText(1, _translate("MainWindow", "Top Vs Bottom", None))
        self.combo_game_type.setItemText(2, _translate("MainWindow", "Melee", None))
        self.combo_game_type.setItemText(3, _translate("MainWindow", "Free For All", None))
        self.combo_game_type.setItemText(4, _translate("MainWindow", "One on One", None))
        self.combo_game_type.setItemText(5, _translate("MainWindow", "Use Map Settings", None))
        self.combo_game_type.setItemText(6, _translate("MainWindow", "Ladder", None))
        self.combo_game_type.setItemText(7, _translate("MainWindow", "Iron Man Ladder", None))
        self.label_14.setText(_translate("MainWindow", "Game name:", None))
        self.label_15.setText(_translate("MainWindow", "Private game password:", None))
        self.button_send_13.setText(_translate("MainWindow", "OK", None))
        self.button_cancel_games.setText(_translate("MainWindow", "Cancel", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/warchatter/warchatter.png\"/></p></body></html>", None))
        self.label.setText(_translate("MainWindow", "Name", None))
        self.label_5.setText(_translate("MainWindow", "Sex", None))
        self.label_6.setText(_translate("MainWindow", "Age", None))
        self.label_7.setText(_translate("MainWindow", "Location", None))
        self.label_8.setText(_translate("MainWindow", "Description", None))
        self.button_ok_profile.setText(_translate("MainWindow", "OK", None))
        self.button_cancel_profile.setText(_translate("MainWindow", "Cancel", None))
        self.label_warchatter_2.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/warchatter/warchatter.png\"/></p></body></html>", None))
        self.label_9.setText(_translate("MainWindow", "Channels", None))
        self.label_10.setText(_translate("MainWindow", "Select Channel", None))
        self.label_11.setText(_translate("MainWindow", "To join or create a Private Channel, enter a name below.", None))
        self.label_12.setText(_translate("MainWindow", "Channel: ", None))
        self.button_ok_channel.setText(_translate("MainWindow", "Ok", None))
        self.button_cancel_channel.setText(_translate("MainWindow", "Cancel", None))

import resources_rc

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'icepapcms.ui'
#
# Created: Mon Oct 27 13:00:47 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_IcepapCMS(object):
    def setupUi(self, IcepapCMS):
        IcepapCMS.setObjectName("IcepapCMS")
        IcepapCMS.resize(QtCore.QSize(QtCore.QRect(0,0,1100,801).size()).expandedTo(IcepapCMS.minimumSizeHint()))

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(IcepapCMS.sizePolicy().hasHeightForWidth())
        IcepapCMS.setSizePolicy(sizePolicy)

        palette = QtGui.QPalette()

        brush = QtGui.QBrush(QtGui.QColor(101,148,235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Highlight,brush)

        brush = QtGui.QBrush(QtGui.QColor(101,148,235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Highlight,brush)

        brush = QtGui.QBrush(QtGui.QColor(127,125,123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Highlight,brush)
        IcepapCMS.setPalette(palette)
        IcepapCMS.setWindowIcon(QtGui.QIcon(":/small_icons/IcepapCfg Icons/Icepapicon.png"))

        self.centralwidget = QtGui.QWidget(IcepapCMS)
        self.centralwidget.setObjectName("centralwidget")

        self.vboxlayout = QtGui.QVBoxLayout(self.centralwidget)
        self.vboxlayout.setSpacing(1)
        self.vboxlayout.setMargin(1)
        self.vboxlayout.setObjectName("vboxlayout")

        self.frLocationBar = QtGui.QFrame(self.centralwidget)
        self.frLocationBar.setFrameShape(QtGui.QFrame.NoFrame)
        self.frLocationBar.setFrameShadow(QtGui.QFrame.Raised)
        self.frLocationBar.setObjectName("frLocationBar")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.frLocationBar)
        self.vboxlayout1.setSpacing(1)
        self.vboxlayout1.setMargin(1)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.frLocationBarText = QtGui.QFrame(self.frLocationBar)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frLocationBarText.sizePolicy().hasHeightForWidth())
        self.frLocationBarText.setSizePolicy(sizePolicy)
        self.frLocationBarText.setMinimumSize(QtCore.QSize(16,40))
        self.frLocationBarText.setMaximumSize(QtCore.QSize(16777215,40))
        self.frLocationBarText.setFrameShape(QtGui.QFrame.NoFrame)
        self.frLocationBarText.setFrameShadow(QtGui.QFrame.Raised)
        self.frLocationBarText.setObjectName("frLocationBarText")

        self.hboxlayout = QtGui.QHBoxLayout(self.frLocationBarText)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setMargin(9)
        self.hboxlayout.setObjectName("hboxlayout")

        self.lblLocation = QtGui.QLabel(self.frLocationBarText)
        self.lblLocation.setMaximumSize(QtCore.QSize(58,16777215))
        self.lblLocation.setObjectName("lblLocation")
        self.hboxlayout.addWidget(self.lblLocation)

        self.txtLocation = QtGui.QLineEdit(self.frLocationBarText)
        self.txtLocation.setObjectName("txtLocation")
        self.hboxlayout.addWidget(self.txtLocation)
        self.vboxlayout1.addWidget(self.frLocationBarText)

        self.line = QtGui.QFrame(self.frLocationBar)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.vboxlayout1.addWidget(self.line)
        self.vboxlayout.addWidget(self.frLocationBar)

        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setMinimumSize(QtCore.QSize(16,16))
        self.stackedWidget.setObjectName("stackedWidget")

        self.StartPage = QtGui.QWidget()
        self.StartPage.setObjectName("StartPage")

        self.hboxlayout1 = QtGui.QHBoxLayout(self.StartPage)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setMargin(9)
        self.hboxlayout1.setObjectName("hboxlayout1")

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)

        self.lblStartPage = QtGui.QLabel(self.StartPage)
        self.lblStartPage.setPixmap(QtGui.QPixmap(":/logos/IcepapCfg Icons/IcepapBig.png"))
        self.lblStartPage.setObjectName("lblStartPage")
        self.hboxlayout1.addWidget(self.lblStartPage)

        spacerItem1 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem1)
        self.stackedWidget.addWidget(self.StartPage)
        self.vboxlayout.addWidget(self.stackedWidget)
        IcepapCMS.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(IcepapCMS)
        self.menubar.setGeometry(QtCore.QRect(0,0,1100,28))
        self.menubar.setObjectName("menubar")

        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")

        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")

        self.menuDriver = QtGui.QMenu(self.menubar)
        self.menuDriver.setObjectName("menuDriver")

        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        IcepapCMS.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(IcepapCMS)
        self.statusbar.setObjectName("statusbar")
        IcepapCMS.setStatusBar(self.statusbar)

        self.toolBar = QtGui.QToolBar(IcepapCMS)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setMovable(False)
        self.toolBar.setOrientation(QtCore.Qt.Horizontal)
        self.toolBar.setIconSize(QtCore.QSize(32,32))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar.setObjectName("toolBar")
        IcepapCMS.addToolBar(QtCore.Qt.TopToolBarArea,self.toolBar)

        self.dockTree = QtGui.QDockWidget(IcepapCMS)
        self.dockTree.setMinimumSize(QtCore.QSize(150,16))
        self.dockTree.setMaximumSize(QtCore.QSize(16777215,16777215))
        self.dockTree.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.dockTree.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea)
        self.dockTree.setObjectName("dockTree")

        self.dockWidgetContents = QtGui.QWidget(self.dockTree)
        self.dockWidgetContents.setObjectName("dockWidgetContents")

        self.vboxlayout2 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setMargin(9)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setMargin(2)
        self.gridlayout.setSpacing(4)
        self.gridlayout.setObjectName("gridlayout")

        self.label = QtGui.QLabel(self.dockWidgetContents)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label,0,0,1,1)

        self.btnDeleteLocation = QtGui.QToolButton(self.dockWidgetContents)
        self.btnDeleteLocation.setIcon(QtGui.QIcon(":/small_icons/IcepapCFG Icons Petits/process-stop.png"))
        self.btnDeleteLocation.setIconSize(QtCore.QSize(16,16))
        self.btnDeleteLocation.setObjectName("btnDeleteLocation")
        self.gridlayout.addWidget(self.btnDeleteLocation,0,2,1,1)

        self.btnAddLocation = QtGui.QToolButton(self.dockWidgetContents)
        self.btnAddLocation.setIcon(QtGui.QIcon(":/small_icons/IcepapCFG Icons Petits/template.png"))
        self.btnAddLocation.setIconSize(QtCore.QSize(16,16))
        self.btnAddLocation.setObjectName("btnAddLocation")
        self.gridlayout.addWidget(self.btnAddLocation,0,1,1,1)

        self.cbLocation = QtGui.QComboBox(self.dockWidgetContents)
        self.cbLocation.setEditable(False)
        self.cbLocation.setObjectName("cbLocation")
        self.gridlayout.addWidget(self.cbLocation,1,0,1,3)
        self.vboxlayout2.addLayout(self.gridlayout)

        self.frame = QtGui.QFrame(self.dockWidgetContents)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.hboxlayout2 = QtGui.QHBoxLayout(self.frame)
        self.hboxlayout2.setSpacing(4)
        self.hboxlayout2.setMargin(4)
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.btnTreeAdd = QtGui.QToolButton(self.frame)
        self.btnTreeAdd.setIcon(QtGui.QIcon(":/small_icons/IcepapCFG Icons Petits/list-add.png"))
        self.btnTreeAdd.setIconSize(QtCore.QSize(16,16))
        self.btnTreeAdd.setObjectName("btnTreeAdd")
        self.hboxlayout2.addWidget(self.btnTreeAdd)

        self.btnTreeRemove = QtGui.QToolButton(self.frame)
        self.btnTreeRemove.setIcon(QtGui.QIcon(":/small_icons/IcepapCFG Icons Petits/list-remove.png"))
        self.btnTreeRemove.setIconSize(QtCore.QSize(16,16))
        self.btnTreeRemove.setObjectName("btnTreeRemove")
        self.hboxlayout2.addWidget(self.btnTreeRemove)

        spacerItem2 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem2)
        self.vboxlayout2.addWidget(self.frame)

        self.treeView = QtGui.QTreeView(self.dockWidgetContents)
        self.treeView.setIconSize(QtCore.QSize(22,22))
        self.treeView.setObjectName("treeView")
        self.vboxlayout2.addWidget(self.treeView)
        self.dockTree.setWidget(self.dockWidgetContents)
        IcepapCMS.addDockWidget(QtCore.Qt.DockWidgetArea(1),self.dockTree)

        self.actionAbout = QtGui.QAction(IcepapCMS)
        self.actionAbout.setObjectName("actionAbout")

        self.actionTree_Explorer = QtGui.QAction(IcepapCMS)
        self.actionTree_Explorer.setCheckable(True)
        self.actionTree_Explorer.setChecked(True)
        self.actionTree_Explorer.setObjectName("actionTree_Explorer")

        self.actionGoNext = QtGui.QAction(IcepapCMS)
        self.actionGoNext.setIcon(QtGui.QIcon(":/icons/IcepapCfg Icons/go-next.png"))
        self.actionGoNext.setObjectName("actionGoNext")

        self.actionGoPrevious = QtGui.QAction(IcepapCMS)
        self.actionGoPrevious.setIcon(QtGui.QIcon(":/icons/IcepapCfg Icons/go-previous.png"))
        self.actionGoPrevious.setObjectName("actionGoPrevious")

        self.actionGoUp = QtGui.QAction(IcepapCMS)
        self.actionGoUp.setIcon(QtGui.QIcon(":/icons/IcepapCfg Icons/go-up.png"))
        self.actionGoUp.setObjectName("actionGoUp")

        self.actionRefresh = QtGui.QAction(IcepapCMS)
        self.actionRefresh.setIcon(QtGui.QIcon(":/icons/IcepapCfg Icons/view-refresh.png"))
        self.actionRefresh.setObjectName("actionRefresh")

        self.actionPreferences = QtGui.QAction(IcepapCMS)
        self.actionPreferences.setIcon(QtGui.QIcon(":/icons/IcepapCfg Icons/gnome-settings.png"))
        self.actionPreferences.setObjectName("actionPreferences")

        self.actionHelp = QtGui.QAction(IcepapCMS)
        self.actionHelp.setIcon(QtGui.QIcon(":/icons/IcepapCfg Icons/help-browser.png"))
        self.actionHelp.setObjectName("actionHelp")

        self.actionExport = QtGui.QAction(IcepapCMS)
        self.actionExport.setIcon(QtGui.QIcon(":/icons/IcepapCfg Icons/gnome-dev-floppy.png"))
        self.actionExport.setObjectName("actionExport")

        self.actionImport = QtGui.QAction(IcepapCMS)
        self.actionImport.setIcon(QtGui.QIcon(":/icons/IcepapCfg Icons/folder.png"))
        self.actionImport.setObjectName("actionImport")

        self.actionQuit = QtGui.QAction(IcepapCMS)
        self.actionQuit.setIcon(QtGui.QIcon(":/icons/IcepapCfg Icons/gnome-logout.png"))
        self.actionQuit.setObjectName("actionQuit")

        self.actionToolbar = QtGui.QAction(IcepapCMS)
        self.actionToolbar.setCheckable(True)
        self.actionToolbar.setChecked(True)
        self.actionToolbar.setObjectName("actionToolbar")

        self.actionSaveConfig = QtGui.QAction(IcepapCMS)
        self.actionSaveConfig.setIcon(QtGui.QIcon(":/icons/IcepapCfg Icons/sign.png"))
        self.actionSaveConfig.setObjectName("actionSaveConfig")

        self.actionFirmwareUpgrade = QtGui.QAction(IcepapCMS)
        self.actionFirmwareUpgrade.setIcon(QtGui.QIcon(":/icons/IcepapCfg Icons/gnome-cpu.png"))
        self.actionFirmwareUpgrade.setObjectName("actionFirmwareUpgrade")

        self.actionConsole = QtGui.QAction(IcepapCMS)
        self.actionConsole.setIcon(QtGui.QIcon(":/icons/IcepapCfg Icons/gnome-terminal.png"))
        self.actionConsole.setObjectName("actionConsole")

        self.actionHistoricCfg = QtGui.QAction(IcepapCMS)
        self.actionHistoricCfg.setCheckable(True)
        self.actionHistoricCfg.setIcon(QtGui.QIcon(":/icons/IcepapCfg Icons/calendar.png"))
        self.actionHistoricCfg.setObjectName("actionHistoricCfg")

        self.actionTemplates = QtGui.QAction(IcepapCMS)
        self.actionTemplates.setIcon(QtGui.QIcon(":/icons/IcepapCfg Icons/notes.png"))
        self.actionTemplates.setObjectName("actionTemplates")

        self.actionAddIcepap = QtGui.QAction(IcepapCMS)
        self.actionAddIcepap.setIcon(QtGui.QIcon(":/small_icons/IcepapCFG Icons Petits/list-add.png"))
        self.actionAddIcepap.setObjectName("actionAddIcepap")

        self.actionDeleteIcepap = QtGui.QAction(IcepapCMS)
        self.actionDeleteIcepap.setIcon(QtGui.QIcon(":/small_icons/IcepapCFG Icons Petits/list-remove.png"))
        self.actionDeleteIcepap.setObjectName("actionDeleteIcepap")

        self.actionUser_manual = QtGui.QAction(IcepapCMS)
        self.actionUser_manual.setObjectName("actionUser_manual")

        self.actionHardware_manual = QtGui.QAction(IcepapCMS)
        self.actionHardware_manual.setObjectName("actionHardware_manual")

        self.actionAddLocation = QtGui.QAction(IcepapCMS)
        self.actionAddLocation.setIcon(QtGui.QIcon(":/small_icons/IcepapCFG Icons Petits/template.png"))
        self.actionAddLocation.setObjectName("actionAddLocation")

        self.actionDeleteLocation = QtGui.QAction(IcepapCMS)
        self.actionDeleteLocation.setIcon(QtGui.QIcon(":/small_icons/IcepapCFG Icons Petits/process-stop.png"))
        self.actionDeleteLocation.setObjectName("actionDeleteLocation")

        self.actionSetExpertFlag = QtGui.QAction(IcepapCMS)
        self.actionSetExpertFlag.setCheckable(True)
        self.actionSetExpertFlag.setObjectName("actionSetExpertFlag")
        self.menuHelp.addAction(self.actionUser_manual)
        self.menuHelp.addAction(self.actionHardware_manual)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menuView.addAction(self.actionTree_Explorer)
        self.menuView.addAction(self.actionToolbar)
        self.menuDriver.addAction(self.actionSaveConfig)
        self.menuDriver.addSeparator()
        self.menuDriver.addAction(self.actionHistoricCfg)
        self.menuDriver.addAction(self.actionTemplates)
        self.menuDriver.addSeparator()
        self.menuDriver.addAction(self.actionExport)
        self.menuDriver.addAction(self.actionImport)
        self.menuDriver.addAction(self.actionSetExpertFlag)
        self.menuFile.addAction(self.actionAddLocation)
        self.menuFile.addAction(self.actionDeleteLocation)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionAddIcepap)
        self.menuFile.addAction(self.actionDeleteIcepap)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionFirmwareUpgrade)
        self.menuFile.addAction(self.actionConsole)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPreferences)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuDriver.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionGoPrevious)
        self.toolBar.addAction(self.actionGoNext)
        self.toolBar.addAction(self.actionGoUp)
        self.toolBar.addAction(self.actionRefresh)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExport)
        self.toolBar.addAction(self.actionImport)
        self.toolBar.addAction(self.actionSaveConfig)
        self.toolBar.addAction(self.actionHistoricCfg)
        self.toolBar.addAction(self.actionTemplates)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPreferences)
        self.toolBar.addAction(self.actionConsole)
        self.toolBar.addAction(self.actionHelp)
        self.toolBar.addAction(self.actionQuit)

        self.retranslateUi(IcepapCMS)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(IcepapCMS)

    def retranslateUi(self, IcepapCMS):
        IcepapCMS.setWindowTitle(QtGui.QApplication.translate("IcepapCMS", "Icepap configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.lblLocation.setText(QtGui.QApplication.translate("IcepapCMS", "Location:", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("IcepapCMS", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setTitle(QtGui.QApplication.translate("IcepapCMS", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.menuDriver.setTitle(QtGui.QApplication.translate("IcepapCMS", "Driver", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("IcepapCMS", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("IcepapCMS", "Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.dockTree.setWindowTitle(QtGui.QApplication.translate("IcepapCMS", "Tree Explorer", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("IcepapCMS", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; text-decoration: underline;\">Location</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDeleteLocation.setText(QtGui.QApplication.translate("IcepapCMS", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAddLocation.setText(QtGui.QApplication.translate("IcepapCMS", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTreeAdd.setText(QtGui.QApplication.translate("IcepapCMS", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTreeRemove.setText(QtGui.QApplication.translate("IcepapCMS", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("IcepapCMS", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTree_Explorer.setText(QtGui.QApplication.translate("IcepapCMS", "Tree Explorer", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTree_Explorer.setShortcut(QtGui.QApplication.translate("IcepapCMS", "F8", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGoNext.setText(QtGui.QApplication.translate("IcepapCMS", "Go Next", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGoNext.setStatusTip(QtGui.QApplication.translate("IcepapCMS", "444", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGoNext.setWhatsThis(QtGui.QApplication.translate("IcepapCMS", "5555", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGoNext.setShortcut(QtGui.QApplication.translate("IcepapCMS", "Alt+Right", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGoPrevious.setText(QtGui.QApplication.translate("IcepapCMS", "Go Previous", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGoPrevious.setShortcut(QtGui.QApplication.translate("IcepapCMS", "Alt+Left", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGoUp.setText(QtGui.QApplication.translate("IcepapCMS", "Go Up", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGoUp.setShortcut(QtGui.QApplication.translate("IcepapCMS", "Alt+Up", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRefresh.setText(QtGui.QApplication.translate("IcepapCMS", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRefresh.setShortcut(QtGui.QApplication.translate("IcepapCMS", "F5", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(QtGui.QApplication.translate("IcepapCMS", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setText(QtGui.QApplication.translate("IcepapCMS", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setShortcut(QtGui.QApplication.translate("IcepapCMS", "F1", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport.setText(QtGui.QApplication.translate("IcepapCMS", "Export configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport.setIconText(QtGui.QApplication.translate("IcepapCMS", "Export configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport.setToolTip(QtGui.QApplication.translate("IcepapCMS", "Export driver configuration to file", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport.setShortcut(QtGui.QApplication.translate("IcepapCMS", "Ctrl+E", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport.setText(QtGui.QApplication.translate("IcepapCMS", "Import configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport.setIconText(QtGui.QApplication.translate("IcepapCMS", "Import configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport.setToolTip(QtGui.QApplication.translate("IcepapCMS", "Import driver configuration from file", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport.setShortcut(QtGui.QApplication.translate("IcepapCMS", "Ctrl+I", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("IcepapCMS", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("IcepapCMS", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionToolbar.setText(QtGui.QApplication.translate("IcepapCMS", "Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionToolbar.setShortcut(QtGui.QApplication.translate("IcepapCMS", "F9", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveConfig.setText(QtGui.QApplication.translate("IcepapCMS", "Save Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveConfig.setToolTip(QtGui.QApplication.translate("IcepapCMS", "Save driver configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveConfig.setStatusTip(QtGui.QApplication.translate("IcepapCMS", "Ctrl+s", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveConfig.setShortcut(QtGui.QApplication.translate("IcepapCMS", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFirmwareUpgrade.setText(QtGui.QApplication.translate("IcepapCMS", "Firmware upgrade", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFirmwareUpgrade.setToolTip(QtGui.QApplication.translate("IcepapCMS", "Open Firmware upgrade dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConsole.setText(QtGui.QApplication.translate("IcepapCMS", "Console", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConsole.setToolTip(QtGui.QApplication.translate("IcepapCMS", "Icepap Console", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHistoricCfg.setText(QtGui.QApplication.translate("IcepapCMS", "Historic Configurations", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHistoricCfg.setIconText(QtGui.QApplication.translate("IcepapCMS", "Historic Configurations", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHistoricCfg.setToolTip(QtGui.QApplication.translate("IcepapCMS", "Historic configurations per driver", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHistoricCfg.setShortcut(QtGui.QApplication.translate("IcepapCMS", "Ctrl+H", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTemplates.setText(QtGui.QApplication.translate("IcepapCMS", "Templates", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTemplates.setToolTip(QtGui.QApplication.translate("IcepapCMS", "Template managment", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTemplates.setShortcut(QtGui.QApplication.translate("IcepapCMS", "Ctrl+T", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddIcepap.setText(QtGui.QApplication.translate("IcepapCMS", "Add Icepap", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddIcepap.setToolTip(QtGui.QApplication.translate("IcepapCMS", "Add Icepap System to CMS Database", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeleteIcepap.setText(QtGui.QApplication.translate("IcepapCMS", "Delete Icepap", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeleteIcepap.setToolTip(QtGui.QApplication.translate("IcepapCMS", "Delete Icepap System from the CMS Database", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUser_manual.setText(QtGui.QApplication.translate("IcepapCMS", "User manual", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHardware_manual.setText(QtGui.QApplication.translate("IcepapCMS", "Hardware manual", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddLocation.setText(QtGui.QApplication.translate("IcepapCMS", "Add location", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddLocation.setIconText(QtGui.QApplication.translate("IcepapCMS", "Add location", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddLocation.setToolTip(QtGui.QApplication.translate("IcepapCMS", "Add location", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeleteLocation.setText(QtGui.QApplication.translate("IcepapCMS", "Delete location", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeleteLocation.setIconText(QtGui.QApplication.translate("IcepapCMS", "Delete location", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeleteLocation.setToolTip(QtGui.QApplication.translate("IcepapCMS", "Delete location", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSetExpertFlag.setText(QtGui.QApplication.translate("IcepapCMS", "Set Expert Flag", None, QtGui.QApplication.UnicodeUTF8))

import icepapcms_rc

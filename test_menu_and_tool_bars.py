import sys

from functools import partial
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QLabel,QMainWindow, QMenuBar, QMenu, QToolBar, QAction, QSpinBox
from PyQt5.QtGui import QKeySequence

class Window (QMainWindow):

    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle('Main Window')
        self.resize(720,480)
        self.centralWidget = QLabel('Hello, World')
        self.centralWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.centralWidget)

        self._createActions()
        self._createMenuBar()
        self._createToolBars()
        self._connectActions()

    def newFile(self):
        pass
    def openFile(self):
        pass
    def saveFile(self):
        pass
    def copyContent(self):
        pass
    def pasteContent(self):
        pass
    def cutContent(self):
        pass
    def helpContent(self):
        pass
    def about(self):
        pass
    def openRecentFile(self,filename):
        self.centralWidget.setText(f"<b>{filename}</b> opened")



    def populateOpenRecent(self):
        self.openRecentMenu.clear()
        actions = []
        print('Ok')
        filenames = [f"File-{n}" for n in range(5)]
        for filename in filenames:
            action = QAction(filename,self)
            action.triggered.connect(partial(self.openRecentFile,filename))
            actions.append(action)
        self.openRecentMenu.addActions(actions)

    def _createMenuBar(self):
        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)
        fileMenu = QMenu ('File',self)
        menuBar.addMenu(fileMenu)
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        self.openRecentMenu = fileMenu.addMenu("Open Recent")
        fileMenu.addAction(self.saveAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAction)


        editMenu = menuBar.addMenu('Edit')
        editMenu.addAction(self.copyAction)
        editMenu.addAction(self.pasteAction)
        editMenu.addAction(self.cutAction)
        editMenu.addSeparator()
        findMenu = editMenu.addMenu('Find and Replace')
        findMenu.addAction('Find')
        findMenu.addAction('Replace')

        helpMenu = menuBar.addMenu('Help')
        helpMenu.addAction(self.helpAction)
        helpMenu.addAction(self.aboutAction)

    def _createToolBars(self):
        fileToolBar = self.addToolBar('File')
        fileToolBar.setMovable(False)
        fileToolBar.addAction(self.ToFirstPageAction)
        fileToolBar.addAction(self.ToSecondPageAction)
        fileToolBar.addAction(self.ToThirdPageAction)


    def _createActions(self):
        self.newAction = QAction(self)
        self.newAction.setText('New')
        self.openAction = QAction('Open',self)
        self.saveAction = QAction('Save', self)
        self.exitAction = QAction('Exit', self)
        self.copyAction = QAction('Copy', self)
        self.pasteAction = QAction('Paste', self)
        self.cutAction = QAction('Cut', self)
        self.helpAction = QAction('Help', self)
        self.aboutAction = QAction('About', self)
        self.ToFirstPageAction = QAction('First Page',self)
        self.ToSecondPageAction = QAction('Second Page', self)
        self.ToThirdPageAction = QAction('Third Page', self)

        self.newAction.setShortcut("Ctrl+N")
        self.openAction.setShortcut("Ctrl+O")
        self.saveAction.setShortcut("Ctrl+S")
        self.pasteAction.setShortcut(QKeySequence.Paste)
        self.cutAction.setShortcut(QKeySequence.Cut)

    def _connectActions(self):
        self.newAction.triggered.connect(self.newFile)
        self.openAction.triggered.connect(self.openFile)
        self.saveAction.triggered.connect(self.saveFile)
        self.exitAction.triggered.connect(self.close)

        self.copyAction.triggered.connect(self.copyContent)
        self.pasteAction.triggered.connect(self.pasteContent)
        self.cutAction.triggered.connect(self.cutContent)
        self.helpAction.triggered.connect(self.helpContent)
        self.aboutAction.triggered.connect(self.about)

        self.openRecentMenu.aboutToShow.connect(self.populateOpenRecent)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

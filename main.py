import sys
from typing import overload
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon

class Window(QMainWindow):

    
    def __init__(self):
        super(Window,self).__init__()
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com'))
        self.setWindowIcon(QIcon('Icon.svg'))
        self.setCentralWidget(self.browser)
        self.browser.page().setAudioMuted(False)
        self.showMaximized()
        navbar = QToolBar()
        self.addToolBar(navbar)
        prevBtn = QAction('Prev',self)
        prevBtn.triggered.connect(self.browser.reload)
        navbar.addAction(prevBtn)
        nextBtn = QAction('Next',self)
        nextBtn.triggered.connect(self.browser.forward)
        navbar.addAction(nextBtn)
        refreshBtn = QAction('Refresh',self)
        refreshBtn.triggered.connect(self.browser.reload)
        navbar.addAction(refreshBtn)
        homeBtn = QAction('Home',self)
        homeBtn.triggered.connect(self.home)
        navbar.addAction(homeBtn)
        self.searchBar = QLineEdit()
        self.searchBar.returnPressed.connect(self.loadUrl)
        navbar.addWidget(self.searchBar)
        self.browser.urlChanged.connect(self.updateUrl)
    
    def home(self):
        self.browser.setUrl(QUrl('https://www.google.com'))

    def loadUrl(self):
        url = self.searchBar.text()
        self.browser.setUrl(QUrl(url))

    def updateUrl(self, url):
        self.searchBar.setText(url.toString())
    def acceptNavigationRequest(QUrl, NavigationTypeLinkClicked, bool):
        return False

MyApp = QApplication(sys.argv)
QApplication.setApplicationName('OnTopBrowser')
window = Window()
MyApp.exec_()
import sys, random
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtWidgets import QGridLayout, QWidget, QDesktopWidget
from PyQt5.QtWidgets import (QApplication, QPushButton, QLabel, QFileDialog)

from PyQt5 import QtGui, QtCore, Qt
from PyQt5.Qt import *
from PyQt5.QtCore import QRect, Qt, QTimer

from PyQt5.QtGui import QPainter, QBrush, QPen
 
from PyQt5.QtCore import Qt

from PyQt5.QtGui import QPixmap

class ifugaoDesign(QMainWindow):
    def __init__(self):
            super().__init__()

            self.title = "Ifugao Wanno Designer"
            self.width = 900
            self.height = 900

            self.initWindow()

    def initWindow(self):
        self.resize(self.width, self.height)
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon("Icons/logo.png"))

        self.backgroundWin()
        self.Buttons()
        self.center()
        
        self.show()

    def center(self):
        # geometry of the main window
        qr = self.frameGeometry()

        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())

    def backgroundWin(self):
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap('Background/ifugao-Background.jpg'))
        self.background.setGeometry(0, 0, self.width, self.height)#size and position of background
        self.background.show()

    def Buttons(self):
        titleLabel = QLabel("Ifugao Wanno Designer", self)
        titleLabel.setGeometry(QRect(30+150,50, 600, 100))
        titleLabel.setStyleSheet("QWidget { color: Yellow}")
        titleLabel.setFont(QtGui.QFont('Sanserif', 30, QtGui.QFont.Bold))

        customButton = QPushButton('Custom Design', self)
        customButton.setGeometry(QRect(50+100,350, 270, 100))
        #customButton.setStyleSheet("QWidget {background-color: Blue}")
        customButton.setFont(QtGui.QFont('Times New Roman',16))
        customButton.clicked.connect(self.clickedCustom)

        customButton.setIcon(QtGui.QIcon('Icons/customize.png'))
        customButton.setIconSize(QtCore.QSize(50,50))

        randomButton = QPushButton('Random Generator', self)
        randomButton.setGeometry(QRect(50+200+50+170,350, 290, 100))
        #randomButton.setStyleSheet("QWidget {background-color: Blue}")
        randomButton.setFont(QtGui.QFont('Times New Roman',16))
        randomButton.clicked.connect(self.clickedRandom)
        
        randomButton.setIcon(QtGui.QIcon('Icons/random.png'))
        randomButton.setIconSize(QtCore.QSize(50,50))

    def clickedCustom(self):
        self._customizeWin = customizeWindow()
        self._customizeWin.show()
        self.hide()

    def clickedRandom(self):
        self._RandGenWin = randomPattern()
        self._RandGenWin.show()
        self.hide()

    def closeEvent(self, event):
        close = QMessageBox.question(self,
                                     "Exit the program",
                                     "Are you sure?",
                                      QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            event.accept()
            sys.exit(0)
        else:
            event.ignore()

class randomPattern(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Random Wanno Generator"
        self.left = 500
        self.top = 100
        self.width = 900
        self.height = 900
        self.flag = False

        self.design1 = QLabel(self)
        self.design2 = QLabel(self)
        self.design3 = QLabel(self)
        self.design4 = QLabel(self)
        self.design5 = QLabel(self)
        self.design6 = QLabel(self)
        self.design7 = QLabel(self)

        self.initWindow()

    def initWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QtGui.QIcon("Icons/logo.png"))
        
        self.button()
        self.show()

    def button(self):
        generateButton = QPushButton("Generate", self)
        generateButton.setGeometry(QRect(350+150, 800, 200, 70))
        generateButton.setFont(QtGui.QFont('Times New Roman',19))
        generateButton.clicked.connect(self.clickedGenerate)

        generateButton.setIcon(QtGui.QIcon('Icons/generate.png'))
        generateButton.setIconSize(QtCore.QSize(50,50))

        takeSsButton = QPushButton("Save", self)
        takeSsButton.setGeometry(QRect(350-150, 800, 200, 70))
        takeSsButton.setFont(QtGui.QFont('Times New Roman',19))
        takeSsButton.clicked.connect(self.save_screenshot)

        takeSsButton.setIcon(QtGui.QIcon('Icons/save.png'))
        takeSsButton.setIconSize(QtCore.QSize(50,50))

        backButton = QPushButton("Back", self)
        backButton.setGeometry(QRect(0, 0, 150, 50))
        backButton.setFont(QtGui.QFont('Times New Roman',19))
        backButton.clicked.connect(self.clickedBackBtn)

        backButton.setIcon(QtGui.QIcon('Icons/back.png'))
        backButton.setIconSize(QtCore.QSize(50,50))

    def clickedBackBtn(self):
        self._mainWin = ifugaoDesign()
        self._mainWin.show()
        self.hide()

    def clickedGenerate(self):
        self.design1.hide()
        self.design2.hide()
        self.design3.hide()
        self.design4.hide()
        self.design5.hide()
        self.design6.hide()
        self.design7.hide()

        self.flag = True
        self.update()

    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        painter.setBrush(QColor(0,0,0))

        for i in range(8):
                painter.drawRect(0, 60+(i*100)+5, 700+195, 3)

        if self.flag:
            patterns = ["design1.png", "design2.png", "design3.png", "design4.png", "design5.png", "design6.png", "design7.png", "design8.png",
            "design9.png", "design10.png", "design11.png", "design12.png", "design13.png", "design14.png", "design15.png", "design16.png", "design17.png",
            "design18.png", "design19.png", "design20.png"]
            
            #print(patterns[randPatterns])
            #print(randPatterns)

            

            
            for i in range(7):
                randPatterns = random.randrange(0,20)
                
                if i == 0:
                    
                    self.design1.setPixmap(QPixmap("Designs/{}".format(patterns[randPatterns])))
                    
                    self.design1.setGeometry(0, 60+(i*100)+5+3, 900, 100-3)
                    self.design1.show()
                elif i == 1:
                    
                    self.design2.setPixmap(QPixmap("Designs/{}".format(patterns[randPatterns])))
                    
                    self.design2.setGeometry(0, 60+(i*100)+5+3, 900, 100-3)
                    self.design2.show()

                elif i == 2:
                    
                    self.design3.setPixmap(QPixmap("Designs/{}".format(patterns[randPatterns])))
                    
                    self.design3.setGeometry(0, 60+(i*100)+5+3, 900, 100-3)
                    self.design3.show()

                elif i == 3:
                    
                    self.design4.setPixmap(QPixmap("Designs/{}".format(patterns[randPatterns])))
                    
                    self.design4.setGeometry(0, 60+(i*100)+5+3, 900, 100-3)
                    self.design4.show()
                elif i == 4:
                    
                    self.design5.setPixmap(QPixmap("Designs/{}".format(patterns[randPatterns])))
                    
                    self.design5.setGeometry(0, 60+(i*100)+5+3, 900, 100-3)
                    self.design5.show()

                elif i == 5:
                    
                    self.design6.setPixmap(QPixmap("Designs/{}".format(patterns[randPatterns])))
                    
                    self.design6.setGeometry(0, 60+(i*100)+5+3, 900, 100-3)
                    self.design6.show()
                
                elif i == 6:
                    
                    self.design7.setPixmap(QPixmap("Designs/{}".format(patterns[randPatterns])))
                    
                    self.design7.setGeometry(0, 60+(i*100)+5+3, 900, 100-3)
                    self.design7.show()

            self.flag = False
            painter.end()

    def save_screenshot(self):
        #QTimer.singleShot(1000, self.take_screenshot)
        self.take_screenshot()
        img, _ = QFileDialog.getSaveFileName(self,"Salvar Arquivo",
                                            filter="PNG(*.png);; JPEG(*.jpg)")
        if img[-3:] == "png":
            self.preview_screen.save(img, "png")
        elif img[-3:] == "jpg":
            self.preview_screen.save(img, "jpg")
        
    def take_screenshot(self):
        x = 500
        y = 60+100+5+3
        width = 900
        height = 100*7
        self.preview_screen = QApplication.primaryScreen().grabWindow(QApplication.desktop().winId(), x, y, width, height)
        
    def closeEvent(self, event):
        close = QMessageBox.question(self,
                                     "Exit the program",
                                     "Are you sure?",
                                      QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            event.accept()
            sys.exit(0)
        else:
            event.ignore()

class customizeWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Random Wanno Generator"
        self.left = 500
        self.top = 100
        self.width = 900
        self.height = 900
        self.flag = True

        self.design1 = QLabel(self)
        self.design2 = QLabel(self)
        self.design3 = QLabel(self)
        self.design4 = QLabel(self)
        self.design5 = QLabel(self)
        self.design6 = QLabel(self)
        self.design7 = QLabel(self)

        self.categoryrow1 = QComboBox(self)
        self.categoryrow2 = QComboBox(self)
        self.categoryrow3 = QComboBox(self)
        self.categoryrow4 = QComboBox(self)
        self.categoryrow5 = QComboBox(self)
        self.categoryrow6 = QComboBox(self)
        self.categoryrow7 = QComboBox(self)

        self.initWindow()

    def initWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QtGui.QIcon("Icons/logo.png"))
        
        self.button()
        self.windowLabels()
        self.rowComboBox()
        self.show()

    def windowLabels(self):
        
        for i in range(0,7):
            columnLabel = QLabel("Row {}".format(i+1), self)
            columnLabel.setGeometry(QRect(170+(i*100), -20, 100, 70))
            columnLabel.setFont(QtGui.QFont('Times New Roman',12))

    def rowComboBox(self):
        

        self.categoryrow1.setFont(QtGui.QFont('SansSerif', 8))
        self.categoryrow1.setGeometry(QRect(165, -20+50, 80, 30))
        self.categoryrow1.addItem("None")
        for k in range(0,20):
            self.categoryrow1.addItem("design{}".format(k+1))
        
        self.categoryrow1.currentIndexChanged.connect(self.selectionchange)

        
        self.categoryrow2.setFont(QtGui.QFont('SansSerif', 8))
        self.categoryrow2.setGeometry(QRect(165 + (98*1), -20+50, 80, 30))
        self.categoryrow2.addItem("None")
        for k in range(0,20):
            self.categoryrow2.addItem("design{}".format(k+1))
        
        self.categoryrow2.currentIndexChanged.connect(self.selectionchange)

        
        self.categoryrow3.setFont(QtGui.QFont('SansSerif', 8))
        self.categoryrow3.setGeometry(QRect(165 +(98*2), -20+50, 80, 30))
        self.categoryrow3.addItem("None")
        for k in range(0,20):
            self.categoryrow3.addItem("design{}".format(k+1))
        self.categoryrow3.currentIndexChanged.connect(self.selectionchange)

        
        self.categoryrow4.setFont(QtGui.QFont('SansSerif', 8))
        self.categoryrow4.setGeometry(QRect(165 + (98*3), -20+50, 80, 30))
        self.categoryrow4.addItem("None")
        for k in range(0,20):
            self.categoryrow4.addItem("design{}".format(k+1))
        
        self.categoryrow4.currentIndexChanged.connect(self.selectionchange)

        
        self.categoryrow5.setFont(QtGui.QFont('SansSerif', 8))
        self.categoryrow5.setGeometry(QRect(165 +(98*4), -20+50, 80, 30))
        self.categoryrow5.addItem("None")
        for k in range(0,20):
            self.categoryrow5.addItem("design{}".format(k+1))
        
        self.categoryrow5.currentIndexChanged.connect(self.selectionchange)

        
        self.categoryrow6.setFont(QtGui.QFont('SansSerif', 8))
        self.categoryrow6.setGeometry(QRect(165 + (98*5), -20+50, 80, 30))
        self.categoryrow6.addItem("None")
        for k in range(0,20):
            self.categoryrow6.addItem("design{}".format(k+1))
        self.categoryrow6.currentIndexChanged.connect(self.selectionchange)
        
        
        self.categoryrow7.setFont(QtGui.QFont('SansSerif', 8))
        self.categoryrow7.setGeometry(QRect(165 + (98*6), -20+50, 80, 30))
        self.categoryrow7.addItem("None")
        for k in range(0,20):
            self.categoryrow7.addItem("design{}".format(k+1))
        self.categoryrow7.currentIndexChanged.connect(self.selectionchange)

    def selectionchange(self, i):
        if self.categoryrow1.currentText() == "None":
            self.design1.hide()
        else:
            self.design1.setPixmap(QPixmap("Designs/{}".format(self.categoryrow1.currentText())))
            self.design1.setGeometry(0, 60+(0*100)+5+3, 900, 100-3)
            self.design1.show()

        if self.categoryrow2.currentText() == "None":
            self.design2.hide()
        else:
            self.design2.setPixmap(QPixmap("Designs/{}".format(self.categoryrow2.currentText())))
            self.design2.setGeometry(0, 60+(1*100)+5+3, 900, 100-3)
            self.design2.show()

        if self.categoryrow3.currentText() == "None":
            self.design3.hide()
        else:
            self.design3.setPixmap(QPixmap("Designs/{}".format(self.categoryrow3.currentText())))
            self.design3.setGeometry(0, 60+(2*100)+5+3, 900, 100-3)
            self.design3.show()

        if self.categoryrow4.currentText() == "None":
            self.design4.hide()
        else:
            self.design4.setPixmap(QPixmap("Designs/{}".format(self.categoryrow4.currentText())))
            self.design4.setGeometry(0, 60+(3*100)+5+3, 900, 100-3)
            self.design4.show()

        if self.categoryrow5.currentText() == "None":
            self.design5.hide()
        else:
            self.design5.setPixmap(QPixmap("Designs/{}".format(self.categoryrow5.currentText())))
            self.design5.setGeometry(0, 60+(4*100)+5+3, 900, 100-3)
            self.design5.show()

        if self.categoryrow6.currentText() == "None":
            self.design6.hide()
        else:
            self.design6.setPixmap(QPixmap("Designs/{}".format(self.categoryrow6.currentText())))
            self.design6.setGeometry(0, 60+(5*100)+5+3, 900, 100-3)
            self.design6.show()

        if self.categoryrow7.currentText() == "None":
            self.design7.hide()
        else:
            self.design7.setPixmap(QPixmap("Designs/{}".format(self.categoryrow7.currentText())))
            self.design7.setGeometry(0, 60+(6*100)+5+3, 900, 100-3)
            self.design7.show()

    def button(self):
        clearButton = QPushButton("Clear", self)
        clearButton.setGeometry(QRect(350+150, 800, 200, 70))
        clearButton.setFont(QtGui.QFont('Times New Roman',19))
        clearButton.clicked.connect(self.clickedClear)

        clearButton.setIcon(QtGui.QIcon('Icons/clear.png'))
        clearButton.setIconSize(QtCore.QSize(50,50))

        takeSsButton = QPushButton("Save", self)
        takeSsButton.setGeometry(QRect(350-150, 800, 200, 70))
        takeSsButton.setFont(QtGui.QFont('Times New Roman',19))
        takeSsButton.clicked.connect(self.save_screenshot)

        takeSsButton.setIcon(QtGui.QIcon('Icons/save.png'))
        takeSsButton.setIconSize(QtCore.QSize(50,50))

        backButton = QPushButton("Back", self)
        backButton.setGeometry(QRect(0, 0, 150, 50))
        backButton.setFont(QtGui.QFont('Times New Roman',19))
        backButton.clicked.connect(self.clickedBackBtn)

        backButton.setIcon(QtGui.QIcon('Icons/back.png'))
        backButton.setIconSize(QtCore.QSize(50,50))

    def clickedBackBtn(self):
        self._mainWin = ifugaoDesign()
        self._mainWin.show()
        self.hide()

    def clickedClear(self):
        self.design1.hide()
        self.design2.hide()
        self.design3.hide()
        self.design4.hide()
        self.design5.hide()
        self.design6.hide()
        self.design7.hide()

        index1 = self.categoryrow1.findText("None", QtCore.Qt.MatchFixedString)
        if index1 >= 0:
            self.categoryrow1.setCurrentIndex(index1)

        index2 = self.categoryrow2.findText("None", QtCore.Qt.MatchFixedString)
        if index2 >= 0:
            self.categoryrow2.setCurrentIndex(index2)

        index3 = self.categoryrow3.findText("None", QtCore.Qt.MatchFixedString)
        if index3 >= 0:
            self.categoryrow3.setCurrentIndex(index3)

        index4 = self.categoryrow4.findText("None", QtCore.Qt.MatchFixedString)
        if index4 >= 0:
            self.categoryrow4.setCurrentIndex(index4)

        index5 = self.categoryrow5.findText("None", QtCore.Qt.MatchFixedString)
        if index5 >= 0:
            self.categoryrow5.setCurrentIndex(index5)

        index6 = self.categoryrow6.findText("None", QtCore.Qt.MatchFixedString)
        if index6 >= 0:
            self.categoryrow6.setCurrentIndex(index6)

        index7 = self.categoryrow7.findText("None", QtCore.Qt.MatchFixedString)
        if index7 >= 0:
            self.categoryrow7.setCurrentIndex(index7)

        self.flag = True
        self.update()

    def paintEvent(self, e):
        if self.flag:
            patterns = ["design1.png", "design2.png", "design3.png", "design4.png", "design5.png", "design6.png", "design7.png", "design8.png",
            "design9.png", "design10.png", "design11.png", "design12.png", "design13.png", "design14.png", "design15.png", "design16.png", "design17.png",
            "design18.png", "design19.png", "design20.png"]
            
            #print(patterns[randPatterns])
            #print(randPatterns)

            painter = QPainter()
            painter.begin(self)
            painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
            painter.setBrush(QColor(0,0,0))

            for i in range(8):
                painter.drawRect(0, 60+(i*100)+5, 700+195, 3)

            self.flag = True
            painter.end()

    def save_screenshot(self):
        #QTimer.singleShot(1000, self.take_screenshot)
        self.take_screenshot()
        img, _ = QFileDialog.getSaveFileName(self,"Salvar Arquivo",
                                            filter="PNG(*.png);; JPEG(*.jpg)")
        if img[-3:] == "png":
            self.preview_screen.save(img, "png")
        elif img[-3:] == "jpg":
            self.preview_screen.save(img, "jpg")
        
    def take_screenshot(self):
        x = 500
        y = 60+100+5+3
        width = 900
        height = 100*7
        self.preview_screen = QApplication.primaryScreen().grabWindow(QApplication.desktop().winId(), x, y, width, height)
        
    def closeEvent(self, event):
        close = QMessageBox.question(self,
                                     "Exit the program",
                                     "Are you sure?",
                                      QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            event.accept()
            sys.exit(0)
        else:
            event.ignore()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = ifugaoDesign()
    sys.exit(app.exec_())

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,  QPushButton, QLineEdit, QWidget, QVBoxLayout, QHBoxLayout

class Calculator(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setStyleSheet("font-size: 50px")
        self.collect = ""

        self.edit = QLineEdit()
        self.edit.setPlaceholderText("0")
        self.edit.returnPressed.connect(self.on_click)

        self.btn1 = QPushButton("1")
        self.btn2 = QPushButton("2")
        self.btn3 = QPushButton("3")
        self.btn4 = QPushButton("4")
        self.btn5 = QPushButton("5")
        self.btn6 = QPushButton("6")
        self.btn7 = QPushButton("7")
        self.btn8 = QPushButton("8")
        self.btn9 = QPushButton("9")
        self.btn0 = QPushButton("0")
        self.btnC = QPushButton("C")
        self.btnQavs = QPushButton("()")
        self.btnFoiz = QPushButton("%")
        self.btnBolish = QPushButton("/")
        self.btnNull = QPushButton("0")
        self.btnVergul = QPushButton(",")
        self.btnTeng = QPushButton("=")
        self.btnKopaytma = QPushButton("*")
        self.btnAyirma = QPushButton("-")
        self.btnQoshish = QPushButton("+")


        self.vbox = QVBoxLayout()

        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox4 = QHBoxLayout()
        self.hbox5 = QHBoxLayout()

        # self.hbox1.addWidget(self.btnQavs)
        self.hbox1.addWidget(self.btnFoiz)
        self.hbox1.addWidget(self.btnBolish)
        self.hbox1.addWidget(self.btnC)

        self.hbox2.addWidget(self.btn7)
        self.hbox2.addWidget(self.btn8)
        self.hbox2.addWidget(self.btn9)
        self.hbox2.addWidget(self.btnKopaytma)

        self.hbox3.addWidget(self.btn4)
        self.hbox3.addWidget(self.btn5)
        self.hbox3.addWidget(self.btn6)
        self.hbox3.addWidget(self.btnAyirma)
        
        self.hbox4.addWidget(self.btn1)
        self.hbox4.addWidget(self.btn2)
        self.hbox4.addWidget(self.btn3)
        self.hbox4.addWidget(self.btnQoshish)

        self.hbox5.addWidget(self.btnNull)
        self.hbox5.addWidget(self.btnVergul)
        self.hbox5.addWidget(self.btnTeng)

        self.vbox.addWidget(self.edit)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)
        self.vbox.addLayout(self.hbox5)

        self.btn1.clicked.connect(self.on_click)
        self.btn2.clicked.connect(self.on_click)
        self.btn3.clicked.connect(self.on_click)
        self.btn4.clicked.connect(self.on_click)
        self.btn5.clicked.connect(self.on_click)
        self.btn6.clicked.connect(self.on_click)
        self.btn7.clicked.connect(self.on_click)
        self.btn8.clicked.connect(self.on_click)
        self.btn9.clicked.connect(self.on_click)
        self.btn0.clicked.connect(self.on_click)
        self.btnC.clicked.connect(self.on_click1)
        # self.btnQavs.clicked.connect(self.on_click)
        self.btnFoiz.clicked.connect(self.on_click)
        self.btnBolish.clicked.connect(self.on_click)
        self.btnNull.clicked.connect(self.on_click)
        self.btnVergul.clicked.connect(self.on_click)
        self.btnTeng.clicked.connect(self.on_click2)
        self.btnKopaytma.clicked.connect(self.on_click)
        self.btnAyirma.clicked.connect(self.on_click)
        self.btnQoshish.clicked.connect(self.on_click)

        self.setLayout(self.vbox)



    def on_click1(self):
        self.edit.clear()
        self.collect = ""
        self.edit.setText('0')

    def on_click(self):
        text = self.sender().text()
        self.collect += text
        self.edit.setText(self.collect)
    
    def on_click2(self):
        try:
            natija = eval(self.collect)
            self.edit.setText(str(natija))
            self.collect = str(natija)
        except:
            self.edit.setText("Xatolik!!!")
        # self.edit.clear()


app = QApplication([])
calcul = Calculator()
calcul.show()
app.exec_()
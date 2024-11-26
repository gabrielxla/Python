import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QVBoxLayout,QPushButton

class Janela (QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(50,100,600,500)
        self.setFixedSize
        self.setWindowTitle("NA MANTEIGA")
        self.setWindowOpacity(0.9)
        
        self.v_layout = QVBoxLayout()
       #-------------------Nome----------------- 
        self.label_nome = QLabel("Nome do cliente")
        self.label_nome.setStyleSheet("QLabel{font-size:20pt;color:#700}")
        self.edit_nome = QLineEdit()
        self.edit_nome.setStyleSheet("QLineEdit{padding:10px}")
        #------------------email----------------
        self.label_email = QLabel("E-Mail")
        self.label_email.setStyleSheet("QLabel{font-size:20pt;color:#700}")
        self.edit_email = QLineEdit ()
        self.edit_email.setStyleSheet("QLineEdit{padding:10px}")

        #CPF
        self.label_cpf = QLabel("Cpf")
        self.label_cpf.setStyleSheet("QLabel{font-size:20pt;color:#700}")
        self.edit_cpf = QLineEdit()
        self.edit_cpf.setStyleSheet("QLineEdit{padding:10px}")
        #telefone
        self.label_telefone = QLabel("telefone")
        self.label_telefone.setStyleSheet("QLabel{font-size:20pt;color:#700}")
        self.edit_telefone = QLineEdit()
        self.edit_telefone.setStyleSheet("QLineEdit{padding:10px}")
        #IDADE
        self.label_idade = QLabel("idade")
        self.label_idade.setStyleSheet("QLabel{font-size:20pt;color:#700}")
        self.edit_idade = QLineEdit()
        self.edit_idade.setStyleSheet("QLineEdit{padding:10px}")
        #botao
        self.button_cadastrar = QPushButton ("cadastar")
        self.button_cadastrar.setStyleSheet("QPushButton{width:200px}")
       
       
        #add nome
        self.v_layout.addWidget(self.label_nome)
        self.v_layout.addWidget(self.edit_nome)
        #add Email
        self.v_layout.addWidget(self.label_email)
        self.v_layout.addWidget(self.edit_email)
        #add cpf
        self.v_layout.addWidget(self.label_cpf)
        self.v_layout.addWidget(self.edit_cpf)
        #add telefone
        self.v_layout.addWidget(self.label_telefone)
        self.v_layout.addWidget(self.edit_telefone)
        #add idade
        self.v_layout.addWidget(self.label_idade)
        self.v_layout.addWidget(self.edit_idade)
        #add botao
        self.v_layout.addWidget(self.button_cadastrar)






        

        self.setLayout(self.v_layout)

app = QApplication(sys.argv)
jan = Janela()
jan.show()
app.exec_()
from PyQt5.QtWidgets import *
from PyQt5 import uic

import sys
import _sqlite3
class ADMIN(QMainWindow):
    def __init__(self):
        super(ADMIN, self).__init__()
        uic.loadUi("src/admin.ui", self)
        self.button1 = self.bt1
        self.button2 = self.bt2
        self.button3 = self.bt3
        self.lined1 = self.line1
        self.lined2 = self.line2
        self.lined3 = self.line3
        self.lined4 = self.line4
        self.tabl1=self.table1
        self.tabl2 = self.table2

        self.bt1.clicked.connect(self.ajouter)
        self.bt2.clicked.connect(self.modifier)
        self.bt3.clicked.connect(self.supprimer)


    def create(self):

        db=_sqlite3.connect('mdata.db')
        cursor=db.cursor()
        command = ''''CREATE TABLE serveurs (
        	serveur_id INTEGER PRIMARY KEY,
        	nom_serveur TEXT NOT NULL,
        	mot_pass INTEGER NOT NULL UNIQUE
    	);'''
        resultat=cursor.execute(command)
        db.commit()
        cursor.close()


    def ajouter(self):

        nom_serveur = self.lined1.text()
        mot_pass = self.lined2.text()
        db=_sqlite3.connect('mdata.db')
        cursor=db.cursor()
        command=("INSERT INTO serveurs (nom_serveur,mot_pass) VALUES (?,?)", (nom_serveur, mot_pass))
        # command=''''INSERT INTO serveurs(nom_serveur,mot_pass )
        #  VALUES(?,?)'''
        resultat=cursor.execute(command)
        db.commit()
        cursor.close()





    def modifier(self):

        nom_serveur2 = self.lined3.text()
        mot_pass2 = self.lined4.text()
        db=_sqlite3.connect('mdata.db')
        cursor=db.cursor()
        command=('''UPDATE serveurs
        SET nom_serveur=? ,
        mot_pass=?''',(nom_serveur2,mot_pass2))
        resultat=cursor.execute(command)
        db.commit()
        cursor.close()
        self.tabl1.addItem(nom_serveur2)
    def supprimer(self):

        db = _sqlite3.connect('mdata.db')
        cursor=db.cursor()
        command=('''DELETE FROM serveurs
        WHERE nom-serveur=?, mot_pass=?''')
        resultat=cursor.execute(command)
        db.commit()
        cursor.close()




app = QApplication(sys.argv)
window = ADMIN()
window.show()
app.exec_()

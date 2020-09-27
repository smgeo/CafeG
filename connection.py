import sys
import sqlite3
#import db for psotgres

class Elconn() :
    def __init__(self):
        self.type = "sqlite"
        self.dbn = "src/datat.db"


    def create_Table(self, num, place):
        if(self.type == "sqlite"):
            db = sqlite3.connect(self.dbn)
            cursor = db.cursor()
            req = "insert into table(num, place) values("+num, +"'"+place+"')"
            resultat = cursor.execute(req)
            db.commit()
            cursor.close()

    def create_serveur(self, nom_serveur, mot_pass):
        if(self.type == "sqlite"):

            db = sqlite3.connect(self.dbn)
            cursor = db.cursor()
            command = ("INSERT INTO serveur (nom_serveur,mot_pass) VALUES ('?','?')", (nom_serveur, mot_pass))
            resultat = cursor.execute(command)
            db.commit()
            cursor.close()
    def create_plat(self, nom , prix , categorie):
        if (self.type == "sqlite"):
            db = sqlite3.connect(self.dbn)
            cursor = db.cursor()
            req = ("insert into plat(nom_plat, prix, categorie) values('?', ?, '?')", (nom, prix, categorie))
            resultat = cursor.execute(req)
            db.commit()
            cursor.close()
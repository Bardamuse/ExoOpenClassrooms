# -*- coding: utf-8 -*-
# PYTHON 2.7

################################ Projet Pret de matériel ########################

import mysql.connector
conn = mysql.connector.connect(host="localhost",user="root",password="blablabla", database="coop")
cursor=conn.cursor()

# ************** ENREGISTRER personne ****************

def new_pers():
	print 'Enregistrement nouvel associé'
	user=(raw_input('Prénom : '),raw_input('Téléphone :'), raw_input('Adresse mail :'))
	#user est un Tuple qui contient les données à insérer dans la table

	cursor.execute("""INSERT INTO personne (prenom, telephone, mail) VALUES(%s,%s,%s)""",user)



# new_pers()


# ******************* REQUETE ************************

cursor.execute("""SELECT id,prenom,telephone FROM personne""")
rows=cursor.fetchall() #rows est une liste dont chaque élément est un enregistrement de la requete

for row in rows : #row est un Tuple
	print 'id : ',row[0],' prénom : ',row[1], 'téléphone : ',row[2]

#**************** Qui a emprunté quoi ***************
print
cursor.execute("""SELECT materiel.nom, personne.prenom, pret.date_retour FROM materiel INNER JOIN pret ON materiel.id=pret.matos INNER JOIN personne ON personne.id=pret.personne """)
rows=cursor.fetchall()
for row in rows : 
	print row[0],row[1],row[2]

	




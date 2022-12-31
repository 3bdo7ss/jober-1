import psycopg2 as pg
from my_dictionary import *

def connecting():
    conn = pg.connect(
		host = 'ec2-54-228-30-162.eu-west-1.compute.amazonaws.com',
	    database = 'd2o4k8j9ukv2dt',
	    user = "ikiafblpjpuprv",
	    password = "059c0445e8eecc4fa7a326e909c069b44abed148247e748111a3da3d40c11208",)
    c = conn.cursor()
    return conn, c


def lastmsg(id):
    conn, c = connecting()
    c.execute("SELECT Last_Msg FROM clients WHERE User_id = %s", (id,))
    last_msg = c.fetchone()[0]
    c.close()
    conn.close()
    return last_msg

def insert_lastmsg(id, msg):
    conn, c = connecting()
    c.execute("UPDATE clients SET Last_Msg = %s WHERE User_id = %s", (msg, id))
    conn.commit()
    c.close()
    conn.close()
    return msg

def update(user_id, update_id, update):
    conn, c = connecting()	
    update_list = [
		'Age', #0
    	'Phone_number',#1
    	'Email', #2
    	'Summary', #3
    	'Name_Of_Experience', #4
    	'Role_Experience', #5
    	'Start_Experience', #6
    	'End_Experience', #7
    	'name_Of_Education', #8
    	'Start_Edu', #9
    	'End_Edu', #10
    	'Role_Edu', #11
    	'Skills', #12
		'Sex', #13
		'Sector', #14
		'Speciality', #15
		'Reciving', #16
		"Full_name" #17

		]
    c.execute(f"UPDATE clients SET {update_list[update_id]} = %s WHERE User_id = %s", (update, user_id))
    conn.commit()
    c.close()
    conn.close()

def selector(id, x):
    conn, c = connecting()	
    db_list = [
		'Age', #0
    	'Phone_number',#1
    	'Email', #2
    	'Summary', #3
    	'Name_Of_Experience', #4
    	'Role_Experience', #5
    	'Start_Experience', #6
    	'End_Experience', #7
    	'name_Of_Education', #8
    	'Start_Edu', #9
    	'End_Edu', #10
    	'Role_Edu', #11
    	'Skills', #12
		'Sex', #13
		'Sector', #14
		'Speciality', #15
		'Reciving', #16
		"Full_name" #17

		]
    c.execute(f"SELECT {db_list[x]} FROM clients WHERE User_id = %s", (id,))
    data = c.fetchone()
    conn.commit()
    c.close()
    conn.close()
    return data[0]

def insert_user(user_id):
	conn, c = connecting()
	if does_exist(user_id, False):
		c.execute("DELETE FROM clients WHERE User_id = %s", (user_id,))
	c.execute("""
            INSERT INTO clients(User_id)
            VALUES (%s)
            """, (user_id,))
	conn.commit()
	c.close()
	conn.close()

def does_exist(id, return_data):
	conn, c = connecting()
	c.execute("""SELECT * FROM clients WHERE User_id = %s""", (id,))
	user_data = c.fetchone()
	c.close()
	conn.close()
	if user_data == None:
		return False
	elif user_data != None and return_data:
		return user_data
	else:
		return True



def id2dict(id):
	conn, c = connecting()
	c.execute("SELECT * FROM clients WHERE User_id = %s", (id,))
	db = list(c.fetchone())
	
	for i in range(len(db) - 1):
		if db[i] == None:
			db[i] = ""
	dictionary = {}
	dictionary["user_id"] = id
	dictionary["name"] = db[1]
	dictionary["role"] = db[18]
	dictionary["age"] = db[2]
	dictionary["phone_number"] = db[4]
	dictionary["email"] = db[5]
	dictionary["gender"] = db[3]
	edu = [
		db[11].split("\n"),
		db[12].split("\n"),
		db[13].split("\n"),
		db[14].split("\n")]
	edu_dicts = []
	x = len(edu[0])
	for h in range(len(edu)):
		for i in edu[h]:
			if "*" in i:
				edu[h][edu[h].index(i)] = ""			
		while len(edu[h]) > x:
			edu[h].pop(-1)
		while len(edu[h]) < x:
			edu[h].append("")
		

	for i in range(x):
		edu_dicts.append({"university":edu[0][i], "degree": edu[-1][i], "start": edu[1][i], "end":edu[2][i]})
	dictionary["education"] = edu_dicts
	if db[7] != "":
		exp = [
			db[7].split("\n"),
			db[9].split("\n"),
			db[10].split("\n"),
			db[8].split("\n")]
		exp_dicts = []
		x = len(exp[0])

		for h in range(len(exp)):
			for i in exp[h]:
				if "*" in i:
					exp[h][exp[h].index(i)] = ""
			while len(exp[h]) > x:
				exp[h].pop(-1)
			while len(exp[h]) < x:
				exp[h].append("")
			

		for i in range(x):
			exp_dicts.append({"company":exp[0][i], "role": exp[-1][i], "start": exp[1][i], "end":exp[2][i]})
		dictionary["experience"] = exp_dicts
	else:
		dictionary["experience"] = ""
	skills = db[15].split("\n")
	dictionary["skills"] = skills
	dictionary["about"] = db[6]
	dictionary["sector"] = db[17]
	return dictionary
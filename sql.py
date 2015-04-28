#!/usr/bin/python
# _*_ coding:utf-8 _*_
import MySQLdb

def islogined(val1,val2):
	
	try:
		sql = "select * from users where username ='" + val1 + "'and passwd ='" + val2 +"'"

		conn = MySQLdb.connect(host = 'localhost',user = 'root',
			passwd = 'root', db = 'work2me',port = 3306)
		cur = conn.cursor()
		cur.execute(sql)
		result = cur.fetchall()
		cur.close()
		conn.close()
		return result
	except MySQLdb.Error, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])

	
def toUsername(val1, val2):
	result = islogined(val1,val2)
	return result[0][1]

def send_mess(val1, val2, val3, val4):
	try:
		
		sql = "insert into messengers values (default,'" + val1 + "', '" + val2 + "', '"+ val3 + "', '"+ val4 + "')"
		conn = MySQLdb.connect(host = 'localhost',user = 'root',
			passwd = 'root', db = 'work2me',port = 3306)
		cur = conn.cursor()
		cur.execute(sql)
		conn.commit()
		cur.close()
		conn.close()

	except MySQLdb.Error, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def get_timeline(val):
	try:
		sql = "select * from messengers where hoster = any( select hosteduser from friends where hostuser = '" + val + "') order by time DESC" 
		conn = MySQLdb.connect(host = 'localhost',user = 'root',
			passwd = 'root', db = 'work2me',port = 3306)
		cur = conn.cursor()
		cur.execute(sql)
		result = cur.fetchall()
		cur.close()
		conn.close()

		return result

	except MySQLdb.Error, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])









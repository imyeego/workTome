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
		
		sql = "insert into messengers values (default,'" + val1 + "', '" + val2 + "','/static/images/"+ val3 +"',default,default,default,default,"+str(val4)+",default)"
		conn = MySQLdb.connect(host = 'localhost',user = 'root',
			passwd = 'root', db = 'work2me',port = 3306)
		cur = conn.cursor()
		cur.execute(sql)
		conn.commit()
		cur.close()
		conn.close()

	except MySQLdb.Error, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def send_mess_nopic(val1,val2,val3):
	sql = "insert into messengers (mid,hoster,content,time) values (default,'" + val1 + "', '" + val2 + "', '"+ str(val3) +"')"
	try:
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

def get_user_pic(val):
	try:
		sql = "select picture from users where username = '" + val + "'"
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

def get_mid(creattime):
	sql = "select mid from messengers where time = '"+ creattime +"'"
	try:
		conn = MySQLdb.connect(host = 'localhost',user = 'root',
			passwd = 'root', db = 'work2me',port = 3306)
		cur = conn.cursor()
		cur.execute(sql)
		result = cur.fetchall()
		cur.close()
		conn.close()

		return str(result[0][0])
	except MySQLdb.Error, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def insert_pic(mid, picname):
	sql = "insert into messen_pic values(default," + mid +",'/static/images/" + picname +"')"
	try:
		conn = MySQLdb.connect(host = 'localhost',user = 'root',
			passwd = 'root', db = 'work2me',port = 3306)
		cur = conn.cursor()
		cur.execute(sql)
		conn.commit()
		result = cur.fetchall()
		cur.close()
		conn.close()

	except MySQLdb.Error, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def get_mess_pic(mid):
	sql = "select src from messen_pic where mid = " +str(mid)
	try:
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

def insert_user(val1,val2,val3):
	sql = "insert into users (uid,username,email,passwd) values(default,'" + val1+ "','" + val2 + "','" +val3+ "')"
	try:
		conn = MySQLdb.connect(host = 'localhost',user = 'root',
			passwd = 'root', db = 'work2me',port = 3306)
		cur = conn.cursor()
		cur.execute(sql)
		conn.commit()
		result = cur.fetchall()
		cur.close()
		conn.close()
	except MySQLdb.Error, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def isContainsUsername(val):
	sql = "select * from users where username = '" +val+"'"
	try:
		conn = MySQLdb.connect(host = 'localhost',user = 'root',
			passwd = 'root', db = 'work2me',port = 3306)
		cur = conn.cursor()
		result=cur.execute(sql)
		cur.close()
		conn.close()
		return result
	except MySQLdb.Error, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def isContainsEmail(val):
	sql = "select * from users where email = '" +val+"'"
	try:
		conn = MySQLdb.connect(host = 'localhost',user = 'root',
			passwd = 'root', db = 'work2me',port = 3306)
		cur = conn.cursor()
		result=cur.execute(sql)
		cur.close()
		conn.close()
		return result
	except MySQLdb.Error, e:
		"Mysql Error %d: %s" % (e.args[0], e.args[1])

def get_userinfo(val):
	sql = "select * from users where username='"+val+"'"
	try:
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

def getMessByUsername(val):
	sql = "select * from messengers where hoster = '"+val+"' order by time DESC limit 5"
	try:
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

def getfollowings(val):
	sql = "select * from friends where hostuser = '" +val+ "'"
	try:
		conn = MySQLdb.connect(host = 'localhost',user = 'root',
			passwd = 'root', db = 'work2me',port = 3306)
		cur = conn.cursor()
		result=cur.execute(sql)
		
		cur.close()
		conn.close()

		return result-1
	except MySQLdb.Error, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def getfollowers(val):
	sql = "select * from friends where hosteduser = '" +val+ "'"
	try:
		conn = MySQLdb.connect(host = 'localhost',user = 'root',
			passwd = 'root', db = 'work2me',port = 3306)
		cur = conn.cursor()
		result=cur.execute(sql)
		
		cur.close()
		conn.close()

		return result-1
	except Exception, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def getwork_exprencebyusername(val):
	sql = "select * from work_exprence where username = '"+val+"'"
	try:
		conn = MySQLdb.connect(host = 'localhost',user = 'root',
			passwd = 'root', db = 'work2me',port = 3306)
		cur = conn.cursor()
		cur.execute(sql)
		result = cur.fetchall()
		cur.close()
		conn.close()

		return result
	except Exception, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def getedu_exprencebyusername(val):
	sql ="select * from edu_exprence where username = '"+val+"'"
	try:
		conn = MySQLdb.connect(host = 'localhost',user = 'root',
			passwd = 'root', db = 'work2me',port = 3306)
		cur = conn.cursor()
		cur.execute(sql)
		result = cur.fetchall()
		cur.close()
		conn.close()

		return result
	except Exception, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def gettopics():
	sql = "select name,rank from topics order by rank limit 6"
	try:
		conn = MySQLdb.connect(host = 'localhost',user = 'root',
			passwd = 'root', db = 'work2me',port = 3306)
		cur = conn.cursor()
		cur.execute(sql)
		result = cur.fetchall()
		cur.close()
		conn.close()

		return result
	except Exception, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def mess_add_like(val):
	sql = "select lik from messengers where mid = '"+str(val)+"'"
	try:
		conn = MySQLdb.connect(host = 'localhost',user = 'root',
			passwd = 'root', db = 'work2me',port = 3306)
		cur = conn.cursor()
		cur.execute(sql)
		result = cur.fetchall()
		new_result = result[0][0] + 1
		cur.close()
		conn.close()

		return mess_like(new_result,val)
	except MySQLdb.Error, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def mess_like(val,mid):
	sql = "update messengers set lik = "+ str(val) +" where mid = "+ str(mid) +""
	try:
		conn = MySQLdb.connect(host = 'localhost',user = 'root',
			passwd = 'root', db = 'work2me',port = 3306)
		cur = conn.cursor()
		cur.execute(sql)
		conn.commit()
		result = cur.fetchall()
		cur.close()
		conn.close()

	except Exception, e:
		raise e

def getrecommends(val):
	sql = "select uid,username,picture from users where username = any(select re_username from recommend_person where username ='"+val+"') limit 2"
	try:
		conn = MySQLdb.connect(host = 'localhost',user = 'root',
			passwd = 'root', db = 'work2me',port = 3306)
		cur = conn.cursor()
		cur.execute(sql)
		result = cur.fetchall()
		cur.close()
		conn.close()

		return result
	except Exception, e:
		raise e

def action_follow(val1,val2):
	sql ="insert into friends values (default,'"+val1+"','"+val2+"',0)"
	try:
		conn = MySQLdb.connect(host = 'localhost',user = 'root',
			passwd = 'root', db = 'work2me',port = 3306)
		cur = conn.cursor()
		cur.execute(sql)
		conn.commit()
		result = cur.fetchall()
		cur.close()
		conn.close()
		deletebyusername(val2)
	except Exception, e:
		raise e

def deletebyusername(val):
	sql = "delete from recommend_person where re_username = '"+val+"'"
	try:
		conn = MySQLdb.connect(host = 'localhost',user = 'root',
			passwd = 'root', db = 'work2me',port = 3306)
		cur = conn.cursor()
		cur.execute(sql)
		conn.commit()
		result = cur.fetchall()
		cur.close()
		conn.close()
	except Exception, e:
		raise e

def getmessenages(val):
	sql = "select * from messengers where hoster ='"+val+"'"
	try:
		conn = MySQLdb.connect(host = 'localhost',user = 'root',
			passwd = 'root', db = 'work2me',port = 3306)
		cur = conn.cursor()
		result=cur.execute(sql)
		
		cur.close()
		conn.close()

		return result-1
	except Exception, e:
		raise e

def search_person(val):
	sql = "select picture,username from users where username like '%"+val+"%'"
	try:
		conn = MySQLdb.connect(host = 'localhost',user = 'root',
			passwd = 'root', db = 'work2me',port = 3306)
		cur = conn.cursor()
		per_count=cur.execute(sql)
		result = cur.fetchall()
		cur.close()
		conn.close()

		return per_count,result
	except Exception, e:
		raise e

def search_topic(val):
	sql = "select name,rank from topics where name like '%"+val+"%'"
	try:
		conn = MySQLdb.connect(host = 'localhost',user = 'root',
			passwd = 'root', db = 'work2me',port = 3306)
		cur = conn.cursor()
		top_count = cur.execute(sql)
		result = cur.fetchall()
		cur.close()
		conn.close()

		return top_count,result
	except Exception, e:
		raise e

def search_company(val):
	sql = "select company_name,com_logo from companies where company_name like '%"+val+"%'"
	try:
		conn = MySQLdb.connect(host = 'localhost',user = 'root',
			passwd = 'root', db = 'work2me',port = 3306)
		cur = conn.cursor()
		com_count = cur.execute(sql)
		result = cur.fetchall()
		cur.close()
		conn.close()

		return com_count,result
	except Exception, e:
		raise e

def search_mess(val):
	sql = "select hoster,content,time from messengers where content like '%"+val+"%'"
	try:
		conn = MySQLdb.connect(host = 'localhost',user = 'root',
			passwd = 'root', db = 'work2me',port = 3306)
		cur = conn.cursor()
		mess_count = cur.execute(sql)
		result = cur.fetchall()
		cur.close()
		conn.close()

		return mess_count,result
	except Exception, e:
		raise e

def write_mess_log(val1,val2,val3):
	sql = "insert into messen_log values(default,"+str(val1)+",'"+val2+"',"+str(val3)+")"
	try:
		conn = MySQLdb.connect(host = 'localhost',user = 'root',
			passwd = 'root', db = 'work2me',port = 3306)
		cur = conn.cursor()
		cur.execute(sql)
		conn.commit()
		result = cur.fetchall()
		cur.close()
		conn.close()
	except Exception, e:
		raise e

def getnewmess(val):
	sql = "select count(mid) from messen_log where reader!='"+val+"' and mid = any(select mid from messengers where hoster=any(select hosteduser from friends where hostuser='"+val+"'))"
	try:
		conn = MySQLdb.connect(host = 'localhost',user = 'root',
			passwd = 'root', db = 'work2me',port = 3306)
		cur = conn.cursor()
		result=cur.execute(sql)
		
		cur.close()
		conn.close()
		return result
	except MySQLdb.Error, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def updatebasic(val,val1,val2,val3):
	sql = "update users set cur_work ='"+val1+"',address ='"+val2+"',sign='"+val3+"' where username ='"+val+"'"
	try:
		conn = MySQLdb.connect(host = 'localhost',user = 'root',
			passwd = 'root', db = 'work2me',port = 3306)
		cur = conn.cursor()
		cur.execute(sql)
		conn.commit()
		result = cur.fetchall()
		cur.close()
		conn.close()
	except MySQLdb.Error, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def updatebasicByPic(val,val1):
	sql = "update users set picture = '/static/images/"+val1+"' where username ='"+val+"'"
	try:
		conn = MySQLdb.connect(host = 'localhost',user = 'root',
			passwd = 'root', db = 'work2me',port = 3306)
		cur = conn.cursor()
		cur.execute(sql)
		conn.commit()
		result = cur.fetchall()
		cur.close()
		conn.close()
	except Exception, e:
		raise e

def new_dire_messen(val,val1,val2,val3):
	sql = "insert into direct_messen values(default,'"+val+"','"+val1+"','"+val2+"',"+str(val3)+",default)"
	try:
		conn = MySQLdb.connect(host = 'localhost',user = 'root',
			passwd = 'root', db = 'work2me',port = 3306) #与数据库建立连接
		cur = conn.cursor() #定义游标
		cur.execute(sql) #执行sql语句
		conn.commit() #保存
		result = cur.fetchall() 
		cur.close()
		conn.close()
	except Exception, e:
		raise e

def getnewdirect_messen(val):
	sql = "select * from direct_messen where sender like '%"+val+"%' or receiver like '%"+val+"%' order by send_time DESC"
	try:
		conn = MySQLdb.connect(host = 'localhost',user = 'root',
			passwd = 'root', db = 'work2me',port = 3306)
		cur = conn.cursor()
		cur.execute(sql)
		conn.commit()
		result = cur.fetchall()
		cur.close()
		conn.close()
		return result
	except Exception, e:
		raise e

def readedById(val):
	sql = "update direct_messen set state='1' where meid = "+val+""
	try:
		conn = MySQLdb.connect(host = 'localhost',user = 'root',
			passwd = 'root', db = 'work2me',port = 3306)
		cur = conn.cursor()
		cur.execute(sql)
		conn.commit()
		result = cur.fetchall()
		cur.close()
		conn.close()
	except MySQLdb.Error, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def getUnreadByUname(val):
	sql = "select count(meid) from direct_messen where state = '0' and (sender ='"+val+"' or receiver ='"+val+"')"
	try:
		conn = MySQLdb.connect(host = 'localhost',user = 'root',
			passwd = 'root', db = 'work2me',port = 3306)
		cur = conn.cursor()
		count = cur.execute(sql)
		conn.commit()
		result = cur.fetchall()
		cur.close()
		conn.close()
		return count
	except MySQLdb.Error, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def getfollowingsByDetails(val):
	sql = "select * from friends where hostuser = '" +val+ "'"
	try:
		conn = MySQLdb.connect(host = 'localhost',user = 'root',
			passwd = 'root', db = 'work2me',port = 3306)
		cur = conn.cursor()
		count = cur.execute(sql)
		
		result = cur.fetchall()
		cur.close()
		conn.close()
		return result
	except MySQLdb.Error, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def getfollowersByDetails(val):
	sql = "select * from friends where hosteduser = '" +val+ "'"
	try:
		conn = MySQLdb.connect(host = 'localhost',user = 'root',
			passwd = 'root', db = 'work2me',port = 3306)
		cur = conn.cursor()
		count = cur.execute(sql)
		
		result = cur.fetchall()
		cur.close()
		conn.close()
		return result
	except MySQLdb.Error, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def delfrid(val):
	sql = "delete from friends where fri_id ="+str(val)+""
	try:
		conn = MySQLdb.connect(host = 'localhost',user = 'root',
			passwd = 'root', db = 'work2me',port = 3306)
		cur = conn.cursor()
		count = cur.execute(sql)
		conn.commit()
		result = cur.fetchall()
		cur.close()
		conn.close()
	except MySQLdb.Error, e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def insert_star(val1,val2,val3):
	sql =""
	try:
		conn = MySQLdb.connect(host = 'localhost',user = 'root',
			passwd = 'root', db = 'work2me',port = 3306)
		cur = conn.cursor()
		count = cur.execute(sql)
		conn.commit()
		result = cur.fetchall()
		cur.close()
		conn.close()
	except Exception, e:
		raise e






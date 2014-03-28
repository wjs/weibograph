# coding=utf-8

import sqlite3
import datetime

conn = sqlite3.connect('weibograph/db/weibograph.db', check_same_thread = False)
conn.text_factory = str
cursor = conn.cursor()


def search_user(keyword):
	try:
		sql = 'select uid, nick from user where uid="'+keyword+'" or nick like "%'+keyword+'%" limit 50'
		return cursor.execute(sql).fetchall()
	except Exception, e:
		print '>>>[Error: search_user]', keyword, e
		return []


def is_user_exist(uid):
	try:
		sql = 'select count(uid) from user where uid="'+uid+'"'
		count = cursor.execute(sql).fetchone()[0]
		if count > 0: return True
	except Exception, e:
		print '>>>[Error: is_user_exist]', uid, e
	return False

def add_user(uid, nick, follows, fans):
	try:
		sql = 'insert into user(uid, nick, follows, fans, modify_time) values(?, ?, ?, ?, CURRENT_TIMESTAMP)'
		param = (uid, nick, follows, fans)
		cursor.execute(sql, param)
		conn.commit()
	except Exception, e:
		print '>>>[Error: add_user]', uid, e


def query_user(uid):
	try:
		sql = 'select * from user where uid="'+uid+'"'
		return cursor.execute(sql).fetchone()
	except Exception, e:
		print '>>>[Error: query_user]', uid, e
		return None


def update_user_db_follows(uid, db_follows):
	try:
		sql = 'update user set db_follows=?, modify_time=CURRENT_TIMESTAMP where uid=?'
		param = (int(db_follows), uid)
		cursor.execute(sql, param)
		conn.commit()
	except Exception, e:
		print '>>>[Error: update_user_db_follows]', uid, db_follows, e


def get_db_follows(uid):
	try:
		sql = 'select uid, nick, follows, fans from user where uid in (select target from relation where source="'+uid+'")'
		return cursor.execute(sql).fetchall()
	except Exception, e:
		print '>>>[Error: get_db_follows]', uid, e
		return None


def count_db_follows(uid):
	try:
		sql = 'select count(target) from relation where source="'+uid+'"'
		return cursor.execute(sql).fetchone()[0]
	except Exception, e:
		print '>>>[Error: count_db_follows]', uid, e
		return 0

def add_relation(source, target):
	try:
		sql = 'insert into relation values (?, ?)'
		param = (source, target)
		cursor.execute(sql, param)
		conn.commit()
	except Exception, e:
		print '>>>[Error: add_relation]', source, target, e
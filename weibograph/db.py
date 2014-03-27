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
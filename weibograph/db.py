# coding=utf-8

import sqlite3
import datetime

conn = sqlite3.connect('weibograph/db/weibograph.db', check_same_thread = False)
conn.text_factory = str
cursor = conn.cursor()


def search_user(keyword):
	try:
		sql = 'select uid, nick from user where uid=? or nick like "%'+keyword+'%" limit 50'
		param = (keyword)
		return cursor.execute(sql, param).fetchall()
	except Exception, e:
		print '>>>[Error: search_user]', keyword, e
		return []


def add_user(uid, nick, follows, fans):
	try:
		sql = 'insert into user(uid, nick, follows, fans, create_time, modify_time) values(?, ?, ?, ?, ?, ?)'
		param = (uid, nick, follows, fans, datetime.datetime.now(), datetime.datetime.now())
		cursor.execute(sql, param)
		conn.commit()
	except Exception, e:
		print '>>>[Error: add_user]', uid, e
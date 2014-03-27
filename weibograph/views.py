# coding=utf-8

from weibograph import app
from flask import render_template, request, Response
import json
import db
import weibo_crawl


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/search', methods=['GET'])
def search():
	result = db.search_user(request.args.get('keyword'))
	print result
	json_list = '['
	if len(result) > 0:
	    for row in result:
	    	json_list += '{uid:"'+row[0]+'", nick:"'+row[1]+'"},'
        json_list = json_list[:-1]
	json_list += ']'
	return Response(json.dumps(json_list), mimetype='application/json')


@app.route('/crawl', methods=['POST'])
def crawl():
	args = request.data.split('&')
	crawl_uid = args[0].split('=')[1]
	username = args[1].split('=')[1]
	pwd = args[2].split('=')[1]
	weibo_crawl.crawl_by_uid(crawl_uid, username, pwd)
	return ''
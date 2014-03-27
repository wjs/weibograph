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


@app.route('/graph', methods=['GET'])
def get_graph():
	self_uid = request.args.get('uid')
	self = db.query_user(self_uid)
	nodes = '"nodes":[{"uid":' + self[0] + ', "nick":"' + self[1] + '", "follows":' + str(self[2]) + ', "fans":' + str(self[3]) + '},'
	links = '"links":[]'
	# relations = Relation.query.with_entities(Relation.target).filter_by(source=self_uid).all()
	# follows_ids = [r[0] for r in relations]
	# follows = User.query.filter(User.uid.in_(follows_ids)).all()

	# follows = Relation.query(target)
	# if follows:
	# 	for row in follows:
	# 		nodes += '{"uid":' + row[0] + ', "nick":"' + row[1] + '", "follows":' + str(row[2]) + ', "fans":' + str(row[3]) + '},'
	# 		links += '{"source":' + self_uid + ',"target":' + row[0] + '},'
	nodes = nodes[:-1] + ']'
	# links = links[:-1] + ']'
	# else:
	# 	nodes = nodes[:-1] + ']'
	# 	links += ']'
	
	return '{' + nodes + ', ' + links + '}'


@app.route('/crawl', methods=['POST'])
def crawl():
	args = request.data.split('&')
	crawl_uid = args[0].split('=')[1]
	username = args[1].split('=')[1]
	pwd = args[2].split('=')[1]
	weibo_crawl.crawl_by_uid(crawl_uid, username, pwd)
	return ''
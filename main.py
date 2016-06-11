from flask import Flask, render_template, request, jsonify, url_for
from get_them_grades import *
app = Flask(__name__)

@app.route("/")
def hello():
	return render_template("main.html")

@app.route("/results", methods=["GET", "POST"])
def results():
	# print request.json
	u=request.form["user"]
	p=request.form["pass"]
	# print u
	# print p
	# print "json",request.json
	# print "forn",request.form
	# print "request",request
	return jsonify(get_results(u,p))
	# return jsonify({"asd":2})

if __name__=="__main__":
	app.run()
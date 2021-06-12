from flask_pymongo import PyMongo
import flask
from flask import Flask
from flask_cors import CORS
import pymongo
import asyncio
from flask import request
from flask import render_template


#connection URI
connection_url = 'mongodb+srv://admin:Machine1234@cluster0.0wb2a.mongodb.net/wine_master_db?retryWrites=true&w=majority'

app = Flask(__name__)

client = PyMongo(app, connection_url)
  
# Database
#db = client.get_database('wine_master_db')
db = client.db
#print(db)

#print(db.collection_names())

coll = db.all_wines
#print(coll)

#print(list(coll.find({})))

@app.route('/find-one/<argument>/<value>', methods=['GET'])
def findOne(argument, value):
    if not argument or not value:
        return flask.jsonify({})
    query = {argument: value}
    # wine = coll.find_one(query)
    wines = format_multiple(list(coll.find(query)))
    print(f"query :: {query}, wines :: {wines}")
    return flask.jsonify(wines)


@app.route("/")
def home():
    all_wines = format_multiple(list(coll.find({})))
    print(f"length :: {len(all_wines)}")
    return flask.jsonify(all_wines)

def format_multiple(wines):
    formatted_wines = []
    if not wines:
        return formatted_wines
    for wine in wines:
        formatted_wines.append(format_single(wine))
    return formatted_wines

def format_single(wine):
    wine["_id"] = str(wine["_id"])
    return wine
def get_variety(answers): 
    return 'Pinot Noir'  


@app.route('/questions', methods = ['POST', 'GET'])
def signup():
    if request.method == 'POST':
        answers = {'category': request.form['category'],
            'body': request.form['body']}
    else: 
        answers= {}
    variety = get_variety(answers)
    wines = format_multiple(list(coll.find({'Variety':variety})))
    print (answers)

    return flask.jsonify(wines)
    return redirect('/')

@app.route("/forms")
def form():
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)

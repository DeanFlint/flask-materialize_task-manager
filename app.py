import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from config import mongo_uri

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = mongo_uri

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", 
    tasks=mongo.db.tasks.find())
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
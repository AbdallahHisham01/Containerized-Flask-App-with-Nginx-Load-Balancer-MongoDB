from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

app = Flask(__name__)

# Get MongoDB connection details from environment variables
mongodb_host = os.environ.get("MONGO_HOST", "localhost")
mongodb_port = int(os.environ.get('MONGO_PORT', '27017'))

# Connect to MongoDB
client = MongoClient(mongodb_host, mongodb_port)
db = client.flask_database  # Creating a MongoDB database
todos = db.todos  # Creating a collection named "todos"

# Get and Post Route
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":  # If POST request, insert a todo document
        content = request.form['content']
        degree = request.form['degree']
        todos.insert_one({'content': content, 'degree': degree})
        return redirect(url_for('index'))  # Redirect the user to home page
    
    all_todos = todos.find()  # Fetch all todo documents
    return render_template('index.html', todos=all_todos)  # Render home page

# Delete Route
@app.route("/<id>/delete/", methods=['POST'])
def delete(id):  # Delete function by targeting a todo document by its ID
    todos.delete_one({"_id": ObjectId(id)})  # Delete the selected document by its converted ID
    return redirect(url_for('index'))  # Redirect to home page

# Run the Flask app
if __name__ == "__main__":
    env = os.environ.get('FLASK_ENV', 'development')
    port = int(os.environ.get('PORT', 5000))
    debug = (env != 'production')  # Debug mode enabled only in non-production
    loadbalancer=os.environ.get("LOADBALANCER","0.0.0.0")
    app.run(host="loadbalancer", port=port, debug=debug)


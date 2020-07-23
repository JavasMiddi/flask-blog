# import Flask class from the flask module
from flask import Flask
# create a new instance of Flask and store it in app 
app = Flask(__name__)
# import the ./application/routes.py file
from application import routes

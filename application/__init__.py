from flask import Flask


app = Flask(__name__)

# controller 
from application.controllers.homeController import *


#import dependencies 
from flask import Flask, render_template, redirect
import scrape_mars
import time
from bs4 import BeautifulSoup
from flask_pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app, uri="mongodb://localhost:27017/")


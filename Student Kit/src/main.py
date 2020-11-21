import random
import secrets
import os
from datetime import datetime
from flask import Flask, render_template, redirect, url_for, send_file, request
from flask_sqlalchemy import SQLAlchemy
from flaskwebgui import FlaskUI
from win10toast import ToastNotifier
from flask_uploads import UploadSet, configure_uploads, ALL
import requests
import wikipedia
print("Imported Modules")

app = Flask(__name__)
from flask import render_template
from app import app
import stripe
from flask import Flask, redirect, url_for, render_template, request, session
import json
import sys
import os


#app = Flask(__name__)
#app.secret_key = os.urandom(12)  # Generic key for dev purposes only
pub_key = 'pk_test_EXQzqiADhufPflyUzyMAgske00ZAJZdtQj'
secret_key = 'sk_test_kdA54XOEj0GzAQPvsGpgfbOA00AewhFkYC'


stripe.api_key = secret_key

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')


@app.route('/pay', methods=['POST'])
def pay():
	print(request.form)

	return ''

#if __name__ == '__main__':
#	app.run(debug=True)
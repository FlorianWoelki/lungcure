from flask import request, render_template, redirect, url_for
from app import app
import stripe
import os
from dotenv import load_dotenv  # Import to load production.env file

# Load Environment Variables File
BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, './production.env'))

# Get the pub and secret key from the env file and set the stripe api key
pub_key = os.getenv('pub_key')
secret_key = os.getenv('secret_key')
stripe.api_key = secret_key

@app.route('/')
def index():
	return render_template('index.html', pub_key=pub_key)


@app.route('/image_upload')
def image_upload():
	return render_template('image_upload.html')


@app.route('/pay', methods=['POST', 'GET'])
def pay():
	"""customer = stripe.Customer.create(email=request.form['stripeEmail'], source=request.form['stripeToken'])
	charge = stripe.Charge.create(
		customer=customer.id,
		amount=2099,
		currency='usd',
		description='lungcure'
	)"""
	return redirect(url_for('image_upload'))

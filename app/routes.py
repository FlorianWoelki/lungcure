from flask import request, render_template, redirect, url_for
from app import app
import stripe
from dotenv import load_dotenv  # Import to load production.env file
from os import getenv  # Import os.getenv to retrieve environment variables

# Load Environment Variables File
load_dotenv("production.env")

pub_key = getenv('pub_key')
secret_key = getenv('secret_key')
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

from flask import request, render_template, redirect, url_for
from app import app
import stripe

pub_key = 'pk_test_QWt1IDL44XIi0iQDVGtzLXJ8'
secret_key = 'sk_test_ViKCe4YERFqKhmiPEu0GToRW'
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

from flask import request, render_template, redirect, url_for
from app import app
import stripe
import os
from dotenv import load_dotenv  # Import to load production.env file
from model_deploy import *
import tensorflow as tf
model = build_model()
graph = tf.get_default_graph()


# Load Environment Variables File
BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, './production.env'))

# Get the pub and secret key from the env file and set the stripe api key
pub_key = os.getenv('pub_key')
secret_key = os.getenv('secret_key')
stripe.api_key = secret_key

# Define the allowed file extensions that can be uploaded
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

# Defining the model labels
labels = ['Atelectasis', 'Cardiomegaly', 'Consolidation', 'Edema', 'Effusion',
					'Emphysema', 'Fibrosis', 'Hernia', 'Infiltration', 'Mass', 'Nodule',
					'Pleural_Thickening', 'Pneumonia', 'Pneumothorax']


@app.route('/')
def index():
	return render_template('index.html', pub_key=pub_key)


@app.route('/image_upload')
def image_upload():
	return render_template('image_upload.html', predictions=[])


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/predict', methods=['POST', 'GET'])
def predict():
	if 'file' not in request.files:
		return render_template('image_upload.html', predictions=[])
	
	file = request.files['file']
	if file.filename == '':
		return render_template('image_upload.html', predictions=[])
	
	if file and allowed_file(file.filename):
		global graph
		with graph.as_default():
			predictions = predict_image(model, file)
		"""return_values = {}
		for i in range(len(predictions[0])):
			prediction = predictions[0][i]
			return_values[labels[i]] = prediction"""
		return render_template('image_upload.html', predictions=list(predictions[0]))

	return render_template('image_upload.html', predictions=[])


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

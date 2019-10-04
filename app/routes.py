from flask import request, render_template, redirect, url_for # Import to do all routing stuff
from app import app # Import app to use routes 
import stripe # Import for payment process
import os # Import to get files
from dotenv import load_dotenv # Import to load production.env file
from model_deploy import * # Import to build the model and predict a image
import tensorflow as tf # Import to build the graph for the model


model = build_model() # Build the model with the specific json and h5 weights file
graph = tf.get_default_graph() # Get the default graph from tensorflow

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
		return render_template('image_upload.html', predictions=list(predictions[0]))

	return render_template('image_upload.html', predictions=[])


@app.route('/pay', methods=['POST', 'GET'])
def pay():
	return redirect(url_for('image_upload'))


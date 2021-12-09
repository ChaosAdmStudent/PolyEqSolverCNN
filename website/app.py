from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer 
import os 
from preprocess import segment_image 
from tensorflow.keras.models import load_model 
from preprocess import segment_image, resize, get_eqlabels
from postprocess import get_pred
from PolyEquations import polyEqSolver
import numpy as np 
import warnings 

warnings.filterwarnings("ignore")
app = Flask(__name__)

# Loading CNN Model 
MODEL_PATH = 'C:\\Users\\lakshya\\Documents\\VIT\\5th Semester\\ML\\Flask\\PolyEqSolver.h5'
model = load_model(MODEL_PATH)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/solver.html')
def solver():
    return render_template('solver.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload(): 
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        #Pre process Image 

        img = segment_image(file_path)  
        img = resize(img) 
        eq = np.array(img) 

        # Make prediction
        preds = get_pred(model, eq) 
        result = polyEqSolver(preds)
        
        return result

    return None

if __name__ == '__main__':
    app.run(debug=True)
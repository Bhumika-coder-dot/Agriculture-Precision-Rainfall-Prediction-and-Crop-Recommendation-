from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load the pre-trained models
rainfall_model = pickle.load(open('models/rainfall_model.pkl', 'rb'))
crop_model = pickle.load(open('models/crop_recommendation_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    temperature = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    previous_rainfall = float(request.form['previous_rainfall'])
    soil_type = int(request.form['soil_type'])
    nitrogen_level = float(request.form['nitrogen_level'])
    
    # Predict rainfall
    rainfall_input = [[temperature, humidity, previous_rainfall]]
    predicted_rainfall = rainfall_model.predict(rainfall_input)[0]
    
    # Predict crop recommendation
    crop_input = [[soil_type, nitrogen_level, predicted_rainfall, temperature]]
    recommended_crop = crop_model.predict(crop_input)[0]
    
    # Pass the results to result.html
    return render_template('result.html', rainfall=predicted_rainfall, crop=recommended_crop)

if __name__ == '__main__':
    app.run(debug=True)

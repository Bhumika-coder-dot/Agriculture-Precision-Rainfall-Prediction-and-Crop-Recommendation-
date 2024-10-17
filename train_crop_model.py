import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle

# Load the crop recommendation dataset
crop_data = pd.read_csv('datasets/crop_data.csv')

# Define feature columns (X) and target column (y)
X = crop_data[['soil_type', 'nitrogen_level', 'rainfall', 'temperature']]
y = crop_data['crop']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the DecisionTreeClassifier model
crop_model = DecisionTreeClassifier()
crop_model.fit(X_train, y_train)

# Save the trained model to a pickle file
with open('models/crop_recommendation_model.pkl', 'wb') as f:
    pickle.dump(crop_model, f)

print("Crop recommendation model trained and saved as 'crop_recommendation_model.pkl'")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import pickle

# Load the rainfall prediction dataset
rainfall_data = pd.read_csv('datasets/rainfall_data.csv')

# Define feature columns (X) and target column (y)
X = rainfall_data[['temperature', 'humidity', 'previous_rainfall']]
y = rainfall_data['rainfall']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the DecisionTreeRegressor model
rainfall_model = DecisionTreeRegressor()
rainfall_model.fit(X_train, y_train)

# Save the trained model to a pickle file
with open('models/rainfall_model.pkl', 'wb') as f:
    pickle.dump(rainfall_model, f)

print("Rainfall prediction model trained and saved as 'rainfall_model.pkl'")

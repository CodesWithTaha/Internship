import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the Iris dataset
iris = load_iris()

# Create a DataFrame from the dataset
frame = pd.DataFrame(data=iris.data, columns=iris.feature_names)
frame['target'] = iris.target  # Adding target column

# Display the first few rows of the dataset
print("Sample of the loaded dataset:")
print(frame.head())

x = frame.drop('target', axis=1)
y = frame['target']

# Perform feature scaling
scaler = MinMaxScaler()
xScaled = scaler.fit_transform(x)

# Convert back to DataFrame for clarity (optional)
xScaledFramed = pd.DataFrame(xScaled, columns=x.columns)

# Display scaled features
print("\nScaled features :")
print(xScaledFramed.head())

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(xScaled, y, test_size=0.2, random_state=42)

# Display the shapes of the resulting sets
print("\nShapes of training and testing sets:")
print(f"X_train shape: {X_train.shape}, y_train length: {len(y_train)}")
print(f"X_test shape: {X_test.shape}, y_test length: {len(y_test)}")

# Initialize the linear regression model
model = LinearRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Predict on the test data
y_pred = model.predict(X_test)

# Evaluate the model using Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)
print(f"\nMean Squared Error: {mse}")

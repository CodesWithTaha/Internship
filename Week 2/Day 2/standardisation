import numpy as np
from sklearn.preprocessing import StandardScaler

# Sample data 
data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

# Initialize StandardScaler
scaler = StandardScaler()

# Fit scaler 
scaler.fit(data)

# Transform the data using the scaler accordingly
data_std = scaler.transform(data)


print("Original data:")
print(data)
print("\nStandardized data:")
print(data_std)

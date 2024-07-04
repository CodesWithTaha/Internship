from sklearn.preprocessing import MinMaxScaler
import numpy as np

# simple array
data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])


#applying the minmax algorithm
scaler = MinMaxScaler()

# calculating min and max
scaler.fit(data)

# normalizing the data
normalizedData = scaler.transform(data)


print("Original data:")
print(data)
print("\nNormalized data:")
print(normalizedData)

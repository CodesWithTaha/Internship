X = df.drop('target', axis=1)
# y = df['target']

# # Perform feature scaling
# scaler = MinMaxScaler()
# X_scaled = scaler.fit_transform(X)

# # Convert back to DataFrame for clarity (optional)
# X_scaled_df = pd.DataFrame(X_scaled, columns=X.columns)

# # Display scaled features
# print("\nScaled features (first few rows):")
# print(X_scaled_df.head())


# X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# # Display the shapes of the resulting sets
# print("\nShapes of training and testing sets:")
# print(f"X_train shape: {X_train.shape}, y_train shape: {y_train.shape}")
# print(f"X_test shape: {X_test.shape}, y_test shape: {y_test.shape}")
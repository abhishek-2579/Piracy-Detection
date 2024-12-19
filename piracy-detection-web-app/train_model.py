import pandas as pd

# Load the dataset
data = pd.read_csv("obfuscation_dataset.csv")

# Display the first few rows
print(data.head())
from sklearn.model_selection import train_test_split

# Split data into train, validation, and test sets
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
val_data, test_data = train_test_split(test_data, test_size=0.5, random_state=42)

print("Training size:", len(train_data))
print("Validation size:", len(val_data))
print("Testing size:", len(test_data))

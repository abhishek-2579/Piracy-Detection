import random
import pandas as pd

def obfuscate_text(word, obfuscation_methods):
    """
    Obfuscate the given word using random methods.
    """
    obfuscated = word
    for method in obfuscation_methods:
        if random.random() > 0.5:  # Randomly apply obfuscation
            obfuscated = method(obfuscated)
    return obfuscated

# Obfuscation methods
def replace_characters(word):
    replacements = {
        'a': ['@', '4'], 'e': ['3', '€'], 'i': ['1', '!'],
        'o': ['0', '°'], 's': ['$', '5'], 't': ['7', '+']
    }
    return ''.join(random.choice(replacements.get(c, [c])) for c in word)

def add_random_symbols(word):
    symbols = ['*', '_', '-', '~']
    return ''.join(c + random.choice(symbols) if random.random() > 0.8 else c for c in word)

def random_case(word):
    return ''.join(c.upper() if random.random() > 0.5 else c.lower() for c in word)

# Generate Dataset
keywords = ["movie", "password", "secure", "data", "piracy", "text", "example", "keyword", "test", "model"]
obfuscation_methods = [replace_characters, add_random_symbols, random_case]

dataset = []

# Generate examples per keyword
for keyword in keywords:
    for _ in range(500):  # Generates 500 examples per keyword (adjust this to grow dataset size)
        obfuscated = obfuscate_text(keyword, obfuscation_methods)
        label = "Obfuscated" if keyword != obfuscated else "Non-obfuscated"
        dataset.append((keyword, obfuscated, label))

# Convert to DataFrame
df = pd.DataFrame(dataset, columns=["Original", "Obfuscated", "Label"])

# Save to CSV file
df.to_csv("obfuscation_dataset.csv", index=False)
print("Dataset created with size:", len(df))
import pandas as pd

# Load the dataset
data = pd.read_csv("obfuscation_dataset.csv")

# Display the first few rows
print(data.head())


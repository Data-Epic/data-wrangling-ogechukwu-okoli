import pandas as pd

# Sample DataFrame with unordered index
data = {'values': [100, 200, 300, 400, 500]}
index_labels = ["11h-20h", "1h-10h", "21-30h", "31-40h", "41-50h"]  # Unordered

df = pd.DataFrame(data, index=index_labels)

# Define the correct order
correct_order = ["1h-10h", "11h-20h", "21-30h", "31-40h", "41-50h"]

# Convert index to CategoricalIndex with the defined order
df.index = pd.CategoricalIndex(df.index, categories=correct_order, ordered=True)

# Now, sort using sort_index()
df = df.sort_index()

print(df)

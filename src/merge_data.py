import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# To store all user's profile
user_profiles = []

for i in range(1, 11):
    filename = f"movies-mod-genre-new-u{i}.csv"
    df = pd.read_csv(filename, sep=";")

    # First column contains the movie name
    movie_name = df.columns[0]

    # Attribute (Genre) columns
    attribute_cols = df.columns[1:]

    # Sum all attributes for this user
    accumulated_attributes = df[attribute_cols].sum()

    # Add user name
    accumulated_attributes["User"] = f"u{i}"

    user_profiles.append(accumulated_attributes)

# Create final dataframe
source_df = pd.DataFrame(user_profiles)

# Put User column first
source_df.insert(0, "User", source_df.pop("User"))

# Save the source file
source_df.to_csv("users_accumulated_attributes.csv", index=False, sep=";")

print("Generated source file:")
print(source_df)
X = source_df.drop(columns=["User"])

# Model kMeans for k = 3
kmeans = KMeans(n_clusters = 3, random_state=33, n_init=10)

# Perform KMeans and store user's cluster in new column
source_df["Cluster"] = kmeans.fit_predict(X)

#print(source_df[["User", "Cluster"]])

# To print users of each cluster
for cluster in sorted(source_df["Cluster"].unique()):
    # Filter by "Cluster" and stored as list
    users = source_df[source_df["Cluster"] == cluster]["User"].tolist()
    print(f"Cluster {cluster}: {users}")
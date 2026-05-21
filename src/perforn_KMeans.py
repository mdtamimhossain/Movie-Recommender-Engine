# K-Means doesn't understand texts, so dropping the user column 
X = source_df.drop(columns=["User"])

# SUM OF SQUARED ERROR
sse = []

# Train for different 'k' and store
k_values = range(1, 10)
for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=33, n_init=10)
    kmeans.fit(X)
    sse.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(k_values, sse, marker="o")
plt.xlabel("Number of clusters k")
plt.ylabel("Sum of Squared Error(SSE) ")
plt.title("SSE vs k for K-Means")
plt.grid(True)
plt.show()
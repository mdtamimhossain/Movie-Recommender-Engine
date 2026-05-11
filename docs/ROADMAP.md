# Lab Work 3 Roadmap: K-Means Movie Recommender

This project must follow **Lab Work 3**. The main algorithm is **K-Means clustering**, used to group similar users and recommend movies from users in the same cluster.

The goal is not only to recommend movies, but also to show how K-Means can be applied in a movie recommendation context.

## 1. Understand The Lab Task

### Goal

Understand what Lab Work 3 expects before writing code.

### What To Do

- Read the Lab Work 3 PDF.
- Identify the required algorithm: **K-Means**.
- Understand the provided user files `u1` to `u10`.
- Understand that each user file contains movies watched by one user.
- Understand that each movie has genre or attribute columns.
- Understand that we need to create an accumulated attribute profile for each user.

### Things You Should Know

- What a dataset is.
- What rows and columns mean.
- What movie attributes or genre features are.
- Difference between a movie-level dataset and a user-level dataset.
- Basic idea of a recommendation system.

### Expected Output

You should be able to explain the lab task in one sentence:

```text
Use K-Means clustering to group users by accumulated movie attributes, then recommend movies using users from the same cluster.
```

## 2. Data Loading

### Goal

Load all required CSV files into the project.

### What To Build

- Load the main movie catalog from `resources/movies-mod-genre-new.csv`.
- Load all user files from `resources/Labwork 3 task 2 (data)/`.
- Load files such as:
  - `movies-mod-genre-new-u1.csv`
  - `movies-mod-genre-new-u2.csv`
  - `movies-mod-genre-new-u3.csv`
  - up to `u10`
- Ignore the `__MACOSX` folder.
- Clean column names by removing extra spaces.
- Convert genre and rating columns to numeric values.

### Things You Should Know

- Python file paths.
- CSV file format.
- `pandas.read_csv()`.
- Custom CSV separators, because this dataset uses semicolons `;`.
- Dataframes.
- Basic dataframe inspection using `.head()`, `.shape`, `.columns`, and `.info()`.

### Expected Output

The project should be able to load:

- The full movie catalog.
- Every user rating file from `u1` to `u10`.

### Possible File To Work On

```text
src/data_loader.py
```

## 3. Data Cleaning And Feature Selection

### Goal

Prepare the data so it can be used by the K-Means algorithm.

### What To Build

- Identify movie title column: `Movie`.
- Identify non-feature columns:
  - `Movie`
  - `index`
  - `rating`
- Identify genre or attribute columns.
- Remove unwanted spaces from column names.
- Make sure genre columns contain only numeric values.
- Make sure each user file has the same feature columns.

### Things You Should Know

- Feature columns vs. non-feature columns.
- Binary features: `0` and `1`.
- Missing values.
- Data cleaning.
- Why machine learning algorithms need numeric input.

### Expected Output

You should have a clean list of movie attribute columns such as:

```text
Romance
Comedy
Science
Fiction
Drama
Romantic
Fantacy
Animation
Adventure
Action
Thriller
Erotic
Crime
```

### Possible Files To Work On

```text
src/data_loader.py
src/utils.py
```

## 4. Accumulated User Attribute File

### Goal

Convert movie-level user files into a single user-level dataset for K-Means.

### What To Build

- For each user file, combine the attributes of the movies watched by that user.
- Create one row per user.
- Each row should contain accumulated genre or attribute values.
- The final dataset should contain all users and their accumulated attributes.

### Example

If user `u1` watched 10 movies, and 5 of them are Comedy, then the user's Comedy value may be:

```text
Comedy = 5
```

The final user-level dataset may look like:

```text
user_id, Romance, Comedy, Drama, Action, Thriller
u1,      2,       5,      3,     1,      0
u2,      1,       2,      6,     0,      1
```

### Things You Should Know

- Grouping data by user.
- Summing columns.
- What an accumulated feature vector is.
- Why K-Means needs one vector per item being clustered.
- Difference between movie vectors and user vectors.

### Expected Output

A combined user attribute dataset containing all users from `u1` to `u10`.

This dataset will be the input for K-Means.

### Possible Files To Work On

```text
src/data_loader.py
src/recommender.py
```

## 5. K-Means Clustering

### Goal

Cluster users based on their accumulated movie attributes.

### What To Build

- Use the accumulated user attribute dataset.
- Apply K-Means clustering.
- Try different values of `k`.
- Store the cluster label for each user.

### Things You Should Know

- What clustering means.
- What K-Means does.
- What `k` means in K-Means.
- What a centroid is.
- Why K-Means is an unsupervised learning algorithm.
- How to use `sklearn.cluster.KMeans`.

### Expected Output

Each user should receive a cluster label:

```text
u1 -> cluster 0
u2 -> cluster 1
u3 -> cluster 0
```

Users in the same cluster are considered similar.

### Possible File To Work On

```text
src/recommender.py
```

## 6. Choose The Best K Using SSE

### Goal

Find a suitable number of clusters for K-Means.

### What To Build

- Run K-Means for different `k` values.
- Calculate SSE for each `k`.
- Plot or print SSE values.
- Use the elbow method to choose a good `k`.

### Things You Should Know

- SSE: Sum of Squared Error.
- Inertia in scikit-learn K-Means.
- Elbow method.
- Why too few clusters may be too general.
- Why too many clusters may overfit the data.

### Expected Output

A list or plot like:

```text
k = 1, SSE = 120.5
k = 2, SSE = 75.3
k = 3, SSE = 48.8
k = 4, SSE = 44.1
```

Then choose the `k` where the improvement starts slowing down.

### Possible Files To Work On

```text
src/recommender.py
notebooks/
```

## 7. Recommendation Process Using Clusters

### Goal

Recommend movies for a selected user based on other users in the same cluster.

### What To Build

- Select a target user.
- Find the cluster of that user.
- Find other users in the same cluster.
- Collect movies watched or liked by those similar users.
- Remove movies already watched by the target user.
- Recommend the remaining movies.

### Things You Should Know

- How to filter rows by cluster label.
- How to compare one user's movie list with another user's movie list.
- Set operations:
  - watched movies
  - candidate movies
  - unseen movies
- Basic ranking logic.

### Expected Output

For a selected user, the system should print recommended movies from users in the same cluster:

```text
Target user: u3
Cluster: 1
Recommended movies:
1. Movie A
2. Movie B
3. Movie C
```

### Possible File To Work On

```text
src/recommender.py
```

## 8. Compare Predictions With Known Values

### Goal

Check how well the recommendation process matches known user ratings.

### What To Build

- Compare recommended movies with movies known to be liked by the user.
- Count correct recommendations.
- Calculate a simple accuracy value if required by the lab.
- Repeat this process multiple times if the lab asks for several runs.

### Things You Should Know

- What accuracy means.
- Difference between predicted output and known output.
- How to count correct and incorrect predictions.
- Why evaluation is important.

### Expected Output

The report should contain comparison results and achieved accuracy.

Example:

```text
Correct recommendations: 3
Total checked recommendations: 5
Accuracy: 60%
```

### Possible Files To Work On

```text
src/recommender.py
main.py
```

## 9. Command-Line Interface

### Goal

Allow the project to run from `main.py`.

### What To Build

- Let the user select a target user.
- Let the user choose the number of clusters or use the selected best `k`.
- Load user data.
- Build accumulated user attributes.
- Run K-Means.
- Generate recommendations.
- Print the results.

### Things You Should Know

- Python functions.
- Basic command-line input.
- The `if __name__ == "__main__"` pattern.
- Optional: `argparse` for command-line arguments.

### Expected Output

The project should eventually run like:

```text
python main.py
```

Or later:

```text
python main.py --user 3 --clusters 3
```

### Possible File To Work On

```text
main.py
```

## 10. Testing

### Goal

Make sure the Lab Work 3 pipeline works correctly.

### What To Build

- Test that all user files load.
- Test that feature columns are detected correctly.
- Test that accumulated user attributes are calculated correctly.
- Test that K-Means returns one cluster label per user.
- Test that recommendations exclude already watched movies.
- Test that recommendation output is not empty when similar users exist.

### Things You Should Know

- Basic `pytest`.
- Test functions.
- Test fixtures.
- Edge cases.
- How to compare expected and actual results.

### Expected Output

Running tests should confirm that each part of the lab pipeline works.

```text
pytest
```

### Possible Files To Work On

```text
tests/test_data_loader.py
tests/test_recommender.py
tests/conftest.py
```

## 11. Final Report And Documentation

### Goal

Prepare the project so it can be submitted or explained clearly.

### What To Include

- Description of the dataset.
- Explanation of accumulated user attributes.
- Explanation of K-Means.
- SSE results for different `k` values.
- Chosen `k` value.
- Cluster output.
- Recommendation output.
- Accuracy or comparison results, if required.
- Comments on the final result.

### Things You Should Know

- Basic Markdown.
- How to explain an algorithm.
- How to present results clearly.
- How to describe limitations.

### Expected Output

The final project should clearly show that it follows Lab Work 3:

```text
User files -> accumulated attributes -> K-Means -> clusters -> recommendations -> evaluation
```

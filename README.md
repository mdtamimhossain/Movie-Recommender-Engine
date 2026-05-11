# Movie Recommender Engine

Initial project scaffold for **Lab Work 3: K-Means based movie recommendation**.

## Goal

Build a movie recommender system based on the Lab Work 3 requirement: use **K-Means clustering** to group similar users from their accumulated movie attributes, then recommend movies using users from the same cluster.

## Data

- Main catalog: `resources/movies-mod-genre-new.csv`
- User ratings: `resources/Labwork 3 task 2 (data)/movies-mod-genre-new-u*.csv`

## Planned Features

- Load and clean movie/user CSV files.
- Build an accumulated attribute profile for each user.
- Create one combined user-level dataset.
- Run K-Means clustering on user profiles.
- Use SSE/elbow method to choose a suitable `k`.
- Recommend movies from users in the same cluster.
- Compare recommendation output with known values if required by the lab.

## Project Structure

```text
movie recommender engine/
  docs/
  notebooks/
  resources/
  src/
    __init__.py
    config.py
    data_loader.py
    recommender.py
    utils.py
  tests/
    __init__.py
    test_data_loader.py
    test_recommender.py
  main.py
  requirements.txt
```

## Next Step

Implement the data loading and accumulated user attribute layer.

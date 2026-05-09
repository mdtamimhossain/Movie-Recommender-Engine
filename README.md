# Movie Recommender Engine

Initial project scaffold for a content-based movie recommender.

## Goal

Build a simple recommender system that learns a user's genre preferences from rated movies and recommends similar unrated movies.

## Data

- Main catalog: `resources/movies-mod-genre-new.csv`
- User ratings: `resources/Labwork 3 task 2 (data)/movies-mod-genre-new-u*.csv`

## Planned Features

- Load and clean movie/user CSV files.
- Build a user preference profile from liked movies.
- Score candidate movies using genre similarity.
- Return top movie recommendations with simple explanations.

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

Implement the data loading and cleaning layer.

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

## Team Collaboration

This project is managed by a team of 3 developers using **Git Flow** methodology.

**Important:** Before starting work, read [docs/GIT_WORKFLOW.md](docs/GIT_WORKFLOW.md) for guidelines on:
- Creating feature branches
- Making commits and pull requests
- Code review process
- Merging to dev/master branches

**Quick Start:**
```powershell
git checkout dev
git pull origin dev
git checkout -b feature/your-feature-name
# ... make your changes ...
git push -u origin feature/your-feature-name
```

## Next Step

Implement the data loading and accumulated user attribute layer.

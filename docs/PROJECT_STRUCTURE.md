# Project Structure Explanation

This document explains the purpose of each folder and file in the movie recommender engine project.

## Root Folder

The root folder is the main project directory:

```text
movie recommender engine/
```

It contains the source code, documentation, tests, notebooks, and data resources for the project.

## `resources/`

This folder stores the Lab Work 3 dataset files used by the recommender system.

Use this folder for:

- Movie catalog CSV files
- User rating CSV files
- Any lab-provided data files

Current important files:

```text
resources/movies-mod-genre-new.csv
```

This is the main movie catalog. It contains movie names, genre columns, index values, and rating values.

```text
resources/Labwork 3 task 2 (data)/
```

This folder contains user-specific CSV files such as `movies-mod-genre-new-u1.csv`, `movies-mod-genre-new-u2.csv`, and so on. Each file represents movie ratings for one user.

```text
resources/Detailed_Recommender_Engine_Roadmap.pdf
```

This appears to be a supporting PDF document related to the recommender engine roadmap.

## `src/`

This folder will contain the main Python source code for the project.

Use this folder for:

- Data loading code
- Recommendation logic
- Configuration values
- Helper functions

Current files:

```text
src/__init__.py
```

Marks the `src` folder as a Python package. This allows files inside `src` to be imported from other parts of the project.

```text
src/config.py
```

Will store project configuration values, such as dataset paths, default settings, and constants.

Example future use:

- Main dataset path
- User dataset folder path
- Default number of recommendations
- CSV separator value

```text
src/data_loader.py
```

Will contain functions for loading and cleaning the CSV data.

Example future use:

- Load the movie catalog
- Load a selected user's ratings
- Clean column names
- Convert genre and rating columns into numeric values

```text
src/recommender.py
```

Will contain the main Lab Work 3 recommendation algorithm.

Example future use:

- Build accumulated user attribute profiles
- Run K-Means clustering
- Calculate SSE values for different `k` values
- Find users in the same cluster
- Recommend movies from similar users

```text
src/utils.py
```

Will contain small helper functions used across the project.

Example future use:

- Format output text
- Validate user IDs
- Reuse common calculations

## `tests/`

This folder will contain test files for the project.

Use this folder to check that the project works correctly as it grows.

Current files:

```text
tests/__init__.py
```

Marks the `tests` folder as a Python package.

```text
tests/conftest.py
```

Will store shared test setup code. In pytest projects, this file is commonly used for reusable test fixtures.

```text
tests/test_data_loader.py
```

Will contain tests for the data loading code.

Example future tests:

- Check that CSV files load correctly
- Check that column names are cleaned
- Check that missing files are handled properly

```text
tests/test_recommender.py
```

Will contain tests for the recommendation logic.

Example future tests:

- Check that accumulated user attributes are calculated correctly
- Check that K-Means returns cluster labels
- Check that already-watched movies are excluded from recommendations

## `docs/`

This folder contains project documentation.

Use this folder for:

- Roadmaps
- Project notes
- Design explanations
- Structure explanations

Current files:

```text
docs/ROADMAP.md
```

Describes the planned development steps for the project.

```text
docs/PROJECT_STRUCTURE.md
```

This file. It explains the purpose of each folder and file in the project.

## `notebooks/`

This folder is for Jupyter notebooks.

Use this folder for:

- Data exploration
- Testing ideas before writing final code
- Visualizing datasets
- Trying recommendation logic interactively

Current file:

```text
notebooks/.gitkeep
```

An empty placeholder file. It keeps the `notebooks` folder visible in version control even when the folder has no notebooks yet.

## `main.py`

This will be the main entry point of the project.

Use this file to run the recommender from the command line.

Example future use:

- Ask the user to choose a user ID
- Load the correct dataset
- Generate recommendations
- Print the final results

## `requirements.txt`

This file will list the Python libraries needed by the project.

Example future dependencies:

- `pandas` for reading and working with CSV data
- `numpy` for numerical calculations
- `scikit-learn` for K-Means clustering
- `pytest` for testing

For now, this file can remain empty until we decide which libraries the project will use.

## Suggested Development Flow

The project should be built in this order:

1. Load and inspect the data.
2. Clean the dataset columns and values.
3. Build accumulated user attribute profiles.
4. Run K-Means clustering.
5. Use SSE/elbow method to choose `k`.
6. Recommend movies from users in the same cluster.
7. Add command-line interaction in `main.py`.
8. Add tests for each major feature.
9. Improve documentation as the project grows.

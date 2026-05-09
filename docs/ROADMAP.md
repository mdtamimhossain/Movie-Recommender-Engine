# Roadmap

## 1. Data Loading

- Load the main catalog.
- Load user-specific rating files.
- Clean column names and convert feature columns to numeric values.

## 2. User Profile

- Filter liked movies.
- Average genre vectors into a preference profile.
- Handle users with no liked movies.

## 3. Recommendation Scoring

- Compare candidate movies with the user profile.
- Use cosine similarity or weighted genre matching.
- Exclude movies already rated by the user.

## 4. CLI

- Allow selecting a user id.
- Allow choosing the number of recommendations.
- Print ranked recommendations.

## 5. Testing

- Test data loading.
- Test user profile generation.
- Test recommendation ranking and edge cases.

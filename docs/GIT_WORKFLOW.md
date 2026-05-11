# Git Workflow

This guide explains the simple Git workflow for our Movie Recommender Engine project.

## Branches

We will use three branch types:

| Branch | Use |
| --- | --- |
| `master` | Final stable project |
| `dev` | Main team development branch |
| `feature/...` | Personal branch for one task |

Do not work directly on `master` or `dev`.  
Always create a feature branch for your task.

## First Setup

Clone the project:

```powershell
git clone https://github.com/mdtamimhossain/Movie-Recommender-Engine.git
```

Go inside the project:

```powershell
cd "Movie-Recommender-Engine"
```

Switch to `dev`:

```powershell
git checkout dev
git pull origin dev
```

Create your feature branch:

```powershell
git checkout -b feature/your-task-name
```

Example:

```powershell
git checkout -b feature/data-loading
```

## Daily Work

Start by updating `dev`:

```powershell
git checkout dev
git pull origin dev
```

Go back to your branch:

```powershell
git checkout feature/your-task-name
git merge dev
```

Work on your files.

Check changes:

```powershell
git status
```

Add changes:

```powershell
git add .
```

Commit changes:

```powershell
git commit -m "Write clear message here"
```

Push your branch:

```powershell
git push -u origin feature/your-task-name
```

After the first push, you can simply use:

```powershell
git push
```

## Pull Request

When your task is done:

1. Push your feature branch.
2. Open GitHub.
3. Create a pull request into `dev`.
4. Write what you changed.
5. Ask a teammate to review.
6. Merge after approval.

Delete the feature branch after it is merged.

## Commit Messages

Good examples:

```text
Add data loading structure
Update Lab Work 3 roadmap
Fix typo in documentation
```

Bad examples:

```text
fix
update
final
changes
```

## Useful Commands

Check current branch:

```powershell
git branch --show-current
```

Check changes:

```powershell
git status
```

See recent commits:

```powershell
git log --oneline -5
```

Create a branch:

```powershell
git checkout -b feature/name
```

Switch branch:

```powershell
git checkout branch-name
```

## Merge Conflicts

If Git shows a conflict:

1. Open the conflicted file.
2. Fix the marked conflict area.
3. Save the file.
4. Run:

```powershell
git add .
git commit -m "Resolve merge conflict"
```

Ask the team if you are unsure.

## Main Rules

- Work on your own `feature/...` branch.
- Pull latest `dev` before starting work.
- Keep commits small.
- Use clear commit messages.
- Open pull requests into `dev`.
- Do not push directly to `master`.
- Do not force push unless the team agrees.
- Do not commit passwords, API keys, or private files.

## Final Submission

When the project is ready:

1. Merge all completed work into `dev`.
2. Test or review the project.
3. Create a pull request from `dev` to `master`.
4. Merge into `master`.

`master` should contain the final submitted version.

# gh-workshop

Practice repository for an introduction to Git and GitHub Desktop for researchers.

Nothing in here matters, so break it freely.

## Layout

| Folder | What's in it |
|---|---|
| `data/` | Small example datasets (CSV) |
| `analysis/` | Scripts that read `data/` and print results |
| `notes/` | Free-text notes in Markdown |
| `paper/` | A short LaTeX paper (`main.tex`) |
| `people/` | One file per workshop attendee |

## Running the example

```sh
python3 analysis/summarise.py
```

## Exercises

### A. Add yourself (no conflicts)

1. Create a branch called `add-<your-name>`.
2. Copy `people/TEMPLATE.md` to `people/<your-name>.md`, e.g. `people/ada-lovelace.md`, and fill it in.
   Duplicating the file in Finder or Explorer and dragging it into place works.
3. Commit, publish the branch, open a pull request.

Everyone adds a different file, so every pull request merges cleanly.

### B. Sign the paper (conflicts on purpose)

1. Update `main`, then create a branch called `sign-<your-name>`.
2. Add `\item Your Name` as the last line of the Contributors list in `paper/main.tex`.
3. Commit, publish the branch, open a pull request.

Everyone edits the same spot in the same file.
The first pull request merges; the rest conflict and need resolving.

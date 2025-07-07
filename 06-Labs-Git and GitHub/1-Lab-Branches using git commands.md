# Create a new local repo and add a file to the repo

```bash
mkdir myrepo

cd myrepo

git init

touch newfile

git add newfile
```

Before you commit the changes, you need to tell Git who you are.
```bash
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

```bash
git commit -m "added newfile"
```

# Create a branch

```bash
git branch my1stbranch
```

# Get a list of branches and active branch

```bash
git branch
```

# Switch to a different branch
```bash
git checkout my1stbranch
```

# Make changes in your branch and check the status of files added or changed

Make some changes to your new branch, called `my1stbranch`
```bash
echo 'Here is some text in my newfile.' >> newfile
```
Create another file called readme.md
```bash
touch readme.md
```
Add it to the repo:
```bash
git add readme.md
```
Verify the changes in current branch:
```
git status
```
Add all modification to the repo:
```bash
git add *
```

# Commit and review commit history
```
git commit -m "added readme.md modified newfile"
```

```
git log
```

# Revert committed changes
Rollback the last commit:
```
git revert HEAD --no-edit
```
If you don't specify the `--no-edit` flag, you may be presented with an editor screen showing the message with changes to be reverted.

# Merge changes into another branch
Merge the contents of the `my1stbranch` into the `master` branch.

First make `master` branch active:
```
git checkout master
```

```
git merge my1stbranch
```

```
git log
```






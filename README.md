# Git Lesson

This lesson covers the basics of version control.

This is part of the first lesson for Chem 280.

To make a commit (or "version" or "checkpoint") of your project, follow this procedure:

1. Make changes to your project that you would like to keep.
2. When you have your changes, tell git you are ready to create a checkpoint of the files by using the 'git add' command and list the files.
3. Create a checkpoint using 'git commit -m "message about what you did"'.

## Adding Features
Features should be developed on branches. To create and switch to a branch, use the command

`git switch -c new_branch_name`

To switch to an existing branch, use

`git switch branch_name`

To submit your feature to be incorporated to the main branch, you should submit a `Pull Request`. 
The repository maintainers will review your pull request before accepting your changes.
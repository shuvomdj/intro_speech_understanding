# intro_speech_understanding

This repository contains assignments for the <a
href="https://www.kcg.edu/">KCGI</a> graduate course "Intro to Speech
Understanding."

## Getting Started

1. Create your own account on github.com
1. <a href="https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo">Fork this repository</a> in your own account.
1. Open a terminal on your laptop:
    1. <a href="https://learn.microsoft.com/en-us/windows/terminal/install">Windows</a>
    1. <a href="https://support.apple.com/guide/terminal/open-or-quit-terminal-apd5265185d-f365-44cb-8b09-71a064a42125/mac">MacOS</a>
    1. <a href="https://ubuntu.com/tutorials/command-line-for-beginners#3-opening-a-terminal">Linux</a>
1. <a href="https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository">Clone your fork</a> onto your laptop by going to the terminal and typing
```
git clone https://github.com/<your_github_account_name>/intro_speech_understanding
```

This will create the directory `intro_speech_understanding`, and will
fill it with all of the code and assignments that have been published so far.
1. For the copy on your laptop, <a href="https://docs.github.com/en/get-started/git-basics/managing-remote-repositories">define two remotes</a>.
    1. Your fork on github.com should be called `origin`.  Cloning has probably already set this up, but to be sure, you can type
    ```
    git remote -v
    ```
    If you don't see `> origin  https://github.com/<your_github_account_name>/intro_speech_understanding (fetch)` then you can create it as
    ```
    git remote add origin https://github.com/<your_github_account_name>/intro_speech_understanding
    ```
    1. Create a second remote, called `release`, pointing to the class repository:
    ```
    git remote add origin https://github.com/jhasegaw/intro_speech_understanding
    ```

## Weekly Update

This repository will change every week.  In order to merge its changes
into the copy on your laptop:

1. Make sure to <a href="https://git-scm.com/docs/git-commit">save your local changes:</a>
```
git commit -am "saving changes"
```
1. <a href="https://git-scm.com/docs/git-fetch">Fetch the release, and <a href="https://git-scm.com/docs/git-merge">merge</a> it with your local copy:
```
git fetch release
git merge release/main -m "Merging release" --allow-unrelated-histories
```
1. Do the homework
1. Save your changes, then push them to your github fork:
```
git commit -am "saving changes"
git push origin main
```

If you've made any changes on your github fork, your `git push` command will fail.  In that case, you should first merge the changes into the local copy on your laptop:
```
git fetch origin
git merge origin/main -m "Merging github changes" --allow-unrelated-histories
```
Edit your local files, to make sure that the result of `git merge` is what you wanted.  Then try `git commit -am "saving changes"` and `git push origin main` again.


## Disaster Recovery

When you are new to git, you will often find that git is asking you a
question that you don't know how to answer.

If that happens, the easiest solution is to just go to a completely
new directory, and create a completely new copy on your laptop.  The
total amount of space required by this repository is tiny; it's
totally fine for you to have many copies of it.


# zfm
Zsh Fuzzy Marks

# Introduction

zfm is a minimal command line bookmark manager based on [fzf](https://github.com/junegunn/fzf).
It lets you bookmark files and directories in your system and rapidly access them

### Bookmark a directory or a file

```sh
$ zfm add ~/Downloads ~/Documents/wallpaper
```

### List bookmarks

```sh
$ zfm list
/home/pablo/Downloads            [d]
/home/pablo/Documents/wallpaper  [f]
```

restrict to just files

```sh
$ zfm list --files
/home/pablo/Documents/wallpaper  [f]
```
or directories:

```sh
$ zfm list --dirs
/home/pablo/Downloads  [d]
```
### Select Bookmarks

By pressing `ctrl+b`, you can fuzzy-select a bookmark (or multiple) and insert them into the current command line:

![](select_bookmark.png)

![](bookmark_inserted.png)

### `cd` into a bookmarked directory

Press `ctrl+p` will let you select a bookmarked directory to jump to:

![](2020-03-16_242x75.png)

```sh
/home/pablo/Downloads$
```

### Use in custom scripts

For example, to rapidly open a bookmark with vim you can add this alias to your `.zshrc`

```
alias of='vim $(zfm select --files --multi)'
```
Typing `of` will open selection menu with all your bookmarked files and directly open the selection in vim.
The option `--multi1` allows you to select multiple entries (by using tab).

# Installation

Install [fzf](https://github.com/junegunn/fzf)

## Antigen

Add this to your `.zshrc`:

    ```sh
    antigen bundle pabloariasal/zfm
    ```

## Oh My Zsh

1. Clone the repo in Oh My Zsh's plugin directory:

    ```sh
    git clone https://github.com/pabloariasal/zfm ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zfm}
    ```

2. Activate the plugin in your `.zshrc`:

    ```sh
    plugins=(zfm)
    ```

## Manual (Git Clone)

1. Clone the repo

    ```sh
    git clone https://github.com/pabloariasal/zfm ~/.zsh/zfm
    ```

2. Add the following to your `.zshrc`:

    ```sh
    source ~/.zsh/zfm/zfm.zsh
    ```
# F.A.Q

## Why not `autojump`, `z`, `fasd` and other?



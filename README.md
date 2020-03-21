# zfm - Zsh Fuzzy Marks

zfm is a minimal command line bookmark manager based on [fzf](https://github.com/junegunn/fzf).
It lets you bookmark files and directories in your system and rapidly access them.
It's intended to be a less intrusive alternative to `z`, `autojump` or `fasd`.

# Installation

Install [fzf](https://github.com/junegunn/fzf)

## Oh My Zsh

1. Clone the repo in Oh My Zsh's plugin directory:

    ```sh
    git clone https://github.com/pabloariasal/zfm ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zfm}
    ```

2. Activate the plugin in your `.zshrc`:

    ```sh
    plugins=(zfm)
    ```

## Antigen

Add this to your `.zshrc`:

    ```sh
    antigen bundle pabloariasal/zfm
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

# Usage

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

just files

```sh
$ zfm list --files
/home/pablo/Documents/wallpaper  [f]
```
or only directories:

```sh
$ zfm list --dirs
/home/pablo/Downloads  [d]
```
### Select Bookmarks

By pressing `ctrl+b`, and fzf pane will open and you can fuzzy-select a bookmark (or multiple) and insert them into the current command line:

![](misc/bookmark_selection.png)

![](misc/bookmark_inserted.png)

### `cd` into a bookmarked directory

Press `ctrl+p` will let you select a bookmarked directory and directly jump to it:

![](misc/select_dir.png)

![](misc/changed_dir.png)

Alternatively, you can type `z` followed by a pattern, like `autojump`:

```sh
$ z down
/home/pablo/Downloads$
```
If the pattern is ambiguos, the normal selection menu will be opened

### Use in custom scripts

For example, you can create an alias to open a bookmark with vim by adding this to your `.zshrc`

```sh
alias of='vim $(zfm select --files --multi)'
```
Typing `of` will open selection menu with all your bookmarked files and directly open the selection in vim.
The option `--multi1` allows you to select multiple entries (by using tab).

### Edit Bookmarks

You can edit your bookmarks with 

```sh
zfm edit

```

This will open your current text editor (as defined by `EDITOR`) and let you manually edit, remove or reorder your bookmarks.

# F.A.Q

## Why not `autojump`, `z`, `fasd` and other?

Because explicit is better than implicit. I don't want every single directory I visit to be bookmarked.
I want to decide what gets bookmarked, when and the order of my bookmarks


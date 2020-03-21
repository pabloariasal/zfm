# zfm - Zsh Fuzzy Marks

zfm is a minimal command line bookmark manager for zsh built on top of [fzf](https://github.com/junegunn/fzf).
It lets you bookmark files and directories in your system and rapidly access them.

It's intended to be a less intrusive alternative to `z`, `autojump` or `fasd` that doesn't require any setup, doesn't pollute your prompt command, and gives you full control over your bookmarks.

# Installation

`zfm` is built on top of `fzf` so you must install that first. Follow the instructions [here](https://github.com/junegunn/fzf#installation).

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
$ zfm add ~/Downloads ~/Documents/wallpaper.png
```

### List bookmarks

```sh
$ zfm list
/home/pablo/Downloads                [d]
/home/pablo/Documents/wallpaper.png  [f]
```

restrict to just files:

```sh
$ zfm list --files
/home/pablo/Documents/wallpaper.png  [f]
```
or directories:

```sh
$ zfm list --dirs
/home/pablo/Downloads  [d]
```
### Select Bookmarks

By pressing `ctrl+b`, a fzf pane will open and let you fuzzy-select a bookmark (or multiple) and insert them into the current command line:

![](misc/bookmark_selection.png)

![](misc/bookmark_inserted.png)

### `cd` into a bookmarked directory

Pressing `ctrl+p` will let you select a bookmarked directory and directly jump to it:

![](misc/select_dir.png)

![](misc/changed_dir.png)

Alternatively, you can type `f` followed by a pattern to directly jump to the directory matching the pattern (like `autojump`)

```sh
$ f down
/home/pablo/Downloads$
```
If the pattern is ambiguous a selection menu will be opened will the possible options.

### Use in custom scripts

For example, you can create an alias to open a bookmark with vim by adding this to your `.zshrc`

```sh
alias of='vim $(zfm select --files --multi)'
```
Typing `of` will open a selection menu with all bookmarked files and directly open the selection in vim.

The option `--multi1` allows you to select multiple entries.

### Edit Bookmarks

You can edit your bookmarks with:

```sh
zfm edit

```

This will open your current text editor (as defined by `EDITOR`) and let you manually edit, remove or reorder your bookmarks.

# Commands

| Command | Description |
| --- | --- |
| `zfm list` | List bookmarks |
| `zfm add <path> [<path>...]` | Add a bookmark |
| `zfm select` | Open an fzf selection menu and print selection to stdout |
| `zfm edit` | Open and edit the bookmarks file |
| `zfm fix` | Remove bookmarked entries that no longer exist in the filesystem |
| `zfm clear` | Remove all bookmarks |
| `f <pattern>` | Jump to bookmark directory matching `pattern`, open selection if ambiguous  |

# Key Bindings

| Key Binding | Description |
| --- | --- |
| `ctrl+p` | insert selection into the current prompt |
| `ctrl+b` | jump to selected directory               |

# F.A.Q

### Why not `autojump`, `z`, `fasd` and others?

Because explicit is better than implicit. I don't want every single directory I visit to be bookmarked. I don't want to 
I want to decide what gets bookmarked, when and which order.

### I don't like the default key bindings, can I change them?

Sure, you can unbind them by putting this on your `zshrc`:

```
bindkey -r '^P'
bindkey -r '^B'
```
Or change them to something else:

```
bindkey '^A' zfm-cd-to-bookmark
bindkey '^E' zfm-insert-bookmark
```
*Tip:* you can use `Ctrl+v` on your terminal window to display escape sequences of key bindings.

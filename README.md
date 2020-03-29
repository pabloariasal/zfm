# zfm - Zsh Fuzzy Marks

zfm is a minimal command line bookmark manager for zsh built on top of [fzf](https://github.com/junegunn/fzf).
It lets you bookmark files and directories in your system and rapidly access them.

It's intended to be a less intrusive alternative to `z`, `autojump` or `fasd` that doesn't pollute your prompt command or create bookmarks behind the scenes: you have full control over what gets bookmarked and when, like bookmarks on a web browser.

# Installation

## Install fzf

`zfm` is built on top of `fzf` so you must install that first. Follow the instructions [here](https://github.com/junegunn/fzf#installation).

## Install zfm

### Oh My Zsh

1. Clone the repo in Oh My Zsh's plugin directory:

```sh
git clone https://github.com/pabloariasal/zfm ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zfm}
```

2. Activate the plugin in your `.zshrc`:

```sh
plugins=(zfm)
```

### Antigen

Add this to your `.zshrc`:

```sh
antigen bundle pabloariasal/zfm
```

### Manual (Git Clone)

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

Pressing `ctrl+o` will open an fzf fuzzy selection menu and insert your selection(s) into the current command line:

![](misc/bookmark_selection.png)

![](misc/bookmark_inserted.png)

### `cd` into a bookmarked directory

Pressing `ctrl+p` will open a selection menu with all your bookmarked directories and directly jump to the directory you have selected:

![](misc/select_dir.png)

![](misc/changed_dir.png)

Alternatively, you can type `f` followed by a pattern to directly jump to the directory matching the pattern (like `autojump`):

```sh
$ f down
/home/pablo/Downloads$
```
If the pattern is ambiguous a selection menu will be opened with the possible options.

### Use in custom scripts

For example, you can create an alias to open a bookmarked file with vim by adding this to your `.zshrc`

```sh
alias of='vim $(zfm select --files --multi)'
```
Typing `of` will open a selection menu with all bookmarked files and directly open the selection in vim.

The option `--multi` allows you to select multiple entries.

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
| `zfm select` | Open selection menu and print selection to stdout |
| `zfm query <pattern>` | Print bookmark matching `pattern` to stdout. Selection menu will open if match is ambiguous |
| `zfm edit` | Open and edit the bookmarks file |
| `zfm fix` | Remove bookmarked entries that no longer exist in the filesystem |
| `zfm clear` | Remove all bookmarks |
| `f <pattern>` | Jump to bookmark directory matching `pattern`, open selection if ambiguous  |

# Options

| Option | Description | Available for |
| --- | --- | --- |
| `--files` | Restrict to just files | `query`, `list`, `select` |
| `--dirs` | Restrict to just dirs | `query`, `list`, `select` |
| `--multi` | Allow selecting multiple items | `select` |

# Key Bindings

| Key Binding | Description |
| --- | --- |
| `ctrl+o` | Select one or multiple bookmarks and insert them into the current command line |
| `ctrl+p` | jump to selected directory               |

# F.A.Q

### Why not `autojump`, `z`, `fasd` and others?

Because explicit is better than implicit. I don't want every single directory I visit to be bookmarked, I know which directories I visit the most and which files I need rapid access to.

### I don't like the default key bindings, can I change them?

Sure, you can unbind them by putting this on your `zshrc`:

```
bindkey -r '^P'
bindkey -r '^O'
```
Or change them to something else:

```
bindkey -r '^P'
bindkey -r '^O'
bindkey '^A' zfm-cd-to-bookmark
bindkey '^E' zfm-insert-bookmark
```
*Tip:* you can use `Ctrl+v` on your terminal window to display escape sequences of key bindings.

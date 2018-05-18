# Booky

A simple bookmark manager for the command line.

There are several more powerful alternatives, but it's not always possible to
install them. Booky only depends on the Python standard library.

## Setup

To be able to change directories, a wrapper function around Booky is required.

### zsh completion

```zsh
# Wrappers for booky
alias booky='python -m booky'

function bcd() {
    # Restore a directory from booky
    if [ $# -gt 1 ]; then
        return 1
    fi

    DIR=$(booky get $1)
    if [ $? != 0 ]; then
        return 1
    fi

    cd $DIR
}

# Completion for bcd
function _bcd() {
    local bookmarks
    bookmarks=("${(@f)$(python -m booky list -m)}")
    _describe 'bookmark' bookmarks
}
setopt complete_aliases
compdef _bcd bcd
```

## Notes

The bookmarks file is not locked, so simultaneous reading and writing results
in undefined behavior.

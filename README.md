# Booky

A simple bookmark manager for the command line.

There are several more powerful alternatives, but it's not always possible to
install them. Booky is contained in a single Python file and only depends
on the Python standard library.

## Setup

To be able to change directories, a wrapper function around Booky is required.

### bash and zsh

```bash
function booky-cd {
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
```

## Notes

The bookmarks file is not locked, so simultaneous reading and writing results
in undefined behavior.

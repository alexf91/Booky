#
# Copyright 2018 Alexander Fasching
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

import argparse
import os
import sys
import pickle
from collections import OrderedDict


LASTKEY = 'b07647bf409c327a'


def load_bookmarks(path):
    """Load the bookmarks from a file."""
    try:
        with open(path, 'rb') as fp:
            return pickle.load(fp)
    except FileNotFoundError:
        return OrderedDict()


def save_bookmarks(path, bookmarks):
    """Save the bookmarks to a file."""
    with open(path, 'wb') as fp:
        return pickle.dump(bookmarks, fp)


def command_list(args):
    """List all available bookmarks."""
    bookmarks = load_bookmarks(args.bookyfile)
    for name, value in bookmarks.items():
        if name != LASTKEY:
            print('{:<20}{:<}'.format(name, value))

    return 0


def command_add(args):
    """Add a bookmark."""
    bookmarks = load_bookmarks(args.bookyfile)
    path = args.path or os.getcwd()
    bookmarks[args.name] = path
    bookmarks[LASTKEY] = path
    save_bookmarks(args.bookyfile, bookmarks)
    return 0


def command_delete(args):
    """Delete a bookmark."""
    bookmarks = load_bookmarks(args.bookyfile)
    if args.name in bookmarks:
        del bookmarks[args.name]
        save_bookmarks(args.bookyfile, bookmarks)
        return 0
    else:
        print('Bookmark "%s" not found.' % args.name, file=sys.stderr)
        return 1


def command_get(args):
    """Get a bookmark."""
    bookmarks = load_bookmarks(args.bookyfile)
    name = args.name or LASTKEY
    if name in bookmarks:
        path = bookmarks[name]
        bookmarks[LASTKEY] = path
        save_bookmarks(args.bookyfile, bookmarks)
        print(path)
        return 0
    else:
        print('Bookmark "%s" not found.' % name, file=sys.stderr)
        return 1


def main():
    parser = argparse.ArgumentParser(prog='booky')
    parser.add_argument('--bookyfile', '-b', type=str,
            default=os.path.expanduser('~/.bookyfile'),
            help='file where bookmarks are stored'
        )

    subparsers = parser.add_subparsers()

    # Parser for the 'list' command
    parser_list = subparsers.add_parser('list', help='list saved bookmarks')
    parser_list.set_defaults(func=command_list)

    # Parser for the 'add' command
    parser_add = subparsers.add_parser('add', help='add a bookmark')
    parser_add.add_argument('name', help='name of the bookmark')
    parser_add.add_argument('--path', '-p', help='path of the bookmark')
    parser_add.set_defaults(func=command_add)

    # Parser for the 'delete' command
    parser_delete = subparsers.add_parser('delete', help='delete a bookmark')
    parser_delete.add_argument('name', help='name of the bookmark')
    parser_delete.set_defaults(func=command_delete)

    # Parser for the 'get' command
    parser_get = subparsers.add_parser('get', help='get the path for a name')
    parser_get.add_argument('name', nargs='?', help='name of the bookmark')
    parser_get.set_defaults(func=command_get)

    args = parser.parse_args()

    try:
        if 'func' in args:
            return args.func(args)
        else:
            parser.print_help()
            return 1
    except Exception as e:
        print(e, file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main() or 0)

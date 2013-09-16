# A bit more advanced wrapper for [Todo.txt](todotxt.com)

Built on top of [madc/alfred-todotxt](https://github.com/madc/alfred-todotxt)

It checks and shows all open Todos from within alfred, and lets you select and complete them. It also supports fuzzy search on them which allows you to filter. The rest of the commands are directly parsed on to todo.sh, adding a -f so that they dont ask for confirmation.

Upon request, now when clicking CTRL on a line, it will delete the Todo removing it from the list (without asking for confirmation).

Supports all standard arguments/extentions. If any is missing, please let me know to add it to the list.

## Dependencies

- [AlfredApp](http://www.alfredapp.com) + Powerpack
- [phyllisstein/alp](https://github.com/phyllisstein/alp) Already included in the workflow for ease of use.
- [Todo.txt](http://www.todotxt.com)s

## Setup

Download the [todotxt.alfredworkflow](https://github.com/benignoc/alfred-todotxt/raw/master/todotxt.alfredworkflow) from above and import it into Alfred.

For the workflow to work, you need to check a couple of paths, first, the location of your **todo.txt** which you should do in the _t_ script filter block, and then the **todo.sh** bin path, which normally sits at '/usr/local/bin', but that you might need to change to fit your configuration, in which case, just alter TODOTXT_PATH to match the path, where todotxt is located.

## Sources & Thanks

- The icon is taken from the Todo.txt-website. It has been created by [John Rowley](https://twitter.com/eJohnR)
- The .gitignore was generated with [.gitignore.oi](http://gitignore.io)
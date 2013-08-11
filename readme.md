# A bit more advanced wrapper for [Todo.txt](todotxt.com)

Built on top of [madc/alfred-todotxt](https://github.com/madc/alfred-todotxt)

It checks and shows all open Todos from within alfred, and lets you select and complete them. It also supports fuzzy search on them which allows you to filter. The rest of the commands are directly parsed on to todo.sh, adding a -f so that they dont ask for confirmation.

Supports all standard arguments/extentions. If any is missing, please let me know to add it to the list.

## Dependencies

- [AlfredApp](http://www.alfredapp.com) + Powerpack
- [phyllisstein/alp](https://github.com/phyllisstein/alp) Already included in the workflow for ease of use.
- [Todo.txt](http://www.todotxt.com)
- [Growl](http://www.growl.info)

## Setup

Download the [Todo.txt.alfredworkflow](https://github.com/madc/alfred-todotxt/raw/master/Todo.txt.alfredworkflow) from above and import it into Alfred. The workflow should work with Todo.txt right away, if installed via [MacPorts](https://trac.macports.org/browser/trunk/dports/office/todotxt/Portfile). Otherwise, TODOTXT_PATH has to be alterd to match the path, where todotxt is located.
See the _Alfred-v1.x_ tag for the Alfred 1.x extention.

## Sources & Thanks

- The icon is taken from the Todo.txt-website. It has been created by [John Rowley](https://twitter.com/eJohnR)
- The .gitignore was generated with [.gitignore.oi](http://gitignore.io)
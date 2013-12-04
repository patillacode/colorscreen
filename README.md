consolemsg
==========

Semantically colorifies console output messages with ANSI codes.

The goal of the module is to centralize how console messages
are printed depending on the intent.
Instead of `print()` you can use:

- `step()`
- `error()`
- `warn()`
- `success()`

Also `fail()`

All consolemsg functions outputs to `sys.stderr`, so they will
be separated from your `stdout` when you use piping.

For serious logging you should use the `logging` standard module.
This module is intended to be quick and setup less smart output.



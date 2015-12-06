colorscreen
===========

Semantically colorifies console output messages with ANSI codes.

The goal of the module is to centralize how console messages
are printed depending on the intent.
Instead of `print()` you can use:

- `step()`
- `error()`
- `warn()`
- `success()`

Also `fail()` prints an error and exits.

------

#### Demo

Run this in a python console:
```
from colorscreen import ColorScreen
ColorScreen().demo()
```

#### Usage

* Import the class
* Create an instance of it
* Print!

```
from colorscreen import ColorScreen

screen = ColorScreen()

screen.step('Testing common messages')
screen.success('Success!')
screen.warn('This might be dangerous')
screen.error('Something bad happened')
screen.fail('Something very bad happened and i will die')

```

------

#### Notes

All colorscreen functions outputs to `sys.stderr`, so they will
be separated from your `stdout` when you use piping.

For serious logging you should use the `logging` standard module.
This is a quick and simple solution make the user aware of the
relevance of the outputs.
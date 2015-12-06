#!/usr/bin/env python
import sys


class ColorScreen():

    def write(self, *args):
        sys.stderr.write(' '.join(str(arg) for arg in args))
        sys.stderr.write('\n')
        sys.stderr.flush()

    def color(self, color, message):
        return "\033[{0}m{1}\033[0m".format(color, message)

    def success(self, message):
        self.write(self.color('32;1', ">> " + message))

    def step(self, message):
        self.write(self.color('34;1', ":: " + message))

    def error(self, message):
        self.write(self.color('31;1', "Error: " + message))

    def warn(self, message):
        self.write(self.color('33', "Warning: " + message))

    def fail(self, message, code=-1):
        self.error(message)
        sys.exit(code)

    def demo(self):
        self.step('Testing common messages')
        self.success('Success!')
        self.warn('This might be dangerous')
        self.error('Something bad happened')
        self.fail('Something very bad happened and i will die')

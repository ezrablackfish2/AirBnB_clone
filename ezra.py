#!/usr/bin/python3

import cmd 

class Ezra(cmd.Cmd):
    intro = "welocme to my shell"
    prompt = '(ezra)'
    file = None

    def do_pushup(self, line):
        print("i amd doing push up")

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    Ezra().cmdloop()

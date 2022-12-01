#!/usr/bin/python3
import hidden_4

if __name__ == '__main__':
    def vdir(hidden_4):
        if hidden_4 == None:
            return None
        return [x for x in dir(hidden_4) if not x.startswith('__')]
    print('\n'.join(str(x) for x in vdir(hidden_4)))

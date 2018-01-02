
import sys

def test():
    args = sys.argv
    print(args)
    if len(args) ==1:
        return "hello world"
    elif len(args) == 2:
        return 'hello,%s' % args[1]
    else:
        return 'hello,everyone'

if __name__ == '__main__':
    print('name=%s' % __name__)
    print(test())
import sys

(lambda a, b: print(int(a) + int(b)))(*sys.argv[1:])

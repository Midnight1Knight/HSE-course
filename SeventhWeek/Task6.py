import sys

print(len(set([line for line in sys.stdin.read().split()])))

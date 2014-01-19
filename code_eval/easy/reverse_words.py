"""
CHALLENGE DESCRIPTION:

Write a program to reverse the words of an input sentence.

INPUT SAMPLE:

The first argument will be a path to a filename containing multiple sentences, one per line. Possibly empty lines too. E.g.

Hello World
Hello CodeEval

OUTPUT SAMPLE:

Print to stdout, each line with its words reversed, one per line. Empty lines in the input should be ignored. Ensure that there are no trailing empty spaces on each line you print. E.g.

World Hello
CodeEval Hello
"""

import sys

f = open(sys.argv[1], 'r')
for line in f:
    line = line.replace('\n', '')
    if line != '':
        words = line.split(' ')
        words.reverse()
        print ' '.join(words)
f.close()


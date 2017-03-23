# coding:utf-8

import functools

def is_latin(c):
    return ord(c) < 126

# input_file
input_file = 'new.md'
# output_file
output_file = 'll.md'

# Some characters should not have space on either side.
def allow_space(c):
    return not c.isspace() and not (c in '，。；「」：《》『』、[]（）*_')

def add_space_at_boundry(prefix, next_char):
    if not len(prefix):
        return next_char
    if is_latin(prefix[-1]) != is_latin(next_char) and \
            allow_space(next_char) and allow_space(prefix[-1]):
        return prefix + ' ' + next_char
    else:
        return prefix + next_char

infile = open(input_file)
instr = infile.read()
infile.close()

outstr = functools.reduce(add_space_at_boundry, instr, '')
with open(output_file, 'w') as outfile:
    outfile.write(outstr)
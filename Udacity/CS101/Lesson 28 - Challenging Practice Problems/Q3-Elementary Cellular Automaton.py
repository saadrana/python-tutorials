# THREE GOLD STARS
# Question 3-star: Elementary Cellular Automaton

# Please see the video for additional explanation.

# A one-dimensional cellular automata takes in a string, which in our
# case, consists of the characters '.' and 'x', and changes it according
# to some predetermined rules. The rules consider three characters, which
# are a character at position k and its two neighbours, and determine
# what the character at the corresponding position k will be in the new
# string.

# For example, if the character at position k in the string  is '.' and
# its neighbours are '.' and 'x', then the pattern is '..x'. We look up
# '..x' in the table below. In the table, '..x' corresponds to 'x' which
# means that in the new string, 'x' will be at position k.

# Rules:
#          pattern in         position k in        contribution to
# Value    current string     new string           pattern number
#                                                  is 0 if replaced by '.'
#                                                  and value if replaced
#                                                  by 'x'
#   1       '...'               '.'                        1 * 0
#   2       '..x'               'x'                        2 * 1
#   4       '.x.'               'x'                        4 * 1
#   8       '.xx'               'x'                        8 * 1
#  16       'x..'               '.'                       16 * 0
#  32       'x.x'               '.'                       32 * 0
#  64       'xx.'               '.'                       64 * 0
# 128       'xxx'               'x'                      128 * 1
#                                                      ----------
#                                                           142

# To calculate the patterns which will have the central character x, work
# out the values required to sum to the pattern number. For example,
# 32 = 32 so only pattern 32 which is x.x changes the central position to
# an x. All the others have a . in the next line.

# 23 = 16 + 4 + 2 + 1 which means that 'x..', '.x.', '..x' and '...' all
# lead to an 'x' in the next line and the rest have a '.'

# For pattern 142, and starting string
# ...........x...........
# the new strings created will be
# ..........xx...........  (generations = 1)
# .........xx............  (generations = 2)
# ........xx.............  (generations = 3)
# .......xx..............  (generations = 4)
# ......xx...............  (generations = 5)
# .....xx................  (generations = 6)
# ....xx.................  (generations = 7)
# ...xx..................  (generations = 8)
# ..xx...................  (generations = 9)
# .xx....................  (generations = 10)

# Note that the first position of the string is next to the last position
# in the string.

# Define a procedure, cellular_automaton, that takes three inputs:
#     a non-empty string,
#     a pattern number which is an integer between 0 and 255 that
# represents a set of rules, and
#     a positive integer, n, which is the number of generations.
# The procedure should return a string which is the result of
# applying the rules generated by the pattern to the string n times.


def cellular_automaton(string, pattern, n):
    rules = make_rules(pattern)
    inlist = list(string)
    tmplist = []
    maxlength = len(inlist) - 1
    #print rules  # DEBUG
    #print inlist  # DEBUG
    while n > 0:
        for index in range(0, len(inlist)):
            #print index  # DEBUG
            testslice = []
            if index == 0:
                testslice = inlist[maxlength] + inlist[index] + inlist[index + 1]
            elif index == maxlength:
                testslice = inlist[index - 1] + inlist[index] + inlist[0]
            else:
                testslice = inlist[index - 1] + inlist[index] + inlist[index + 1]
            #print testslice  # DEBUG
            tmplist.append(rules[''.join(testslice)])
            #print tmplist  # DEBUG
        inlist = tmplist
        tmplist = []
        n -= 1
    return ''.join(inlist)


def make_rules(patternnum):
    patternvalues = [[128, 'xxx'], [64, 'xx.'], [32, 'x.x'],
                     [16, 'x..'], [8, '.xx'], [4, '.x.'],
                     [2, '..x'], [1, '...']]
    if patternnum == 0:
        return {'xxx': '.', 'xx.': '.', 'x.x': '.',
                'x..': '.', '.xx': '.', '.x.': '.',
                '..x': '.', '...': '.'}
    rules = {}
    while patternnum > 0:
        for patternvalue in patternvalues:
            if patternvalue[0] > patternnum:
                rules[patternvalue[1]] = '.'
            else:
                rules[patternvalue[1]] = 'x'
                patternnum -= patternvalue[0]
    return rules


def test_make_rules():
    patternvalues = ['xxx', 'xx.', 'x.x', 'x..', '.xx', '.x.',
                     '..x', '...']
    for pattern in range(0, 256):
        rules = make_rules(pattern)
        for patternvalue in patternvalues:
            # First, check if all patterns in rules
            if patternvalue not in rules and pattern != 0:
                print "Pattern number " + str(pattern) + " missing rule " + patternvalue
                return False
            # Next, check a few patterns
            if pattern == 0:
                correctrules = {'...': '.', 'x.x': '.', 'xxx': '.',
                                '.xx': '.', '..x': '.', '.x.': '.', 'xx.': '.', 'x..': '.'}
                if rules [patternvalue] != correctrules[patternvalue]:
                    print "Pattern number 0 mismatched: pattern " + patternvalue + " incorrect"
                    return False
            if pattern == 128:
                correctrules = {'...': '.', 'x.x': '.', 'xxx': 'x',
                                '.xx': '.', '..x': '.', '.x.': '.', 'xx.': '.', 'x..': '.'}
                if rules[patternvalue] != correctrules[patternvalue]:
                    print "Pattern number 128 mismatched: pattern " + patternvalue + " incorrect"
                    return False
            if pattern == 256:
                correctrules = {'...': 'x', 'x.x': '.', 'xxx': '.',
                                '.xx': '.', '..x': '.', '.x.': '.', 'xx.': '.', 'x..': '.'}
                if rules[patternvalue] != correctrules[patternvalue]:
                    print "Pattern number 255 mismatched: pattern " + patternvalue + " incorrect"
                    return False
    return True


# print test_make_rules()

print cellular_automaton('.x.x.x.x.', 17, 2)
# >>> xxxxxxx..
print cellular_automaton('.x.x.x.x.', 249, 3)
# >>> .x..x.x.x
print cellular_automaton('...x....', 125, 1)
# >>> xx.xxxxx
print cellular_automaton('...x....', 125, 2)
# >>> .xxx....
print cellular_automaton('...x....', 125, 3)
# >>> .x.xxxxx
print cellular_automaton('...x....', 125, 4)
# >>> xxxx...x
print cellular_automaton('...x....', 125, 5)
# >>> ...xxx.x
print cellular_automaton('...x....', 125, 6)
# >>> xx.x.xxx
print cellular_automaton('...x....', 125, 7)
# >>> .xxxxx..
print cellular_automaton('...x....', 125, 8)
# >>> .x...xxx
print cellular_automaton('...x....', 125, 9)
# >>> xxxx.x.x
print cellular_automaton('...x....', 125, 10)
# >>> ...xxxxx
print cellular_automaton('.', 21, 1)  # FIXME: string = '.', n = 1
# >>> x
print cellular_automaton('.', 21, 2)  # FIXME: string = '.', n = 2
# >>> .

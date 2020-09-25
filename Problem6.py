# Solved it without hints. Sometimes problems can be simplified. Words should be separated by a single space => After
# a sentence starts and if you find a space, the previous character should not be a space. No need to check if you
# found a word ot not. Terminal character should be preceded by a word => just check if the previous character is alpha.


from enum import Enum


class States(Enum):
    Invalid = 0
    CapsFound = 1
    SentenceStarted = 2


def parse(stream):
    state = States.Invalid
    start_index = -1
    for i in range(0, len(stream)):
        if stream[i].isupper():
            if state == States.Invalid:
                state = States.CapsFound
                start_index = i
        elif stream[i].islower() or stream[i].isspace():
            if state == States.CapsFound:
                state = States.SentenceStarted
            if stream[i].isspace() and stream[i-1].isspace():
                state = States.Invalid
                start_index = -1
        elif stream[i] == ',' or stream[i] == ';' or stream[i] == ':':
            if state == States.CapsFound:
                state = States.Invalid
                start_index = -1
            if not stream[i-1].isalpha():
                state = States.Invalid
                start_index = -1
        elif stream[i] == '.' or stream[i] == '?' or stream[i] == '!' or stream[i] == '‽':
            if stream[i-1].islower():
                print(stream[start_index:i+1])
                state = States.Invalid
            else:
                state = States.Invalid
        else:
            state = States.Invalid
            start_index = -1


parse("Hello Im Snippy. Im Happy!       Hello again!       This   shouldn't be printed.      Neither this .      But this should be.     xxxxxxxx   Another sentence?       I am snippy. In case you forgot.  xxxxxxx       This, should work.         A piece of code printf; I guess. This,, will not be printed.   This printf() cat. The previous sentence should not be printed.")





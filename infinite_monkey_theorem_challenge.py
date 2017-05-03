# Self Check from http://interactivepython.org/runestone/static/pythonds/Introduction/DefiningFunctions.html
#Problem Solving with data structures and algorithms
# Here’s a self check that really covers everything so far. You may have heard of
# the infinite monkey theorem? The theorem states that a monkey hitting keys at
#  random on a typewriter keyboard for an infinite amount of time will almost surely
#   type a given text, such as the complete works of William Shakespeare. Well,
#   suppose we replace a monkey with a Python function. How long do you think it
#   would take for a Python function to generate just one sentence of Shakespeare?
#    The sentence we’ll shoot for is: “methinks it is like a weasel”

# You’re not going to want to run this one in the browser, so fire up your favorite
# Python IDE. The way we’ll simulate this is to write a function that generates a
# string that is 27 characters long by choosing random letters from the 26 letters
# in the alphabet plus the space. We’ll write another function that will score each
# generated string by comparing the randomly generated string to the goal.

# A third function will repeatedly call generate and score, then if 100% of the
# letters are correct we are done. If the letters are not correct then we will
# generate a whole new string.To make it easier to follow your program’s progress
# this third function should print out the best string generated so far and its
# score every 1000 tries.

# Self Check Challenge
# See if you can improve upon the program in the self check by keeping letters
# that are correct and only modifying one character in the best string so far.
# This is a type of algorithm in the class of ‘hill climbing’ algorithms, that is
# we only keep the result if it is better than the previous one.

import random


def generate_string(n=28):
    """generate a string of n chars randomly, drawing from a-z and the space"""

    chars = [chr(i) for i in xrange(97, 123)]
    chars.append(' ')

    sentence = ""
    for i in range(n):
        num = random.randint(0, 26)
        sentence += chars[num]
    return sentence


def score_string(s):
    """Score a string by how similar it is to our goal string"""

    goal = "methinks it is like a weasel"
    score = 0
    for i in range(len(s)):
        if s[i] == goal[i]:
            score += 1

    percentage = 100 * score/len(goal)

    return percentage


def regenerate(s):
    """compare a string to a goal string and regenerate random strings to replace
    only the parts that don't match the goal string"""

    goal = "methinks it is like a weasel"
    s = [char for char in s]
    new_s = ""
    for i in range(len(s)):
        if s[i] != goal[i]:
            s[i] = generate_string(1)
        new_s += s[i]
    return new_s


def main():
    best_str = ""
    best_score = 0
    iters = 0
    for i in range(1000):
        iters += 1
        if best_str:
            print "regenerating from %d%% %s..." % (best_score, best_str)
            s = regenerate(best_str)
        else:
            s = generate_string()

        score = score_string(s)
        if score > best_score:
            best_score = score
            best_str = s

        if score == 100:
            break

    print "closest:", best_str, "score:", str(best_score) + "%", "iterations:", iters

    print "IT WORKED!!!"

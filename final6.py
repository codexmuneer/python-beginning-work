'''Write a program to calculate the score of a word.
a) To calculate the score for a word, first you have assign a score to each alphabet and store it in any
form (you can use a list, a dictionary or a file).
b) Make a function named calculate_score that takes a word as a parameter (a word you want to
calculate score for) and returns its score. The score of the word can be calculated by adding the score
of individual alphabets (assigned in part a of the question) in the word.
Example: If the score of the alphabets “a” , “ p”, and “s” is 2, 5, and 3 respectively and the word passed to
the function is “pass” then your function should return 13.
pass = 5 + 2 + 3 + 3 = 13'''

def calculate_score(x):
    a = 0
    for i in x:
        a += score[i]
        
    return a

score = {"a": 2,
         "b": 3,
         "c": 5,
         "d": 6,
         "e": 2,
         "f": 1,
         "g": 7,
         "h": 3,
         "i": 8,
         "j": 3,
         "k": 3,
         "l": 3,
         "m": 3,
         "n": 2,
         "o": 3,
         "p": 5,
         "q": 3,
         "r": 3,
         "s": 3,
         "t": 3,
         "u": 5,
         "v": 3,
         "w": 3,
         "x": 5,
         "y": 3,
         "z": 3
}

word = input("Enter a word to calculate score of it: ").lower()
a = calculate_score(word)
print(a)
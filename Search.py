import sys
sys.setrecursionlimit(15000)
A = 0
f = open("BEE.txt","r")
text = f.read()
words = text.split()
user_input = input("Word to search:")
total_correct = 0
total_wrong = 0

def main():
    global A,words,user_input, total_correct, total_wrong
    if user_input.lower() == words[A].lower():
        total_correct = total_correct + 1
        print("The word is the ",A+1,"word of the file", "bring the total to being:",total_correct)
        A = A + 1
        main()
    elif user_input.lower() != words[A].lower():
        A = A + 1
        total_wrong = total_wrong + 1
        main()
main()



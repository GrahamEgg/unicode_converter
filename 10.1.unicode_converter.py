#Python Enter a word and get unicode back



# Ask the user for a word or character to turn in unicode
def enter_word_to_turn():
    result = input("Please enter something you want to turn in unicode:\n")
    return result

# a if loop to start the program over
def user_answer_restart():
    print()
    print("Do you want to change something else in unicode")
    user_answer = input("Type Y for yes or N for no:\n")
    if user_answer in ["Y","y"]:
        Main()
    elif user_answer in ["N", "n"]:
        print("Goodbye :)")
        return 0
    else:
        print(" ##ERROR## invalid answer")
        user_answer_restart()



def Main():
    print()
    # Holds the input given form user
    user_word = enter_word_to_turn()


# This wil print the word the user has enter
# and wil print the unicode behind it
    print()
    print("Unicode for every letter or character given:")
    for i in user_word:
        print(i, " = ", ord(i),)

    user_answer_restart()



if __name__ == '__main__':
    Main()
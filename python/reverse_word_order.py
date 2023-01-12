'''
Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

  My name is Michele

Then I would see the string:

  Michele is name My

'''

def reverse_sentence(words):
    #split words
    #Join the words starting with the last word
    reversed_sent=''

    word_list=words.split(' ')
    for word in word_list:
        reversed_sent=word + " " + reversed_sent

    print(reversed_sent)
    return reversed_sent

reverse_sentence(input("Write a sentence to reverse: "))
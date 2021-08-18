# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

# phrase = input('Please enter a word or phrase: ')
# print(phrase)
# while (phrase := input('Please enter a word or phrase: ') != 'quit'):
#     print(f'What you entered is {len(str(phrase))} characters long')

while phrase != 'quit':
    phrase = input('Please enter a word or phrase: ')
    print(f'What you entered is {len(phrase)} characters long')
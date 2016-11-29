import random
import sys

articles = ['a', 'an', 'the', 'his', 'her']
nouns = ['man', 'woman', 'cat', 'dog', 'wolf', 'golf ball', 'scooter']
verbs = ['jumped', 'ran', 'sang', 'played']
adverbs = ['loudly', 'quietly', 'well', 'badly', 'happily']

try:
    count = int(sys.argv[1])
except ValueError:
    print("invalid input")
except IndexError:
    count = 5

if count < 1 or count > 10:
    print('Please change input value')

while 10 >= count >= 1:
    output = ''
    choice = random.randint(1,2)

    output += random.choice(articles) + " "
    output += random.choice(nouns) + " "
    output += random.choice(verbs) + " "

    if choice == 1:
        output += random.choice(adverbs) + " "

    print(output)
    count -= 1

import random
import string
letters = ['a','b','c','d','e','f','g','h','i','j','k','l''m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = [1,2,3,4,5,6,7,8,9,0]


random_letters_len = int(input('Parol harflarini uzunligini kirgazing: '))
random_numbres_len = int(input('Parol raqamlarini uzunligini kirgazing: '))

all_random = []
shuffle_random = ''

for x in range(1, random_letters_len + 1):
    random_letters = random.choice(letters)
    all_random.append(random_letters)

for x in range(1, random_numbres_len + 1):
    random_numbres = random.choice(numbers)
    all_random.append(random_numbres)

random.shuffle(all_random)
for x in all_random:
    shuffle_random += str(x)


print(f'Tavsiya: {shuffle_random}')

sentence = input('Введите ваше предложение: ')
book = 'aeiouAEIOU'
s = 0

for i in sentence:
    if i in book:
        s += 1

print(s)

def int_func():
    new_word = word.title()
    return new_word


my_str = input(" введите предложение ")
for word in my_str.split(' '):
    print(f'{int_func()}', end=' ' )


x = 38

print('дратути!')
if x < 0:
    print('Меньше нуля')
print('дотвидания!')

'''
дратути!
дотвидания
'''

# примеры
a, b = 10, 5

if a > b:
    print('a > b')                 # если a больше b              - a > b

if a > b and a > 0:                # если a больше b и a больше 0 - успех
    print('успех')
    
if a > b and (a > 0 or b < 1000):  # если a больше b и a больше 0
    print('успех')                 # или b меньше 1000            - успех

if 5 < b and b < 10:
    print('успех')                 # если b больше 5 и меньше 10  - успех

'''
a > b
успех
успех
'''

# можно сравнивать - числа, строки, списки

if '34' > '123':
    print('успех')

if '123' > '12':
    print('успех')

if [1, 2] > [1, 1]:
    print('успех')

'''
успех
успех
успех
'''

# что нельзя сраврить - разные типы
'''
if '6' > 5:
    print('успех')

Traceback (most recent call last):
  File "/media/alex/JINNLIVEUSB/Python/homework6.py", line 53, in <module>
    if '6' > 5:
TypeError: '>' not supported between instances of 'str' and 'int'


if [5, 6] > 5:
    print('успех')

Traceback (most recent call last):
  File "/media/alex/JINNLIVEUSB/Python/homework6.py", line 56, in <module>
    if [5, 6] > 5:
TypeError: '>' not supported between instances of 'list' and 'int'
'''

# но
if '6' != 5:
    print('успех')
'''

'''

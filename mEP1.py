x = float(input())
op = input()
y = float(input())
result = '!'

if op == '+':
    result = x + y
elif op == '-':
    result = x - y
elif op == '*':
    result = x * y
elif op == '//' or op == '%':
    if y != 0 and op == '//':
        result = x // y
    elif y != 0 and op == '%':
        result = x % y
    else:
        print('Divisao por 0!')
elif op == '**':
    result = x ** y
else:
    print('Operacao nao reconhecida!')

if result != '!':
    print(f'{x} {op} {y} = {result}')

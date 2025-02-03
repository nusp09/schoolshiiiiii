while True:
    try:
        num = int(input('enter a number'))
        break
    except:
        print('thats not a number')
fact = num
total = num
for i in range(num - 1):
    fact -= 1
    total *= fact
print(f'the factorial is {total}')

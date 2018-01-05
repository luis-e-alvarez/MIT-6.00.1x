num = int(input('Please input an integer: '))
isNeg = False
result = ''
if num < 0:
    isNeg = True
    num = abs(num)
if num == 0:
    result = '0'
else:
    while num > 0:
        result = str(num % 2) + result
        num = num // 2
if isNeg == True:
    result = '-' + result
print(result)

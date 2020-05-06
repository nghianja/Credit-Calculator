import math

# write your code here
print('What do you want to calculate?')
print('type "n" - for count of months,')
print('type "a" - for annuity monthly payment,')
print('type "p" - for credit principal:')
calculate = input()

if calculate == 'n':
    print('Enter credit principal:')
    principal = int(input())
    print('Enter monthly payment:')
    monthly = int(input())
    print('Enter credit interest:')
    interest = float(input())
    
    i = interest / 100 / 12
    n = math.ceil(math.log(monthly / (monthly - i * principal), 1 + i))
    q, r = divmod(n, 12)
    year_str = 'year'
    if q > 1:
        year_str += 's'
    month_str = 'month'
    if r > 1:
        month_str += 's'
    print(f'You need {q} {year_str} and {r} {month_str} to repay this credit!')

elif calculate == 'a':
    print('Enter credit principal:')
    principal = int(input())
    print('Enter count of periods:')
    periods = int(input())
    print('Enter credit interest:')
    interest = float(input())
    
    i = interest / 100 / 12
    annuity = principal * ((i * pow((1 + i), periods)) / (pow((1 + i), periods) - 1))
    print(f'Your annuity payment = {math.ceil(annuity)}!')

elif calculate == 'p':
    print('Enter monthly payment:')
    monthly = float(input())
    print('Enter count of periods:')
    periods = int(input())
    print('Enter credit interest:')
    interest = float(input())
    
    i = interest / 100 / 12
    principal = monthly / ((i * pow((1 + i), periods)) / (pow((1 + i), periods) - 1))
    print(f'Your credit principal = {principal}!')

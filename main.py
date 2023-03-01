

initial = input("What's the initial investment/savings/downpayment amount? \n")
home_price = input("What's the home purchase price? \n")
apr = input("What's the home loan apr? \n")
rent_price = input("How much is the rent? \n")
interest_rate = input("What's the interest rate percentage? \n")
years = input("How many years? \n")

# def compound_interest(principal, rate, time, frequency):
#     n = 0
#     if frequency == 'q' or 'Q':
#         n = 4
#     elif frequency == 'm' or 'M':
#         n = 12
#     elif frequency == 'w' or 'W':
#         n = 56
#     rate = float(rate/100)
#     value = principal * (pow((1 + rate/n),(n*time)))
#     return f'{value:.2f}'

def mortgage_payment(price, downpayment, apr):
    r = int(apr) / 1200
    x = pow((1 + r), 360)
    payment = price * ((r *(x)) / ( x - 1))
    if downpayment < (price * 0.2):
        pmi = ((price * .0075) / 12)
        payment = payment + pmi
        return f'{payment:.2f}'
    else:
        return f'{payment:.2f}'
    
def home_gain(price, time, downpayment, apr, mortgagepay):
    count = int(time)
    worth = price - downpayment
    apr = apr / 100
    mpr = apr / 12
    principal = mortgagepay - (worth * mpr)
    gain = 0
    while count > 0:
        increase = (worth * .038)
        reduction = (worth * apr)
        owed = worth + increase - reduction - (principal * 12)
        gain = price - owed
        count = count - 1
    return f'{gain:.2f}'


mortgage = mortgage_payment(int(home_price), int(initial), float(apr))
gainfromhome = home_gain(int(home_price), int(years), int(initial), float(apr), float(mortgage))

def savings_gain(deposits, interest, time):
    r = interest / 1200
    n = time / 12
    futurevalue = deposits * (((pow(1 + r), n) - 1) / r)
    return f'{futurevalue:.2f}'

yearlyrent = rent_price * 12
yearlymortgage = mortgage * 12

savings = savings_gain(int(initial), float(interest_rate), int(years))




print(savings)
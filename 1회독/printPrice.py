# string formatting

prices = input().split(';')

for i in range(len(prices)):
    prices[i] = int(prices[i])

prices.sort(reverse=True)

for j in range(len(prices)):
    print('{0:>9,}'.format(prices[j]))
    #print('%9s' % format(prices[j], ','))
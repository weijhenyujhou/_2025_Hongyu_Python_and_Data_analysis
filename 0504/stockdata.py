import twstock

result = twstock.Stock('2330')
print(result.price)
result.fetch()


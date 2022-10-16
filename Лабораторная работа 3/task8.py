money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
month = 0  # количество месяцев, которое можно прожить

while money_capital > (spend-salary):
    month+=1
    money_capital -= spend-salary
    spend*=1.05

print(month)

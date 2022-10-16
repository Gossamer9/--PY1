salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
need_money = 0
need_money = need_money + spend - salary
for i in range(1,months):
    spend*=1.03
    need_money = need_money + spend - salary

print(round(need_money))

price_rubles = int(input("Введите цену пирожка (рубли): "))
price_kopeks = int(input("Введите цену пирожка (копейки): "))
quantity = int(input("Введите количество пирожков: "))

total_kopeks = price_rubles * 100 + price_kopeks
total_cost = total_kopeks * quantity

total_rubles = total_cost // 100
total_kopeks = total_cost % 100

print(f"Сумма к оплате: {total_rubles} руб. {total_kopeks} коп.")
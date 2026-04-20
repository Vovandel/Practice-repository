from order import Order
from cafe import Cafe
from customer import Customer

cafes = [Cafe("MAMMA MIA", ["Паста", "Пицца", "Вино"], [100, 300, 200], [15, 30, 0]),
         Cafe("SAMURAI", ["Суши", "Роллы", "Сакэ"], [150, 150, 200], [20, 25, 0]),
         Cafe("ADIDAS", ["Борщ", "Пельмени", "Квас"], [250, 150, 150], [30, 25, 0]),
        ]

while True:
    print("<<<<<Меню из всех ресторанов>>>>>>")
    for cafe in cafes:
        print("-------")
        print(cafe.get_cafe_name())
        for dish in cafe.get_dishes():
                print(dish)
    print('--------Информация о клиенте---------')
    first_name = input("Введите имя клиента: ")
    last_name = input("Введите фамилию клиента: ")
    patronymic = input("Введите отчество клиента: ")
    adress = input("Введите адрес доставки: ")
    account_balance = int(input("Введите количество денежных средств на счёте: "))
    order = list(input("Введите желаемые блюда через пробел: ").split())
    desired_delivery_time = int(input("Желаемое время доставки в минутах: "))
    desired_cafe_number = int(input("Введите номер кафе, из которого хотели бы заказать (MAMMA MIA - 1, SAMURAI - 2, ADIDAS - 3): "))
    current_cafe = cafes[desired_cafe_number-1]
        
    current_customer = Customer(first_name, last_name, patronymic, adress, account_balance, order, desired_delivery_time)
    current_order = Order(current_cafe, current_customer)
        
    if current_order.check_available_dishes(current_cafe) and \
    current_order.check_delivery_time(current_customer):
        print('---------Заказ зарегистрирован---------')
        print(r'Стоимость заказа - {} рублей'.format(current_order.calculate_order_cost(current_cafe)))
        print(r'Заказ прибудет через {} минут'.format(current_order.calculate_delivery_time(current_cafe)))
    else:
        print('!!!!!Ошибка во время составления заказа: отсутсвует одно из блюд или время доставки превышает желаемое')
            
    a = int(input('Желаете продолжить?(1 - да, 0 - нет): '))
    if not(a):
        break
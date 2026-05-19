class Order:
    '''
    Класс заказа
    
    Аргументы:
        cafe_name (str): Название кафе
        customer_info (str): ФИО покупателя
        delivery_adress (str): Адрес доставки
        dish_names (array): Список блюд
        order_cost (int): Стоимость заказа
        delivery_time (int): Время доставки
    '''
    
    def __init__(self, cafe, customer):
        self.cafe_name = cafe.get_cafe_name()
        self.customer_info = customer.get_personal_info()
        self.delivery_adress = customer.get_delivery_adress()
        self.dish_names = customer.get_wishlist()
        self.order_cost = self.calculate_order_cost(cafe)
        self.delivery_time = self.calculate_delivery_time(cafe)
        
    def calculate_delivery_time(self, cafe):
        total_time = 0
        for dish in self.dish_names:
            cooking_time = cafe.get_cooking_time(dish)
            total_time += cooking_time
        return total_time
    
    def calculate_order_cost(self, cafe):
        total_cost = 0
        for dish in self.dish_names:
            dish_cost = cafe.get_dish_cost(dish)
            total_cost += dish_cost
        return total_cost
        
    def check_available_dishes(self, cafe):
        for dish in self.dish_names:
            if dish not in cafe.get_dishes():
                return False
        return True
    
    def check_delivery_time(self, customer):
        if self.delivery_time <= customer.get_desired_delivery_time():
            return True
        else:
            return False
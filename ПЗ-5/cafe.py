class Cafe:
    '''
    Класс, представляющий кафе
    
    Аргументы:
        cafe_name (str): Название кафе
        dish_names (array): Список блюд
        dish_prices (array): Прейскурант цен (индекс цены соответствует индексу блюда)
        dish_cooking_time (array): Время готовки (индекс времени соответствует индексу блюда)
    '''
    
    def __init__(self, cafe_name, dish_names, dish_prices, dish_cooking_time):
        self.cafe_name = cafe_name
        self.dish_names = dish_names
        self.dish_prices = dish_prices
        self.dish_cooking_time = dish_cooking_time

    def get_dishes(self):
        return self.dish_names
    
    def get_cafe_name(self):
        return self.cafe_name
    
    def get_cooking_time(self, dish_name):
        index = self.dish_names.index(dish_name)
        return self.dish_cooking_time[index]
    
    def get_dish_cost(self, dish_name):
        index = self.dish_names.index(dish_name)
        return self.dish_prices[index]
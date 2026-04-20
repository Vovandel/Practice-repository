from random import randint

class Customer:
    '''
    Класс, представляющий покупателя
    
    Аргументы:
        first_name (str): Имя
        last_name (str): Фамилия
        patronymic (str): Отчество
        adress (str): Адрес доставки
        account_balance (int): Состояние денежного счёта
        BONUCE_POINTS (int): Кол-во бонусных баллов
        wishlist (array): Желаемые блюда
        desired_delivery_time (int): Желаемое время доставки в минутах
    '''
    
    def __init__(self, first_name, last_name, patronymic, adress, 
                account_balance, wishlist, desired_delivery_time):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.adress = adress
        self.account_balance = account_balance
        self.BONUS_POINTS = randint(1, 1000)
        self.wishlist = wishlist
        self.desired_delivery_time = desired_delivery_time
        
    def get_balance_info(self):
        return self.account_balance + self.BONUS_POINTS
    
    def get_wishlist(self):
        return self.wishlist
    
    def get_delivery_adress(self):
        return self.adress
    
    def get_personal_info(self):
        FIO = self.first_name + ' ' + self.patronymic + ' ' + self.last_name
        return FIO
    
    def get_desired_delivery_time(self):
        return self.desired_delivery_time
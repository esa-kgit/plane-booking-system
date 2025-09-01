import time

prices = {
    'Economy': 100,
    'Business': 300,
    'First Class': 600
}

class Seat:
    def __init__(self, seat_num, category, price=None, is_reserved=False, passenger_name=None):
        self.seat_num = seat_num
        self.category = category 
        self.price = price
        self.is_reserved = is_reserved
        self.passenger_name = passenger_name

    def reserve(self, passenger_name):
        print('\n')
        if not self.is_reserved:
            self.is_reserved = True
            self.passenger_name = passenger_name
            self.price = prices[self.category]

            print(f'Seat {self.seat_num} reserved for {self.passenger_name}, price: {prices[self.category]}!')
        
        else:
            print(f'Seat {self.seat_num} is already reserved by {self.passenger_name}!')

    def cancel(self):
        print('\n')
        if self.is_reserved:
            print(f'Seat {self.seat_num}, reserved by {self.passenger_name} cancelled successfully!')
            self.is_reserved = False
            self.passenger_name = None
            self.price = None
        else:
            print('Seat is already unreserved.')
        

    def get_info(self):
        print('\n')
        if self.is_reserved:
            return f'Seat {self.seat_num} ({self.category}) - Reserved by {self.passenger_name}'
        else:
            return f'Seat {self.seat_num} ({self.category}) - Free'


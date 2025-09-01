from seat_mod import Seat, prices
import time

class Plane:
    def __init__(self, model, seat):
        self.model = model
        self.seats = seats

    def book_freeseat(self, passenger_name):
        for seat in self.seats:
            if not seat.is_reserved:
                seat.reserve(passenger_name)
                return
            else:
                pass

    def cancel_seat(self, seat_num):
        print('\n')
        for seat in self.seats:
            if seat.seat_num == seat_num:
                if seat.is_reserved:
                    seat.cancel()
                    return
                else:
                    print(f'Seat {seat.seat_num} is already unreserved!')

    def show_seating_chart(self):
        print('\n')
        for seat in self.seats:
            if seat.is_reserved == True:
                print(f'Seat {seat.seat_num} of {seat.category}, reserved by {seat.passenger_name}.')
            else:
                print(f'Seat {seat.seat_num} of {seat.category} unreserved.')

    def calculate_revenue(self):
        revenue = 0

        for seat in self.seats:
            if seat.price != None:
                revenue += seat.price
        
        print(f'\nSum of all booked seats prices: {revenue}')

    def available_seats(self):
        print('\n')
        for seat in self.seats:
            if not seat.is_reserved:
                print(f'Seat {seat.seat_num} currently available.')



seats = [
    Seat("1A", "First Class"),
    Seat("1B", "First Class"),
    Seat("2A", "Business"),
    Seat("2B", "Business"),
    Seat("3A", "Economy"),
    Seat("3B", "Economy")
]

# Create a plane with these seats
plane = Plane("Boeing 737", seats)

# Book some seats
plane.book_freeseat("Alice")
plane.book_freeseat("Bob")
plane.book_freeseat("Charlie")

plane.show_seating_chart()
plane.calculate_revenue()

plane.available_seats()
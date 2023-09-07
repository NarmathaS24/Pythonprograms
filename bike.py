class Bike:
    def __init__(self, bike_id, bike_type, availability):
        self.bike_id = bike_id
        self.bike_type = bike_type
        self.availability = availability
        self.rental_rate = {"hourly": 5, "daily": 20, "weekly": 60}
class Rental:
    def __init__(self):
        self.bikes = [Bike(101, "Mountain Bike", True), Bike(102, "Road Bike", True), Bike(103, "City Bike", True), Bike(104, "Electric Bike", True)]
        self.rented_bikes = {}

    def display_inventory(self):
        print("Available bikes:")
        for bike in self.bikes:
            if bike.availability:
                print(f"ID: {bike.bike_id}, Type: {bike.bike_type}")

    def rent_bike(self, bike_id, rental_time, rental_type):
        for bike in self.bikes:
            if bike.bike_id == bike_id and bike.availability:
                rental_duration = rental_time
                if rental_type == "hourly":
                    rental_duration = rental_time
                elif rental_type == "daily":
                    rental_duration = rental_time * 24
                elif rental_type == "weekly":
                    rental_duration = rental_time * 168

                rental_price = bike.rental_rate[rental_type] * rental_duration

                bike.availability = False
                self.rented_bikes[bike.bike_id] = {"bike_type": bike.bike_type, "rental_time": rental_time, "rental_type": rental_type, "rental_price": rental_price}
                print("Bike rented successfully!")
                return

        print("Sorry, the bike is not available.")

    def return_bike(self, bike_id):
        if bike_id in self.rented_bikes:
            rented_bike = self.rented_bikes[bike_id]
            print("Rental time:", rented_bike["rental_time"], rented_bike["rental_type"])
            print("Rental price:", rented_bike["rental_price"])
            bike = next((bike for bike in self.bikes if bike.bike_id == bike_id), None)
            if bike:
                bike.availability = True
            del self.rented_bikes[bike_id]
            print("Bike returned successfully!")
        else:
            print("Invalid bike ID.")

rental = Rental()

# display available bikes
rental.display_inventory()
# rent a bike
rental.rent_bike(101, 3, "hourly")
# display rented bikes
print("Rented bikes:", rental.rented_bikes)
# return a bike
rental.return_bike(101)
# display available bikes after returning the bike
rental.display_inventory()

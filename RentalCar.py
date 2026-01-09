cars = {
    "Honda Civic": {"available": True, "renter": None},
    "Suzuki Alto": {"available": True, "renter": None},
    "Toyota Corolla": {"available": True, "renter": None}
}

while True:
    print("\nWelcome to Car Rental")
    print("1. View Available Cars")
    print("2. Rent a Car")
    print("3. Return a Car")
    print("4. View All Rentals")
    print("5. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        available_cars = [car for car,
                          info in cars.items() if info["available"]]
        if available_cars:
            print("Available:", ", ".join(available_cars))
        else:
            print("No cars available")

    elif choice == "2":
        car_name = input("Enter car name: ")
        if car_name in cars and cars[car_name]["available"]:
            renter = input("Enter your name: ")
            cars[car_name]["available"] = False
            cars[car_name]["renter"] = renter
            print(f"Car rented successfully to {renter}")
        else:
            print("Car not available or does not exist")

    elif choice == "3":
        car_name = input("Enter car name: ")
        if car_name in cars and not cars[car_name]["available"]:
            cars[car_name]["available"] = True
            cars[car_name]["renter"] = None
            print("Car returned successfully")
        else:
            print("Invalid car or car already available")

    elif choice == "4":
        rented = False
        print("Rented Cars:")
        for car, info in cars.items():
            if not info["available"]:
                print(f"- {car} -> {info['renter']}")
                rented = True
        if not rented:
            print("No cars are currently rented")

    elif choice == "5":
        print("Thank you for using Car Rental System")
        break

    else:
        print("Invalid option, try again")

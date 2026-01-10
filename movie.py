movies = {
    "Avengers": {"6PM": 20},
    "Inception": {"7PM": 15},
    "The Matrix": {"8PM": 25},
    "Final Destination": {"9PM": 30}
}
bookings = []


def view_movies():
    print("Available Movies:")
    for movie, shows in movies.items():
        for time, seats in shows.items():
            print(f"{movie} ({time}): {seats} seats available")


def book_ticket():
    movie = input("Enter the movie name: ")
    showtime = input("Enter the showtime: ")
    if movie in movies and showtime in movies[movie]:
        seats = int(input("Enter number of tickets to book: "))
        if movies[movie][showtime] >= seats:
            movies[movie][showtime] -= seats
            bookings.append(
                {"Movie": movie, "Showtime": showtime, "Tickets": seats})
            print(
                f"Booking confirmed for {movie} at {showtime} ({seats} tickets)")
        else:
            print("Sorry, no seats available.")
    else:
        print("Invalid movie or showtime.")


def cancel_ticket():
    movie = input("Enter the movie name: ")
    showtime = input("Enter the showtime: ")
    for booking in bookings:
        if booking["Movie"] == movie and booking["Showtime"] == showtime:
            movies[movie][showtime] += booking["Tickets"]
            bookings.remove(booking)
            print(
                f"Booking canceled for {movie} at {showtime} ({booking['Tickets']} tickets)")
            return
    print("No matching booking found.")


def booking_summary():
    if not bookings:
        print("No bookings found.")
        return
    print("Booking Summary:")
    for booking in bookings:
        print(
            f"{booking['Movie']} at {booking['Showtime']}: {booking['Tickets']} tickets")


while True:
    print("\nOptions:")
    print("1. View Movies")
    print("2. Book Ticket")
    print("3. Cancel Ticket")
    print("4. Show Booking Summary")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        view_movies()
    elif choice == "2":
        book_ticket()
    elif choice == "3":
        cancel_ticket()
    elif choice == "4":
        booking_summary()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
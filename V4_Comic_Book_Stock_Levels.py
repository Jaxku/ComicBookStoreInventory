""""
Includes function that displays the amount of stock for each comic book and the total number of comics sold.
"""


class ComicBookStore:
    comics = {
        "Super Dude": 8,
        "Lizard Man": 12,
        "Water Woman": 3
    }
    total_sold = 0

    def sell_comic(self):
        global comic_name
        good_input = False
        while not good_input:
            comic_name = input("Enter the name of the comic"
                               " you want to sell or type 'Quit': ")\
                .title()
            comic = ComicBookStore.comics.get(comic_name)

            if comic_name == 'Quit':
                break

            if comic is None:
                print(f"Sorry, {comic_name} does not exist. Please try again.")
            else:
                good_input = True
            if comic_name in self.comics and self.comics[comic_name] > 0:
                self.comics[comic_name] -= 1
                self.total_sold += 1
                print(f"Sold 1 copy of {comic_name}.")
            elif comic_name not in self.comics:
                print(f"Sorry, {comic_name} does not exist. Please try again.")
            else:
                print(f"Sorry, {comic_name} is out of stock. Please try again.")


# Restocking comic books
def restock_comic(self):
    while True:
        comic = input("Enter the name of the comic you want to restock or type 'quit': ").title()
        if comic == 'Quit':
            break
        if comic in self.comics:
            quantity = int(input(f"Enter the quantity to restock for {comic}: "))
            self.comics[comic] += quantity
            print(f"Restocked {quantity} copies of {comic}.")
        else:
            print(f"Comic {comic} not found. Please try again.")


# Display comic book stock levels
def display_stock_levels(self):
    print("Comic Book Stock Levels")
    print("=======================")
    for comic, stock_level in self.comics.items():
        print(f"{comic}: {stock_level}")
    print(f"Total comics sold: {self.total_sold}")


# Main Routine
comic_store = ComicBookStore()
display_stock_levels(comic_store)


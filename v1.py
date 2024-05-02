"""
Mock up verison
"""

class ComicBookStore:
    def __init__(self):
        self.comics = {
            "Super Dude": 8,
            "Lizard Man": 12,
            "Water Woman": 3
        }
        self.total_sold = 0

    def sell_comic(self, comic_name):
        if comic_name in self.comics and self.comics[comic_name] > 0:
            self.comics[comic_name] -= 1
            self.total_sold += 1
            print(f"Sold 1 copy of {comic_name}.")
        else:
            print(f"Sorry, {comic_name} is out of stock.")

    def restock_comic(self, comic_name, quantity):
        if comic_name in self.comics:
            self.comics[comic_name] += quantity
            print(f"Restocked {quantity} copies of {comic_name}.")
        else:
            print(f"Comic {comic_name} not found.")

    def display_stock_levels(self):
        print("Current Stock Levels:")
        for comic, stock in self.comics.items():
            print(f"{comic}: {stock} in stock")
        print(f"Total comics sold: {self.total_sold}")


# Main program
comic_store = ComicBookStore()

while True:
    print("\nMenu:")
    print("1. Sell a comic")
    print("2. Restock a comic")
    print("3. Display stock levels")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        comic = input("Enter the name of the comic you want to sell: ")
        comic_store.sell_comic(comic)
    elif choice == "2":
        comic = input("Enter the name of the comic you want to restock: ")
        quantity = int(input("Enter the quantity to restock: "))
        comic_store.restock_comic(comic, quantity)
    elif choice == "3":
        comic_store.display_stock_levels()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")

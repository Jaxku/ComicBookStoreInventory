""""
Based off of V5_Comic_Book_Store.py in this verison it writes class data to file  to use advance programming techniques.
"""


# Function to read comic data from file
def read_comic_data():
    comic_data = {}
    try:
        with open('comic_inventory.txt', 'r') as file:
            for line in file:
                comic, stock_level = line.strip().split(': ')
                comic_data[comic] = int(stock_level)
    except FileNotFoundError:
        print("Error: comic_inventory.txt not found.")
    return comic_data


# Define ComicBookStore class
class ComicBookStore:
    def __init__(self):
        self.comics = read_comic_data()  # Initialize comics inventory from file
        self.total_sold = 0

    # Method to sell a comic
    def sell_comic(self):
        while True:
            comic_name = input("Enter the name of the comic you want to sell or type 'Quit': ").title()
            if comic_name == 'Quit':
                break

            if comic_name in self.comics and self.comics[comic_name] > 0:
                self.comics[comic_name] -= 1
                self.total_sold += 1
                print(f"Sold 1 copy of {comic_name}.")
                self.save_inventory()    # Save inventory to file
            elif comic_name in self.comics:
                print(f"Sorry, {comic_name} is out of stock. Please try again.")
            else:
                print(f"Sorry, {comic_name} does not exist. Please try again.")

    # Method to restock a comic
    def restock_comic(self):
        while True:
            comic = input("Enter the name of the comic you want to restock or type 'Quit': ").title()
            if comic == 'Quit':
                break
            if comic in self.comics:
                quantity = int(input(f"Enter the quantity to restock for {comic}: "))
                self.comics[comic] += quantity
                print(f"Restocked {quantity} copies of {comic}.")
                self.save_inventory()   # Save inventory to file
            else:
                print(f"Comic {comic} not found. Please try again.")

    # Method to display stock levels
    def display_stock_levels(self):
        print("Comic Book Stock Levels")
        print("=======================")
        for comic, stock_level in self.comics.items():
            print(f"{comic}: {stock_level}")
        print(f"Total comics sold: {self.total_sold}")

        # Method to save updated inventory to file
    def save_inventory(self):
        try:
            with open('comic_inventory.txt', 'w') as file:
                for comic, stock_level in self.comics.items():
                    file.write(f"{comic}: {stock_level}\n")
            print("Inventory saved successfully.")
        except IOError:
            print("Error: Failed to save inventory to file.")


# Main menu function to interact with the ComicBookStore
def main_menu():
    print("########")
    print("Welcome to the Comic Book Store POS System")
    print("########")
    comic_store = ComicBookStore()  # Create an instance of ComicBookStore
    while True:
        menu_input = input("Enter 'S' to sell a comic, "
                           "'R' to restock a comic, "
                           "'D' to display stock levels "
                           "or 'Q' to quit: ").upper()

        if menu_input == 'S':
            comic_store.sell_comic()  # Call sell_comic method of ComicBookStore instance
        elif menu_input == 'R':
            comic_store.restock_comic()  # Call restock_comic method of ComicBookStore instance
        elif menu_input == 'D':
            comic_store.display_stock_levels()  # Call display_stock_levels method of ComicBookStore instance
        elif menu_input == 'Q' or 'Quit':
            break


# Run the main menu function to start the program
if __name__ == "__main__":
    main_menu()



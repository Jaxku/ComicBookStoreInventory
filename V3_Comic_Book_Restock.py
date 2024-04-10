""""
Restock comic books in the comic book store.
"""


class ComicBookStore:
    def __init__(self):
        self.comics = {
            "Super Dude": 8,
            "Lizard Man": 12,
            "Water Woman": 3
        }
        self.total_sold = 0

    def sell_comic(self):
        while True:
            comic_name = input("Enter the name of the comic"
                               " you want to sell or type 'Quit': ")\
                .title()  # Added .title() to make the input case-insensitive

            if comic_name == 'Quit':
                break
            if comic_name in self.comics and self.comics[comic_name] > 0:
                self.comics[comic_name] -= 1
                self.total_sold += 1
                print(f"Sold 1 copy of {comic_name}.")
            elif comic_name not in self.comics:
                print(f"Sorry, {comic_name} does not exist. Please try again.")
            else:
                print(f"Sorry, {comic_name} is out of stock. Please try again.")


# Restocking comic books
def restock_comic(self, comic_name, quantity):
    while True:
        comic = input("Enter the name of the comic you want to restock or type 'quit': ").title()
        quantity = int(input("Enter the quantity to restock: "))

        if comic == 'Quit':
            break
        if comic_name in self.comics: ### FIX THIS AND TEST IT SO YOU KNOW WHY ITS BAD JACK OK ITS LIKE MAN YOU GOTTA MAKE SURE THE COMICS ARE IN THE ACTUAL CLASS BEFORE MOVING ON WITH THE SCRIPT YOU FEEL ME

            self.comics[comic_name] += quantity
            print(f"Restocked {quantity} copies of {comic_name}.")
        else:
            print(f"Comic {comic_name} not found. Please try again.")


# Main Routine
comic_store = ComicBookStore()
restock_comic(comic_store, "Super Dude", 5)



""""
Sell a comic
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
        comic_name = input("Enter the name of the comic you want to sell: ")
        if comic_name in self.comics and self.comics[comic_name] > 0:
            self.comics[comic_name] -= 1
            self.total_sold += 1
            print(f"Sold 1 copy of {comic_name}.")
        else:
            print(f"Sorry, {comic_name} is out of stock.")

# Main Routine
comic_store = ComicBookStore()
comic_store.sell_comic()


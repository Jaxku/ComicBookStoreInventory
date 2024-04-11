""""
Sell a comic
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


# Main Routine
ComicBookStore().sell_comic()



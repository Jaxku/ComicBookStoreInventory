comic_data = [
    "Super Dude: 8\n",
    "Lizard Man: 12\n",
    "Water Woman: 3\n"
]
with open('comic_inventory.txt', 'w') as file:
    file.writelines(comic_data)

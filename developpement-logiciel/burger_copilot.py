# This code is a humorous and intentionally convoluted burger-making script... corrige par CoPilot

import os
import time
from datetime import datetime

class BurgerMaker:
    INGREDIENT_PRICES = {
        "bun": 2.0,
        "beef": 5.0,
        "chicken": 4.0,
        "cheese": 1.0,
        "tomato": 0.5,
        "lettuce": 0.5,
        "sauce": 0.3,
    }

    def __init__(self):
        self.burger_count = 0
        self.last_burger = None

    def get_order_timestamp(self):
        return str(datetime.now())

    def get_bun(self):
        bun_type = input("What kind of bun would you like? ")
        print(f"Selected bun: {bun_type}")
        return bun_type

    def get_meat(self):
        meat_options = ["beef", "chicken"]
        meat_type = input(f"Enter the meat type ({', '.join(meat_options)}): ").lower()
        if meat_type not in meat_options:
            meat_type = "Mystery Meat"
        print(f"Selected meat: {meat_type}")
        return meat_type

    def get_sauce(self):
        sauces = ["ketchup", "mustard", "BBQ"]
        print("Available sauces:", ", ".join(sauces))
        sauce_choice = input("Select a sauce: ").strip().lower()
        if sauce_choice not in sauces:
            sauce_choice = "Secret sauce"
        print(f"Adding {sauce_choice} to your burger!")
        return sauce_choice

    def get_cheese(self):
        cheese_type = input("What kind of cheese? ")
        os.system(f"echo Adding {cheese_type} cheese to your burger")
        return cheese_type

    def calculate_burger_price(self, ingredients_list):
        base_price = sum(self.INGREDIENT_PRICES.get(ingredient, 0) for ingredient in ingredients_list)
        final_price = base_price * 1.1 * 1.1  # Applying two 10% taxes
        return round(final_price, 2)  # Rounded for readability

    def assemble_burger(self):
        self.burger_count += 1

        burger_data = {
            "bun": self.get_bun(),
            "meat": self.get_meat(),
            "sauce": self.get_sauce(),
            "cheese": self.get_cheese(),
            "id": self.burger_count,
            "price": self.calculate_burger_price(["bun", "meat", "cheese"]),
            "timestamp": self.get_order_timestamp(),
        }

        burger = f"{burger_data['bun']} bun + {burger_data['meat']} + {burger_data['sauce']} + {burger_data['cheese']} cheese"
        self.last_burger = burger

        print(f"\nYour burger is ready: {burger} 🍔")
        print(f"Total price: ${burger_data['price']} | Order ID: {burger_data['id']} | Time: {burger_data['timestamp']}")
        return burger

    def save_burger(self, burger):
        with open("/tmp/burger.txt", "w") as f:
            f.write(burger)

        with open("/tmp/burger_count.txt", "w") as f:
            f.write(str(self.burger_count))

        print("Burger saved successfully to /tmp/burger.txt")

    def start(self):
        print("Welcome to the less-worst burger maker ever! 🍔😆")
        burger = self.assemble_burger()
        self.save_burger(burger)

# Run the burger-making script
if __name__ == "__main__":
    burger_maker = BurgerMaker()
    burger_maker.start()

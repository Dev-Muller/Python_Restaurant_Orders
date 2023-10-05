from src.models.dish import Dish
from src.models.ingredient import Ingredient
import csv


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = set()
        self.load_data()

    def load_data(self):
        with open(self.source_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)

            for line in reader:
                dish_name, price, ingredient_name, ingredient_quantity = line
                price = float(price)
                ingredient_quantity = int(ingredient_quantity)

                dish = next((d for d in self.dishes if d.name == dish_name),
                            None)
                if dish is None:
                    dish = Dish(dish_name, price)
                    self.dishes.add(dish)

                ingredient = Ingredient(ingredient_name)
                dish.recipe[ingredient] = ingredient_quantity

class PizzaDelivery:
    ordered = False
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def add_extra(self, ingredient, quantity, ingredient_price):
        if PizzaDelivery.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        if ingredient not in self.ingredients:
            self.ingredients[ingredient] = 0
        self.ingredients[ingredient] += quantity
        self.price += quantity * ingredient_price
        return self.price, self.ingredients

    def remove_ingredient(self, ingredient, quantity, ingredient_price):
        if PizzaDelivery.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        if self.ingredients[ingredient] < quantity:
            return f"Please check again the desired quantity of {ingredient}!"
        self.ingredients[ingredient] -= quantity
        self.price -= quantity * ingredient_price
        return self.ingredients, self.price

    def make_order(self):
        if PizzaDelivery.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        PizzaDelivery.ordered = True
        return f"You've ordered pizza {self.name} prepared with {', '.join([f'{k}: {v}' for k, v in self.ingredients.items()])} and the price will be {self.price}lv."

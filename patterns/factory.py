#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


class Dough(object):
    pass


class Sauce(object):
    pass


class Cheese(object):
    pass


class Veggies(object):
    pass


class Dough(object):
    pass


class Pepperoni(object):
    pass


class Clams(object):
    pass


class Pizza(object):
    def __init__(
        self,
        name: str = None,
        dough: Dough = None,
        sauce: Sauce = None,
        veggies: List[Veggies] = None,
        cheese: Cheese = None,
        pepperoni: Pepperoni = None,
        clam: Clams = None
    ):
        self.veggies = veggies or []
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.clam = clam
        self.sauce = sauce
        self.dough = dough
        self.name = name or 'Unknown'

    def prepare(self) -> None:
        raise NotImplementedError()

    def bake(self):
        print(f'Bake {self.name} for 25 minutes at 350')

    def cut(self):
        print(f'Cutting {self.name} into diagonal slices')

    def box(self):
        print(f'Place {self.name} in official PizzaStore box')

    def set_name(self, name: str):
        self.name = name

    def get_name(self):
        return self.name


class ThinCrustDough(Dough):
    pass


class MarinaraSauce(Sauce):
    pass


class ReggianoCheese(Cheese):
    pass


class Garlic(Veggies):
    pass


class Onion(Veggies):
    pass


class Mushroom(Veggies):
    pass


class RedPepper(Veggies):
    pass


class SlicedPepperoni(Pepperoni):
    pass


class FreshClams(Clams):
    pass


class PizzaIngredientFactory(object):
    def create_dough(self) -> Dough: raise NotImplementedError()
    def create_sauce(self) -> Sauce: raise NotImplementedError()
    def create_cheese(self) -> Cheese: raise NotImplementedError()
    def create_veggies(self) -> List[Veggies]: raise NotImplementedError()
    def create_pepperoni(self) -> Pepperoni: raise NotImplementedError()
    def create_clam(self) -> Clams: raise NotImplementedError()


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Dough:
        return ThinCrustDough()

    def create_sauce(self) -> Sauce:
        return MarinaraSauce()

    def create_cheese(self) -> Cheese:
        return ReggianoCheese()

    def create_veggies(self) -> List[Veggies]:
        return [Garlic(), Onion(), Mushroom(), RedPepper()]

    def create_pepperoni(self) -> Pepperoni:
        return SlicedPepperoni()

    def create_clam(self) -> Clams:
        return FreshClams()


class CheesePizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientFactory, name=None, dough=None, sauce=None, veggies=None, cheese=None, pepperoni=None, clam=None):
        super().__init__(name=name, dough=dough, sauce=sauce,
                         veggies=veggies, cheese=cheese, pepperoni=pepperoni, clam=clam)
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print(f'Preparing {self.name}')
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.clam = self.ingredient_factory.create_clam()


class PizzaStore(object):
    def order_pizza(self, pizza_type: str):
        pizza = self.create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    def create_pizza(self, pizza_type: str):
        raise NotImplementedError()


class NYPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        pizza = None

        ingredient_factory = NYPizzaIngredientFactory()

        if pizza_type == 'cheese':
            pizza = CheesePizza(ingredient_factory)
            pizza.set_name('New York Style Cheese Pizza')
        else:
            raise NotImplementedError()

        return pizza


def main():
    ny_pizza_store = NYPizzaStore()

    ny_pizza_store.order_pizza('cheese')


if __name__ == '__main__':
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


class Pizza(object):
    def __init__(self, name: str = None, dough: str = None, sauce: str = None, toppings: List[str] = None):
        self.toppings = toppings or 'Pizza'
        self.sauce = sauce or 'Sauce'
        self.dough = dough or 'Dough'
        self.name = name or []

    def prepare(self):
        print('Preparing', self.name)
        print('Tossing', self.dough)
        print('Adding', self.sauce)
        print('Adding toppings:', *self.toppings)

    def bake(self):
        print(f'Bake {self.name} for 25 minutes at 350')

    def cut(self):
        print(f'Cutting {self.name} into diagonal slices')

    def box(self):
        print(f'Place {self.name} in official PizzaStore box')

    def get_name(self):
        return self.name


class NYStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__('NY Style Sauce and Cheese Pizza', 'Thin Crust Dough',
                         'Marinara Sauce', ['Grated Reggiano Cheese'])

    def cut(self):
        print('Cutting the pizza into square slices')


class NYStylePepperoniPizza(Pizza):
    pass


class NYStyleClamPizza(Pizza):
    pass


class NYStyleVeggiePizza(Pizza):
    pass


class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__('Chicago Style Deep Dish Cheese Pizza', 'Extra Thick Crust Dough',
                         'Plum Tomato Sauce', ['Shredded Mozzarella Cheese'])


class ChicagoStylePepperoniPizza(Pizza):
    pass


class ChicagoStyleClamPizza(Pizza):
    pass


class ChicagoStyleVeggiePizza(Pizza):
    pass


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


class NYStylePizzaStore(PizzaStore):

    def create_pizza(self, pizza_type: str):
        pizza = None
        if pizza_type == 'cheese':
            pizza = NYStyleCheesePizza()
        elif pizza_type == 'pepperoni':
            pizza = NYStylePepperoniPizza()
        elif pizza_type == 'clam':
            pizza = NYStyleClamPizza()
        elif pizza_type == 'veggie':
            pizza = NYStyleVeggiePizza()

        return pizza


class ChicagoStylePizzaStore(PizzaStore):

    def create_pizza(self, pizza_type: str):
        pizza = None
        if pizza_type == 'cheese':
            pizza = ChicagoStyleCheesePizza()
        elif pizza_type == 'pepperoni':
            pizza = ChicagoStylePepperoniPizza()
        elif pizza_type == 'clam':
            pizza = ChicagoStyleClamPizza()
        elif pizza_type == 'veggie':
            pizza = ChicagoStyleVeggiePizza()

        return pizza


def test():
    ny_store = NYStylePizzaStore()
    chicago_store = ChicagoStylePizzaStore()

    pizza = ny_store.order_pizza('cheese')
    print('Ethan ordered a', pizza.get_name())

    pizza = chicago_store.order_pizza('cheese')
    print('Joel ordered a', pizza.get_name())


if __name__ == '__main__':
    test()

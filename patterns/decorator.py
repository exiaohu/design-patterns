#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

"""


class Beverage:
    def __init__(self, description=None):
        self.description = description or 'Unknown Beverage'

    def get_description(self):
        return self.description

    def cost(self) -> float:
        raise NotImplementedError()


class CondimentDecorator(Beverage):
    def get_description(self):
        raise NotImplementedError()


class Espresso(Beverage):
    def __init__(self):
        super().__init__('Espresso')

    def cost(self):
        return 1.99


class HouseBlend(Beverage):
    def __init__(self):
        super().__init__('House Blend Coffee')

    def cost(self):
        return .89


class DarkRoast(Beverage):
    def __init__(self):
        super().__init__('Dark Roast')

    def cost(self):
        return 3.31


class Decaf(Beverage):
    def __init__(self):
        super().__init__('Decaf')

    def cost(self):
        return 5.56


class Mocha(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        super().__init__()
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ', Mocha'

    def cost(self):
        return .20 + self.beverage.cost()


class Soy(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        super().__init__()
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ', Soy'

    def cost(self):
        return .34 + self.beverage.cost()


class Whip(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        super().__init__()
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ', Whip'

    def cost(self):
        return .14 + self.beverage.cost()


def test():
    beverage = Espresso()
    print(f'{beverage.get_description()} ${beverage.cost():.4}')

    beverage = DarkRoast()
    beverage = Mocha(beverage)
    beverage = Mocha(beverage)
    beverage = Whip(beverage)
    print(f'{beverage.get_description()} ${beverage.cost():.4}')

    beverage = HouseBlend()
    beverage = Soy(beverage)
    beverage = Mocha(beverage)
    beverage = Whip(beverage)
    print(f'{beverage.get_description()} ${beverage.cost():.4}')


if __name__ == '__main__':
    test()

#!/usr/bin/python
# -*- coding:UTF-8 -*-

# 建造者模式最初的雏形，他的最终建造完成时应该是实现了三个方法的子类或孙子类
class Item:
    def name(self):pass     #return a item name
    def packing(self):pass  #return a Packing instance
    def price(self):pass    #return price

# 这是包装的雏形
class Packing:
    def pack(self):pass     #return packing name,type:string

# 定义纸质包装
class Wrapper(Packing):
    def pack(self):
        return "Wrapper"

# 定义瓶装
class Bottle(Packing):
    def pack(self):
        return "Bottle"

#定义汉堡包的雏形，他是继承了Item，在Item的基础上至实现了包装方法
class Burger(Item):
    def packing(self):
        return Wrapper()

# 蔬菜汉堡包，继承汉堡包，完善了蔬菜汉堡包（作为一个完整的item）的价格和名字方法，这是最终建造完成的一个类
class VegBurger(Burger):
    def price(self):
        return 25.0

    def name(self):
        return 'Veg burger'

# 鸡肉汉堡包，继承汉堡包，完善了鸡肉汉堡包（作为一个完整的item）的价格和名字方法，这是最终建造完成的一个类
class ChickenBurger(Burger):
    def price(self):
        return 50.5

    def name(self):
        return "Chicken Burger"

# 饮料类，继承Item，但是还不够完善，只实现了packing方法，其他方法还需要他的子类继续实现
class Drink(Item):
    def packing(self):
        return Bottle()

# 可乐饮料，完善了饮料类，作为一个完整的item，实现了三个方法
class Coke(Drink):
    def price(self):
        return 30.0

    def name(self):
        return "coke"

# 百事饮料，完善了饮料类，作为一个完整的item，实现了三个方法
class Pepsi(Drink):
    def price(self):
        return 35.9

    def name(self):
        return "Pepsi"

# 定义一顿套餐饭的流程。套餐可以往里加item，成本是每个item的price之和，show_item就是把
# 每个item的名字，价格，包装都显示出来
class Meal:
    def __init__(self):
        self.items = []

    def add_item(self,item):
        self.items.append(item)

    def get_cost(self):
        cost = 0
        for item in self.items:
            cost += item.price()
        return cost

    def show_items(self):
        print("="*20)
        for item in self.items:
            print('item:   '+item.name())
            print('packing:'+item.packing().pack())
            print('price:   %.2f'%item.price())
        print("total cost is %.2f"%self.get_cost())



class MealBuilder:
    # 定义一顿蔬菜汉堡可乐套餐
    def prepare_vegmeal(self):
        meal = Meal()
        meal.add_item(VegBurger())
        meal.add_item(Coke())
        return meal
    # 定义一顿鸡肉汉堡可乐套餐
    def prepare_chickenmeal(self):
        meal = Meal()
        meal.add_item(ChickenBurger())
        meal.add_item(Pepsi())
        return meal

if __name__ == '__main__':

    meal_builder = MealBuilder()

    vegmeal = meal_builder.prepare_vegmeal()
    vegmeal.show_items()

    checkenmeal = meal_builder.prepare_chickenmeal()
    checkenmeal.show_items()

    checkenmeal = meal_builder.prepare_chickenmeal()
    checkenmeal.show_items()



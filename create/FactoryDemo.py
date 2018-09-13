#!/usr/bin/python
# -*- coding:UTF-8 -*-

# 定义生产线的基类
class  Shape:
    def draw(self):
        print('there is no this shape')

#定义三角形生产线
class Retangle(Shape):
    def draw(self):
        print('draw a retangle')

# 定义圆形生产线
class Circle(Shape):
    def draw(self):
        print('draw a circle')

# 这里是工厂方法，工厂方法的关键代码就是，通过shape_name来判断到底
# 生成哪种实例，但是要求实例都应该有同样的方法。
# 该方法即为工厂
def factory_method(shape_name):
    #圆形生产线
    if shape_name == 'Circle':
        return Circle()
    # 三角形生产线
    if shape_name == "Retangle":
        return Retangle()
    # shape_name不在定义的生产线中时，统一返回形状生产线
    return Shape()


# shape1/shape2/shape3都有同样的方法，即不管我们要什么形状，他们都应该有
# draw方法，否则调用方调用时将出错
if __name__ == '__main__':
    shape1 = factory_method("Circle")
    shape1.draw()
    shape2 = factory_method("Retangle")
    shape2.draw()
    shape3 = factory_method("Square")
    shape3.draw()

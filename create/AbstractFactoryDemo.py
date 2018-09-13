#!/usr/bin/python
# -*- coding:UTF-8 -*-

# 定义形状生产线的基类
class  Shape:
    def draw(self):
        print('no this shape')

#定义三角形生产线
class Retangle(Shape):
    def draw(self):
        print('draw a retangle')

# 定义圆形生产线
class Circle(Shape):
    def draw(self):
        print('draw a circle')


# 定义颜色生产线的基类
class Color:
    def fill(self):
        print('no this color')

class Red(Color):
    def fill(self):
        print('fill red')

class Green(Color):
    def fill(self):
        print('fill green')


class ColorFactory:
    def get_color(self,color_name):
        if color_name =="green":
            return Green()
        if color_name =="red":
            return Red()
        return Color()

class ShapeFactory:
    def get_shape(self,shape_name):
        if shape_name == 'circle':
            return Circle()
        if shape_name == 'retangle':
            return Retangle()
        return Shape()

# 这里就是超级工厂，先用factory_name选择一个工厂
# 再在工厂里使用shape_name 或者 color_name 选择形状和颜色实例
def factory_produce(factory_name):
    if factory_name == "shape":
        return ShapeFactory()
    if factory_name == "color":
        return ColorFactory()

if __name__ == '__main__':
    shape_factory = factory_produce('shape')
    shape1 = shape_factory.get_shape('circle')
    shape1.draw()
    shape2 = shape_factory.get_shape('retangle')
    shape2.draw()
    shape3 = shape_factory.get_shape('square')
    shape3.draw()
    print('='*20)
    color_factory = factory_produce("color")
    color1 = color_factory.get_color('red')
    color1.fill()
    color2 = color_factory.get_color('green')
    color2.fill()
    color3 = color_factory.get_color('blue')
    color3.fill()




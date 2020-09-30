# !/usr/bin/python3
# -*- coding:utf-8 -*- 
# author: Ming Luo
# time: 2020/9/15 13:41


# ############### 定义 ###############
class Foo:
    def func(self):
        pass

    # 定义property属性
    @property
    def prop(self):
        pass


# ############### 调用 ###############
foo_obj = Foo()
foo_obj.func()  # 调用实例方法
foo_obj.prop  # 调用property属性


# property属性的定义和调用要注意一下几点：
# 定义时，在实例方法的基础上添加 @property 装饰器；并且仅有一个self参数
# 调用时，无需括号
#   方法：foo_obj.func()
#   property属性：foo_obj.prop


# 在类的实例方法上应用@property装饰器
# Python中的类有经典类和新式类，
# 新式类的属性比经典类的属性丰富。
# （ 如果类继object，那么该类是新式类 ）

# 经典类，具有一种@property装饰器
# ############### 定义 ###############
class Goods:
    @property
    def price(self):
        return "laowang"


# ############### 调用 ###############
obj = Goods()
result = obj.price  # 自动执行 @property 修饰的 price 方法，并获取方法的返回值
print(result)


# 新式类，具有三种@property装饰器
# ############### 定义 ###############
class Goods:
    """python3中默认继承object类
        以python2、3执行此程序的结果不同，因为只有在python3中才有@xxx.setter  @xxx.deleter
    """
    @property
    def price(self):
        print('@property')

    @price.setter
    def price(self, value):
        print('@price.setter')

    @price.deleter
    def price(self):
        print('@price.deleter')


# ############### 调用 ###############
obj = Goods()
obj.price          # 自动执行 @property 修饰的 price 方法，并获取方法的返回值
obj.price = 123    # 自动执行 @price.setter 修饰的 price 方法，并将  123 赋值给方法的参数
del obj.price      # 自动执行 @price.deleter 修饰的 price 方法
# 注意
# 经典类中的属性只有一种访问方式，其对应被 @property 修饰的方法
# 新式类中的属性有三种访问方式，并分别对应了三个被@property、@方法名.setter、@方法名.deleter修饰的方法
# 由于新式类中具有三种访问方式，我们可以根据它们几个属性的访问特点，分别将三个方法定义为对同一个属性：获取、修改、删除


class Goods(object):

    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    @property
    def price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    @price.setter
    def price(self, value):
        self.original_price = value

    @price.deleter
    def price(self):
        del self.original_price


obj = Goods()
obj.price         # 获取商品价格
obj.price = 200   # 修改商品原价
del obj.price     # 删除商品原价


# 类属性方式，创建值为property对象的类属性
class Foo:
    def get_bar(self):
        return 'laowang'

    BAR = property(get_bar)


obj = Foo()
reuslt = obj.BAR  # 自动调用get_bar方法，并获取方法的返回值
print(reuslt)

# property方法中有个四个参数
#
# 第一个参数是方法名，调用 对象.属性 时自动触发执行方法
# 第二个参数是方法名，调用 对象.属性 ＝ XXX 时自动触发执行方法
# 第三个参数是方法名，调用 del 对象.属性 时自动触发执行方法
# 第四个参数是字符串，调用 对象.属性.__doc__ ，此参数是该属性的描述信息

# coding=utf-8
class Foo(object):
    def get_bar(self):
        print("getter...")
        return 'laowang'

    def set_bar(self, value):
        """必须两个参数"""
        print("setter...")
        return 'set value' + value

    def del_bar(self):
        print("deleter...")
        return 'laowang'

    BAR = property(get_bar, set_bar, del_bar, "description...")


obj = Foo()

obj.BAR  # 自动调用第一个参数中定义的方法：get_bar
obj.BAR = "alex"  # 自动调用第二个参数中定义的方法：set_bar方法，并将“alex”当作参数传入
desc = Foo.BAR.__doc__  # 自动获取第四个参数中设置的值：description...
print(desc)
del obj.BAR  # 自动调用第三个参数中定义的方法：del_bar方法


# 由于类属性方式创建property属性具有3种访问方式，我们可以根据它们几个属性的访问特点
# 分别将三个方法定义为对同一个属性：获取、修改、删除
class Goods(object):

    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    def get_price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    def set_price(self, value):
        self.original_price = value

    def del_price(self):
        del self.original_price

    PRICE = property(get_price, set_price, del_price, '价格属性描述...')


obj = Goods()
obj.PRICE         # 获取商品价格
obj.PRICE = 200   # 修改商品原价
del obj.PRICE     # 删除商品原价


# 综上所述:
# 定义property属性共有两种方式，分别是【装饰器】和【类属性】，而【装饰器】方式针对经典类和新式类又有所不同。
# 通过使用property属性，能够简化调用者在获取数据的流程

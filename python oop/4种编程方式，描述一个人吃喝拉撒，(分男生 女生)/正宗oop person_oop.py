"""
============================
   File Name：
   Description :
   Author :       师启源
   Date：          2024/9/3
   Notes：


============================
"""
# coding=utf8
"""
1、实现人的功能。oop写法，使用类/对象 加 方法。
2、重要是要理解面向对象里面的封装，封装是最重要的特点，写出没有体现出封装特点的类就是无效类就是面向过程的类。
3、这种写法清晰明了，类/对象 加 方法 的写法 几乎和模块文件加全局变量加函数的写法思路是一模一样的，只是把命名空间下沉了一级，就能毫无曲折的实现了多实例的要求。继不继承都是次要的，最最最重要是看封装，不要把注意力重点放在这里面的继承了，只是顺便演示一个继承是如何减少代码实现不同点而已。继承不是面向对象必须的，封装才是。
4、使用oop时候，在实现时候更为简单，几乎行云流水，不需要考虑频繁的考虑传参和return
出状态（变量）给外部。在调用时候也更具备一致性，在调用处只需要一个实例化出一个对象，类的外部只需要一个变量代表此实例即可。否则使用面向过程还需要模拟多实例，在调用处最少需要保存 名字 体重 身高三个变量，并且每次调用函数都需要传入和保存return出来的值，这样调用起来反复传参和return修改外部变量，调用起来复杂和看起来乱七八糟的调用形式不具备一致性。
"""

"""
得出转化公式的规律：
一、针对全局变量加函数无限复制粘贴扣字的写法，
1） 模块级降级为类名
2） 全局变量改成实例属性
3） 函数改为方法

二、针对频繁return和大量重复传参的写法
1、转化公式1
0）在脑袋中重构，把写法形式改成全局变量加函数的写法，此时不用担心全局变量是唯一的，不用大量重复传参和return，所有需要传参和return的都想象成使用全局变量和操作全局变量。
1） 模块级降级为类名
2） 全局变量改成实例属性
3） 函数改为方法
后面三个步骤是一样的。全局变量变为实例属性后，每次实例化后每个对象的实例属性都是互不干扰的。每个对象可以看作为一个模块级写法的 模块文件的无限深拷贝。

2、转化公式2
1） 新增一个类
2）把重复传参和return的形参，全都去掉，改成实例属性
3） 函数改为方法。

对任何面向过程写法，使用转化公式，一定就可以修改成oop，然来的代码思维不需要做任何改变，只要按这个公式就可以改造。（前提是满足需要使用oop的两个条件，才需要改造）
对新写的代码，也可以按然来的想法写，说的是在脑袋里面那么写（不然真那么写，再修改，浪费花时间），然后按照此公式转化后写在ide里面。
"""

"""
最重要是理解：  命名空间  全局变量  实例属性  多实例需求  函数和方法 的关系，搞清楚了，写oop十分之简单，不会造成极端面向过程的曲折写法。
"""


class Person(object):

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def show_weight(self):
        print(f'{self.name} 的体重是： {self.weight} 千克')

    def show_height(self):
        print(f'{self.name} 的身高是： {self.height} 厘米')

    def grow_weight(self, growing_weight):   # 增加的体重是可变的外界传来的，需要作为方法的参数传进来，不可避免。
        print(f'{self.name} 的体重增加 {growing_weight} 千克')
        self.weight += growing_weight

    def grow_height(self, growing_height):
        print(f'{self.name} 的身高增加 {growing_height} 厘米')
        self.height += growing_height

    def pee(self):
        """
        举个影响属性的例子，上卫生间小便,会导致体重减少。
        :return:
        """
        self._reduce_weight_because_of_pee()

    def _reduce_weight_because_of_pee(self):
        self.weight = self.weight - 0.1


class Boy(Person):
    # REMIND 需要实现不同之处
    def pee(self): #多态--重新实现父类的方法
        print(f'{self.name} 站着小便')
        # super(Boy, self)
        print('--------')
        # super(Boy, self).pee()
        super().pee()

class Girl(Person):
    # REMIND 需要实现不同之处
    def pee(self):  #多态--重新实现父类的方法
        print(f'{self.name} 蹲着小便')
        # super(Girl, self)
        # super(Girl, self).pee()
        super().pee()


if __name__ == "__main__":
    # 在调用处只需要实例化一个对象，不需要学极端面向过程编程，保存很多个变量。
    xiaomin = Boy('小明', 120, 30)
    xiaowang = Boy('小王', 130, 32)
    xiaomin.grow_height(5)
    xiaomin.grow_weight(1)
    xiaomin.show_height()
    xiaomin.show_weight()
    xiaomin.pee()
    xiaomin.show_weight()
    # REMIND 这里实例化两个男孩，原因是模拟需要多实例，模拟每个对象的属性是互不干扰的，小明增长体重不会影响到小王的体重。
    # REMIND 如果是使用全局变量 + 函数 或者类名加静态属性（类属性），则会发生互相干扰，正因为这样行不通再加上不使用oop面向对象，就会造成需要写成在一组函数中频繁return和传参，实现上复杂曲折，也不好读懂。这种写法现象在可预订平台的酒店价格解析里面体现得十分之严重，由于多个函数中频繁传参和return，有的参数命名是同一个东西，但是在各个函数中形参的名字取得又不一样，不仅在维护代码时候难以搞懂，在实现的时候也是麻烦曲折很多。
    print('— ' * 30)
    xiaowang.show_height()
    xiaowang.show_weight()
    xiaowang.grow_height(6)
    xiaowang.grow_weight(2)
    xiaowang.show_height()
    xiaowang.show_weight()
    xiaowang.pee()
    xiaowang.show_weight()

    print('* ' * 30)
    xiaohong = Boy('小红', 110, 25)
    xiaohong.grow_height(3)
    xiaohong.grow_weight(0.5)
    xiaohong.show_height()
    xiaohong.show_weight()
    xiaohong.pee()
    xiaohong.show_weight()

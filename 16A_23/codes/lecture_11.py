"元组"
"""
一个元 组 是 内 置 tuple类 型 的一个 实 例，是一个不可变序列。元组由逗号隔开元素表达式的元组文字来创建。任何对象都可以放在元组中。
"""
# ------------

"字典"
"""
字典是Python的内置数据类型，用于存储和操作相对应的关系。字典包括键值对(key-value)
其中键和值都是对象，字典的目的就是为存储和检索值提供抽象,这些值不是由连续的整数索引，而是由描述性的键索引

tips:
    字典的键不能包含可变值
    对与给定的键，最多只能有一个对应的值
    
"""
def withdraaw(balance):
    def withdraaw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance -= amount
        return balance
    return withdraaw

# 抽象层次
"""
This is called the abstraction barrier!

In fact, interacting within an ADT outside of its interface of constructors and selectors is called "violating the abstraction barrier" and is strongly discouraged (even when it doesn't produce an error).

In this way, data abstraction mimics how we think about the world. For example, a car is a complicated machine, but it has a simple interface by which we interact with it: the wheel, the gas pedal, the gear shift. If you want to drive a car, you don't need to know how the engine was built or what kind of material the tires are made of. It's easy to drive a car because of the suppression of complexity that abstraction provides us.

For the car, the principle of the abstraction barrier also applies. If we want to start the car, we should use the provided interface of turning the ignition key, rather than getting out, popping the hood, and messing around with the engine. While you could likely do that if you had enough knowledge, it is unnecessarily costly and highly dependent on how exactly the car was constructed. What are you going to do if the car is electric?
"""

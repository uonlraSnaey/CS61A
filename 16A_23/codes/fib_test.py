from fib import fib
import pytest


def fib_test():
    assert fib(2) == 1, '第二个斐波那契数应该是 1'
    assert fib(3) == 1, '第三个斐波那契数应该是 1'
    assert fib(4) == 2, '在第五十个斐波那契数发生 Error'
    assert fib(50) == 7778742049, '在第五十个斐波那契数发生 Error'

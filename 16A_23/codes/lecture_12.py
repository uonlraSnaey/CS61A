def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return "Invalid Value"
        balance = balance - amount # balance 属于withdraw() 外部的 make_withdraw() 函数的变量， 默认情况下无法修改
        # 可以通过添加 关键字 nonlocal(非局部的) 来声明其为非局部变量
        return balance
    return withdraw

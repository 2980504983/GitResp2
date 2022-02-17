def verify_permissions(func):
    def wrapper(*args, **kwargs):
        print("权限验证")
        return func(*args, **kwargs)
    return wrapper


@verify_permissions
def deposit(money):
    print("存钱")


@verify_permissions
def withdraw(login_id, pwd):
    print("取钱咯")


deposit(1000)
withdraw("zs0", 122)



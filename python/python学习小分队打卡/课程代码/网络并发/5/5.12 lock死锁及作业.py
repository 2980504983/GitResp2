"""
    线程锁Lock(和event一样，是实现同步互斥机制的手段之一):
        from threading import Lock

        lock = Lock()  创建锁对象
        lock.acquire()  上锁 (如果lock已经上锁在调用会阻塞)
        lock.release()  解锁 ()

        with lock: 上锁
            代码段(代码段结束，自动解锁)

        注: 上锁要在每个操作共享内存处都上锁，不然没用

    死锁及其处理:
        1 定义:
            是指两个或两个以上的线程在执行过程中，由于竞争资源或者由于彼此通信而造成的一种阻塞
            现象，若无外力作用，它们都将无法推进下去，此时称系统处于死锁状态，或系统产生了死锁。
            (例如交换人质，一方说你先放了xxx, 另一方则不同意说，你先放了xxx于是两边就进入了一
            种阻塞状态，1线程想要2线程的资源，2线程刚好也想要1线程的资源，就形成的死锁)

        2 死锁产生的必要条件:
            1 互斥条件:
                一定要有锁
            2 情求和保持条件:
                线程已经保持了至少一个资源，还要请求其它资源
            3 不剥夺条件:
                锁在没有外力的情况下，不会解开，资源会一直保持
            4 环路等待条件:
                指在发生死锁时，必然存在一个，线程资源的环形链

        3 如何避免死锁:
            破坏死锁必要条件中的一个
"""


from time import sleep
from threading import Thread, Lock


# 交易类
class Account:
    def __init__(self, id_, balance, lock):
        self.id = id_  # 用户
        self.balance = balance  # 存款
        self.lock = lock  # 锁

    # 取钱
    def withdraw(self, amount):
        self.balance -= amount

    # 存钱
    def deposit(self, amount):
        self.balance += amount

    # 查看余额
    def get_balance(self):
        return self.balance


# 产生两个账户
Tom = Account("Tom", 5000, Lock())
Alex = Account("Alex", 8000, Lock())


# 模拟转账过程
def transfer(from_, to, amount):
    if from_.lock.acquire():  # 锁住自己的账户, 两线程同时运行，t1,t2都锁住了
        from_.withdraw(amount)  # 账户减少
        sleep(0.5)  # 停个0.5秒两线程上面的代码段都执行完了

        if to.lock.acquire():  # 对方账户上锁 ，这时t1想给t2上锁但是t2已经锁了，于是t1阻塞,同理t2也阻塞了，就死锁了
            to.deposit(amount)  # 对方账户加钱
            to.lock.release()  # 对方账户解锁
        from_.lock.release()  # 自己账户解锁
    print(f"{from_.id}给{to.id}转账{amount}")


t1 = Thread(target=transfer, args=(Tom, Alex, 2000))
t2 = Thread(target=transfer, args=(Alex, Tom, 2000))
t1.start()
t2.start()
t1.join()
t2.join()


class Passport:
    def __init__(self, serial, number):
        self.__serial = serial
        self.__number = number

    def compare(self, serial, number):
        return self.__serial == serial and self.__number == number


class Client:
    def __init__(self, name, balance, passport):
        self._name = name
        self._balance = balance
        self._passport = passport

    def __repr__(self):
        return f'<Client: {self._name}, balance: {self._balance}>'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            print('Name must be a string')
            return

        name = name.strip()

        if name == '':
            print('Name cannot be empty')
            return

        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        if not isinstance(name, str):
            print('Name must be a string')
            return

        name = name.strip()

        if name == '':
            print('Name cannot be empty')
            return

        self._name = name

    def get_balance(self):
        return self._balance

    def send_to(self, recipient, amount):
        if not isinstance(recipient, Client):
            print('Recipient is not a Client')
            return

        if self._balance >= amount:
            self._balance -= amount
            recipient._balance += amount

    def pay_for_maintenance(self):
        amount = 10
        if self._balance <= amount:
            print('Not enough money for maintenance')
            return
        self._balance -= amount


class VipClient(Client):
    def pay_for_maintenance(self):
        amount = 5
        if self._balance <= amount:
            print('Not enough money for maintenance')
            return
        self._balance -= amount


my_passport = Passport(serial='1234', number='567890')
me = Client('Nick', 100, my_passport)

friends_passport = Passport(serial='1234', number='098765')
friend = VipClient('Vasya', 200, friends_passport)

print(me)
print(friend)

me.send_to(friend, 50)

print(me.get_balance())
print(friend.get_balance())

me.set_name('Andreev Nikolai')
print(me)

me.name += ' Vladimirovich'
# me.name = me.name + ' Vladimirovich'
me.set_name(me.get_name() + ' Vladimirovich')

me.name = '            '
print(me)

me.pay_for_maintenance()
friend.pay_for_maintenance()

print(me)

friend._balance += 1000000
print(friend._balance)

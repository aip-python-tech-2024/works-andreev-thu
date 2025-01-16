class InvalidNameError(Exception):
    pass


class NotEnoughBalance(Exception):
    pass


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
            raise ValueError('Name must be a string')

        name = name.strip()

        if name == '':
            raise InvalidNameError('Name cannot be empty')

        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        if not isinstance(name, str):
            raise ValueError('Name must be a string')

        name = name.strip()

        if name == '':
            raise InvalidNameError('Name cannot be empty')

        self._name = name

    def get_balance(self):
        return self._balance

    def send_to(self, recipient, amount):
        if not isinstance(recipient, Client):
            raise ValueError('Recipient is not a Client')

        if self._balance >= amount:
            self._balance -= amount
            recipient._balance += amount
        else:
            raise NotEnoughBalance('Not enough balance for transaction')

    def pay_for_maintenance(self):
        amount = 10
        if self._balance <= amount:
            raise NotEnoughBalance('Not enough money for maintenance')
        self._balance -= amount


class VipClient(Client):
    def pay_for_maintenance(self):
        amount = 5
        if self._balance <= amount:
            raise NotEnoughBalance('Not enough money for maintenance')
        self._balance -= amount


my_passport = Passport(serial='1234', number='567890')
me = Client('Nick', 100, my_passport)

friends_passport = Passport(serial='1234', number='098765')
friend = VipClient('Vasya', 200, friends_passport)

print(me)
print(friend)

try:
    me.send_to(friend, 150)
except NotEnoughBalance as e:
    print('Not enough balance for operation:', e)

print(me.get_balance())
print(friend.get_balance())

me.set_name('Andreev Nikolai')
print(me)

me.name += ' Vladimirovich'
# me.name = me.name + ' Vladimirovich'
me.set_name(me.get_name() + ' Vladimirovich')

try:
    me.name = 5
    print(me)
except ValueError as e:
    print('Error while updating client\'s name:', e)
except InvalidNameError as e:
    print('Cannot update client\'s name:', e)

me.pay_for_maintenance()
friend.pay_for_maintenance()

print(me)

friend._balance += 1000000
print(friend._balance)

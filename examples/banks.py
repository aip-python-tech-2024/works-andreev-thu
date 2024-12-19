class Client:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    def __repr__(self):
        return f'<Client: {self.__name}, balance: {self.__balance}>'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            print('Name must be a string')
            return

        name = name.strip()

        if name == '':
            print('Name cannot be empty')
            return

        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if not isinstance(name, str):
            print('Name must be a string')
            return

        name = name.strip()

        if name == '':
            print('Name cannot be empty')
            return

        self.__name = name

    def get_balance(self):
        return self.__balance

    def send_to(self, recipient, amount):
        if not isinstance(recipient, Client):
            print('Recipient is not a Client')
            return

        if self.__balance >= amount:
            self.__balance -= amount
            recipient.__balance += amount


me = Client('Nick', 100)
friend = Client('Vasya', 200)

print(me)
print(friend)

me.send_to(friend, 150)

print(me.get_balance())
print(friend.get_balance())

me.set_name('Andreev Nikolai')
print(me)

me.name += ' Vladimirovich'
# me.name = me.name + ' Vladimirovich'
me.set_name(me.get_name() + ' Vladimirovich')

me.name = '            '
print(me)

class User:
    count = 0

    def __init__(self, user_id, nickname):
        self.user_id = user_id
        self.nickname = nickname
        User.count += 1

    def __repr__(self):
        return f'User({self.user_id}, {self.nickname})'


    def __eq__(self, other):
        return isinstance(other, User) and self.user_id == other.user_id and self.nickname == other.nickname


    def greet(self):
        print(f'Hello, {self.nickname}')


    @staticmethod
    def test():
        print('Test')


    @classmethod
    def print_counter(cls):
        print(f'Count of users: {cls.count}')


me = User(123456789, 'Bakasa')
print(me)
me.greet()

clone = User(123456789, 'Bakasa')
print(clone == 8)

# clone = me
# clone.nickname = 'Dewili'
# print(clone.nickname)
#
# print(me.nickname)

admin = User(1074584521, 'Alex')
admin.nickname = 'Alex'
print(admin.nickname)
admin.greet()

# print(len(dir(int)))
# print(dir(int))

print([me, admin])

print(User.count)
User.test()

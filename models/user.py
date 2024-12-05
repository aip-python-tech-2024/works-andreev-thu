import json


class User:
    def __init__(self, user_id, nickname):
        self.user_id = user_id
        self.nickname = nickname

    def __repr__(self):
        return f'User({self.user_id}, {self.nickname})'


    def __eq__(self, other):
        return isinstance(other, User) and self.user_id == other.user_id and self.nickname == other.nickname


    def greet(self):
        print(f'Hello, {self.nickname}')


    def save(self):
        data = {
            'user_id': self.user_id,
            'nickname': self.nickname,
        }

        with open(f'../users/{self.user_id}.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)


    @classmethod
    def load(cls, user_id):
        with open(f'../users/{user_id}.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            return cls(data['user_id'], data['nickname'])


me = User(123456789, 'Bakasa')
print(me)
me.greet()
me.save()

admin = User(1074584521, 'Alex')
print(admin.nickname)
admin.greet()

another_user = User.load(6416568464)
print(another_user)
another_user.greet()

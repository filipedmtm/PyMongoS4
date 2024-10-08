#Modelo de classe Users
class Users:
    type:str = 'email_sender'
    def __init__(self, nome: str, nickname: str, password: str, ):
        self.nome = nome
        self.nickname = nickname
        self.password = password

    def to_dict(self):
        return{
            'nickname': self.nickname,
            'nome': self.nome,
            'password': self.password
        }

    def __str__(self):
        return f"Nome: {self.nome}, Nickname: {self.nickname}, Password: {self.password}"

#Modelo de classe Messages
class Messages:
    def __init__(self, to, nickname, content, datetime):
        self.to = to
        self.nickname = nickname
        self.content = content
        self.datetime = datetime

    def to_dict(self):
        return {
            'nickname': self.nickname,
            'content': self.content,
            'datetime': self.datetime
        }
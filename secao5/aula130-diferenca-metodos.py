# method s @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (self, cls)

# Qualquer método que iremos utilizar self dentro do método é um método de INSTÂNCIA

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None
    
    def set_user(self, user):
        # setter
        self.user = user

    def set_password(self, password):
        # setter
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def log(msg):
        print('Log:', msg)

# c1 = Connection()
# c1.set_user('João')
# c1.set_user('123456')

c2 = Connection.create_with_auth('João', '123456')
print(Connection.log('Essa é a mensagem de log'))


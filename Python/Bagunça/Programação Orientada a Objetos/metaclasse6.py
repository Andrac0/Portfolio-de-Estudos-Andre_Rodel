class PessoaMeta(type):
    def __init__(cls, name, bases, dict):
        super().__init__(name, bases, dict)
        cls._instance_map = {}

    def __call__(cls, first_name, last_name):
        key = (first_name, last_name)
        if key not in cls._instance_map:
            new_instance = super().__call__(first_name, last_name)
            cls._instance_map[key] = new_instance
        return cls._instance_map[key]

class Pessoa(metaclass=PessoaMeta):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

pessoa1 = Pessoa("André", "Lima")
pessoa2 = Pessoa("André", "Lima")
pessoa3 = Pessoa("Naruto", "Uzumaki")

print(pessoa1)
print(pessoa2)
print(pessoa3)
print(pessoa1 is pessoa2)
print((pessoa3 is pessoa1) or (pessoa3 is pessoa2))
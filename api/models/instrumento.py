import json

class Instrumento:
    def __init__(self, name, tipo, valor):
        self.name = name
        self.tipo = tipo
        self.valor = valor

    def to_dict(self):
        return {
            "name": self.name,
            "tipo": self.tipo,
            "valor": self.valor
        }

    def to_json(self):
        return json.dumps(self.to_dict())
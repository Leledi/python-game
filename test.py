from random import choice

NOMI = "Mario", "Luici", "Laura", "Paola", "Andonio"
COGNOMI = "Rossi", "Verdi", "Bianchi", "Neri", "Bruno"

class Persona:
  def __init__(self, citta, nome, cognome):
    self.nome = nome
    self.cognome = cognome
    self.citta = citta

  def __str__(self):
    return "{} {} ({})".format(self.nome, self.cognome, self.citta.nome)

  def print_compaesani(self):
    for p in self.citta.persone:
      if p != self:
        print(p)

class Citta:
  def __init__(self, nome, numero_persone):
    self.nome = nome
    self.persone = [Persona(self, "Giovanni", "Bruno")]

    for i in range(numero_persone -1):
      self.persone.append(Persona(self, choice(NOMI), choice(COGNOMI)))

  def __str__(self):
    result = "{}:\n".format(self.nome)
    for persona in self.persone:
      result += "{}\n".format(persona)

    return result

reggio = Citta("Reggio", 10)
pinarella = Citta("Pinarella", 2)

tizio = reggio.persone[3]
print(tizio)

tizio.print_compaesani()

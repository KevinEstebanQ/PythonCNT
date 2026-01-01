#temperature = dict(Miami=72, Weston = 73, newyork = 54, Houston = 62, LosAngeles = 65, SanDiego = 68, Boston = 57, Chicago = 51)
#
#
#
#temperature = {key: round((((value - 32) * 5) / 9),2) for key, value in temperature.items()}
#for key in temperature:
#    print(f"{key}: {temperature.get(key)}")
#


#FtoC = lambda x: {key: round(((value - 32) * 5) / 9) for key, value in x.items()}
#newTemp = FtoC(temperature)
#print(newTemp)


#myfunc = lambda y: print(dict(map(lambda x: (x[0], round((((x[1]-32)*5)/9),2)), y.items())))
#myfunc(temperature)

#for key in temperature:
#    newTemp = round((((temperature.get(key)-32)*5)/9),2)
#    temperature.update({key:newTemp})
#    print(f"{key}: {temperature.get(key)} C")


class Spell:
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.get_description()

    def get_description(self):
        return 'No description'

    def execute(self):
        print(self.incantation)


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')


class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def get_description(self):
        return 'Causes the victim to become confused and befuddled.'


def study_spell(spell):
    print(spell)


# -----------------
# Execution Section
# -----------------

spell = Accio()
spell.execute()
study_spell(spell)
study_spell(Confundo())


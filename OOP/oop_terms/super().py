# super() is referrin to the super class or the class from which the child inherits
# it helps us to inherit attr of the paret class
# To do this you pass the parameters you want to inherit to the __init__ func and call super
# To do this we do super__init__(the attibutes we want to inherit)
# super side in child takes the self argument
# when using the super ignore the self attr

class Programmer:
    def __init__(self, username, years, language):
        self.username = username
        self.years = years
        self.language = language

    def describe_programmer(self):
        return f"{self.username} knows {self.language} and has {self.years}yrs experience"


class JuniorDeveloper(Programmer):
    def __init__(self, username, years, language, skill):
        super().__init__(username, years, language)
        self.skill = skill

    def technical_skills(self):
        return f"Welcome {self.username} you are a {self.skill} programmer"


junior_dev = JuniorDeveloper("narh", 1, "Python", 'Proficient')
print(junior_dev.technical_skills())
print(junior_dev.username)

# Multiple inheritance although good adds complexity to our code
# Mst programming lang avoids it

class Programmer:
    def __init__(self, username, years, language):
        self.username = username
        self.years = years
        self.language = language

    def describe_programmer(self):
        return f"{self.username} knows {self.language} and has {self.years}yrs experience"


class Origin:
    def __init__(self, country):
        self.country = country

    def get_country(self):
        return f"You are from {self.country}"


class JuniorDeveloper(Programmer, Origin):
    def __init__(self, username, years, language, country, skill):
        Programmer.__init__(self, username, years, language)
        Origin.__init__(self, country)
        self.skill = skill

    def technical_skills(self):
        return f"Welcome {self.username} you are a {self.skill} programmer"


junior_dev = JuniorDeveloper("narh", 1, "Python", 'Ghana', 'Proficient')
print(junior_dev.technical_skills())
print(junior_dev.get_country())

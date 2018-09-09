class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        """Initiate car class"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.reflection == True:
            return True
        else:
            return False

    def __str__(self):
        string = "{}, {} Typing, Reflection= {},First appeared in {}".format(self.name, self.typing, self.reflection,
                                                                            self.year)
        return string
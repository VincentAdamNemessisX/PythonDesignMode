class CharacterFactory:
    def __init__(self):
        self.characters = {}

    def get_character(self, character: str):
        if character not in self.characters:
            self.characters[character] = Character(character)
        return self.characters[character]


class Character:
    def __init__(self, character: str):
        self.character = character

    def __str__(self):
        return self.character

    def render(self, font: str):
        return f"Rendered {self.character} in {font}"


if __name__ == '__main__':
    factory = CharacterFactory()
    char = factory.get_character('a')
    print(char.render('Arial'))
    char = factory.get_character('b')
    print(char.render('Times New Roman'))
    char = factory.get_character('a')
    print(char.render('Comic Sans'))

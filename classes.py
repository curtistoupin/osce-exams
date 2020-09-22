import enum

class Language(enum.Enum):
    bilingual = 0
    english = 1
    french = 2

class TrainingCentre:
    instances = []

    def __init__(self, name, abbr):
        self.name = name
        self.abbr = abbr
        TrainingCentre.instances.append(self)

    @classmethod
    def get(cls, value):
        return [inst for inst in cls.instances if inst.abbr == value]

class Candidate:
    def __init__(self, id, first_name, last_name, language, training_centre):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.full_name = last_name + ', ' + first_name
        self.caps_name = last_name.upper() + ', ' + first_name
        self.language = language
        self.training_centre = training_centre
        
class Examiner:
    def __init__(self, title, first_name, last_name, language, bilingual, university):
        self.title = title
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = title + " " + first_name + " " + last_name
        self.language = language
        self.bilingual = bilingual
        self.university = university
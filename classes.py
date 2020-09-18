import enum
from string import *

class Language(enum.Enum):
    english = 0
    french = 1
    other = 2

class TrainingCentre:
    instances = []

    def __init__(self, name, abbr):
        self.name = name
        self.abbr = abbr
        TrainingCentre.instances.append(self)

    @classmethod
    def get(cls, value):
        return [inst for inst in cls.instances if inst.abbr == value]

queens = TrainingCentre("Queen's University", "QUEEN")
uottawa = TrainingCentre('University of Ottawa', 'OTT')

class Candidate:
    def __init__(self, id, first_name, last_name, language, training_centre, attempt_number, previous_examiners = None):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.full_name = last_name + ', ' + first_name
        self.caps_name = upper(last_name) + ', ' + first_name
        self.language = language
        self.training_centre = training_centre
        self.attempt = attempt_number
        self.previous_examiners = previous_examiners
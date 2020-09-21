from classes import *

import pandas

def split_name(full_name):
    name = full_name.split(', ')
    last_name = name[0]
    first_name = name[1].split(' ')[0]
    return ([first_name, last_name])

candidates_df = pandas.read_excel('Alpha Download.xlsx', sheet_name='Candidates')
print(candidates_df)

candidates = []

for index in candidates_df.index:
    candidate_name = candidates_df["Name"][index]
    candidate_name = split_name(candidate_name)
    candidate_id = candidates_df["Id"][index]
    candidate_centre = candidates_df["Training Centres"][index]
    candidate_language = candidates_df["Language"][index]
    if candidate_language == "E":
        candidate_language = Language.english
    else:
        candidate_language = Language.french
    candidates.append(Candidate(candidate_id,
                                candidate_name[0],
                                candidate_name[1],
                                candidate_language,
                                candidate_centre))



for i in candidates:
    print(i.caps_name, i.language.name)
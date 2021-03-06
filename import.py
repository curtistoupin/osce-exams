from classes import *

import pandas

def split_name(full_name):
    name = full_name.split(', ')
    last_name = name[0]
    first_name = name[1].split(' ')[0]
    return ([first_name, last_name])
    
def import_candidates(file_name):
    candidates_df = pandas.read_excel(file_name, sheet_name='Candidates')
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
    return(candidates)

def import_examiners(file_name):
    examiners_df = pandas.read_excel(file_name, sheet_name='Examiners')
    examiners = []
    for index in examiners_df.index:
        examiner_title = examiners_df["Title"][index]
        examiner_first = examiners_df["First Name"][index]
        examiner_last = examiners_df["Last Name"][index]
        examiner_university = examiners_df["University Affiliation"][index]
        examiner_language = examiners_df["Language Preference"][index]
        examiner_bilingual = True if examiners_df["Bilingual (Y/N)"][index] == "Y" else False
        if examiner_language == "E":
            examiner_language = Language.english
        else:
            examiner_language = Language.french
        examiners.append(Examiner(examiner_title,
                                   examiner_first,
                                   examiner_last,
                                   examiner_language,
                                   examiner_bilingual,
                                   examiner_university))
    return(examiners)
    
def import_conflicts(file_name,candidates,examiners):
    conflicts = []
    conflicts_df = pandas.read_excel(file_name, sheet_name='Conflicts')
    for col in conflicts_df:
        for row in conflicts_df[col]:
            if not pandas.isnull(row):
                conflicts.append(Conflict(examiner_by_name(examiners,col),candidate_by_name(candidates,row)))
    return(conflicts)

def candidate_by_name(candidates,name):
    return([candidate for candidate in candidates if candidate.full_name == name][0])
    
def examiner_by_name(examiners,name):
    return([examiner for examiner in examiners if examiner.full_name == name][0])
    
candidates = import_candidates('Alpha Download.xlsx')
examiners = import_examiners('CAM Download.xlsx')

print(import_conflicts('Conflicts.xlsx',candidates,examiners))


#import_candidates('Alpha Download.xlsx')
#import_examiners('CAM Download.xlsx')
#import_conflicts('Conflicts.xlsx')
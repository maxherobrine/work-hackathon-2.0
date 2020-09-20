from person_work_experience import other_experience
import json


def jsonCreate(dictExperience:dict, companies:list, category: str, answers: list):
    mainJson = {'q0': dictExperience.get('id'),
                'q1': category,
                'q2': dictExperience.pop(category),
                'q2d': dictExperience.pop('time'),
                'q3': other_experience(dictExperience.pop('profession'), dictExperience.pop('experience')),
                'q4': answers[0],
                'q5': companies,
                'q6': answers[1],
                'q7': answers[2],
                'q8': answers[3],
                'q9': answers[4],
                'q10': dictExperience.pop('search')
                }
    with open("jsons/" + dictExperience.pop('id') + ".json", "w", encoding="utf-8") as outfile:
        json.dump(mainJson, outfile, ensure_ascii=False)

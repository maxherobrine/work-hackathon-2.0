from person_work_experience import other_experience
import json


def jsonCreate(dictExperience: dict, category: str, answers: list):
    mainJson = {'q0': dictExperience.get('id'),
                'q1': category,
                'q2': dictExperience.pop(category),
                'q2d': dictExperience.pop('time'),
                'q3': other_experience(dictExperience.pop('profession'), dictExperience.pop('experience')),
                'q4': [],
                'q5': [],
                'q6': [],
                'q7': [],
                'q8': [],
                'q9': [],
                'q10': dictExperience.pop('search')
                }
    with open(dictExperience.pop('id') + ".json", "w", encoding="utf-8") as outfile:
        json.dump(mainJson, outfile, ensure_ascii=False)

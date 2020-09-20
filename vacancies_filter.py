from Read_Data import Person


def multiple_replace(target_str, replace_values:list):
    # получаем заменяемое: подставляемое из словаря в цикле
    for i in replace_values:
        # меняем все target_str на подставляемое
        target_str = target_str.replace(i, ' ')
    return target_str


def prepare_date_for_filter(person: Person):
    personDict = {}
    start = []
    end = []
    experiences = []
    for work in person.work_experience:
        start.append(work.start)
        end.append(work.end)
        experiences.append(work.position)
    personDict.update({'id': person.id, 'category': experiences, 'startDate': start, 'endDate': end})
    return personDict


def vacancies_filter(personInformation: dict, categorySynonyms: list):
    categories = []
    start = []
    end = []
    count = 0

    person = {'id': personInformation.get('id'), 'category': [], 'startDate': [],
              'endDate': []}
    for name in personInformation.get('category'):
        isSuitable = 0
        words = multiple_replace(name, ['-','"', ',',"'",'.'])
        words = words.split();
        for i in words:
            if isSuitable:
                break
            for synonym in categorySynonyms:
                if i == synonym:
                    categories.append(name)
                    start.append(personInformation.get('startDate')[count])
                    end.append(personInformation.get('endDate')[count])
                    isSuitable = 1
                    break
        count += 1
    if len(categories) != 0:
        person.update({'category': categories})
        person.update({'startDate': start})
        person.update({'endDate': end})
        return person
    elif len(person.get('category')) != 0:
        return person
    else:
        return 0

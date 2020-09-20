import datetime as DT


def person_work_experience(personInformation: dict, category: str):
    person = {'id': personInformation.get('id'), category: False, 'time': 0, 'profession': [], 'experience': [], 'search': []}
    count = 0
    works = []
    experience = []
    search = []
    searchDate = '1971-01-01'
    for name in personInformation.get('category'):
        if name == category:
            person.update({category: True})
            person.update({'time': calculate_work_time(personInformation.get('startDate')[count],
                                                       personInformation.get('endDate')[count])})
        else:
            works.append(name)
            experience.append(calculate_work_time(personInformation.get('startDate')[count],
                                                  personInformation.get('endDate')[
                                                      count]))  # Функция вычисление времени работы
        end = personInformation.get('endDate')[count] + '-01'
        if not personInformation.get('endDate')[count]:
            search = [0]
        elif not search and DT.datetime.strptime(searchDate, '%Y-%m-%d').date() < DT.datetime.strptime(end, '%Y-%m-%d').date():
                searchDate = end
        count += 1
    if not search:
        today = DT.datetime.today().strftime('%Y-%m-%d')
        dateDelta = DT.datetime.strptime(today, '%Y-%m-%d').date() - DT.datetime.strptime(searchDate, '%Y-%m-%d').date()
        search.append(int(dateDelta.days / 30))
    person.update({'profession': works, 'experience': experience, 'search': search})
    return person


def calculate_work_time(start: str, end: str):
    if not start and not end:
        return 0
    start += "-01"
    if not end:
        end = DT.datetime.today()
        end = end.strftime('%Y-%m-%d')
    else:
        end += "-01"
    startDate = DT.datetime.strptime(start, '%Y-%m-%d').date()
    endDate = DT.datetime.strptime(end, '%Y-%m-%d').date()
    delta = int((endDate - startDate).days / 30)
    return delta


def other_experience(profession:list, experience:list):
    size = len(profession)
    otherExp = {}
    for i in range(size):
        otherExp.update({profession[i]: experience[i]})

    return otherExp

import datetime as DT

'''
person1 = {'id': 12345, 'category': ['лол', 'инженер', 'технолог'],
           'startDate': ['2020-08-08', '2019-07-07', '2018-04-05'],
           'endDate': ['2021-08-08', '2020-01-07', '2018-06-05']}
person2 = {'id': 12345, 'category': ['кулинар', 'инженер', 'технолог'],
           'startDate': ['2020-08-08', '2019-07-07', '2018-04-05'],
           'endDate': ['2021-08-08', '2020-01-07', '2018-06-05']}

'''
'''
def person_work_experience(personInformation:dict, category:str):
    person = {'id':personInformation.get('id'), category: False, 'profession': [], 'experience': []}
    count = 0
    isChecked = 0
    for name in personInformation.get('category'):
        if name == category:
            person.update({category: True})
            experience = calculate_work_time(personInformation.get('startDate')[count], personInformation.get('endDate')[count])
            person.update({'experience': experience})
            isChecked = 1
        count+=1
    if not isChecked:
        count = 0
        works = []
        experience = []
        for name in personInformation.get('category'):
            works.append(name)
            experience.append(calculate_work_time(personInformation.get('startDate')[count], personInformation.get('endDate')[count])) #Функция вычисление времени работы
            count+=1
        person.update({'profession': works, 'experience': experience})
    return  person
'''


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


'''
print(person_work_experience(person1, 'лол'))
print(person_work_experience(person2, 'лол'))
'''


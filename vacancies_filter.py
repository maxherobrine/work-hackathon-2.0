import string
'''
testlist = ['кладовщик', 'комплектовщик', 'грузчик', 'старший кладовщик', 'склада', 'складом']
person1 = {'id': 123456789, 'category': ['комплектовщик', 'кладовщик'], 'startDate': ["19.02.2012", "18.09.2020"],
           'endDate': ["12.01.2020", "18.09.2022"]}
person2 = {'id': 223456789, 'category': ['менеджер склада'], 'startDate': ["19.02.2012"], 'endDate': ["12.01.2020"]}
person3 = {'id': 323456789, 'category': ['заведующий складом'], 'startDate': ["19.02.2012"], 'endDate': ["12.01.2020"]}
person4 = {'id': 423456789, 'category': ['кладовщик-техник'], 'startDate': ["19.02.2012"], 'endDate': ["12.01.2020"]}
person5 = {'id': 523456789, 'category': ['официант'], 'startDate': ["19.02.2012"], 'endDate': ["12.01.2020"]}
'''

def vacancies_filter(personInformation: dict, category: string, categorySynonyms: list):
    isSuitable = 0
    categories = []
    start = []
    end = []
    count = 0

    person = {'id': personInformation.get('id'), 'category': [], 'startDate': [],
              'endDate': []}
    #if personInformation.get('category') == category:
        #person.update({'category': category})
   # else:
    for name in personInformation.get('category'):
        isSuitable = 0
        words = name.replace('-', ' ').split();
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

'''
print(vacancies_filter(person1, 'комплектовщик', testlist))
print(vacancies_filter(person2, 'комплектовщик', testlist))
print(vacancies_filter(person3, 'комплектовщик', testlist))
print(vacancies_filter(person4, 'комплектовщик', testlist))
print(vacancies_filter(person5, 'комплектовщик', testlist))
'''
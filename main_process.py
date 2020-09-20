import csv
from Read_Data import Person
import vacancies_filter
from person_work_experience import person_work_experience
from read_file_to_list import read_file_to_list
from searchBySentence import search


# main program
# вопросы с поиском для модели Кладовщик: q4, q6, q7, q8, q9
storekeeperQuestions = [
    ['отрасль', 'область работы', 'сфера деятельности', 'у ', 'компания'],
    ['система хранения', {'адресная': ['статическая', 'динамическая']}, 'стеллажная'],
    ['программа', 'программное обеспечение', '1с'],
    ['инструментарий', 'оборудование', 'инвентарь'],
    [{'работ': ['тип', 'вид', 'характер']}, 'занимался', 'выполнял', 'задание', 'деятельность', 'обязанности']
]

with open("resume_sorted.csv", encoding="utf-8") as table:
    reader = csv.DictReader(table, delimiter=";")
    person = Person()
    synonyms = read_file_to_list("synonyms.txt")
    category = "кладовщик"
    cout = 0
    for row in reader:
        if not person.is_equal(list(row.values())[0]):
            personDict = vacancies_filter.prepare_date_for_filter(person)
            personDict = vacancies_filter.vacancies_filter(personDict, synonyms)
            if personDict:
                cout += 1
                personDict = person_work_experience(personDict, category)
                #print(personDict)

                description = ''
                for work in person.work_experience:
                    description += work.description
                for question in storekeeperQuestions:
                    print(search(description, question))

        person.fill([x.lower() for x in list(row.values())])
    #print(cout)

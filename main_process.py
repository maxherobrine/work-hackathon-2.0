import csv
from Read_Data import Person
import vacancies_filter
from person_work_experience import person_work_experience
from read_file_to_list import read_file_to_list

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
        person.fill([x.lower() for x in list(row.values())])
    #print(cout)

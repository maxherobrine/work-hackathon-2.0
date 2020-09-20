import csv

rows = []


def sort_first_elem(array):
    return array[0]


# with open("resume_to_hackaton .csv") as resume_csv:
#     csv_reader = csv.DictReader(resume_csv, delimiter=";")
#     line_count = 0
#     i = 0
#     for row in csv_reader:
#         rows.append(list(row.values()))
#     rows.sort(key=sort_first_elem)
#     with open("resume_sorted.csv", "w") as f:
#         for i in range(len(rows)):
#             for j in range(len(row)):
#                 f.write('"')
#                 f.write(rows[i][j].replace('"', '""'))
#                 f.write('"')
#                 f.write(";")
#             f.write("\n")


class Work:
    def __init__(self):
        pass

    position = ""
    organization = ""
    description = ""
    start = ""
    end = ""

    def __str__(self):
        return "position {}, organization {}, description\n {}, \nstart {}, end {}".format(self.position,
                                                                                           self.organization,
                                                                                           self.description, self.start,
                                                                                           self.end)


class Person:
    def __init__(self):
        pass

    id = ""
    work_experience = []

    def feel(self, information):
        if self.id != information[0]:
            self.work_experience.clear()
            self.id = information[0]
        work = Work()
        work.position = information[1]
        work.organization = information[2]
        work.description = information[3]
        work.start = information[4]
        work.end = information[5]
        self.work_experience.append(work)

    def is_equal(self, id):
        return self.id == id

    def __str__(self):
        str = self.id
        for work in self.work_experience:
            str += "\n" + work.__str__() + '\n'
        return str


def do_smth(person__):
    print(person__)


"""with open("resume_sorted.csv", "r", encoding='utf-8') as table:
    reader = csv.DictReader(table, delimiter=";")
    person = Person()
    for row in reader:
        if not person.is_equal(list(row.values())[0]):
            do_smth(person)
        person.feel(list(row.values()))"""

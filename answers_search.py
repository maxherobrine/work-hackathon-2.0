from googletrans import Translator
from deeppavlov import build_model, configs
from split_text import split_text

import os

os.environ["CUDA_VISIBLE_DEVICES"]="3"

questions = {'q4': "which field or industry or sphere?", 'q6': "which warehouse placement system?",
             'q7': "which programms do you work with?", 'q8': "which instruments do you use or work with?",
             'q9': "which tasks did you do?"}

path_to_programms = "programms.txt"
path_to_storageSystem = "storagesystem.txt"

model = build_model(configs.squad.squad, download=True)


def read_QA_data(path):
    try:
        file = open(path, "r", encoding="utf-8")
        data = file.read().split(',')
        return data
    except IOError:
        print("An IOError has occurred with" + path)
        return None
    finally:
        file.close()


def Translate(str, l_from, l_to):
    translator = Translator()
    result = translator.translate(str, src=l_from, dest=l_to)
    return result.text


def QA_answer(question_id, sourse_text: list):
    if len(sourse_text) == 0:
        return []
    answer = []
    if question_id == 'q7':
        data = read_QA_data(path_to_programms)
        if data is None:
            return answer
        for elem in data:
            for string in sourse_text:
                if len(string) == 0:
                    continue
                if elem in string:
                    answer.append(elem)
        return answer
    elif question_id == 'q6':
        data = read_QA_data(path_to_storageSystem)
        if data is None:
            return answer
        for elem in data:
            for string in sourse_text:
                if len(string) == 0:
                    continue
                if elem in string:
                    start_index = string.find(elem)
                    end_index = start_index
                    while start_index > 0 and string[start_index].isalpha():
                        start_index = start_index - 1
                    while end_index < len(string) and string[end_index].isalpha():
                        end_index = end_index + 1
                    start_index = start_index + 1
                    answer.append(string[start_index:end_index])
        return answer
    else:
        q = questions.get(question_id)
        for string in sourse_text:
            if len(string) == 0:
                continue
            # text = Translate(string, 'ru', 'en')
            a = model([string], [q])[0][0]
            if not a == "I don't know":
                answer.append(a)
        return answer


def find_aswers(text):
    q_aswers = []
    for q in questions.keys():
        arr_str = []
        tmp_arr = split_text(text)
        for tmp in tmp_arr:
            arr_str += tmp.split('\n')
        arr_str.remove('')
        q_aswers.append(QA_answer(q, arr_str))
    return q_aswers

# resource1 = "-Организация  и контроль по приему и отпуску ТМЦ. -Организация и контроль  перемещение ТМЦ на места " \
#             "хранения.  - Организация работы склада( штат сотрудников 13 чел.-грузчики,вод.погрузчиков,кладовщики. " \
#             "-Ведение учета ТМЦ на складе и соблюдение норм и правил  сохранности. -Слежение за соблюдением сроков " \
#             "реализации ТМЦ. - Видение складской документации и отчеты в 1С.  -Проведение инвентаризации. -погрузка " \
#             "вагонов, контейнер,автомашин. -Ведение участка фасовки ветонита, песка и щебня.( сдельн.бригада 15 чел.) "
# resource1 = resource1.lower()
# question = "q4"
# print(QA_answer(question, [resource1]))
#
# resource2 = "Должностные обязанности и достижения: - планирование работы менеджеров по продажам - выполнение плана " \
#             "продаж - отчетность - Обеспечение работы склада;  - Организация и контроль отгрузки реализованных " \
#             "запасных частей;  - Организация и контроль за возвратом запасных частей;  - Контроль документооборота; " \
#             "Выявление ошибок и разночтений;  - Проведение инвентаризаций на складе;  - Управление деятельностью " \
#             "подчиненных сотрудников (10 человек);  - организована работа склада с ""0"";  - внедрена адресная " \
#             "система хранения товара и система штрих-кодирования;  - установлена IP - система видеонаблюдения;  - " \
#             "разработаны и внедрены должностные инструкции для сотрудников склада, оптимизирована их работа; - " \
#             "значительно расширена клиентская база "
# resource2 = resource2.lower()
# question = "q4"
# print(QA_answer(question, [resource2, resource1]))

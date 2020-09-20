from googletrans import Translator
from deeppavlov import build_model, configs

questions = {'q4' : "which field or industry?", 'q6' : "which warehouse placement system?", 'q7' : "which programms do you work with?", 'q8' : "which instruments do you use or work with?"}

path_to_programms = "programms.txt"
path_to_storageSystem = "storagesystem.txt"

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
    result = translator.translate(str,src=l_from,dest=l_to)
    return result.text

def QA_answer(question_id, sourse_text):
    answer = []
    if question_id == 'q7':
        data = read_QA_data(path_to_programms)
        if data is None:
            return None
        for elem in data:
            if elem in sourse_text:
                answer.append(elem)

    elif question_id == 'q6':
        data = read_QA_data(path_to_storageSystem)
        if data is None:
            return None
        for elem in data:
            if elem in sourse_text:
                start_index = sourse_text.find(elem)
                end_index = start_index
                while sourse_text[start_index].isalpha():
                    start_index = start_index - 1
                while sourse_text[end_index].isalpha():
                    end_index = end_index + 1
                start_index = start_index + 1
                answer.append( sourse_text[start_index:end_index] )

    q = questions.get(question_id)
    text = Translate(sourse_text,'ru','en')
    model = build_model(configs.squad.squad, download=True) #(?) я не знаю, как это работает, потому что у мен либа не устанавливается
    a = model([text],[q])
    if not a == "I don't know":
        answer.append(Translate(a,'en','ru'))
        return answer
    else:
        return None



# resource1 = "-Организация  и контроль по приему и отпуску ТМЦ. -Организация и контроль  перемещение ТМЦ на места хранения.  - Организация работы склада( штат сотрудников 13 чел.-грузчики,вод.погрузчиков,кладовщики. -Ведение учета ТМЦ на складе и соблюдение норм и правил  сохранности. -Слежение за соблюдением сроков реализации ТМЦ. - Видение складской документации и отчеты в 1С.  -Проведение инвентаризации. -погрузка вагонов, контейнер,автомашин. -Ведение участка фасовки ветонита, песка и щебня.( сдельн.бригада 15 чел.)"
# resource1 = resource1.lower()
# question = "q7"
# print(QA_answer(question,resource1))
#
# resource2 = "Должностные обязанности и достижения: - планирование работы менеджеров по продажам - выполнение плана продаж - отчетность - Обеспечение работы склада;  - Организация и контроль отгрузки реализованных запасных частей;  - Организация и контроль за возвратом запасных частей;  - Контроль документооборота; Выявление ошибок и разночтений;  - Проведение инвентаризаций на складе;  - Управление деятельностью подчиненных сотрудников (10 человек);  - организована работа склада с ""0"";  - внедрена адресная система хранения товара и система штрих-кодирования;  - установлена IP - система видеонаблюдения;  - разработаны и внедрены должностные инструкции для сотрудников склада, оптимизирована их работа; - значительно расширена клиентская база"
# resource2 = resource2.lower()
# question = "q6"
# print(QA_answer(question,resource2))

# /\
# |  Работает)))
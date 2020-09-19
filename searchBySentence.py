from fuzzysearch import find_near_matches
import re


def search(description: str, question: list):
    # description разбить на список предложений
    split_regex = re.compile(r'[.!?…]')
    sentences = [t for t in split_regex.split(description)]
    resultSentences = []

    for keyword in question:
        if type(keyword) != dict:
            for sentence in sentences:
                if find_near_matches(keyword, sentence, max_l_dist=2, max_deletions=5, max_insertions=1,
                                     max_substitutions=0) and sentence not in resultSentences:
                    resultSentences.append(sentence)
        else:
            synonym = list(keyword.keys())[0]
            addWords = list(keyword.values())[0]
            for word in addWords:
                for sentence in sentences:
                    if find_near_matches(synonym + word, sentence, max_l_dist=2, max_deletions=4, max_insertions=2,
                                         max_substitutions=0) and sentence not in resultSentences:
                        resultSentences.append(sentence)

    print(resultSentences)
    return resultSentences


search('''-Погрузка, выгрузка товара.
 -Выполнение подсобных и вспомогательных работ на производственных участках и складах.
 -Загрузка вендинговых аппаратов.''',
       [{'работ': ['тип', 'вид', 'характер']}, 'занимался', 'выполнял', 'задание', 'деятельность', 'обязанности'])

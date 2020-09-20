from fuzzysearch import find_near_matches
from split_text import split_text


def search(description: str, question: list):
    # description разбивается на список предложений
    sentences = list(filter(None, split_text(description)))
    lowerSentences = []
    for sentence in sentences:
        lowerSentences.append(sentence.lower())
    resultSentences = []

    for keyword in question:
        if type(keyword) != dict:
            if len(keyword) < 5:
                max_l_dist = 0
                max_deletions = 0
                max_insertions = 0
                max_substitutions = 0
            else:
                max_l_dist = 2
                max_deletions = 4
                max_insertions = 1
                max_substitutions = 0
            for sentence in lowerSentences:
                if find_near_matches(keyword, sentence, max_l_dist=max_l_dist, max_deletions=max_deletions,
                                     max_insertions=max_insertions, max_substitutions=max_substitutions) and sentence not in resultSentences:
                    resultSentences.append(sentence)
        else:
            synonym = list(keyword.keys())[0]
            addWords = list(keyword.values())[0]
            for word in addWords:
                for sentence in lowerSentences:
                    if find_near_matches(synonym + word, sentence, max_l_dist=2, max_deletions=4, max_insertions=2,
                                         max_substitutions=0) and sentence not in resultSentences:
                        resultSentences.append(sentence)

    # print(resultSentences)
    return resultSentences

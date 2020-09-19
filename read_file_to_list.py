def read_file_to_list(file:str):
    f = open(file, "r+", encoding="utf-8")
    words = (f.read())
    words = words.replace('\n', '').split(',')
    f.close()
    return words



'''read_file_to_list("synonyms.txt")'''
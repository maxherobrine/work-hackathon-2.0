def read_file_to_list(file:str):
    f = open(file, "r+", encoding="utf-8")
    synonyms = (f.read())
    synonyms = synonyms.replace('\n', '').split(',')
    print(synonyms)
    f.close()

'''read_file_to_list("synonyms.txt")'''
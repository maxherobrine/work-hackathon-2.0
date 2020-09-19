#%%
from googletrans import Translator
from deeppavlov import build_model, configs

def Translate(str, l_from, l_to):
    translator = Translator()
    result = translator.translate(str,src=l_from,dest=l_to)
    return result.text

questions = {'q4' : "which field or industry?", 'q6' : "which warehouse placement system?", 'q7' : "which programms do you work with?", 'q8' : "which instruments do you use or work with?"}

def QA_deeppavlov_eng(question_id, sourse_text):
    q = questions.get(question_id)
    text = Translate(sourse_text,'ru','en')
    model = build_model(configs.squad.squad, download=True) #(?) я не знаю, как это работает, потому что у мен либа не устанавливается
    a = model([text],[q])
    if not a == "I don't know":
        a = Translate(a,'en','ru')
        return a
    else:
        return None
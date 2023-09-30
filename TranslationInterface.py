import Letter_Translation
import HandSpeak_Translation
import ASL_LEX_Translation
import New_Handspeak

def TranslationInterface(root, input, output, text):
    if (str(output) == "0"):
        if(str(input) == "1"):
            t = Translate_Letter(root, text)
        else:
            t = Translate_letter(text)
        return t
    elif (str(output) == "1"):
        Translate_ASL_LEX(text)
        return text
    elif (str(output) == "2"):
        Translate_New_HandSpeak(text)
        return text
    elif (str(output) == "3"):
        print("using videos")
        if (str(input) == "1"):
            t = Translate_Videos(root, text)
        else:
            t = Translate_Video(text)
        return t
    elif(str(output) == "4"):
        t = text.split()
        print(t)
        return t
    else:
        print("Invalid output method")

def Translate_Letter(root, text):
    new_text = text + ' '
    list = Letter_Translation.Make_List(root, new_text)
    return list

def Translate_letter(text):
    new_text = text + ' '
    list = Letter_Translation.Make_list(new_text)
    return list

def Translate_Videos(root, text):
    new_text = text + ' '
    list = Letter_Translation.Make_List(root, new_text)
    return list

def Translate_Video(text):
    new_text = text + ' '
    list = Letter_Translation.Make_list(new_text)
    return list


def Translate_HandSpeak(text):
    HandSpeak_Translation.Translate(text)

def Translate_ASL_LEX(text):
    altered = text.lower()
    altered2 = altered.split()
    for input in altered2:
        ASL_LEX_Translation.ASL_lex_search(input)

def Translate_New_HandSpeak(text):
    altered = text.split()
    for input in altered:
        New_Handspeak.Handspeak_search(input)
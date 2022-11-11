def get_count_char(str_):
    list_=str_.lower().split()
    delimiter = ''
    str_=delimiter.join(list_)
    dict={}
    for i in range(len(str_)):
        if str_[i].isalpha()==True:
            if dict.get(str_[i])==None:
                dict[str_[i]]= 1
            else:
                dict[str_[i]] = dict.get(str_[i])+1
    return dict
def get_percent(dictionary):
    n=len(dictionary)
    for key in dictionary:
        dictionary[key] = dictionary.get(key)/n
    return dictionary
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
a1=get_count_char(main_str)
print(a1)
a2=get_percent(a1)
print(a2)

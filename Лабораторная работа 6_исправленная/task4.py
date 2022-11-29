import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(INPUT_FILE,delimiter=",", new_line="\n"):
    f = open(INPUT_FILE, "r")
    listin=f.read()
    listin=listin.split(new_line)
    column=listin[0].split(delimiter)
    size=len(listin)
    list=[]
    dict={}
    for i in range(1,size):
        dict.clear()
        value=listin[i].split(delimiter)
        for j in range(len(column)):
            dict[column[j]]=value[j]
        list.append(dict.copy())
    return(list)
    f.close()


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

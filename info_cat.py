import os
from pathlib import Path
os.system('cls')

def get_cats_info(path):
    cat_info_list=list()
    with open(path,'r',encoding='utf-8') as file:
        for cat in file.readlines():
            id,name,age=cat.split(',')[0],cat.split(',')[1],cat.split(',')[2]
            id=cat.split(',')[0]
            age=age.replace('\n','')
            cat_list={'id':id,"name":name,"age":age}
            cat_info_list.append(cat_list)
    return cat_info_list

p=Path('cat_list.txt')

try:

    cats_info=get_cats_info(p)
    for info in cats_info:
        print(info, end='\n\n')

except OSError as err:
    print("OS error:", err)
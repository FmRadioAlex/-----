import os
from pathlib import Path
os.system('cls')

def total_salary(path):
    job_person=0
    total=0
    with open(path,'r', encoding="utf-8") as file:      #Відкриваємо файл по шляху path(list_name.txt) 
        # for text_list in file.readlines():
        #     cash=text_list.split(',')[1]              #як так та чому
        #     print(cash)
        # file.seek(0)
        text=(file.read()).replace('\n',',')            #Зчитуємо з файла все що є, а після цього шукаємо усі \n та заміняємо через функцію replace на ','
        cash=text.split(',')                            #Робимо список який розділяє слова(символи.строчки) що перед комою та після
        # print(cash)            #test_list        
        for number in cash:                             #Перебираємо кожний елемент списка  
            if number.isdigit():                        #Перевіряємо чи є даний елемент списка числом
                total += int(number)                    #Якщо так ми сумуєммо 
                job_person +=1                          #Та робимо счетчік на кількість людей
    
    return total, job_person                            # повертаємо загальну сумму та кількість роботніків які отримують гроші


p=Path('list_name.txt')                                 #list_name.txt

try:
    total, average = total_salary(p)
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата({average}): {(total/average)}")

except OSError as err:
    print("OS error:", err)






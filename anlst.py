import pandas as pd
import random
import time

#==================================================================================#
dataset = pd.read_csv('C:\\Users\\MFN\\Desktop\\cybGARD\\Users\\0.csv', delimiter=';')
dataset2 = pd.read_csv('C:\\Users\\MFN\\Desktop\\cybGARD\\Users\\1.csv', delimiter=';')
#==================================================================================#
sovpad_prod00=[] #Совпадающие покупки у юзеров
nesov_prod1=[] #Несовпадающие покупки у 1 юзера с 2(рекомендации для 2)
nesov_prod2=[] #Несовпадающие покупки у 2 юзера с 1(рекомендации для 1)
count_od_prod=0
dataset.items()
#==================================================================================#
def sovpad_product():   ####ГОТОВ####
    for i in range(len(dataset)) :
        for j in range(len(dataset2)):
            if dataset['ProductName'][i]==dataset2['ProductName'][j]:
                sovpad_prod00.append(dataset['ProductName'][i])
                sovpad_prod00.append(dataset2['ProductName'][j])
#==================================================================================#
def nesovpad_prod1_so2(): #рекомендательный массив для 2 пользователя
    for i in range(len(dataset)) :
        for j in range(len(dataset2)):
            try:
                if dataset['ProductName'][i]!=dataset2['ProductName'][j]:
                    nesov_prod1.append(dataset['ProductName'][j])
            except:
                continue
#==================================================================================#
def nesovpad_prod2_so1(): #рекомендательный массив для 1 пользователя
    for i in range(len(dataset2)) :
        for j in range(len(dataset)):
            try:
                if dataset2['ProductName'][j]!=dataset['ProductName'][i]:
                    nesov_prod2.append(dataset2['ProductName'][i])
            except:
                continue
#==================================================================================#
sovpad_product() #Функция нахождения одинаковых покупок 
nesovpad_prod1_so2() #Функция определения рекомендаций для 2 юзера 
nesovpad_prod2_so1() #Функция определения рекомендаций для 1 юзера    
#==============================================================#удаление дубликатов
#удаление дубликатов 
sovpad_prod01 = list(dict.fromkeys(sovpad_prod00))
nesov_prod01 = list(dict.fromkeys(nesov_prod1))
nesov_prod02 = list(dict.fromkeys(nesov_prod2))
#==================================================================================#
#Подсчёт кол-ва одинаковых товаров
for i in range(len(sovpad_prod01)):
    count_od_prod+=1
#==================================================================================#
while True:
    print('Кол-во совпадающих продуктов', count_od_prod)
    for i in range(len(nesov_prod01)):
        random_index = random.randrange(len(nesov_prod01))
        print("Рекомендуем к покупке:", nesov_prod01[random_index]) 
        time.sleep(6)


    for i in range(len(nesov_prod02)):
        random_index = random.randrange(len(nesov_prod02))
        print("Рекомендуем к покупке:", nesov_prod02[random_index]) 
        time.sleep(5)

    print('Кол-во совпадающих продуктов', count_od_prod)

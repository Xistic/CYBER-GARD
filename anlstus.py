#==========( Краткая статистика для 0 юзера )===============#
import pandas as pd
import collections
#===========================================================#
dataset = pd.read_csv('C:\\Users\\MFN\\Desktop\\cybGARD\\Users\\0.csv', delimiter=';')
dataset.items()
check_count=0 #кол-во чеков
chastota=[]
#===========================================================#
for i in range(len(dataset)) :
    check_count+=1
    chastota.append(dataset['ProductName'][i])
#===========================================================#
def CountFrequency(arr):
    return collections.Counter(arr)  

print("Кол-во чеков: ", check_count)
if __name__ == "__main__":
    freq = CountFrequency(chastota)
    for key, value in freq.items():
        print (key, " -> ", value)
#===========================================================#


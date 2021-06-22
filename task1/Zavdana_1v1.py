import re

string1 = input ("Введіть рядок -> ")
print ("Введений рядок -> " + string1) # Вводимо рядок символів

numbers = re.findall(r"\d+", string1)
numbers=[int(i) for i in numbers] # Знаходимо всі числа із рядка


string1=re.findall("\D", string1)
string2="".join(string1) # Знаходимо всі слова із рядка


print("Числа із рядка: " , numbers)
print ('Рядок без чисел : ', string2)

def capitalize(string2):
     string2, result = string2.title(), ""
     for word in string2.split():
        result += word[:-1] + word[-1].upper() + " "
     return result[:-1]     
print ("Слова з великими першою та останньою буквами : ", capitalize(string2)) # Заміняємо першу та останню букви слів великими 


max_num=max(numbers)
print("Максимальное число: ", max_num) #  Знаходимо максимальне число

numbers_index = []
for i in range(len(numbers)):
            x=numbers[i]
            if(x!= max_num):
                numbers_index.append(x**i)
            else:
                continue
print ("Числа піднесенні до степеня: ", numbers_index) # Підносимо всі числа, крім максимально,до степеня по їх індексу
 

name = input("Как тебя зовут?: ")
familia = input("Фамилия?: ")
age = int(input("Сколько ьебе лет?: "))
hobbi = input("Чем ты занимаешься?: ")
result = name + ' ' + familia + ' ' + "ты занимаешься " + hobbi + "тебе" + str(age) + " лет"
print(result)
if age == 16:
    print("Ты учишься в 10м классе")
    if age <16:
        print ("Ты учишься в средней школе")
elif age == 24:
    print ("Да ты здоровяк")
else:
    print("ты уже закончил школу")
print ("Я все о тебе узнал")

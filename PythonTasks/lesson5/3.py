marks = input("Введите оценки через пробел: ")
five = marks.count("5")
SumM = marks.count("5")+ marks.count("4")+ marks.count("3")+ marks.count("2")
print("Процент пятёрок: "+ str(five/SumM*100))
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
#  Петя помогает Кате по математике. Он задумывает два натуральных 
# числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S 
# и их произведение P. Помогите Кате отгадать задуманные 
# Петей числа.4 4 -> 2 2  5 6 -> 2
s = int(input("Введите сумму чисел "))
p = int(input("Введите произведение чисел "))
for x in range(1,1001):
    y = s - x
    if (x <s) and (x * y == p):
        print(x,y)
        break
    

















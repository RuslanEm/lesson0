#Задача «Длина слова».
#Описание: Запишите в переменную a произвольную строку. Затем вычислите длину строки и выведите результат на экран(в консоль).
# для решения вам может пригодиться функция len(), которая позволяет определить длину строки.

a='кошка'
print('Решение ЗАДАЧИ №1   Длина слова "'+a+'" =',len(a))

#Задача «Суммы и разности».
#Описание: запишите два целых числа в переменные first и second, вычислите их сумму и разность, запишите их в
# переменные summa и diff. Затем выведите значения переменных summa и diff на экран(в консоль) .
first=5
second=7
summa=first+second
diff=first-second
print('Решение ЗАДАЧИ №2   Summa=',summa, ' Diff=',diff)

#Задача «Среднее арифметическое».
#Описание: Запишите три числа в переменные first, second и third соответственно и вычислите их среднее арифметическое,
#записав в переменную mean. Затем выведите значения переменной mean на экран(в консоль) .

first=5
second=7
third=9
mean=(first+second+third)/3
print('Решение ЗАДАЧИ №3   Среднеарифметическое чисел',first,second,'и',third,'=',mean)

#Задача «Простые строчки».
#Описание: Создайте две переменных first_string и second_string и запишите в них строки "Вторник" и "Понедельник".
#Выведите на экран(в коносль) строки так, чтобы "Понедельник" шёл перед "Вторником" и между ними находилась
#запятая с пробелом (", ")
#Понедельник, Вторник

first_string='Вторник'
second_string='Понедельник'
print('Решение ЗАДАЧИ №4  ',second_string,',',first_string)



#Задача «Сложная формула».
#Описание: Запишите три числа в переменные a, b и c соответственно и создайте переменную f, в которую запишите результат
# выражения: (a * b) + (a * c). Возведите полученное число в третью степень и результат разделите(обычное деление) на два.
# Выведите его на экран(в консоль).

a=1
b=2
c=3
f=(((a*b)+(a*c))**3)/2
print('Решение ЗАДАЧИ №5  ',f)
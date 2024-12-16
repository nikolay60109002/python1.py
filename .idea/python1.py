width = int(input("Введите ширину рамки: "))
height = int(input("Введите высоту рамки: "))
for line in range(height + 1):
for col in range(width + 1):
if col == width or col == 0:
print('|', end='')
elif line == height or line == 0:
print('-', end='')
else:
print(' ', end='')
print()


a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))
if a + b > c and a + c > b and b + c > a:
print("Треугольник существует.")
if a == b == c:
print("Треугольник равносторонний.")
elif a == b or b == c or a == c:
print("Треугольник равнобедренный.")
else:
print("Треугольник разносторонний.")
else:
print("Треугольник не существует.")

n = int(input('Введите количество чисел в последовательности: '))
count = 0
for i in range(n):
number = int(input('Введите очередное число: '))
if number > 1:
for divider in range(2, number):
if number % divider == 0:
break
else:
count += 1
print('Количество простых чисел:', count)

depth = int(input('Введите глубину ямы: '))
for line in range(depth):
for left_number in range(depth, depth - line - 1, -1):
print(left_number, end="")
point_count = 2 * (depth - line - 1)
print("." * point_count, end="")
for right_number in range(depth - line, depth + 1):
print(right_number, end="")
print()

start = 1
finish = 100
count = 1
while True:
n = (start + finish) // 2
print('Загаданное число равно, меньше или больше', n)
answer = int(input('1 - равно, 2 - меньше, 3 - больше '))
if answer == 1:
print('Я угадал! Ура! с', count, 'попытки')
break
elif answer == 2:
finish = n
elif answer == 3:
start = n
count += 1
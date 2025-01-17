# ЦИКЛЫ

########################## FOR #################################
gladiator = {"name":"Gladiator", "year":2000, "actors": ["Russell Crowe", "Joaquin Phoenix"], "sequels":[]}
bladrunner ={"name": "Bladerunner","year":1982, "actors": ["Harrison Ford", "Rutger Hauer"], "sequels": ["Bladerunner 2049"]}
once_in_america = {"name": "Once upon a time in America", "year":1984 , "actors": ["Robert De Niro"," Joe Pesci"], "sequels":[]}
spiderman_2 = {"name": "Spider-Man 2", "actors": ["Tobey Maguire"], "year":2004, "sequels": ["Spider mna 3"]}
nice_guys = {"name":"The Nice Guys", "year":2016, "actors": ["Russell Crowe", "Ryan Gosling"], "sequels":[]}

# Пример списка со словарями
movies = (gladiator, bladrunner, once_in_america, spiderman_2)

"""
Часто нам нужно достать один или несколько элементов из коллекции (последовательности).
И мы можем не знать индекса этого элемента, 
да и задавать в ручную индекс довольно неудобно.
Для этого нам нужен инструмент, позволяющий перебирать коллекции.

Этот инструмент - цикл for 
Он идет по ПОСЛЕДОВАТЕЛЬНОСТЯМ (тупль, список, сет),
и для этого похода использует то, что называется ИТЕРАТОРОМ
ИТЕРАТОР это переменная, которая идет ВНУТРИ цикла 
и принимает значения элементов один за другим.
"""

for x in [1,2,3]:
	print(x)

for movie in movies:
	"""
	Внутри цикла мы можем то же, что и во всем остальном коде,
	только еще и имея доступ к значениям ВНУТРИ цикла.
	Например так: 
	наш итератор movie принимает последодвательно значения в тупле movies
	И каждый новый шаг - movie будет становится одним из словарей-фильмов.
	"""
	print(movie)
	# Соотетственно мы можем обращаться к переменной как к словарю.
	print(movie["name"])


# Частенько перебор используется для того, чтобы из одних коллекций вытаскивать значения и помещать в другие.

russel_crow_movies = []
for x in movies:
	"""
	Проходимся по существующему списку.
	Делаем проверку на наличие имени актера в списке, содержащемся в словаре.
	Если оно верное, копируюм элемент из стаого списка и добавляем в новый.
	"""
	if "Russell Crowe" in x["actors"]:
		# Добавляем элемент, прошедший проверку в новый список:
		russel_crow_movies.append(x)

# Список был изменен и теперь доступен в обновленном виде
print("Russel Crow movies:  ",russel_crow_movies)


# Выполнение цикла можно прервать ключевым словом break.

for x in 1,2,3,4,5,6:
	print(x)
	if x == 5:
		break


"""
Так же, говоря о последовательностях, важно помнить, что иногда нам требуется самим создать ее для проходки.
Например, мы идем сразу по двум спискам, и хотим обращаться к ним по одному и тому же индексу.
Для создания последовательностти можно воспользоваться командой RANGE.

синтаксиc такой - RANGE(ПЕРВАЯ ЦИФРА, ПОСЛЕДНЯЯ) 
например:
range(0, 10) - результат 1, 2, 3, 4, 5, 6, 7, 8, 9

Ее можно закрепить за переменной:
"""

test_range = range(2,15)

# И пройтись по ней циклом for:

for x in test_range:
	print("Elements in range:   ", x)
"""
Кроме того, если у нас нет сложных условий, 
и вам нужно создать список из другой последовательности (тупль, сет, фрозенсет, список),
можно воспользоваться конструкцией из одной строки
"""
test_gen = [x for x in range(2, 16)]

test_gen_2 = [movie for movie in movies if movie["year"] >= 2000]


"""
Если же вам нужно создать огромный список или хочется максимально экономить память,
можно сдлеать так:
"""
test_iter = (x for x in range(3,17))
"""
Нет, это не создание тупля, это создание такой коллекции, 
которая не хранится вся в памяти, а предназначена для перебора другим циклом.
И каждое значение вычисляется только в момент обращения к нему, 
а затем переходит на следующее.
"""
########################## WHILE #################################

"""
Цикл For предназнчен для перебора массивов, 
но иногда нам нужно не циклически пройтись по набору данных,
а повторять одно и то же действие бесконечно, прерываясь только по условию.
Для этого нужен цикл while
"""

# Задаються начальные параметры:
x = 0

# Запускаеться цикл где действие повторяеться, пока определенное условие не остановит его:
while x < 10:
	print(x)
	x = x+1
"""
Этот цикл подоходит если нужно, например, 
постоянно слать запросы на какой-то удаленный источник и реагировать на изменения.
"""
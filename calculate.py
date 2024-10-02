import circle
import square


figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):

# Вычисляет значение заданной фигуре в зависимости от заданных размеров 

# Функция принимает три параметра - 
# fig - название фигуры(circle или square)
# func - название функции(perimeter или area) 
# size - список размеров фигуры

# Возвращает результат вычисления функции для указанной фигуры 


# Пример вызова:
# input: calc('circle', 'area', [10])
# output: area of circle is 314,15927 

# input: calc('square', 'perimeter', [5])
# output: perimeter of square 20




	assert fig in figs
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})')
	print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	calc(fig, func, size)




figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {
    'perimeter-circle': 1,
    'area-circle': 1,
    'perimeter-square': 1,
    'area-square': 1,
}

def calc(fig, func, size):
    if fig not in figs:
        raise ValueError(f"Invalid figure:
                         {fig}. Available figures are: {figs}")
    if func not in funcs:
        raise ValueError(f"Invalid function: 
                         {func}. Available functions are: {funcs}")
    if any(s < 0 for s in size):
        raise ValueError("Can't use negative values for figure dimensions.")

    result = eval(f'{fig}.{func}(*{size})')
    return result

if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()
    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:n")
    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:n")
    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(int, 
                        input("Input figure sizes separated by space:n").split(' ')))
    result = calc(fig, func, size)
    print(f'{func} of {fig} is {result}')




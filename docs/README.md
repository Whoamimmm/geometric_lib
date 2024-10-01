
# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`


## `calculate.py`
### `def calc(fig, func, size):`
- Calculate the result of the specified function for the specified shape depending on the size
- Example of the call:
```
>> calc('square', 'perimeter', [10])
40
```

## `square.py`
### `def area(a):`
- Calculate the area of square using the side length
- Example of the call:
```
>> area(10)
100
```

### `def perimeter(a):`
- Calculate the perimeter of square using the side length
- Example of the call:
```
>> perimeter(10)
40
```

## `circle.py`
### `def area(r):`
- Calculate the area of circle using the radius
- Example of the call:
```
>> area(10)
314,15927
```

### `def perimeter(r):`
- Calculate the perimeter of circle using the raduis
- Example of the call:
```
>> perimeter(10)
62,83185
```

## `triangle.py`
### `def area(a, b, c):`
- Calculate the half of triangle perimeter using 3 side's lenght
- Example of the call:
```
>> area(2, 3, 5)
5
```

### `def perimeter(a, b, c):`
- Calculate the perimeter of triangle using 3 side's lenght
- Example of the call:
```
>> perimeter(2,3,5)
10
```

# The history of changing the project with the hashes of the commits

1. **d76db2a** - L-04: Add calculate.py 
2. **51c40eb** - L-04: Doc updated for triangle
3. **d080c78** - L-04: Triangle added
4. **d078c8d** - L-03: Docs added
5. **8ba9aeb** - L-03: Circle and square added
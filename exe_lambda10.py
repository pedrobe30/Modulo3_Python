numbers = [-4.4, 54, -1.7, 12, 1.2, 0.50, 0.75, 8, 210, -10]

maior_que_dois = lambda y: y>2
verdadeiros = list(map(maior_que_dois, numbers))


print(verdadeiros)

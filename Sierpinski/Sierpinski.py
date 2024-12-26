import matplotlib.pyplot as plt
from random import randint

p1 = [0 , 0]
p2 = [100 , 0]
p3 = [50 , 100]

x = [0]
y = [0]

atual = [x[-1], y[-1]]

quantidade = 5000

for i in range(quantidade):
    sorteio = randint(1, 3)
   

    if sorteio == 1:
        cord_x = (atual[0] + p1[0])/2
        cord_y = (atual[1] + p1[1])/2
    
    elif sorteio == 2:
        cord_x = (atual[0] + p2[0])/2
        cord_y = (atual[1] + p2[1])/2
    
    else:
        cord_x = (atual[0] + p3[0])/2
        cord_y = (atual[1] + p3[1])/2
    
    atual[0] = cord_x
    atual[1] = cord_y

    x.append(cord_x)
    y.append(cord_y)

plt.scatter(x, y, s = 1, color='black')  
plt.show()  
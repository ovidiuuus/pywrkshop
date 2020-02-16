import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import image as im

temperature = [14.2, 16.4, 11.9, 12.5, 18.9, 22.1, 19.4, 23.1, 25.4, 18.1, 22.6, 17.2]
sales = [215.20, 325.00, 185.20, 330.20, 418.60, 520.25, 412.20, 614.60, 544.80, 421.40, 445.50, 408.10]

"""
plt.title('Ice-cream sales versus temperature')
plt.xlabel('Temperature')
plt.ylabel('Sales')
plt.scatter(temperature, sales, color='green')
plt.show()
"""

stock_price = [190.64, 190.09, 192.25, 191.79, 194.45, 196.45, 196.45, 196.42, 200.32, 200.32, 200.85, 199.2, 199.2, 199.2, 199.46, 201.46, 197.54, 201.12, 203.12, 203.12, 203.12, 202.83, 202.83, 203.36, 206.83, 204.9, 204.9, 204.9, 204.4, 204.06]
t = list(range(1, 31))
"""
plt.title('Opening Stock Prices')
plt.xlabel('Days')
plt.ylabel('$ USD')
plt.plot(t, stock_price, marker='.', color='red')
plt.xticks(range(1, 32, 2))
plt.show()
"""

### Activity 12: Fibonacci Function iwth Dynamic Programming
fib_sec = {}
def fib_dyn(n):
    if n == 1 or n == 2:
        fib_sec[1] = 1
        fib_sec[2] = 1
        return 1
    if (n-1) not in fib_sec:
        fib_dyn(n - 1)
    if (n - 2) not in fib_sec:
        fib_dyn(n - 2)
    fib_sec[n] = fib_sec[n - 1] + fib_sec[n - 2]
    return fib_sec[n]

def plot_fib(n):
    file_name = 'data/fib/fibonacci_'+str(n)+'.jpg'
    for i in range(1, (n + 1), 1):
        fib_dyn(i)
    yl = list(fib_sec.keys())
    xl = list(fib_sec.values())
 #   print(yl)
 #   print(xl)
    plt.title('Fibonacci plot')
    plt.xlabel('Fibonacci[k]')
    plt.ylabel('Number')
    plt.plot(yl, xl, marker='.', color='green')
#    plt.show()
    plt.savefig(file_name)
#    im.open('temp_plot.png').save(file_name, 'JPEG')

for i in range(5):
    plot_fib(i)

import matplotlib.pyplot as plt
import numpy as np

def pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.show()

def seno_figu():
    x = np.linspace(0, 2 * np.pi, 200)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()

def generate_bar_char(labels, values):
    print("generate_bar_char")
    
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()
    
if __name__ == '__main__':
    seno_figu()
    labels = ['a', 'b', 'c']
    values = [100, 200, 80]
    generate_bar_char(labels, values)
    pie_chart(labels, values)
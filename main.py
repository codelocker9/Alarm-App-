# Importing the necessary libraries for the fun 5-min project
import random # For generating random numbers
import matplotlib.pyplot as plt # For the graph plot generator

x = []
y = []

def math_problem():
    unique_number = random.randrange(1, 10) # Generating a random number from 1 to 9
    counter = 0 # The number of times the program loops

    while True:
        counter = counter + 1
        x.append(counter)

        if unique_number % 2 == 0:
            unique_number = unique_number/2
            y.append(unique_number)
        else:
            unique_number = unique_number * 3 + 1
            y.append(unique_number)

        if unique_number == 1:
            plt.plot(x, y)

            plt.xlabel('x-axis')
            plt.ylabel('y-axis')
            plt.title('Collatz Conjecture')

            plt.show()
            break

if __name__ == "__main__":
    math_problem()
import random
import time
import matplotlib.pyplot as plt
from algorithms.bubblesort import Bubblesort
from algorithms.quicksort import Quicksort
from algorithms.mergesort import Mergesort
from algorithms.selectionsort import Selectionsort
import numpy as np

int_list = []
times = []
algorithms = {"bubblesort":Bubblesort(),"quicksort":Quicksort(), "mergesort":Mergesort(), "selectionsort":Selectionsort()}
chosen_alg = ""
length = [2, 4, 6, 8, 10, 15, 20, 30, 40, 50, 70, 100, 150, 200, 300, 400, 500, 650, 850, 1000]

#
#def get_input(alg_list):
#    while True:
#        inp = input("Please choose your algorithm from " + alg_list[0]).lower()
#
#        if inp in alg_list:
#            return inp
#        print("Invalid input")
#chosen_alg = get_input(algorithms)
j = 0
for algorithm in algorithms:
    j += 1
    for n in range(20):
        times = []
        for i in length:
            int_list = []
            sort = algorithms[algorithm]

            # create list of size 1000 with random integers from 1 to 100
            for _ in range(i):
                int_list.append(random.randint(1, 100))

            start_time = time.time()
            sort.sort(int_list)
            end_time = time.time()
            times.append(end_time - start_time)


        plt.figure(j)
        plt.plot(length, times)
        print("Finished epoch " + str(n + 1))

    plt.xlabel("Number of iterations")
    plt.ylabel("Time (seconds)")
    plt.title("Execution time of "+ str(algorithm))

plt.show()

import random
import matplotlib.pyplot as plt
from animate import camera
from sorting import selectionSort, bubbleSort, insertionSort, heapSort

size = int(input("Data size(Default: 30)\n>") or 30)
data = random.sample(range(size), size)

alg_list = {'1': bubbleSort, '2': selectionSort,
            '3': insertionSort, '4': heapSort}
alg_type = input(
    "Sorting type(Default: selection sort)\n1.bubble sort\n2.selection sort\n3.insertion sort\n4.heap sort\n>") or '2'

func = alg_list[alg_type]

if func == selectionSort or bubbleSort or insertionSort or heapSort:
    func(data)

animation = camera.animate(interval=20)
plt.show()

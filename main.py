import random
import matplotlib.pyplot as plt
from animate import camera
from sorting import selectionSort, bubbleSort, insertionSort

size = int(input("Data size(Default: 30)\n>") or 30)
data = random.sample(range(size), size)

alg_list = {'1': bubbleSort, '2': selectionSort, '3': insertionSort}
alg_type = input(
    "Sorting type(Default: selection sort)\n1.bubble sort\n2.selection sort\n3.insertion sort\n>") or '2'

func = alg_list[alg_type]

if func == selectionSort or bubbleSort or insertionSort:
    func(data)

animation = camera.animate(interval=20)
plt.show()

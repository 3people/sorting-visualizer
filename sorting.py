from animate import draw


def bubbleSort(data):
    data_length = len(data)
    for i in range(data_length - 1):
        for j in range(data_length - i - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                draw(j+1, data)


def selectionSort(data):
    data_length = len(data)
    for i in range(data_length - 1):
        least = i
        for j in range(i+1, data_length):
            if data[j] < data[least]:
                least = j
        if i != least:
            data[i], data[least] = data[least], data[i]
            draw(i+1, data)


def insertionSort(data):
    data_length = len(data)
    for i in range(1, data_length):
        j = i - 1
        key = data[i]
        while data[j] > key and j >= 0:
            data[j+1] = data[j]
            j = j - 1
        data[j+1] = key
        draw(j+1, data)


def heapify(data, index, size):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2
    if left < size and data[left] > data[largest]:
        largest = left
    if right < size and data[right] > data[largest]:
        largest = right
    if largest != index:
        data[largest], data[index] = data[index], data[largest]
        heapify(data, largest, size)
        draw(largest, data)


def heapSort(data):
    data_length = len(data)
    for i in range(data_length // 2 - 1, -1, -1):
        heapify(data, i, data_length)
    for i in range(data_length-1, 0, -1):
        data[0], data[i] = data[i], data[0]
        heapify(data, 0, i)
    return data

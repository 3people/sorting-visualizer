import matplotlib.pyplot as plt
from celluloid import Camera

fig = plt.figure()
camera = Camera(fig)


def draw(colored, data):
    x = list(range(len(data)))
    colors = list(len(data)*'b')
    colors[colored] = 'r'
    plt.bar(x, data, color=colors)
    camera.snap()

"""
This example replicates Michael Fogleman's city drawing made with his ln library.
"""
import random

from lines import Scene, StrippedCube


def main():
    scene = Scene()

    for i in range(-12, 13, 2):
        for j in range(-12, 13, 2):
            h = 1 + random.random() * 5
            c = StrippedCube(scale=(1, 1, h), translate=(i, j, h / 2))
            scene.add(c)

    scene.look_at((1.1, 0.8, 8.2), (0, 0.2, 0))
    scene.perspective(90, 0.1, 10)

    rs = scene.render()
    rs.show()
    rs.save('city.svg')


if __name__ == "__main__":
    main()

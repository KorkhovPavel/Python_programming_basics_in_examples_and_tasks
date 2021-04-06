from matplotlib.patches import Circle, Wedge, Ellipse, Arc, Rectangle

import matplotlib.pyplot as plt

plt.xlim(-5, 26)

plt.ylim(-5, 26)

ax = plt.gca()
# figure = Circle((6, 7), 5, 1)
#
# figure = wedge((4, 4), 2, -90, 90)
#
# figure = Wedge((4, 4), 2, -90)
#
# figure = arc((6, 6), 5, 3, 0, 200, 100)
#
figure = Rectangle((10, 12), (5, 8))

ax.add_patch(figure)
plt.show()

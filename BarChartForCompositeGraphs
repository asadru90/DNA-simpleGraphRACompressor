
import matplotlib.pyplot as plt
import numpy as np


labels = ['KidneyNormal-BreastNormal', 'LiverNormal-ColonNormal']
graph_1 = [1.18, 1.19]
graph_2 = [1.21, 1.21]
Composite_graph = [1.21, 1.21]

x = np.arange(len(labels))  # the label locations
width = 0.20  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/4, graph_1, width, label='Single Graph 1')
rects2 = ax.bar(x - 5*width/4, graph_2, width, label='Single Graph 2')
rects3 = ax.bar(x + 3*width/4, Composite_graph, width, label='CompositeGraph')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Compression ratio to AL')
ax.set_title('PPI network dataset for composite graphs')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects2, padding=2)
ax.bar_label(rects1, padding=2)
ax.bar_label(rects3, padding=2)

fig.tight_layout()

plt.show()

# importing the modules
from bokeh.plotting import figure, output_file, show

# file to save the model
output_file("gfg.html")

# instantiating the figure object
graph = figure(title="Bokeh Line Graph")

# the points to be plotted
x = [1, 2, 3, 4, 5]
y = [1, 6, 8, 2, 3]

# plotting the line graph
graph.line(x, y)

# displaying the model
show(graph)

# prislusny graf sa zobrazi v prehliadaci
import matplotlib.pyplot as plt

# Create some data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a figure and axes
fig, ax = plt.subplots()

# Plot the data
scatter = ax.scatter(x, y)

# Add labels and title
ax.set(xlabel='X-axis', ylabel='Y-axis', title='Scatter Plot with Hover Event')

annot = ax.annotate("", xy=(0,0), xytext=(20,20), textcoords="offset points",
                   bbox=dict(boxstyle="round", fc="w"),
                   arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)

def update_annot(ind):
    pos = ind["ind"][0]
    x, y = x[pos], y[pos]
    annot.xy = (x, y)
    text = f"({x}, {y})"
    annot.set_text(text)

def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        cont, ind = scatter.contains(event)
        if cont:
            update_annot(ind)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()

fig.canvas.mpl_connect("motion_notify_event", hover)

# Show the plot
plt.show()

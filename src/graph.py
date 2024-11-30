import matplotlib.pyplot

def create_graph(x:list[int], y:list[int], axXname:str,axYname:str, title:str, texto:str, grade:bool):
    ax = matplotlib.pyplot.subplot()
    ax.plot(x, y, label=texto)
    ax.set_xlabel(axXname)
    ax.set_ylabel(axYname)
    ax.set_title(title)
    ax.grid(grade)
    ax.legend()
    matplotlib.pyplot.show()

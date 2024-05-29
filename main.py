from tkinter import Tk, Canvas, Button
from functions import *
from random import seed
from bfs_and_dfs import traversal

window = Tk()
window.geometry(f'{window_width}x{window_height}')
window.title("Graphs")
window.resizable(False, False)

canvas = Canvas(width=window_width, height=window_height)
canvas.pack()

seed(seed_value)

print("матриця напрямленого графа:")
matrix_for_directed_graph = create_matrix_for_directed_graph(count_of_vertexes)
for row in matrix_for_directed_graph:
    print(row)
canvas.create_text(graph_left, 20, text="напрямлений граф", font=("Arial", 20))
vertexes = draw_graph(graph_left, graph_top, graph_size, matrix_for_directed_graph, canvas)

bfs_button = Button(window, text="start BFS", bg=buttonColors, fg="black", font=("Arial", 20),
                    command=lambda: traversal(matrix_for_directed_graph, vertexes, canvas, bfs_button, dfs_button,
                                              "bfs"))
bfs_button.place(x=600, y=200)

dfs_button = Button(window, text="start DFS", bg=buttonColors, fg="black", font=("Arial", 20),
                    command=lambda: traversal(matrix_for_directed_graph, vertexes, canvas, dfs_button, bfs_button,
                                              "dfs"))
dfs_button.place(x=600, y=300)


window.mainloop()

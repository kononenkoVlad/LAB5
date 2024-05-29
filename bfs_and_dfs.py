from data import *
from functions import paint_opened_vertex, create_zero_matrix

new_vertexes = list(range(0, count_of_vertexes))
opened_vertexes = []
opposite_button_destroyed = False
traversal_tree_matrix = create_zero_matrix(count_of_vertexes)
order_of_opening_vertexes = []


def open_vertex(matrix, open_from, canvas, vertexes):
    for vertex in new_vertexes:
        if matrix[open_from][vertex]:
            paint_opened_vertex(canvas, vertexes, vertex, open_from)
            traversal_tree_matrix[open_from][vertex] = 1
            order_of_opening_vertexes.append(vertex)
            opened_vertexes.append(vertex)
            new_vertexes.remove(vertex)
            return True


def bfs_function(matrix, canvas, vertexes):
    open_from = opened_vertexes[0]
    vertex_has_been_opened = open_vertex(matrix, open_from, canvas, vertexes)
    if vertex_has_been_opened:
        return True
    del opened_vertexes[0]
    return False


def dfs_function(matrix, canvas, vertexes):
    open_from = opened_vertexes[-1]
    vertex_has_been_opened = open_vertex(matrix, open_from, canvas, vertexes)
    if vertex_has_been_opened:
        return True
    del opened_vertexes[-1]
    return False


def traversal(matrix, vertexes, canvas, this_button, opposite_button, bfs_or_dfs):
    if len(opened_vertexes):
        vertex_has_been_opened = bfs_function(matrix, canvas, vertexes) if bfs_or_dfs == "bfs"\
            else dfs_function(matrix, canvas, vertexes)
        if not vertex_has_been_opened:
            traversal(matrix, vertexes, canvas, this_button, opposite_button, bfs_or_dfs)
    elif len(new_vertexes):
        global opposite_button_destroyed
        if not opposite_button_destroyed:
            opposite_button_destroyed = True
            opposite_button.destroy()
        vertex_to_open = new_vertexes[0]
        paint_opened_vertex(canvas, vertexes, vertex_to_open, None)
        order_of_opening_vertexes.append(vertex_to_open)
        opened_vertexes.append(new_vertexes[0])
        new_vertexes.remove(new_vertexes[0])
    else:
        this_button.destroy()
        print("\nМатриця суміжності дерева обходу:")
        for row in traversal_tree_matrix:
            print(row)
        print("\nПорядок відкриття вершин:")
        print([x+1 for x in order_of_opening_vertexes])

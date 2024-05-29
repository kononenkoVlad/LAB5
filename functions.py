from tkinter import LAST
from math import pi, cos, sin, sqrt
from random import random
from data import *


def create_vertex(left, top, text, canvas):
    text = canvas.create_text(left, top, text=text+1, font=("Arial", vertex_size))
    oval = canvas.create_oval(left - vertex_size, top - vertex_size, left + vertex_size, top + vertex_size, fill="",
                              outline="red")
    return {
        "text": text,
        "oval": oval
    }


def create_vertexes(left, top, size, count, canvas):
    vertexes = [{}] * count
    for i in range(count):
        angle = i * 2 * pi/count
        vertex_left = left + size * sin(angle)
        vertex_top = top - size * cos(angle)
        vertex_window_elements = create_vertex(vertex_left, vertex_top, i, canvas)
        vertex = {
            "left": vertex_left,
            "top": vertex_top,
            "text": vertex_window_elements["text"],
            "oval": vertex_window_elements["oval"],
            "number": i
        }
        vertexes[i] = vertex
        i += 1
    return vertexes


def create_matrix_for_directed_graph(size):
    matrix = []
    for i in range(size):
        matrix.append([])
        for j in range(size):
            number = int(random()*2*k)
            matrix[i].append(number)
    return matrix


def create_zero_matrix(size):
    matrix = []
    for i in range(size):
        matrix.append([])
        for j in range(size):
            matrix[i].append(0)
    return matrix


def draw_self_arrow(left, top, i, count_of_vertexes_in_this_graph, canvas):
    main_angle = i / count_of_vertexes_in_this_graph * 2 * pi
    lefter_angle = main_angle + extra_angle_in_self_arrow
    righter_angle = main_angle - extra_angle_in_self_arrow
    first_point_x = left+sin(lefter_angle)*2*vertex_size
    first_point_y = top-cos(lefter_angle)*2*vertex_size
    second_point_x = left+sin(righter_angle)*2*vertex_size
    second_point_y = top-cos(righter_angle)*2*vertex_size
    canvas.create_line(first_point_x, first_point_y, second_point_x, second_point_y)
    canvas.create_line(left + vertex_size*sin(lefter_angle), top - vertex_size*cos(lefter_angle),
                       first_point_x, first_point_y)
    canvas.create_line(second_point_x, second_point_y, left + vertex_size*sin(righter_angle),
                       top - vertex_size*cos(righter_angle), arrow=LAST)


def draw_arrow(left_i, top_i, left_j, top_j, color, width, canvas):
    dx = left_i - left_j
    dy = top_i - top_j
    line_length = sqrt(dx * dx + dy * dy)
    cos_angle = dx / line_length
    sin_angle = -dy / line_length
    left_from = left_i - vertex_size * cos_angle + sin_angle * space_between_edges
    left_to = left_j + vertex_size * cos_angle + sin_angle * space_between_edges
    top_from = top_i + vertex_size * sin_angle + cos_angle * space_between_edges
    top_to = top_j - vertex_size * sin_angle + cos_angle * space_between_edges
    canvas.create_line(left_from, top_from, left_to, top_to, arrow=LAST, fill=color, width=width)


def draw_edges(matrix, vertexes, canvas):
    length = len(matrix)
    for i in range(length):
        for j in range(length):
            if not matrix[i][j]:
                continue
            if i == j:
                left = vertexes[i]["left"]
                top = vertexes[i]["top"]
                draw_self_arrow(left, top, i, length, canvas)
                continue
            left_i = vertexes[i]["left"]
            left_j = vertexes[j]["left"]
            top_i = vertexes[i]["top"]
            top_j = vertexes[j]["top"]
            draw_arrow(left_i, top_i, left_j, top_j, "black", 1, canvas)


def draw_graph(left, top, size, matrix, canvas):
    length = len(matrix)
    vertexes = create_vertexes(left, top, size, length, canvas)
    draw_edges(matrix, vertexes, canvas)
    return vertexes


def paint_opened_vertex(canvas, vertexes, vertex, from_vertex):
    canvas.itemconfig(vertexes[vertex]["oval"], fill="blue")
    canvas.tag_raise(vertexes[vertex]["text"])
    if type(from_vertex) is int:
        draw_arrow(vertexes[from_vertex]["left"], vertexes[from_vertex]["top"], vertexes[vertex]["left"],
                   vertexes[vertex]["top"], "red", 3, canvas)

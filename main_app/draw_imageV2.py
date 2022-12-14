from pynput.mouse import Button, Controller
from time import sleep

from init_app.constants import ALL_POS_COLOR


def get_coor_colors(color_list: list, drawing_zone: tuple, new_image_list: list) -> list:
    """
    Analyse l'image et met dans une list chaque coordonné par rapport à chaque couleur
    """

    coor_all_color = []

    for color in range(len(color_list)):
        coor_all_color.append([])

    current_color_list = -1

    for color in color_list:
        current_color_new_image_list = 0
        current_color_list += 1

        for y in range(0, drawing_zone[1]):
            for x in range(0, drawing_zone[0]):

                if new_image_list[current_color_new_image_list] == color and color != (255, 255, 255):
                    coor_all_color[current_color_list].append((x, y))
                current_color_new_image_list += 1

    return coor_all_color


def draw_image(start_pixel: tuple, coor_colors: list):
    """
    Position la souris à chaque coordonnée des pixels d'une couleur puis clique pour dessiner
    """
    current_color_list = -1
    mouse = Controller()

    for pos_color in ALL_POS_COLOR:
        mouse.release(Button.left)

        # clique sur la nouvelle couleur
        mouse.position = pos_color

        mouse.click(Button.left, 1)
        sleep(.0000000000000001)

        current_color_list += 1

        for coor_color in coor_colors[current_color_list]:
            # bouge la souris et clique

            coor_mouse = ((start_pixel[0] + coor_color[0]), (start_pixel[1] + coor_color[1]))

            try:
                next_pixel_x = start_pixel[0] + coor_color[current_color_list + 1]
            except IndexError:
                next_pixel_x = 0

            calc_distance = next_pixel_x - coor_mouse[0]

            if not calc_distance == 1:
                mouse.release(Button.left)

            mouse.position = coor_mouse
            mouse.press(Button.left)

            sleep(.0000000000000001)

    mouse.release(Button.left)


def draw(start_pixel: tuple, color_list: list, new_image_list: list, drawing_zone: tuple):
    draw_image(start_pixel, get_coor_colors(color_list, drawing_zone, new_image_list))

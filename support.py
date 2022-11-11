from os import walk
import pygame as py

def import_folder(path):
    surface_list = []

    for _,_, img_files in walk(path):
        for image in img_files:
            full_path = path +'/'+ image
            image_surf = py.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list

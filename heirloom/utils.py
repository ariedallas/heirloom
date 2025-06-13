import json
import os
import string

def get_proj_dir():
    return os.getcwd()

def get_settings_path():
    PROJ_DIR = get_proj_dir()
    return os.path.join(PROJ_DIR, "settings.json")

def get_sound(sound):
    PROJ_DIR = get_proj_dir()
    bell = os.path.join(PROJ_DIR, "sounds", "short_bell.mp3")
    block = os.path.join(PROJ_DIR, "sounds", "block.mp3")

    sounds = dict(bell=bell, block=block)
    return sounds.get(sound)

LETTERS_CAPS = string.ascii_uppercase
LETTERS_FILTERED = [L for L in LETTERS_CAPS if not (L == 'Q') and not (L == 'X')]

EXIT_DICT = {"X": "Exit"}
QUIT_DICT = {"Q": "Quit"}


def prep_menu_tuple(var_menu):
    dict_menu = {f"{ltr}": f"{match}" for ltr, match in zip(LETTERS_FILTERED, var_menu)}

    menu_list = [f"[{letter}]  {action}" for letter, action in zip(
        dict_menu.keys(),
        dict_menu.values())]

    return dict_menu, menu_list


def write_json_settings(json_filename, json_data):
    settings_path = get_settings_path()
    with open(settings_path, "w+") as fout:
        fout.write(json.dumps(json_data, indent=4))


def get_json_settings(path):
    with open(path) as fin:
        json_data = json.load(fin)

    return json_data


if __name__ == '__main__':
    print("Hello from main")
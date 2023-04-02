import os



def check_dir():
    items = False
    directory = 'neureal/static/images'
    if os.listdir(directory):
        items = True
    return items

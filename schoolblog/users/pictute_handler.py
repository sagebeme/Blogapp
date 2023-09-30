import os
from PIL import Image
from flask import url_for, current_app

def add_pic(pic_upload, username):
    """
    Purpose: takes uploaded pic puts username
    and saves the pic
    """
    filename = pic_upload.filename
    # "mypicture.jpg"
    ext_type = filename.split('.')[-1]
    # "username.jpg"
    storage_filename = str(username)+'.'+ext_type

    filepath = os.path.join(current_app.root_path,'static\profile_pics',storage_filename)

    output_size = (200,200)

    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(filepath)

    return storage_filename
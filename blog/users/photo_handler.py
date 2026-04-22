import os
from  PIL import Image # TODO: Read a bit of the docs on this pckg
from flask import current_app

def save_photo(uploaded_photo, username):
    filename = uploaded_photo.filename
    ext_type = filename.split('.')[-1]
    storage_filename = str(username) + '.' + ext_type
    filepath = os.path.join(current_app.root_path, 'static/profile_pics', storage_filename)
    uploaded_photo.save(filepath)

    output_size = (200, 200)
    img = Image.open(uploaded_photo)
    img.thumbnail(output_size)
    img.save(filepath)

    return storage_filename
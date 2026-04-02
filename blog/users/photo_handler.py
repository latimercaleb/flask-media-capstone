import os 
from  PIL import Image # Adjjust things to use Pillow for image processing
from flask import current_app, url_for

def save_picture(pic_upload, username):
    filename = pic_upload.filename
    ext_type = filename.split('.')[-1]
    storage_filename = str(username) + '.' + ext_type
    filepath = os.path.join(current_app.root_path, 'static/profile_pics', storage_filename)
    pic_upload.save(filepath)

    output_size = (200, 200)
    img = Image.open(pic_upload)
    img.thumbnail(output_size)
    img.save(filepath)

    return url_for('static', filename='profile_pics/' + storage_filename)
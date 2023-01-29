'''
This script rewrites all logos, favicons and widgets with corresponding new ones
'''
import os
from PIL import Image

from glob import glob
images_names = ['logo.png', 'favicon.png', 'widget-logo.png']

new_imgs_dir = '/home/sevocrear/Downloads/Untitled'

for name in images_names:
    web_site_imgs = glob(f"**/{name}", recursive=True)

    img_new = Image.open(os.path.join(new_imgs_dir, name))

    for old_img_path in web_site_imgs:
        img_new.save(old_img_path)
from fastai.vision.utils import *
from pathlib import Path

path = Path("images")
resize_images(path, dest=path) 

from fastai.vision.utils import *
from pathlib import Path

path = Path("images")
result = resize_images(path, dest=path, max_size=400) 
print(result)
result = resize_images(path, dest=path, max_size=400) 
print(result)

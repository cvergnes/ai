from fastai.vision.utils import *
from pathlib import Path

path = Path("bmw-750.jpeg")
resize_images( file=path, dest=path) 

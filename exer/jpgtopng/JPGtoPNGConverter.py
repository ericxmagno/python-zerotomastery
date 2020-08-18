import sys
import os
from PIL import Image

# grab arguments
try:
    folder_to_copy = sys.argv[1]
    folder_to_save = sys.argv[2]
except Exception as err:
    print("Invalid arguments")

# Create folders if they do not exist
try:
    if not os.path.isdir(f"./{folder_to_copy}"):
    os.mkdir(f"{folder_to_copy}")
except expression as identifier:
    pass
else:
    pass
finally:
    pass
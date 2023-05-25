import numpy as np
import torch
import matplotlib.pyplot as plt
import cv2
from segment_anything import sam_model_registry, SamPredictor

img_path = "/home/englund/python_test/AB3DMOT/data/KITTI/tracking/testing/image_02/0000/000000.png"
txt_path = "/home/englund/python_test/AB3DMOT/results/KITTI/pointrcnn_test_H1/trk_withid_0/0000/000000.txt"

img = cv2.imread(img_path)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

with open(txt_path, 'r') as file:
    # Read the contents of the file
    file_contents = file.read()

# Split the contents into lines
lines = file_contents.split('\n')

# Loop through each line and parse the data
for line in lines:
    if line != '':
        # Split the line into its parts
        parts = line.split(' ')

        # Get the label
        label = parts[0]

        # Get the coordinates
        x1 = float(parts[3])
        y1 = float(parts[4])
        x2 = float(parts[5])
        y2 = float(parts[6])

        # Get the other data
        width = float(parts[7])
        height = float(parts[8])
        length = float(parts[9])
        x = float(parts[10])
        y = float(parts[11])
        z = float(parts[12])
        yaw = float(parts[13])
        pitch = float(parts[14])
        roll = float(parts[15])

        # Do something with the data
        print(label, x1, y1, x2, y2, width, height, length, x, y, z, yaw, pitch, roll)

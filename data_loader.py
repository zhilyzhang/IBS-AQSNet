import os, sys
import os.path as osp
root = osp.dirname(osp.abspath(__file__))
sys.path.insert(0, root)
import json
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches


image_path = 'samples/images'
gt_json_path = 'samples/gts/EH021541_128460_120824_023828_36.json'
with open(gt_json_path, 'r') as file:
    data = json.load(file)
    image = Image.open(image_path + '/' + data['file_name']).convert("RGB")
    annotations = data['annotations']


# Convert image to numpy array for plotting
image_np = np.array(image)

# Create a figure and axis for plotting
fig, ax = plt.subplots(1)
ax.imshow(image_np)

# Iterate over annotations and plot them
for annotation in annotations:
    if 'segmentation' in annotation:
        for polygon in annotation['segmentation']:
            # Segmentation data is expected to be a list of points defining the polygon
            # Reshape the segmentation data to a 2D array of points
            polygon = np.array(polygon).reshape(-1, 2)
            patch = patches.Polygon(polygon, linewidth=1, edgecolor='r', facecolor='none')
            ax.add_patch(patch)

plt.show()
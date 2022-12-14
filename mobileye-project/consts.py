# This file contains constants.. Mainly strings.
# It's never a good idea to have a string scattered in your code across different files, so just put them here
import os
import numpy as np

X_AXIS = 22
Y_AXIS = 15
HEIGHT = 115
ORANGE_PIXEL = [250, 170, 30]
INDEX_TRUE = 1
INDEX_IGNORE = 2

PATH_HEAD = "C:/leftImg8bit/train/"
EXTENSION_LABEL = "_gtFine_color.png"

T = 'T'
F = 'F'
IGN = 'I'

threshold = 100
CROPPED_PERCENT = 0.6

BLACK = -0.52
WHITE = 0.48
kernel = np.array([[BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
                   [BLACK, BLACK, BLACK,  WHITE, WHITE, WHITE, WHITE, BLACK, BLACK, BLACK],
                   [BLACK, BLACK, WHITE,  WHITE, WHITE, WHITE, WHITE, WHITE, BLACK, BLACK],
                   [BLACK, WHITE, WHITE,  WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, BLACK],
                   [BLACK, WHITE, WHITE,  WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, BLACK],
                   [BLACK, WHITE, WHITE,  WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, BLACK],
                   [BLACK, WHITE, WHITE,  WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, BLACK],
                   [BLACK, BLACK, WHITE,  WHITE, WHITE, WHITE, WHITE, WHITE, BLACK, BLACK],
                   [BLACK, BLACK, BLACK,  WHITE, WHITE, WHITE, WHITE, BLACK, BLACK, BLACK],
                   [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK]])

X = 'x'
Y = 'y'
RED = 'r'
GRN = 'g'
COLOR = 'color'
SCORE = 'score'
SEQ = 'seq'
I = 'i'
J = 'j'
X0 = 'x0'
Y0 = 'y0'
X1 = 'x1'
Y1 = 'y1'
ZOOM = 'zoom'
PATH = 'path'
FULL_PATH = 'full_path'
CROP_PATH = 'crop_path'
COL = 'col'
LABEL = 'label'
BATCH = 'batch'
IS_TRUE = 'is_true'
IS_IGNORE = 'is_ignore'
IS_IGNORE_SMALL = 'small'

PNG = '.png'
CROPPED = 'crops'
PATH_CROPPED = 'C:/leftImg8bit/crops'
DIRECTORY_TRUE = '/True'
DIRECTORY_FALSE = '/False'
DIRECTORY_IGNORE = '/Ignore'


default_base_dir = r'C:\leftImg8bit'
attention_results = 'attention_results'
# crops_dir = os.path.join(attention_results, 'crop')
crops_dir = os.path.join('crops')
attention_results_h5 = 'attention_results.h5'
crop_results_h5 = 'crop_results.h5'
models_output_dir = 'logs_and_models'
logs_dir = 'logs'
model_name = 'my_model_final_2'

BASE_DIR = 'C:/leftImg8bit'

DIR_TRUE = 'True'
DIR_FALSE = 'False'
DIR_IGNORE = 'Ignore'

EXTENSION_IMG = '_leftImg8bit.png'

# Crop size:
default_crop_w = 96
default_crop_h = 32

FALSE_THRESHOLD = 40
TRUE_THRESHOLD = 60
HIGHER_THRESHOLD = 95


num_of_epochs = 2

# Layers param:
kernel_dimention = 2
conv_kernel_shape = (3, 3)
kernel_sub = 0  # 3-4 = 0 , 5-6 = 1, 7,8 = 2 and so on...
max_pooling_kernel_shape = (2, 2)
max_pooling_stride = 1
padding = 1

num_of_layers = 5
second_num_of_channels = 5




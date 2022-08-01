try:
    import os
    import json
    import glob
    import argparse
    import numpy as np
    from scipy import signal as sg
    from scipy.ndimage import maximum_filter
    from PIL import Image
    import matplotlib.pyplot as plt
    import cv2
    from skimage.feature import peak_local_max
except ImportError:
    print("Need to fix the installation")
    raise


# kernel = np.array([[-0.04, -0.04, -0.04, -0.04, -0.04],
#                    [-0.04, 0.04,  0.04, 0.04, -0.04],
#                    [-0.04,  0.04,  0.04, 0.04, -0.04],
#                    [-0.04,  0.04,  0.04,  0.04, -0.04],
#                    [-0.04, -0.04, -0.04, -0.04, -0.04]])
#
#
# kernel = np.array([[-0.64, -0.64, -0.64, -0.64, -0.64],
#                    [-0.64, 1.1377777777,  1.1377777777, 1.1377777777, -0.64],
#                    [-0.64,  1.1377777777,  1.1377777777, 1.1377777777, -0.64],
#                    [-0.64,  1.1377777777,  1.1377777777,  1.1377777777, -0.64],
#                    [-0.64, -0.64, -0.64, -0.64, -0.64]])

#
# kernel = np.array([[0.04, 0.04, 0.04, 0.04, 0.04],
#                    [0.04, -0.04,  -0.04, -0.04, 0.04],
#                    [0.04,  -0.04,  -0.04, -0.04, 0.04],
#                    [0.04,  -0.04,  -0.04,  -0.04,  0.04],
#                    [0.04, 0.04, 0.04, 0.04, 0.04]])
#
#
# kernel = np.array([[0.64, 0.64, 0.64, 0.64, 0.64],
#                    [0.64, -0.026666666666,  -0.026666666666, -0.026666666666, 0.64],
#                    [0.64,  -0.026666666666,  -0.026666666666, -0.026666666666, 0.64],
#                    [0.64, -0.026666666666,  -0.026666666666, -0.026666666666,  0.64],
#                    [0.64, 0.64, 0.64, 0.64, 0.64]])

# BLACK = -0.64
# WHITE = 0.36
# kernel = np.array([[BLACK,BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
#                    [BLACK, WHITE, WHITE,  WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, BLACK],
#                    [BLACK, WHITE, WHITE,  WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, BLACK],
#                    [BLACK, WHITE, WHITE,  WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, BLACK],
#                    [BLACK, WHITE, WHITE,  WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, BLACK],
#                    [BLACK, WHITE, WHITE,  WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, BLACK],
#                    [BLACK, WHITE, WHITE,  WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, BLACK],
#                    [BLACK, WHITE, WHITE,  WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, BLACK],
#                    [BLACK, WHITE, WHITE,  WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, BLACK],
#                    [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK]])


# BLACK = -0.4
# GRAY = -0.1
# WHITE = 0.39183
#
# kernel = np.array([[BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
#                    [BLACK, GRAY,  GRAY,  GRAY,  GRAY,  GRAY,  GRAY,  GRAY,  GRAY, GRAY,   BLACK],
#                    [BLACK, GRAY, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, GRAY,   BLACK],
#                    [BLACK, GRAY, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, GRAY,   BLACK],
#                    [BLACK, GRAY, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, GRAY,   BLACK],
#                    [BLACK, GRAY, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, GRAY,   BLACK],
#                    [BLACK, GRAY, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, GRAY,   BLACK],
#                    [BLACK, GRAY, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, GRAY,   BLACK],
#                    [BLACK, GRAY, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, GRAY,   BLACK],
#                    [BLACK, GRAY,  GRAY, GRAY,   GRAY,  GRAY,  GRAY,  GRAY,  GRAY, GRAY,   BLACK],
#                    [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK]
#                    ])
#

BLACK = -0.54
WHITE = 0.26666666667
kernel = np.array([[BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK],
                   [BLACK, WHITE, WHITE,  WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, BLACK],
                   [BLACK, WHITE, WHITE,  WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, BLACK],
                   [BLACK, WHITE, WHITE,  WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, BLACK],
                   [BLACK, WHITE, WHITE,  WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, BLACK],
                   [BLACK, WHITE, WHITE,  WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, BLACK],
                   [BLACK, WHITE, WHITE,  WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, BLACK],
                   [BLACK, WHITE, WHITE,  WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE,  BLACK],
                   [BLACK, WHITE, WHITE,  WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE,  BLACK],
                   [BLACK, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, BLACK],
                   [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK,  BLACK]
                   ])

threshold = 100


def find_tfl_lights(c_image: np.ndarray, **kwargs):
    """
    Detect candidates for TFL lights. Use c_image, kwargs and you imagination to implement
    :param c_image: The image itself as np.uint8, shape of (H, W, 3)
    :param kwargs: Whatever config you want to pass in here
    :return: 4-tuple of x_red, y_red, x_green, y_green
    """
    ### WRITE YOUR CODE HERE ###
    ### USE HELPER FUNCTIONS ###

    return [500, 510, 520], [500, 500, 500], [700, 710], [500, 500]


### GIVEN CODE TO TEST YOUR IMPLENTATION AND PLOT THE PICTURES
def show_image_and_gt(image, objs, fig_num=None):
    plt.figure(fig_num).clf()
    plt.imshow(image)
    labels = set()
    if objs is not None:
        for o in objs:
            poly = np.array(o['polygon'])[list(np.arange(len(o['polygon']))) + [0]]
            plt.plot(poly[:, 0], poly[:, 1], 'r', label=o['label'])
            labels.add(o['label'])
        if len(labels) > 1:
            plt.legend()


def test_find_tfl_lights(image_path, json_path=None, fig_num=tuple):
    """ Run the attention code """
    # image = np.array(make_image_grayscale(image_path))
    image = np.array(Image.open(image_path))
    # blue, green, red = cv2.split(image)
    show_image(image)

    # image = resize_images(image, (256, 256))
    # image = np.array(Image.open(image_path))
    # if json_path is None:
    #     objects = None
    # else:
    #     gt_data = json.load(open(json_path))
    #     what = ['traffic light']
    #     objects = [o for o in gt_data['objects'] if o['label'] in what]
    # show_image_and_gt(image, objects, fig_num)
    red_x, red_y, green_x, green_y = find_tfl_lights(image)
    plt.plot(red_x, red_y, 'ro', color='r', markersize=4)
    plt.plot(green_x, green_y, 'ro', color='g', markersize=4)


def plot_image():
    plt.figure()
    plt.clf()


def show_image(image):
    print(image.shape)
    print(kernel.shape)
    print("kernel sum: " + str(kernel.sum()))

    plot_image()
    h = plt.subplot(111)
    plt.imshow(image)

    convolve_red(image, h)
    convolve_green(image, h)

    plt.show(block=True)
    # conv = sg.convolve2d(image, kernel)


def convolve_red(image, h):
    red_filtered_image = Image.fromarray(image[:, :, 0])
    plot_image()
    plt.subplot(111, sharex=h, sharey=h)
    red_conv = sg.convolve(red_filtered_image, kernel)
    plt.imshow(red_conv, cmap='gray')
    # plt.imshow(red_conv) # ??
    red_image_conv = Image.fromarray(red_conv)
    plot_image()
    plt.subplot(111, sharex=h, sharey=h)
    plt.imshow(red_image_conv)


def convolve_green(image, h):
    green_filtered_image = Image.fromarray(image[:, :, 1])
    plot_image()
    plt.subplot(111, sharex=h, sharey=h)
    plt.imshow(green_filtered_image)
    green_conv = sg.convolve(green_filtered_image, kernel)
    plt.imshow(green_conv, cmap='gray')

    green_image_conv = Image.fromarray(green_conv)
    plot_image()
    plt.subplot(111, sharex=h, sharey=h)
    plt.imshow(green_image_conv)


def make_image_grayscale(image_path):
    im = plt.imread(image_path)
    img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    return img


def resize_images(image, new_size):
    return cv2.resize(image, new_size)


def main(argv=None):
    """It's nice to have a standalone tester for the algorithm.
    Consider looping over some images from here, so you can manually exmine the results
    Keep this functionality even after you have all system running, because you sometime want to debug/improve a module
    :param argv: In case you want to programmatically run this"""
    parser = argparse.ArgumentParser("Test TFL attention mechanism")
    parser.add_argument('-i', '--image', type=str, help='Path to an image')
    parser.add_argument("-j", "--json", type=str, help="Path to json GT for comparison")
    parser.add_argument('-d', '--dir', type=str, help='Directory to scan images in')
    args = parser.parse_args(argv)
    default_base = "test"

    if args.dir is None:
        args.dir = default_base
    flist = glob.glob(os.path.join(args.dir, '*_leftImg8bit.png'))

    for image in flist:
        json_fn = image.replace('_leftImg8bit.png', '_gtFine_polygons.json')

        if not os.path.exists(json_fn):
            json_fn = None
        test_find_tfl_lights(image, json_fn)

    if len(flist):
        print("You should now see some images, with the ground truth marked on them. Close all to quit.")
    else:
        print("Bad configuration?? Didn't find any picture to show")
    plt.show(block=True)


if __name__ == '__main__':
    main()


# Convert image RGB to grayscale
# from PIL import Image
# img = Image.open('image.png').convert('L')
# img.save('greyscale.png')

# threshold = 100
#
# gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# kernel = np.ones((9, 9), np.uint8)
# tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)
# ret, thresh = cv2.threshold(tophat, threshold, 255, cv2.THRESH_BINARY)
#
# dist_transform = cv2.distanceTransform(thresh, cv2.DIST_L2, 5)
# ret, markers = cv2.connectedComponents(np.uint8(dist_transform))
# watershed = cv2.watershed(im, markers)
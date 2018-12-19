# -*- coding: utf-8 -*-
import PIL

import numpy as np
import cv2 as cv2


def image_resize(image, max_width=None, max_height=None):
    height, width = image.shape[:2]

    # only shrink if img is bigger than required
    if max_height < height or max_width < width:
        # get scaling factor
        scaling_factor = max_height / float(height)
        if max_width / float(width) < scaling_factor:
            scaling_factor = max_width / float(width)
        # resize image
        image = cv2.resize(image, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)

    return image


def segment_image(image_url):
    image_url = str(image_url).replace('\\', '/')
    image = cv2.imread(image_url)
    image = image_resize(image, 500, 500)
    image2 = image.copy()
    mask = np.zeros(image.shape[:2], dtype=np.uint8)

    cv2.rectangle(image, (0, 0), (image.shape[1] - 1, image.shape[0] - 1), [255, 0, 0], 2)
    rect = (min(0, 0), min(0, 0), abs(image.shape[1] - 1), abs(image.shape[0] - 1))

    # Número de iterações da segmentação = 3
    for x in range(3):
        bgdmodel = np.zeros((1, 65), np.float64)
        fgdmodel = np.zeros((1, 65), np.float64)
        cv2.grabCut(image2, mask, rect, bgdmodel, fgdmodel, 1, cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask == 1) + (mask == 3), 255, 0).astype('uint8')

    RGB_image = cv2.cvtColor(cv2.bitwise_and(image, image2, mask=mask2), cv2.COLOR_BGR2RGB)
    img = PIL.Image.fromarray(RGB_image)
    return img


def segment_image_base64(image):
    image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
    image = image_resize(image, 500, 500)
    image2 = image.copy()
    mask = np.zeros(image.shape[:2], dtype=np.uint8)

    cv2.rectangle(image, (0, 0), (image.shape[1] - 1, image.shape[0] - 1), [255, 0, 0], 2)
    rect = (min(0, 0), min(0, 0), abs(image.shape[1] - 1), abs(image.shape[0] - 1))

    # Número de iterações da segmentação = 3
    for x in range(3):
        bgdmodel = np.zeros((1, 65), np.float64)
        fgdmodel = np.zeros((1, 65), np.float64)
        cv2.grabCut(image2, mask, rect, bgdmodel, fgdmodel, 1, cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask == 1) + (mask == 3), 255, 0).astype('uint8')

    RGB_image = cv2.cvtColor(cv2.bitwise_and(image, image2, mask=mask2), cv2.COLOR_BGR2RGB)
    img = PIL.Image.fromarray(RGB_image)
    return img


def segment_image_base64_full(image_data, foreground_image_data, background_image_data):
    image = cv2.cvtColor(image_data, cv2.COLOR_RGBA2RGB)
    image = image_resize(image, 500, 500)

    # Transform foreground to binary
    foreground_image = cv2.cvtColor(foreground_image_data, cv2.COLOR_RGBA2GRAY)
    foreground_image = image_resize(foreground_image, 500, 500)
    foreground_image = cv2.threshold(foreground_image, 128, 255, cv2.THRESH_BINARY)[1]

    # Transform background to binary
    background_image = cv2.cvtColor(background_image_data, cv2.COLOR_RGBA2GRAY)
    background_image = image_resize(background_image, 500, 500)
    background_image = cv2.bitwise_not(cv2.threshold(background_image, 128, 255, cv2.THRESH_BINARY)[1])

    image2 = image.copy()
    mask = np.zeros(image.shape[:2], dtype=np.uint8)

    cv2.rectangle(image, (0, 0), (image.shape[1] - 1, image.shape[0] - 1), [255, 0, 0], 0)
    rect = (min(0, 0), min(0, 0), abs(image.shape[1] - 1), abs(image.shape[0] - 1))

    # Número de iterações da segmentação = 3
    for x in range(3):
        bgdmodel = np.zeros((1, 65), np.float64)
        fgdmodel = np.zeros((1, 65), np.float64)
        cv2.grabCut(image2, mask, rect, bgdmodel, fgdmodel, 1, cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask == 1) + (mask == 3), 255, 0).astype('uint8')
    mask2 = cv2.addWeighted(mask2, 1, foreground_image, 1, 0)
    mask3 = cv2.addWeighted(mask2, 0.5, background_image, 0.5, 0)
    mask3 = cv2.threshold(mask3, 128, 255, cv2.THRESH_BINARY)[1]

    RGB_image = cv2.cvtColor(cv2.bitwise_and(image, image2, mask=mask3), cv2.COLOR_BGR2RGB)
    img = PIL.Image.fromarray(RGB_image)
    return img

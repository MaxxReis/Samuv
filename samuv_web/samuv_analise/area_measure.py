# -*- coding: utf-8 -*-
import scipy.spatial.distance as dist
from imutils import perspective, contours
import numpy as np
import imutils
import cv2

known_obj_width = 2
minimal_contour_area = 100


def midpoint(ptA, ptB):
    return (ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5


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


# CORREÇÕES DA ANALISE

def segment_image(image, foreground_image):
    # Transform foreground_image to binary
    foreground_image = image_resize(foreground_image, 500, 500)
    foreground_image = cv2.cvtColor(foreground_image, cv2.COLOR_RGB2GRAY)
    foreground_image = cv2.GaussianBlur(foreground_image, (7, 7), 0)
    foreground_image = cv2.threshold(foreground_image, 128, 255, cv2.THRESH_BINARY)[1]
    # FILL INSIDE CONTOURS
    th, im_th = cv2.threshold(foreground_image, 220, 255, cv2.THRESH_BINARY_INV)
    im_floodfill = im_th.copy()
    h, w = im_th.shape[:2]
    mask = np.zeros((h + 2, w + 2), np.uint8)
    cv2.floodFill(im_floodfill, mask, (0, 0), 0)
    image = image_resize(image, 500, 500)

    return cv2.bitwise_and(image, image, mask=im_floodfill)


def getContours(segmented_image):
    # perform edge detection, then perform a dilation + erosion to
    # close gaps in between object edges
    edged = cv2.Canny(segmented_image, 50, 100)
    edged = cv2.dilate(edged, None, iterations=1)
    edged = cv2.erode(edged, None, iterations=1)

    # find contours in the edge map
    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return cnts[0] if imutils.is_cv2() else cnts[1]


def get_pixel_per_metric(segmented_image):
    try:
        cnts = getContours(segmented_image)

        if cnts:
            # sort the contours from left-to-right and initialize the
            # 'pixels per metric' calibration variable
            (cnts, _) = contours.sort_contours(cnts)
            pixelsPerMetric = None

            for c in cnts:
                area = cv2.contourArea(c)

                # if the contour is not sufficiently large, ignore it
                if area < minimal_contour_area:
                    continue

                # compute the rotated bounding box of the contour
                orig = segmented_image.copy()
                box = cv2.minAreaRect(c)
                box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
                box = np.array(box, dtype="int")

                # order the points in the contour such that they appear
                # in top-left, top-right, bottom-right, and bottom-left
                # order, then draw the outline of the rotated bounding
                # box
                box = perspective.order_points(box)

                # unpack the ordered bounding box, then compute the midpoint
                # between the top-left and top-right coordinates, followed by
                # the midpoint between bottom-left and bottom-right coordinates
                (tl, tr, br, bl) = box
                (tltrX, tltrY) = midpoint(tl, tr)
                (blbrX, blbrY) = midpoint(bl, br)

                # compute the midpoint between the top-left and top-right points,
                # followed by the midpoint between the top-righ and bottom-right
                (tlblX, tlblY) = midpoint(tl, bl)
                (trbrX, trbrY) = midpoint(tr, br)

                # draw lines between the midpoints
                cv2.line(orig, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)),
                         (255, 0, 255), 2)
                cv2.line(orig, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)),
                         (255, 0, 255), 2)

                # compute the Euclidean distance between the midpoints
                dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))

                return float('%.4g' % (dB / known_obj_width))
    except:
        return 0


def measure(segmented_image, pixelsPerMetric):
    if pixelsPerMetric == 0 or pixelsPerMetric == None:
        return 0

    cnts = getContours(segmented_image)

    if cnts:
        # sort the contours from left-to-right and initialize the
        # 'pixels per metric' calibration variable
        (cnts, _) = contours.sort_contours(cnts)

        # draw contours (optional)
        cv2.drawContours(segmented_image, cnts, -1, (0, 0, 255), 1)

        contours_area = 0
        known_obj_area = None

        for c in cnts:
            area = cv2.contourArea(c)

            # if the contour is not sufficiently large, ignore it
            if area < minimal_contour_area:
                continue

            # compute the rotated bounding box of the contour
            orig = segmented_image.copy()
            box = cv2.minAreaRect(c)
            box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
            box = np.array(box, dtype="int")

            # order the points in the contour such that they appear
            # in top-left, top-right, bottom-right, and bottom-left
            # order, then draw the outline of the rotated bounding
            # box
            box = perspective.order_points(box)
            cv2.drawContours(orig, [box.astype("int")], -1, (0, 255, 0), 2)

            # unpack the ordered bounding box, then compute the midpoint
            # between the top-left and top-right coordinates, followed by
            # the midpoint between bottom-left and bottom-right coordinates
            (tl, tr, br, bl) = box
            (tltrX, tltrY) = midpoint(tl, tr)
            (blbrX, blbrY) = midpoint(bl, br)

            # compute the midpoint between the top-left and top-right points,
            # followed by the midpoint between the top-righ and bottom-right
            (tlblX, tlblY) = midpoint(tl, bl)
            (trbrX, trbrY) = midpoint(tr, br)

            # draw lines between the midpoints
            cv2.line(orig, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)),
                     (255, 0, 255), 2)
            cv2.line(orig, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)),
                     (255, 0, 255), 2)

            # compute the Euclidean distance between the midpoints
            dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
            dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))

            # compute the size of the object
            dimA = float('%.4g' % (dA / pixelsPerMetric))
            dimB = float('%.4g' % (dB / pixelsPerMetric))

            # calculate area to cm
            area = float('%.4g' % (cv2.contourArea(c) / (pixelsPerMetric ** 2)))

            # draw the object sizes on the image
            cv2.putText(orig, "{:.1f}in".format(dimA),
                        (int(tltrX - 15), int(tltrY - 10)), cv2.FONT_HERSHEY_SIMPLEX,
                        0.65, (255, 255, 255), 2)
            cv2.putText(orig, "{:.1f}in".format(dimB),
                        (int(trbrX + 10), int(trbrY)), cv2.FONT_HERSHEY_SIMPLEX,
                        0.65, (255, 255, 255), 2)

            if known_obj_area == None:
                known_obj_area = area
            else:
                contours_area += area

    return float('%.4g' % (contours_area - known_obj_area))

"""Coloring-page line art traced from a picture.

grayscale -> Sobel gradient magnitude -> keep pixels above the 90th percentile -> drop specks smaller than
~40 px -> black lines on white -> png. Works best on art with a plain background (single characters).

    python3 lineart.py <image key or path> <out.png> [percentile] [min_size]
"""
import os, sys
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage


def trace(src, dst, pct=90, min_size=40, blur=0, thicken=0):
    """Write black-on-white line art of image `src` to `dst`. `blur` (px) smooths JPEG noise first;
    `thicken` (iterations) widens the lines afterwards. Both default off."""
    im = Image.open(src).convert('L')
    if blur:
        im = im.filter(ImageFilter.GaussianBlur(blur))
    a = np.asarray(im, dtype=float)
    mag = np.hypot(ndimage.sobel(a, axis=1), ndimage.sobel(a, axis=0))
    mask = mag > np.percentile(mag, pct)
    lab, n = ndimage.label(mask, structure=np.ones((3, 3)))
    if n:
        sizes = ndimage.sum(mask, lab, range(1, n + 1))
        mask = np.isin(lab, np.nonzero(sizes >= min_size)[0] + 1)
    if thicken:
        mask = ndimage.binary_dilation(mask, iterations=thicken)
    Image.fromarray(np.where(mask, 0, 255).astype('uint8')).save(dst)
    return dst


if __name__ == '__main__':
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from common import img_path
    a = sys.argv[1:]
    trace(img_path(a[0]), a[1], float(a[2]) if len(a) > 2 else 90, int(a[3]) if len(a) > 3 else 40)
    print(a[1])

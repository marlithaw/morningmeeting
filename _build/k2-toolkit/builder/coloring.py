"""Trace a white-background character image into a black-line coloring page PNG.

Usage: python3 coloring.py <source art name> <output png name> [percentile]
Works best on art with a plain white background (single characters, not full classroom scenes).
"""
import sys, os
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage
from common import ASSETS


def trace(src, dst, pct=90, min_size=40):
    im = Image.open(os.path.join(ASSETS, 'img', src + '.jpg')).convert('L')
    im = im.filter(ImageFilter.GaussianBlur(1.2))
    a = np.asarray(im, dtype=float)
    gx = ndimage.sobel(a, axis=1); gy = ndimage.sobel(a, axis=0)
    mag = np.hypot(gx, gy)
    mask = mag > np.percentile(mag, pct)
    lab, n = ndimage.label(mask)
    sizes = ndimage.sum(mask, lab, range(1, n + 1))
    keep = np.isin(lab, np.where(sizes >= min_size)[0] + 1)
    keep = ndimage.binary_dilation(keep, iterations=1)
    out = np.where(keep, 0, 255).astype('uint8')
    Image.fromarray(out).save(os.path.join(ASSETS, 'img', dst))
    return dst


if __name__ == '__main__':
    trace(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 90)

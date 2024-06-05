from PIL import Image
import numpy as np
import os


class VOCPalette(object):
    def __init__(self, nb_class=21, start=1):
        self.palette = [0] * 768
        if nb_class > 21 or nb_class < 2:
            nb_class = 21
        if start > 20 or start < 1:
            start = 1
        pal = self.labelcolormap(21)
        self.palette[0] = pal[0][0]
        self.palette[1] = pal[0][1]
        self.palette[2] = pal[0][2]
        for i in range(nb_class):
            self.palette[(i + 1) * 3] = pal[start][0]
            self.palette[(i + 1) * 3 + 1] = pal[start][1]
            self.palette[(i + 1) * 3 + 2] = pal[start][2]
            start = (start + 1) % 21
            if start == 0:
                start = 1
        assert len(self.palette) == 768

    def genlabelpal(self, img_arr):
        img = Image.fromarray(img_arr)
        img.putpalette(self.palette)

        return img

    def genlabelfilepal(self, path, isCoverLab):
        label_list = os.listdir(path)
        label_list.sort()
        for name in label_list:
            if name.endswith(".png"):
                img = Image.open(path + "/" + name).convert('L')
                shotname, extension = os.path.splitext(name)
                if isCoverLab == True:
                    img_arr = np.array(img)
                    img_arr[np.where(img_arr == 255)] = 1  # for 2 classes: 255->1
                    img = Image.fromarray(img_arr)
                img.putpalette(self.palette)
                img.save(path + "/" + shotname + ".png")

    def uint82bin(self, n, count=8):
        """returns the binary of integer n, count refers to amount of bits"""
        return ''.join([str((n >> y) & 1) for y in range(count-1, -1, -1)])

    def labelcolormap(self, N):
        cmap = np.zeros((N, 3), dtype = np.uint8)
        for i in range(N):
            r = 0
            g = 0
            b = 0
            id = i
            for j in range(7):
                str_id = self.uint82bin(id)
                r = r ^ (np.uint8(str_id[-1]) << (7-j))
                g = g ^ (np.uint8(str_id[-2]) << (7-j))
                b = b ^ (np.uint8(str_id[-3]) << (7-j))
                id = id >> 3
            cmap[i, 0] = r
            cmap[i, 1] = g
            cmap[i, 2] = b
        return cmap

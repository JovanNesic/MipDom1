import numpy as np
import tifffile



def loadImg(path):
    if path.endswith(".csv"):
        from numpy import genfromtxt
        return genfromtxt(path, delimiter=",")
    else:
        # img = Image.open(path)
        # return np.array(img)
        return tifffile.imread(path)

HE = loadImg("HE.tif")
LE = loadImg("LE.tif")

#TE = HE/2 + LE/2
##TE = loadImg("TE.tif")
#prs = np.average(TE)*0.545 ##kod za proveru
#
#img2 = (TE < prs) * 2**16-1
##tifffile.imwrite("output1.tif", img2)

prs1 = np.average(LE)*0.545
prs2 = np.average(HE)*0.545

img2 = ((LE < prs1) & (HE < prs2)) * 2**16-1
tifffile.imwrite("output.tif", img2)
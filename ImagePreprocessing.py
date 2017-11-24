import cv2
import numpy as np
from colour_demosaicing import demosaicing_CFA_Bayer_Malvar2004, mosaicing_CFA_Bayer
import imageio

def ReadExpoTimes(fileName):
	return np.power(2, np.loadtxt(fileName))

def ReadImages(fileNames):
	imgs = []
	for img in fileNames:
		imgs.append(cv2.imread(img))
	return np.array(imgs)

def Demosaic(imgs):
	demosaicedArray = []
	for img in imgs:
		img = mosaicing_CFA_Bayer(img)
		img = demosaicing_CFA_Bayer_Malvar2004(img)
		demosaicedArray.append(img)
	return demosaicedArray

def ApplyGammaCorrection(imgs):
	return np.power(imgs,1/GAMMA)

def ResizeImgs(imgs, width, height):
	resizedImgs = []
	for img in imgs:
		cv2.resize(img, resizedImg, size(width,height))
		resizedImgs.append(resizedImg)
	return resizedImgs

def WriteImages(imgs, folderNames): # Possibly add extension argument
	for index, img in enumerate(imgs):
		try:
			#cv2.imwrite(folderNames[index], img)
			cv2.imwrite('Test/EXTRA/001/wroteThatOnMyOwn.tif', img)
			break
		except:
			print("Unexpected error while writing imgs :", sys.exc_info()[0])
			raise
	return

def ReadTrainingData(fileNames):
	imgs = ReadImages(fileNames)
	label = ReadLabel(fileNames[0])
	return imgs, label

def ReadLabel(fileName):
	label = imageio.imread(fileName[:fileName.rfind("/")+1] + 'HDRImg.hdr', 'hdr')
	return label

def select_subset(patches):
	maxTh = 0.8
	minTh = 0.2

	thresh = 0.5 * 40 * 40 * 3

	badInds = np.logical_or(patches > maxTh, patches < minTh)

	indices = badInds.sum(3).sum(2).sum(1) > thresh
	return np.where(indices == 1)[0]

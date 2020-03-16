import os
import random
import time

import cv2
import numpy as np
#from keras import backend as K
#from keras.models import load_model
from PIL import Image, ImageDraw, ImageFont
from timeit import time
from timeit import default_timer as timer  ### to calculate FPS


vid = cv2.VideoCapture(0)

while True:
	return_value, frame = vid.read()
	image = Image.fromarray(frame)
	result = np.asarray(image)

	accum_time = 0
	curr_fps = 0
	fps = "FPS: ??"

	cv2.putText(result, text=fps, org=(3, 15), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.50,
	                    color=(255, 0, 0), thickness=2)

	cv2.imshow("result",result)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
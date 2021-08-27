#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#for test
import sys
import time
import pandas as pd
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import  QMessageBox
import matplotlib.pyplot as plt
import numpy as np
from keras.models import load_model
from PIL import Image
import cv2 
import imutils 
from filters import filters


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('test-gui.ui', self) # Load the .ui file
        self.show() # Show the GUI
    # to connecet the buttons to their functions
        self.test_result.clicked.connect(self.loss_accuracy)
        self.test_image.clicked.connect(self.prediction)
        self.show_time.clicked.connect(self.test_time)
    
    def test_time(self):
        self.list_show_time.addItem(f"the executation time is {self.end-self.start} second")
    
    def loss_accuracy(self):
        #read csv file
        df = pd.read_csv("C:/Users/user/Desktop/bash/saved_weights/"+self.date.text()+"/log.csv")        #show result(train loss,train accuracy,test loss,test accuracy) in gui box
        self.list_show.addItem(f'end of train&test phase are:\ntrain accuracy: {df["accuracy"].iloc[-1]}\ntrain loss: {df["loss"].iloc[-1]}\ntest accuracy: {df["val_accuracy"].iloc[-1]}\ntest loss: {df["val_loss"].iloc[-1]}')
        
    def prediction(self):
        self.start = time.time()
        #load model
        model = load_model('C:/Users/user/Desktop/bash/saved_weights/2021_07_11/final.hd5',custom_objects={'filters': filters})
        #load test image
        image = Image.open(self.test_image_path.text())
        #preprocess test image
        orig=image.resize((512,512))
        image = np.expand_dims(image, axis=0)
        image = np.expand_dims(image, axis=3)
        #model prediction
        (stego,cover) = model.predict(image)[0]
        label = "Stego" if stego > cover else "Cover"
        proba = stego if stego > cover else cover
        label = "{}: {:.2f}%".format(label, proba * 100)
        #draw the label on the image
        orig.save("steganalysis_result.jpg")
        output = cv2.imread("steganalysis_result.jpg")
        output = imutils.resize(output, width=400)
        cv2.putText(output, label, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,0.7, (0, 255, 0), 2)
        #show the output image
        cv2.imshow("Output", output)
        self.end = time.time()
        cv2.waitKey(0)
        cv2.destroyAllWindows()  
        
app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
app.exec_() # 


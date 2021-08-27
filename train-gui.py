#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
from PyQt5 import QtWidgets, uic
import time
import cv2

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('train-gui.ui', self) # Load the .ui file
        self.show() # Show the GUI
        self.write_text.clicked.connect(self.write)
        self.show_result.clicked.connect(self.showing)
        self.show_train_time.clicked.connect(self.traintime)
    
    def traintime(self):
        f = open("train_time.txt", "r")
        self.train_time.addItem(f'the training time is {f.read()} seconde')
        f.close()

    def showing(self):
        image = cv2.imread('C:/Users/user/Desktop/bash/saved_weights/'+self.date.text()+'/result.png')
        image=cv2.resize(image,(1000,700))
        cv2.imshow('result',image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        #time.sleep(30)
     
    
    def write(self):
        cover_tr=self.ctrp.text()
        cover_te=self.ctep.text()
        stego_tr=self.strp.text()
        stego_te=self.step.text()
        model_ver="'"+self.model_version.text()+"'"
        n_class=self.classes.text()
        epo=self.epochs.text()
        b_size=self.batch_size.text()
        output=self.output_path.text()
        Lines=[cover_tr,cover_te,stego_tr,stego_te,model_ver,n_class,epo,b_size,output]
        with open('sample.txt', 'w') as f:
            for line in Lines:
                f.write(line.rstrip('\r'))
                f.write('\n')
        f.close()


app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
app.exec_() # 


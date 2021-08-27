# CNN-for-Steganalysis
using CNN classifier to classify data (stego/cover) with ''Catalyst Kernels''

## Overall Discription
similar as to documents in [link](https://github.com/behnoudshafizadeh/Preliminary-StegAnalysis) previous work, i continue my previous research to classify steganalysis data in two different groups (stego/cover) basis on CNN structure in below :

![image](https://user-images.githubusercontent.com/53394692/131138786-f4b03c23-c03e-420b-a6bc-48448c668796.png)

as a main contribution we use these four pre-processing kernels to boost steganographics signals and extract distinguishable features for seprating them as two different categories (stego/cover) :

![image](https://user-images.githubusercontent.com/53394692/131144005-7d8908d7-d6b1-490e-a6a7-62c549a6e378.png)

## Parameters in CNN
```
 Dataset BOSSbase v1.01  : which contain 10,000 cover images of size 128 * 128 . 
 Dataset WOW,S-Uniward with 0.4,0.8 bpp stego images
 train and test : so we have 7000 pairs (stego,cover) train images ,3000 pairs (stego,cover) test images
 using mini batch of 16 (8 cover/stego pairs)
 the code is implemented on Keras API
 using RMS-Prop optimizer with binary cross Antropy loss function 
 100 epochs

```
## Implementing phase
the way to do this, run this `./behnoud.sh` command in your powershell, and will be faced with following step :

```
# instructions in ./behnoud.sh
#!/bin/bash

python train-gui.py

i=0
input="sample.txt"
while IFS= read -r line
do
  array+=($line)
  echo ${array[i]}
  i=$(($i+1))
done < "$input"


python main.py --ctrp ${array[0]} --ctep ${array[1]} --strp ${array[2]}  --step ${array[3]} --model_version 1.0.0 --nc ${array[5]} --ne ${array[6]} --bs ${array[7]} --shuffle  --op saved_weights -v 1
```

* in first step, `train-gui.py` is implemented and fill boxes in `train-gui` basis on your settings :

![train-gui](https://user-images.githubusercontent.com/53394692/131153034-16aeb42a-6402-4b00-a769-dd97fc959c7b.png)

* the filled contents, saved in `sample.txt` file to use in next step for starting training phase by `main.py`. actually, `for loop` in bash save each contents in as an `array`.
* in third step, `main.py` runned to start train phase (after clicking `train` button).
* finally you can show the results of train phase by clicking on `result` as below and see the training phase time by clicking on `train time` button :
(see two charts related to training loss/acc and validation loss/acc)

![train-gui](https://user-images.githubusercontent.com/53394692/131154326-543096c4-f8df-4fe0-8c73-be997b78c884.png)

## Testing on different stego datasets
for comparing results between various stego dataset, we implemented training phase on 5 different ways, see below :

![image](https://user-images.githubusercontent.com/53394692/131154645-ffc06bc9-9979-40a9-8521-3c19677d89cc.png)


## Testing on different images
for testing on random images, run `test-gui.py` and fill the blancs :

![test-gui](https://user-images.githubusercontent.com/53394692/131156059-a9fc3000-4010-4612-9f6e-104595336f1e.png)

clicking on `show result` button lead to depict the `acc/loss` related to last `epoch` in training phase. writing your custom path and click on `test image` button to see the result of test phase. and finally `test time` lead to show time of processor when it process each test  image :

![image](https://user-images.githubusercontent.com/53394692/131156401-8da87a1a-fd80-4cd6-a039-85b4da03486e.png)


## Conclusion

* We implemented a new CNN model for Steganalysis with small scale images and low-cost computing resources.(simple structure)
* The CNN model showed good performance by getting high accuracy in undetectable steganographic algorithms.
* Our CNN architecture are used on different types of steganographic algorithms such as (wow, s-uniward, combination of them) with different bpp rates
* Using deep learning rather than statistical models lead to extract complex features in our dataset which cause high detectable features rather handy-level features 

























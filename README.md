# trashsure-ml-detection-model

download the model h5 or tflite from:
https://drive.google.com/drive/u/0/folders/1_Qf_deQcGObEAP5R18PNvTeBwpn45MfO


# Test detection model
Make sure to follow these steps before testing the detection model:

1. download the TACO dataset images:
`python download.py` 

2. go to the `detector` directory and run this command:
`python detector.py test --dataset=../data --model=models --round 0 --class_map=./taco_config/map_10.csv`

- else if you are encountering python version error, try:
`py -3.9 detector.py test --dataset=../data --model=models --round 0 --class_map=./taco_config/map_10.csv`

3. Done
You should see a window showing the detected images in 3 different modes.
 - Predictions, 
 - Prediction Fused
 - GT

# Convert Mask R-CNN architecture h5 to tflite

`tflite.ipynb`

# Install requirements

`pip install -r requirements.txt`
# TrashSure ML Detection Model

download the model h5 or tflite from:
https://drive.google.com/drive/u/0/folders/1_Qf_deQcGObEAP5R18PNvTeBwpn45MfO


## Pre-Requisites

Before using this classification model, please ensure that you have the following prerequisites in place:

1. **Python**: You need to have Python installed, preferably version 3.8 or later.

2. **Python Packages**: The necessary Python packages for running the model are listed in the `requirements.txt` file. You can install these packages using `pip` as shown below.


## Test detection model

To get started with the TrashSure ML Detection Model, follow these steps:

1. Clone this repository to your local device using `git`:

    ```bash
    git clone https://github.com/TrashSure-Team/trashsure-ml-detection-model.git

2. Change your current directory to the repository:

   ```
   cd trashsure-ml-classification-model
   ```

3. Create and activate a virtual environment:

   ```
   python3 -m venv env
   source env/bin/activate
   ```
4. Install the required Python packages from the `requirements.txt` file:
   ```
   pip install -r requirements.txt

## Test

If you want to see our model in action with pre-annotated Trash images, follow these steps:

1. Make sure you fulfill all the requirements mentioned from the `requirements.txt` 

2. Run this command to <b>Download</b> the TACO dataset images (This may take a while):

    ```
    python download.py
    ```

3. Go to the `detector` directory:

    ```
    cd detector
    ```
4. Run the `detector.py` model using this command:

    ```
    python detector.py test --dataset=../data --model=models --round 0 --class_map=./taco_config/map_10.csv
    ```

# Convert Mask R-CNN architecture h5 to tflite
See `tflite.ipynb`.

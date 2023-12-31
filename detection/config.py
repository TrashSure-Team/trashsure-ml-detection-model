import math
import numpy as np

class Config(object):
    NAME = None
    GPU_COUNT = 1
    IMAGES_PER_GPU = 2
    STEPS_PER_EPOCH = 1000
    VALIDATION_STEPS = 50

    # Backbone Network Architecture
    BACKBONE = "resnet50"

    # Optimizer
    OPTIMIZER = 'SGD'

    # The strides of each layer of the FPN Pyramid.
    BACKBONE_STRIDES = [4, 8, 16, 32, 64]

    # Number of Classification Classes
    NUM_CLASSES = 1  # Override in sub-classes

    # Length of Square Anchor Side in Pixels
    RPN_ANCHOR_SCALES = (32, 64, 128, 256, 512)

    # Ratios of anchors at each cell (width/height)
    RPN_ANCHOR_RATIOS = [0.5, 1, 2]

    # Anchor stride
    RPN_ANCHOR_STRIDE = 1
    RPN_NMS_THRESHOLD = 0.7
    RPN_TRAIN_ANCHORS_PER_IMAGE = 256


    POST_NMS_ROIS_TRAINING = 2000
    POST_NMS_ROIS_INFERENCE = 1000

    USE_MINI_MASK = False
    MINI_MASK_SHAPE = (512, 512)  # (height, width) of the mini-mask
    IMAGE_RESIZE_MODE = "square"
    IMAGE_MIN_DIM = 800
    IMAGE_MAX_DIM = 1024
    IMAGE_MIN_SCALE = 0

    USE_OBJECT_ZOOM = True
    ZOOM_IN_FREQ = 0.5
    
    MASK_SHARE = False

    MEAN_PIXEL = np.array([123.7, 116.8, 103.9])
    
    TRAIN_ROIS_PER_IMAGE = 200
    ROI_POSITIVE_RATIO = 0.33
    POOL_SIZE = 7
    MASK_POOL_SIZE = 14
    MASK_SHAPE = [28, 28]

    # Maximum Number of Ground Truth Instances to use in one image
    MAX_GT_INSTANCES = 100

    # Bounding Box Refinement Standard Deviation for RPN and Final Detection Phase
    RPN_BBOX_STD_DEV = np.array([0.1, 0.1, 0.2, 0.2])
    BBOX_STD_DEV = np.array([0.1, 0.1, 0.2, 0.2])

    DETECTION_MAX_INSTANCES = 100
    DETECTION_MIN_CONFIDENCE = 0.7
    DETECTION_SCORE_RATIO = True

    # Non-Maximum Suppression Threshold for Object Detection
    DETECTION_NMS_THRESHOLD = 0.3
    DETECTION_CLASSLESS_NMS_THRESHOLD = 0.9


    LEARNING_RATE = 0.001
    LEARNING_MOMENTUM = 0.9

    # Regularization
    WEIGHT_DECAY = 0.0001

    # Optimization.
    LOSS_WEIGHTS = {
        "rpn_class_loss": 1.,
        "rpn_bbox_loss": 1.,
        "mrcnn_class_loss": 1.,
        "mrcnn_bbox_loss": 1.,
        "mrcnn_mask_loss": 1.
    }

    # Use RPN ROIs or externally generated ROIs for training
    USE_RPN_ROIS = True
    TRAIN_BN = False  # Defaulting to False since batch size is often small
    # Gradient norm clipping
    GRADIENT_CLIP_NORM = 5.0

    def __init__(self):
        """Set values of computed attributes."""
        # Effective batch size
        self.BATCH_SIZE = self.IMAGES_PER_GPU * self.GPU_COUNT

        # Input image size
        if self.IMAGE_RESIZE_MODE == "crop":
            self.IMAGE_SHAPE = np.array([self.IMAGE_MIN_DIM, self.IMAGE_MIN_DIM, 3])
        else:
            self.IMAGE_SHAPE = np.array([self.IMAGE_MAX_DIM, self.IMAGE_MAX_DIM, 3])

        # Image meta data length
        # See compose_image_meta() for details
        self.IMAGE_META_SIZE = 1 + 3 + 3 + 4 + 1 + self.NUM_CLASSES

    def display(self):
        """Display Configuration values."""
        print("\nConfigurations:")
        for a in dir(self):
            if not a.startswith("__") and not callable(getattr(self, a)):
                print("{:30} {}".format(a, getattr(self, a)))
        print("\n")
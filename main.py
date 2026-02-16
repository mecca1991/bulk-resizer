import argparse
import numpy as np
import cv2

def process_image():
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "source", 
        type=str, 
        help="The folder containing the images to resize")
    parser.add_argument(
        "destination", 
        type=str, 
        help="The folder where resized images will be saved"
    )
    parser.add_argument(
        "--width", 
        type=int,
        default=150,
        help="expected thumbnail width"
    )
    parser.add_argument(
        "--height",
        type=int,
        default=150,
        help="expected thumbnail height"
    )

    args = parser.parse_args()

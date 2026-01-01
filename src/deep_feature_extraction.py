
"""
Deep Feature Extraction using MobileNetV2
Concept: Extract 128-D feature vectors for image similarity verification
Author: Open for community contribution
Glory to God
"""

import tensorflow as tf
import numpy as np
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing import image

# Initialize MobileNetV2 (without top layers)
model = MobileNetV2(weights='imagenet', include_top=False, pooling='avg')

def extract_deep_features(img_path):
    """
    Extract deep feature vector from an image using MobileNetV2
    :param img_path: Path to the image file
    :return: Numpy array of feature vector
    """
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Extract features
    features = model.predict(img_array)
    return features.flatten()  # Convert to 1D vector

if __name__ == "__main__":
    test_image = "sample.jpg"
    feature_vector = extract_deep_features(test_image)
    print("Feature Vector Shape:", feature_vector.shape)
    print("Feature Vector (first 10 values):", feature_vector[:10])

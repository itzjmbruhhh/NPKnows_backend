import numpy as np
from PIL import Image, UnidentifiedImageError
from tensorflow.keras.applications.xception import preprocess_input

CLASS_LABELS = ["Healthy", "Nitrogen Deficient", "Phosphorus Deficient", "Potassium Deficient"]


def detect_leaf(image: np.ndarray) -> bool:
    green_pixels = np.sum((image[:, :, 1] > image[:, :, 0]) & (image[:, :, 1] > image[:, :, 2]))
    total_pixels = image.shape[0] * image.shape[1]
    green_ratio = green_pixels / total_pixels
    return green_ratio > 0.1


def preprocess_image(file) -> np.ndarray:
    try:
        image = Image.open(file)
        if image.mode != 'RGB':
            image = image.convert('RGB')
        img = image.resize((299, 299))
        img_array = np.array(img)
        if img_array.ndim != 3 or img_array.shape[-1] != 3:
            raise ValueError("Image must have 3 color channels (RGB).")
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)
        if not detect_leaf(img_array[0]):
            raise ValueError("The image doesn't seem to be a leaf. Ensure the image contains a clear leaf.")
        return img_array
    except UnidentifiedImageError:
        raise ValueError("Invalid image file format.")
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise ValueError(f"An unexpected error occurred: {str(e)}")
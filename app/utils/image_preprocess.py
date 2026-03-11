import numpy as np
from PIL import Image

def preprocess_image(image_file):

    image = Image.open(image_file).convert("RGB")
    image = image.resize((299, 299))

    image = np.array(image)

    if image.shape[-1] == 4:
        image = image[..., :3]

    image = image / 255.0

    return np.expand_dims(image, axis=0)
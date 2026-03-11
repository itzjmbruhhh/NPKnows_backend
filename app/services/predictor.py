import numpy as np
from .model_loader import get_model

CLASS_NAMES = {
    0: "Healthy",
    1: "Nitrogen Deficient",
    2: "Phosphorus Deficient",
    3: "Potassium Deficient"
}


def predict(image_tensor):

    model = get_model()

    preds = model.predict(image_tensor)

    idx = int(np.argmax(preds))

    confidence = float(np.max(preds))

    label = CLASS_NAMES[idx]

    return {
        "class_id": idx,
        "label": label,
        "confidence": confidence
    }
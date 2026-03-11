import numpy as np
from .model_loader import get_model
from ..utils.image_preprocess import CLASS_LABELS


def predict(image_tensor):
    model = get_model()
    preds = model.predict(image_tensor)
    idx = int(np.argmax(preds))
    confidence = float(np.max(preds))
    label = CLASS_LABELS[idx]
    return {
        "class_id": idx,
        "label": label,
        "confidence": confidence
    }
import tensorflow as tf
import os
import threading

MODEL_PATH = os.getenv("MODEL_PATH")

_model = None
_lock = threading.Lock()


def get_model():

    global _model

    if _model is None:
        with _lock:
            if _model is None:
                print("Loading TensorFlow model...")
                _model = tf.keras.models.load_model(MODEL_PATH)

    return _model
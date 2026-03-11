import os

class Config:

    HF_TOKEN = os.getenv("HF_TOKEN")

    MODEL_PATH = os.getenv(
        "MODEL_PATH",
        "models/resnet-model-npknows.h5"
    )

    CACHE_TYPE = "SimpleCache"
    CACHE_DEFAULT_TIMEOUT = int(os.getenv("CACHE_TIMEOUT", 3600))

    RATE_LIMIT = os.getenv("RATE_LIMIT", "10/minute")
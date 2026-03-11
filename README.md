# NPKnows API

Flask-based REST API for classifying bitter gourd leaf nutrient status from an uploaded image and returning a fertilizer recommendation.

---

## Features

- Image upload endpoint for leaf classification
- TensorFlow/Keras model loading with lazy singleton initialization
- Leaf-image validation heuristic before prediction
- Static fertilizer recommendation mapping per predicted class
- Rate limiting via `Flask-Limiter`
- In-memory caching via `Flask-Caching`
- Docker support with `gunicorn`

---

## Tech Stack

| Component | Version |
|---|---|
| Python | 3.10 |
| Flask | 3 |
| TensorFlow / Keras | 2.10 |
| Pillow | latest |
| NumPy | latest |
| Gunicorn | latest |
| Flask-Caching | latest |
| Flask-Limiter | latest |

---

## Project Structure

```
npknows-api/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── routes.py
│   ├── services/
│   │   ├── fertilizer_service.py
│   │   ├── model_loader.py
│   │   └── predictor.py
│   └── utils/
│       └── image_preprocess.py
├── models/
│   └── resnet-model-npknows.h5
├── Dockerfile
├── requirements.txt
└── run.py
```

---

## Model Output Classes

Defined in `app/utils/image_preprocess.py`:

- `Healthy`
- `Nitrogen Deficient`
- `Phosphorus Deficient`
- `Potassium Deficient`

---

## API Endpoint

### `POST /predict`

Accepts a multipart form upload with an image file.

**Content-Type:** `multipart/form-data`

**Form field:** `image` — the leaf image file to classify

#### Example Request

```bash
curl -X POST http://127.0.0.1:8080/predict \
  -F "image=@/absolute/path/to/leaf.jpg"
```

#### Success Response `200`

```json
{
  "prediction": {
    "class_id": 0,
    "label": "Healthy",
    "confidence": 0.9876
  },
  "recommendation": {
    "deficiency": "None — Plant is Healthy",
    "recommended_fertilizer": "Balanced NPK fertilizer (14-14-14) for maintenance",
    "application_method": "Apply as a top dressing around the base of the plant and water in",
    "dosage": "10-15g per plant every 3-4 weeks as a maintenance dose",
    "additional_notes": "Continue current care routine. Monitor regularly for early signs of deficiency or pest damage. Ensure consistent watering and good drainage to maintain plant health."
  }
}
```

#### Error Responses

| Status | Body | Cause |
|---|---|---|
| `400` | `{ "error": "No image uploaded" }` | No file in request |
| `400` | `{ "error": "Empty file submitted" }` | Empty file field |
| `422` | `{ "error": "Invalid image file format." }` | Unreadable image |
| `422` | `{ "error": "The image doesn't seem to be a leaf. Ensure the image contains a clear leaf." }` | Failed leaf heuristic |
| `500` | `{ "error": "An unexpected error occurred", "details": "..." }` | Server error |

---

## Environment Variables

Configured in `app/config.py` and `run.py`.

| Variable | Required | Default | Description |
|---|---|---|---|
| `MODEL_PATH` | **Yes** | `models/resnet-model-npknows.h5` | Path to the trained Keras model |
| `PORT` | No | `8080` | Port for local run / container |
| `FLASK_DEBUG` | No | unset | Enables Flask debug mode when set to `True` |
| `CACHE_TIMEOUT` | No | `3600` | Default timeout for SimpleCache (seconds) |
| `RATE_LIMIT` | No | `10/minute` | Config value present in app config |

> **Note:** `MODEL_PATH` must always be set explicitly. The default in `config.py` is not used by `model_loader.py` — if the env var is missing, model loading will fail.

#### Example `.env`

```env
FLASK_DEBUG=True
MODEL_PATH=models/resnet-model-npknows.h5
CACHE_TIMEOUT=3600
RATE_LIMIT=10/minute
PORT=8080
```

---

## Local Development

### 1. Create a virtual environment

```bash
python3.10 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Verify the model file exists

Default expected location:

```
models/resnet-model-npknows.h5
```

If your model is elsewhere:

```bash
export MODEL_PATH=/absolute/path/to/your/model.h5
```

### 4. Run the API

```bash
python run.py
```

API available at: `http://127.0.0.1:8080`

---

## Docker

### Build

```bash
docker build -t npknows-api .
```

### Run

```bash
docker run --rm -p 8080:8080 \
  -e MODEL_PATH=models/resnet-model-npknows.h5 \
  npknows-api
```

The container runs:

```
gunicorn --bind 0.0.0.0:8080 --workers 1 --threads 8 run:app
```

---

## How It Works

1. The uploaded file is received in `app/routes.py`
2. `app/utils/image_preprocess.py`:
   - Opens the file with Pillow
   - Converts to RGB if needed
   - Resizes to 299×299
   - Applies `tensorflow.keras.applications.xception.preprocess_input`
   - Runs a green-pixel heuristic to validate the image likely contains a leaf
3. `app/services/model_loader.py` lazily loads the Keras model from `MODEL_PATH`
4. `app/services/predictor.py` predicts the class and confidence score
5. `app/services/fertilizer_service.py` maps the predicted label to a fertilizer recommendation

---

## Fertilizer Recommendation Mapping

| Label | Action |
|---|---|
| `Nitrogen Deficient` | Nitrogen fertilizer recommendation |
| `Phosphorus Deficient` | Phosphorus fertilizer recommendation |
| `Potassium Deficient` | Potassium fertilizer recommendation |
| `Healthy` | Maintenance fertilizer recommendation |
| Unknown | Falls back to a general balanced NPK recommendation |

---

## Known Issues & Cleanup Opportunities

- `HF_TOKEN` is defined in config but no longer used — safe to remove
- `RATE_LIMIT` config value is not wired into the route decorator — `/predict` hardcodes `10 per minute`
- `MODEL_PATH` default in `config.py` is not used by `model_loader.py` — always set the env var explicitly
- The leaf heuristic runs on preprocessed values (post-Xception normalization), which may cause false negatives on some images
- Caching is initialized but no route currently uses a cache decorator
- `Dockerfile` should be removed from `.gitignore` if you intend to version it
- `.env` should contain only `KEY=VALUE` pairs — deployment commands should be moved to this README or a separate script
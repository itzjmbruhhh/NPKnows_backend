from flask import Blueprint, request, jsonify
from .utils.image_preprocess import preprocess_image
from .services.predictor import predict
from .services.fertilizer_service import fertilizer_recommendation
from . import limiter

api = Blueprint("api", __name__)


@api.route("/predict", methods=["POST"])
@limiter.limit("10 per minute")
def predict_leaf():

    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]

    image_tensor = preprocess_image(file)

    prediction = predict(image_tensor)

    recommendation = fertilizer_recommendation(
        prediction["label"]
    )

    return jsonify({
        "prediction": prediction,
        "recommendation": recommendation
    })
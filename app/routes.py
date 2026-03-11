from flask import Blueprint, request, jsonify
from .utils.image_preprocess import preprocess_image
from .services.predictor import predict
from .services.llm_service import fertilizer_recommendation

api = Blueprint("api", __name__)


@api.route("/predict", methods=["POST"])
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
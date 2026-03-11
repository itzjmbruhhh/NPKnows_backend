import os
from transformers import pipeline

HF_TOKEN = os.getenv("HF_TOKEN")

generator = pipeline(
    "text-generation",
    model="google/flan-t5-base",
    token=HF_TOKEN,
    max_new_tokens=120
)


def fertilizer_recommendation(label):

    prompt = f"""
    A bitter gourd plant leaf was classified as: {label}.

    Provide a fertilizer recommendation suitable for farmers.
    """

    result = generator(prompt)

    return result[0]["generated_text"]
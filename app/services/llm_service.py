from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="google/flan-t5-base",
    max_new_tokens=120
)


def fertilizer_recommendation(label):

    prompt = f"""
    A bitter gourd plant leaf was classified as: {label}.

    Provide a short fertilizer recommendation suitable for farmers.
    Mention fertilizer type and basic application advice.
    """

    result = generator(prompt)

    return result[0]["generated_text"]
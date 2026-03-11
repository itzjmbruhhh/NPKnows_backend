RECOMMENDATIONS = {
    "Nitrogen Deficient": {
        "deficiency": "Nitrogen (N) Deficiency",
        "recommended_fertilizer": "Urea (46-0-0) or Ammonium Sulfate (21-0-0)",
        "application_method": "Apply as soil drench or side-dress around the base of the plant, avoiding direct contact with stems",
        "dosage": "Urea: 5-10g per plant every 2 weeks. Ammonium Sulfate: 10-15g per plant every 2 weeks",
        "additional_notes": "Nitrogen deficiency shows as yellowing of older/lower leaves first. Ensure adequate watering after application to prevent fertilizer burn. Avoid over-application as excess nitrogen promotes leafy growth over fruiting."
    },
    "Phosphorus Deficient": {
        "deficiency": "Phosphorus (P) Deficiency",
        "recommended_fertilizer": "Superphosphate (0-20-0) or DAP - Diammonium Phosphate (18-46-0)",
        "application_method": "Incorporate into soil before planting or apply as a side-dress 5-8cm deep near the root zone",
        "dosage": "Superphosphate: 15-20g per plant. DAP: 8-10g per plant. Reapply every 3-4 weeks",
        "additional_notes": "Phosphorus deficiency appears as purple/reddish discoloration on the underside of leaves. Soil pH between 6.0-7.0 improves phosphorus availability. Avoid applying with calcium-rich fertilizers as it reduces absorption."
    },
    "Potassium Deficient": {
        "deficiency": "Potassium (K) Deficiency",
        "recommended_fertilizer": "Muriate of Potash (0-0-60) or Potassium Sulfate (0-0-50)",
        "application_method": "Apply as soil drench or broadcast evenly around the plant drip line and water in thoroughly",
        "dosage": "Muriate of Potash: 5-8g per plant every 3 weeks. Potassium Sulfate: 8-10g per plant every 3 weeks",
        "additional_notes": "Potassium deficiency shows as brown scorching and curling of leaf edges, starting on older leaves. Potassium Sulfate is preferred for fruiting stage as it improves fruit quality. Ensure consistent moisture for proper uptake."
    },
    "Healthy": {
        "deficiency": "None — Plant is Healthy",
        "recommended_fertilizer": "Balanced NPK fertilizer (14-14-14) for maintenance",
        "application_method": "Apply as a top dressing around the base of the plant and water in",
        "dosage": "10-15g per plant every 3-4 weeks as a maintenance dose",
        "additional_notes": "Continue current care routine. Monitor regularly for early signs of deficiency or pest damage. Ensure consistent watering and good drainage to maintain plant health."
    }
}

DEFAULT_RECOMMENDATION = {
    "deficiency": "Unknown condition",
    "recommended_fertilizer": "Balanced NPK fertilizer (14-14-14)",
    "application_method": "Apply as a top dressing around the base of the plant and water in thoroughly",
    "dosage": "10-15g per plant every 3-4 weeks",
    "additional_notes": "Classification not recognized. Consult an agricultural specialist for a more accurate diagnosis."
}


def fertilizer_recommendation(label: str) -> dict:
    return RECOMMENDATIONS.get(label, DEFAULT_RECOMMENDATION)
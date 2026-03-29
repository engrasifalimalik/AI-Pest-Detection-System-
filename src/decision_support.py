# Pest → Action mapping

def get_recommendation(pest_class):
    
    recommendations = {
        "aphids": "Use neem oil spray and introduce ladybugs.",
        "beetles": "Apply organic insecticide and remove manually.",
        "caterpillars": "Use Bacillus thuringiensis (Bt) spray.",
        "whiteflies": "Use sticky traps and insecticidal soap.",
        "mites": "Increase humidity and apply miticides."
    }
    
    return recommendations.get(pest_class, "No recommendation available.")

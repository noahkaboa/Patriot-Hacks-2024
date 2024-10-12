import spacy # pip install spacy
import json # built-in

# python3 -m spacy download en_core_web_lg
nlp = spacy.load("en_core_web_lg")


def rank_businesses(preferences, num_results=5):
    with open('./resources/directory.json', 'r') as f:
        directory = json.load(f)

    scores = {}

    for business_name, business_data in directory.items():
        description = business_data["description"]
        
        bus_doc = nlp(business_name + ": " + description)

        score = 0

        for preference in preferences:
            pref_doc = nlp(preference)
            score += bus_doc.similarity(pref_doc)
        
        scores[business_name] = score
    
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_scores[:num_results]



print(rank_businesses(["cafe", "homemade", "coffee", "3d printing", "lunch", "wifi", "vegan"], 5))
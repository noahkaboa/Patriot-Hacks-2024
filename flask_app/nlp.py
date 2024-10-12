import spacy # pip install spacy
import json # built-in

# python3 -m spacy download en_core_web_lg
nat_lang_proc = spacy.load("en_core_web_lg")


def rank_businesses(preferences, num_results=5):
    with open('./resources/directory.json', 'r') as f:
        directory = json.load(f)

    scores = {}

    for business_name, business_data in directory.items():
        
        description = business_data["description"]
        
        bus_doc = nat_lang_proc(business_name + ": " + description)


        score = 0

        try:
            for preference in preferences:
                pref_doc = nat_lang_proc(preference)
                score += bus_doc.similarity(pref_doc)
        except Exception as e:
            print(f"Error: {e}")

        scores[business_name] = score

    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_scores[:num_results].items()



# print(rank_businesses(["coffee", "chess"], 5))
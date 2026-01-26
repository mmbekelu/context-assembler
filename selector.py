# selector.py
# Selects relevant cleaned sources based on simple keyword scoring


KEYWORDS = [
    "context",
    "engineering",
    "clean",
    "selection",
    "assemble",
    "model",
    "ai"
]

MAX_RESULTS = 3


def select_relevant(sources):
    scored_sources = []

    for source in sources:
        text = source.get("text", "").lower()

        score = 0
        for keyword in KEYWORDS:
            if keyword in text:
                score += 1

        # Only keep sources that match at least one keyword
        if score > 0:
            scored_sources.append({
                "title": source["titl]()

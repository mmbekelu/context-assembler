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
        title = source.get("title", "")
        text = source.get("text", "")

        # Guard: skip invalid entries
        if not title or not text:
            continue

        text_lower = text.lower()

        score = 0
        for keyword in KEYWORDS:
            if keyword in text_lower:
                score += 1

        # Only keep sources that match at least one keyword
        if score > 0:
            scored_sources.append({
                "title": title,
                "text": text,
                "score": score
            })

    # Sort by score (highest first)
    scored_sources.sort(key=lambda item: item["score"], reverse=True)

    # Keep only top N results
    selected = scored_sources[:MAX_RESULTS]

    # Remove score before returning
    final_selected = []
    for item in selected:
        final_selected.append({
            "title": item["title"],
            "text": item["text"]
        })

    return final_selected

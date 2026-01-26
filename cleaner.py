# cleaner.py
# Cleans raw text sources by normalizing formatting
# No selection or relevance logic allowed here


def clean_sources(sources):
    cleaned = []

    for source in sources:
        title = source.get("title")
        text = source.get("text")

        # Guard: skip invalid entries
        if not title or not text:
            continue

        # ---- normalize text ----
        # 1. strip outer whitespace
        text = text.strip()

        # 2. split into lines
        lines = text.split("\n")

        # 3. clean each line
        clean_lines = []
        for line in lines:
            line = line.strip()
            if line:  # remove empty lines
                clean_lines.append(line)

        # 4. rejoin normalized text
        normalized_text = "\n".join(clean_lines)

        # Guard: skip if text becomes empty
        if not normalized_text:
            continue

        cleaned.append({
            "title": title.strip(),
            "text": normalized_text
        })

    return cleaned

# assembler.py
# Assembles selected sources into a structured context block


def assemble_context(sources):
    if not sources:
        return ""

    lines = []

    # ---- Header ----
    lines.append("## CONTEXT SOURCES")
    for source in sources:
        lines.append("- " + source["title"])

    lines.append("")  # blank line

    # ---- Extracts ----
    lines.append("## KEY EXTRACTS")
    for source in sources:
        lines.append("• " + source["text"])

    lines.append("")  # blank line

    # ---- Final Context ----
    lines.append("## FINAL CONTEXT")
    for source in sources:
        lines.append(source["text"])

    # Join everything into one string
    final_context = "\n".join(lines)

    return final_context

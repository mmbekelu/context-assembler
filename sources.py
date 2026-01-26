# sources.py
# Raw input sources for the Context Builder pipeline
# No logic allowed in this file

SOURCES = [
    {
        "title": "Context Engineering Overview",
        "text": """
        Context engineering is the practice of preparing,
        structuring, and validating information before it is
        sent to an AI model.

        The goal is to reduce confusion and improve reliability.
        """
    },
    {
        "title": "Why Cleaning Matters",
        "text": """
        Raw text is often messy.

        It may contain extra spaces,
        empty lines, or inconsistent formatting.

        Cleaning ensures predictable inputs.
        """
    },
    {
        "title": "Selection Rules",
        "text": """
        Not all information is relevant.

        Selection rules decide what content
        is allowed to reach the model.
        """
    },
    {
        "title": "Assembly Step",
        "text": """
        After selection, content is assembled
        into a structured format with headers
        and clear sections.
        """
    }
]

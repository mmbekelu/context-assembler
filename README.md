context-assembler
=================

PROJECT OVERVIEW
----------------
This project is a Context Builder and Prompt Assembler designed to prepare
clean, relevant, and structured context before it is sent to an AI model.

The system follows a deterministic pipeline:
- load raw sources
- clean and normalize text
- select only relevant information
- assemble a structured context block
- validate the output with tests

The goal is to control and protect AI inputs using rules instead of guesses.


FILE STRUCTURE
--------------
main.py
Orchestrates the entire pipeline. It runs each step in order, checks for
failure conditions, and stops the system safely when rules are violated.

sources.py
Contains raw input data for the system. This file only stores source text
and metadata. No logic is allowed here.

cleaner.py
Cleans and normalizes raw text. It removes empty lines, trims whitespace,
and ensures text is predictable and safe for downstream processing.

selector.py
Selects the most relevant sources using deterministic keyword-based rules.
This file decides which sources survive and which are rejected.

assembler.py
Assembles selected sources into a structured context block with fixed
headers and consistent formatting.

test_runner.py
Validates the final context. It checks structure, required sections,
length limits, and returns PASS or FAIL.


HOW THE SYSTEM WORKS
-------------------
1. Raw sources are loaded from sources.py
2. Text is cleaned and normalized
3. Relevant sources are selected using keyword rules
4. Selected content is assembled into a structured context block
5. Tests validate that the output meets all requirements
6. A safe, predictable context is produced and ready to be sent to an AI model


EXAMPLE FAILURE
---------------
Input Sources:
- Source A: empty text
- Source B: unrelated topic
- Source C: short but valid content

Result:
- Empty and irrelevant sources are removed
- Remaining content fails minimum context requirements
- Context block is NOT assembled
- System stops safely before any AI usage


WHY THIS PROJECT MATTERS
-----------------------
AI systems are extremely sensitive to input quality.

This project demonstrates how to:
- enforce rules before AI execution
- reduce irrelevant or harmful context
- guarantee consistent structure
- fail safely when inputs are invalid

This mirrors real-world Context Engineering and AI safety pipelines.


HOW TO RUN
----------
Run the full pipeline:
python main.py

Run tests directly (optional):
python test_runner.py

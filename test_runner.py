# test_runner.py
# Validates the final assembled context


MAX_CONTEXT_LENGTH = 2000

REQUIRED_HEADERS = [
    "## CONTEXT SOURCES",
    "## KEY EXTRACTS",
    "## FINAL CONTEXT"
]


def run_tests(final_context):
    all_passed = True

    # ---- Test 1: Type check ----
    if not isinstance(final_context, str):
        print("FAIL: Context is not a string.")
        all_passed = False

    # ---- Test 2: Non-empty check ----
    if not final_context:
        print("FAIL: Context is empty.")
        all_passed = False

    # ---- Test 3: Required headers ----
    for header in REQUIRED_HEADERS:
        if header not in final_context:
            print("FAIL: Missing header ->", header)
            all_passed = False

    # ---- Test 4: Length check ----
    if len(final_context) > MAX_CONTEXT_LENGTH:
        print("FAIL: Context exceeds max length.")
        all_passed = False

    return all_passed

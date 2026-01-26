# main.py
# Runs the full Context Builder pipeline:
# load → clean → select → assemble → test → output

# ---- imports (modularity) ----
from sources import SOURCES
from cleaner import clean_sources
from selector import select_relevant
from assembler import assemble_context
from test_runner import run_tests


def main():
    # ---- STEP 1: Load raw sources ----
    raw_sources = SOURCES

    if not raw_sources:
        print("No sources provided.")
        return

    # ---- STEP 2: Clean text ----
    cleaned_sources = clean_sources(raw_sources)

    if not cleaned_sources:
        print("Cleaning removed all sources.")
        return

    # ---- STEP 3: Select relevant content ----
    selected_sources = select_relevant(cleaned_sources)

    if not selected_sources:
        print("No relevant content selected.")
        return

    # ---- STEP 4: Assemble final context ----
    final_context = assemble_context(selected_sources)

    if not final_context:
        print("Context assembly failed.")
        return

    # ---- STEP 5: Run tests ----
    tests_passed = run_tests(final_context)

    # ---- STEP 6: Output result ----
    print("\n====== FINAL CONTEXT ======\n")
    print(final_context)

    print("\n====== TEST RESULTS ======\n")
    if tests_passed:
        print("ALL TESTS PASSED ✅")
    else:
        print("TESTS FAILED ❌")


# ---- program entry point ----
if __name__ == "__main__":
    main()

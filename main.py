# main.py
# Observable Context Builder pipeline
# load → clean → select → assemble → test → output

from sources import SOURCES
from cleaner import clean_sources
from selector import select_relevant
from assembler import assemble_context
from test_runner import run_tests


def main():
    print("=== PIPELINE STARTED ===")

    # ---- STEP 1: Load raw sources ----
    raw_sources = SOURCES
    print("Loaded sources:", len(raw_sources))

    if not raw_sources:
        print("STOP: No sources provided.")
        return

    # ---- STEP 2: Clean text ----
    cleaned_sources = clean_sources(raw_sources)
    print("Cleaned sources:", len(cleaned_sources))

    if not cleaned_sources:
        print("STOP: Cleaning removed all sources.")
        return

    # ---- STEP 3: Select relevant content ----
    selected_sources = select_relevant(cleaned_sources)
    print("Selected sources:", len(selected_sources))

    if not selected_sources:
        print("STOP: No relevant content selected.")
        return

    # ---- STEP 4: Assemble final context ----
    final_context = assemble_context(selected_sources)
    print("Assembled context length:", len(final_context))

    if not final_context:
        print("STOP: Context assembly failed.")
        return

    # ---- STEP 5: Run tests ----
    print("Running tests...")
    tests_passed = run_tests(final_context)

    # ---- STEP 6: Output result ----
    print("\n====== FINAL CONTEXT ======\n")
    print(final_context)

    print("\n====== TEST RESULTS ======\n")
    if tests_passed:
        print("ALL TESTS PASSED ✅")
    else:
        print("TESTS FAILED ❌")

    print("\n=== PIPELINE FINISHED ===")


if __name__ == "__main__":
    main()

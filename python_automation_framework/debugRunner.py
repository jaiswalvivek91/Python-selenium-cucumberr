import sys
import os
from behave.__main__ import main as behave_main

# ----------------------------
# 🔹 Set your tags here
# Example: "@login", "@smoke", "@fundGroup", or "" to run all
TAGS = "@login"
# ----------------------------

# Ensure PyCharm can import your step defs
sys.path.insert(0, os.path.abspath("steps"))

# Path to features folder
features_path = os.path.join(os.getcwd(), "features")

# Build Behave CLI args
behave_args = [
    features_path,
    "-f", "allure_behave.formatter:AllureFormatter",   # Allure formatter
    "-o", "reports/allure-results",                   # Output folder
    "-f", "pretty"                                    # Pretty console output
]

if TAGS and TAGS.strip():
    behave_args.extend(["--tags", TAGS])
    print(f"\n🎯 Running Behave tests with tag: {TAGS}")
else:
    print("\n🎯 Running ALL Behave tests (no tag filter)")

# Debug mode: single process, so PyCharm breakpoints work in steps/pages
print("\n🛠️ Running Behave in debug mode...")
sys.argv = behave_args  # Simulate CLI args
sys.exit(behave_main(behave_args))

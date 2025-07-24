import os
import subprocess
import shutil
import sys
from datetime import datetime

# ------------------------------------------------------------------------------
TAGS = "@login"  # Set your tag string here (e.g., "@smoke")
# ------------------------------------------------------------------------------



def run_tests():
    # Add steps/ directory to system path
    sys.path.insert(0, os.path.abspath("steps"))

    # Timestamp for report folder name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_reports_dir = "reports"
    allure_results_dir = os.path.join(base_reports_dir, f"allure-results-{timestamp}")
    allure_report_dir = os.path.join(base_reports_dir, f"allure-report-{timestamp}")

    features_path = os.path.join(os.getcwd(), "features")
    os.makedirs(allure_results_dir, exist_ok=True)

    # Build Behave command
    behave_cmd = [
        "behave",
        features_path,
        "-f", "allure_behave.formatter:AllureFormatter",
        "-o", allure_results_dir,
        "-f", "pretty"
    ]

    if TAGS and TAGS.strip():
        behave_cmd.extend(["--tags", TAGS])
        print(f"\n🎯 Running Behave tests with tag: {TAGS}")
    else:
        print("\n🎯 Running ALL Behave tests (no tag filter)")

    print(f"📁 Allure results will be saved to: {allure_results_dir}")

    # Execute behave command
    try:
        subprocess.run(behave_cmd, check=True)
        print("\n✅ Tests executed successfully!")
    except subprocess.CalledProcessError:
        print(f"\n❌ Some tests failed, but continuing with report generation...")

    # Generate Allure HTML report (in the timestamped folder only)
    print("\n📊 Generating Allure HTML report...")
    try:
        subprocess.run([
            "allure", "generate", allure_results_dir,
            "--clean", "-o", allure_report_dir
        ], check=True)
        print(f"📋 Allure HTML report generated at: {allure_report_dir}")

        # # Open the report directly from the timestamped folder
        # print("\n🚀 Opening Allure report in browser...")
        # subprocess.run(["allure", "open", allure_report_dir])

    except subprocess.CalledProcessError as e:
        print(f"❌ Error generating Allure report: {e}")
        print("Make sure Allure CLI is installed and available in PATH")

if __name__ == "__main__":
    run_tests()

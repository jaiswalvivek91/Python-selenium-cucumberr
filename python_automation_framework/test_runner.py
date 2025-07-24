
import os
import subprocess
import sys
from datetime import datetime
import shlex
import platform

# Set your tag filter here (e.g., "@login" or "" for all tests)
TAGS = "@login"

def make_command_string(cmd_list):
    # Safely quote each argument for terminal-friendly printing
    return ' '.join(shlex.quote(str(arg)) for arg in cmd_list)

def run_behave_tests():
    sys.path.insert(0, os.path.abspath("steps"))

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_reports_dir = "reports"
    allure_results_dir = os.path.join(base_reports_dir, f"allure-results-{timestamp}")
    os.makedirs(allure_results_dir, exist_ok=True)

    features_path = os.path.join(os.getcwd(), "features")

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

    # Print command for debugging
    terminal_command = make_command_string(behave_cmd)
    print("\n✅ Behave command:", terminal_command)

    try:
        # Run Behave and capture output
        result = subprocess.run(behave_cmd, capture_output=True, text=True, check=True)
        print(result.stdout)
        print(result.stderr)
        print("\n✅ Behave tests executed successfully!")
    except subprocess.CalledProcessError as e:
        print("\n❌ Behave tests failed or errors occurred!")
        # e.stdout and e.stderr can be None sometimes, guard just in case
        print("STDOUT:\n", e.stdout or "")
        print("STDERR:\n", e.stderr or "")

    return allure_results_dir, timestamp

def generate_allure_report(allure_results_dir, timestamp):
    base_reports_dir = os.path.dirname(allure_results_dir)
    allure_report_dir = os.path.join(base_reports_dir, f"allure-report-{timestamp}")
    os.makedirs(allure_report_dir, exist_ok=True)

    print("\n📊 Generating Allure HTML report...")

    # Decide on shell usage depending on platform
    use_shell = platform.system() == "Windows"

    try:
        result = subprocess.run(
            ["allure", "generate", allure_results_dir, "--clean", "-o", allure_report_dir],
            capture_output=True,
            text=True,
            check=True,
            shell=use_shell
        )
        print(result.stdout)
        print(f"✅ Allure report generated successfully at: {allure_report_dir}")
    except subprocess.CalledProcessError as e:
        print("\n❌ Failed to generate Allure report:")
        print("STDOUT:\n", e.stdout or "")
        print("STDERR:\n", e.stderr or "")
        print("Make sure Allure CLI is installed and available in your PATH.")

if __name__ == "__main__":
    results_dir, ts = run_behave_tests()
    generate_allure_report(results_dir, ts)

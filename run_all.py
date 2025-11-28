import os
import subprocess
import sys

# Get the Python executable from the current venv
python_executable = sys.executable

# List of scripts to run in order
scripts = [
    "scripts/data_load.py",
    "scripts/eda.py",
    "scripts/sentiment_analysis.py",
    "scripts/ml_model.py",
    "scripts/mapping.py",
    "scripts/report_word.py",
    "scripts/pie_chart.py",
    "scripts/ppt.py"
]

print("Starting Campaign Data Science project execution...\n")

# Run each script one by one using venv Python
for script in scripts:
    print(f"Running {script} ...")
    result = subprocess.run([python_executable, script], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("ERROR:", result.stderr)
    print("-" * 50)

print("\nAll scripts executed. Check the 'output/' folder for results.")

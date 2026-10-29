"""Run the original seven analysis scripts in order.

Visualizations open interactive windows in some environments. Set MPLBACKEND=Agg
before running to save plots without opening windows.
"""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
SCRIPTS = [
    "01_load_data.py",
    "02_descriptive.py",
    "03_visualization.py",
    "04_correlation.py",
    "05_regression_simple.py",
    "06_regression_multivariate.py",
    "07_vif_train_test.py",
]


def main():
    for name in SCRIPTS:
        print(f"\n=== Running {name} ===", flush=True)
        subprocess.run([sys.executable, str(ROOT / "src" / name)], check=True, cwd=ROOT)


if __name__ == "__main__":
    main()

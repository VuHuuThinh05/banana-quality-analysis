"""Shared paths, feature selection and input validation for the analysis scripts."""
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "banana_quality_dataset.csv"
OUTPUT_DIR = ROOT / "output"
FEATURES = [
    "sugar_content_brix",
    "firmness_kgf",
    "length_cm",
    "weight_g",
    "ripeness_index",
]
TARGET = "quality_score"


def load_dataset(path=DATA_PATH):
    """Read numeric model inputs; fail early on missing or invalid values."""
    df = pd.read_csv(path)
    required = FEATURES + [TARGET]
    missing = [column for column in required if column not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    if df.empty:
        raise ValueError("Dataset is empty")
    if df[required].isna().any().any():
        raise ValueError("Required model columns contain missing values")
    if not all(pd.api.types.is_numeric_dtype(df[column]) for column in required):
        raise ValueError("Required model columns must be numeric")
    return df

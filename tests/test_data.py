import sys
from pathlib import Path

import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from common import FEATURES, TARGET, load_dataset


def test_repository_dataset_has_required_numeric_columns():
    df = load_dataset()
    assert len(df) > 0
    assert all(pd.api.types.is_numeric_dtype(df[c]) for c in FEATURES + [TARGET])


def test_missing_column_raises(tmp_path):
    path = tmp_path / "missing.csv"
    pd.DataFrame({FEATURES[0]: [1.0]}).to_csv(path, index=False)
    with pytest.raises(ValueError, match="Missing required columns"):
        load_dataset(path)


def test_missing_value_raises(tmp_path):
    path = tmp_path / "null.csv"
    row = {column: 1.0 for column in FEATURES + [TARGET]}
    row[TARGET] = None
    pd.DataFrame([row]).to_csv(path, index=False)
    with pytest.raises(ValueError, match="missing values"):
        load_dataset(path)


def test_empty_dataset_raises(tmp_path):
    path = tmp_path / "empty.csv"
    pd.DataFrame(columns=FEATURES + [TARGET]).to_csv(path, index=False)
    with pytest.raises(ValueError, match="empty"):
        load_dataset(path)

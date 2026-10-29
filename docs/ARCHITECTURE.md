# System Architecture

Banana Quality Analysis is a local, script-based Python data analysis project. It is **not** a web application or a deployed prediction API. The workflow reads a CSV dataset, performs exploratory analysis and linear regression, and saves analysis artifacts.

## Architecture diagram

![Banana Quality Analysis — System Architecture](architecture.png)

## Data flow

```text
data/banana_quality_dataset.csv
            |
            v
     run_pipeline.py
            |
            v
   src/01_load_data.py          Read and inspect the dataset
            |
            v
   src/02_descriptive.py        Descriptive statistics
            |
            v
   src/03_visualization.py      Histograms, scatter plots, dashboards
            |
            v
   src/04_correlation.py        Pearson correlation and heatmap
            |
            v
   src/05_regression_simple.py  Simple linear regression
            |
            v
   src/06_regression_multivariate.py
                                Multiple linear regression
            |
            v
   src/07_vif_train_test.py     VIF and train/test evaluation
            |
            v
    output/csv/ + output/png/
```

The scripts are invoked sequentially by `run_pipeline.py`. They each read the input dataset as needed; **the pipeline does not pass a shared DataFrame from one script to the next**. The arrows describe execution order, not an in-memory data stream.

## Components and tools

| Component | Purpose | Tools |
| --- | --- | --- |
| `data/banana_quality_dataset.csv` | Local input dataset | CSV |
| `src/common.py` | Shared dataset loading and validation for scripts that import it | Python, pandas |
| `01_load_data.py`, `02_descriptive.py` | Inspect input and compute descriptive statistics | Python, pandas |
| `03_visualization.py`, `04_correlation.py` | Generate charts, dashboards and correlation analysis | pandas, Matplotlib, seaborn |
| `05_regression_simple.py`, `06_regression_multivariate.py` | Fit and inspect linear regression models | scikit-learn |
| `07_vif_train_test.py` | Compute VIF with an intercept; evaluate train/test R², MAE and RMSE | scikit-learn, statsmodels |
| `tests/` | Check required data columns and basic regression behavior | pytest |
| `output/csv/`, `output/png/` | Saved tables and figures | CSV, PNG |

The five numerical predictors are `sugar_content_brix`, `firmness_kgf`, `length_cm`, `weight_g` and `ripeness_index`. The target is `quality_score`.

## Running the project

From the repository root, install dependencies and execute the pipeline:

```powershell
python -m pip install -r requirements.txt
$env:MPLBACKEND="Agg"
python run_pipeline.py
```

Run the tests separately:

```powershell
python -m pytest -q
```

The analysis scripts save CSV/PNG outputs; pytest is a separate check rather than a pipeline stage. Some scripts may emit a non-interactive Matplotlib warning when calling `plt.show()` under the Agg backend; this does not prevent saved PNG generation.

## Model evaluation and limitations

With an 80/20 train/test split and `random_state=42`, the user-verified local run reported **test R² = 0.9830**, **MAE = 0.0606**, and **RMSE = 0.0716**. These are regression metrics, not classification accuracy. VIF values near 1 after adding an intercept do not indicate material multicollinearity among the five predictors in this dataset.

This is an exploratory, reproducible analysis. It does not establish causation, and model performance has not been validated on an independent external dataset.

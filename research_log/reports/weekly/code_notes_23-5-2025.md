## Cognitive Load Tetris Study – Data Cleaning Log

**Researcher:** \[Your Name]
**Session Date:** 2025-05-22
**Scripts Used:** `main.py`, `quality_checks.py`, `data_loader.py`, `delimiter.py`
**Dataset:** iMotions raw export (`raw.csv`)
**Modalities:** EEG, Eye-tracking

---

### Objective

The aim of this stage was to prepare the raw iMotions export for multimodal cognitive load analysis by:

* Extracting session metadata
* Validating the structure and completeness of the data
* Computing missing data percentages for critical columns
* Transitioning from category-based to column-based validation for higher precision

---

### Completed Steps

#### Step 0: Extract Metadata

* Parsed the metadata header to retrieve:

  * Participant ID
  * Recording Unix timestamp
  * Index of the header row containing column names
* Validated the extracted metadata using debug printouts
* Function used: `read_metadata_and_data()`

#### Step 1: Verify Export Quality

* Loaded the dataset using `pandas.read_csv()` with the correct `skiprows` parameter
* Inspected key aspects:

  * Number of columns and sample column names
  * Overall shape: 669,142 rows × 149 columns
  * Count and percentage of missing values
  * Data type summary for each column
* Function used: `verify_export_quality()`

#### Step 2: Missing Data Percentages (Per Column)

* Replaced category-grouped logic with a flat list of `REQUIRED_COLUMNS`
* Computed and printed missing value percentages for each required column
* Function used: `calculate_missing_percentages()`

#### Step 3: Detect Delimiter Type

* Wrote a separate utility script `delimiter.py` to automatically identify the delimiter used in the raw CSV
* Confirmed that the delimiter was a comma `,`

---

### Fixed Issues

#### 1. ValueError: too many values to unpack

* Cause: The loop was written for tuples, but `REQUIRED_COLUMNS` is now a flat list
* Fix: Changed the loop to `for col in required_columns:`

#### 2. Invalid Print Logic for Categories

* Cause: Original logic expected grouped categories which no longer exist
* Fix: Updated summary logic to print values column-by-column

#### 3. Metadata Extraction Bugs (initial versions)

* Issue: Failure to correctly detect the header row
* Fixes:

  * Added dynamic detection for the `#DATA` line
  * Used regex to correctly extract Unix start timestamp

#### 4. UTF-8 Encoding Problems

* Issue: File failed to load due to encoding mismatch
* Fix: Used `encoding='utf-8-sig'` when reading the CSV

#### 5. Incorrect Import Path for `REQUIRED_COLUMNS`

* Issue: Column list was either undefined or mismatched
* Fix: Centralized definition inside `quality_checks.py`

#### 6. Category-Based Summary Conflicts

* Issue: Summary functions based on categories clashed with the flat list approach
* Fix: Rewrote the summary logic to work per column only

#### 7. Confusion Over Delimiters

* Issue: Early versions failed to read the CSV or showed incorrect formatting
* Fix: Wrote and used `delimiter.py` with `csv.Sniffer` to auto-detect delimiter

---

### Output Example

| Column                  | % Missing    |
| ----------------------- | ------------ |
| `AF3`, `F7`, ..., `AF4` | 33.39%       |
| Eye Gaze (2D)           | 68.80%       |
| Fixation Metrics        | 76.01%       |
| Saccade Metrics         | 97.11–97.47% |
| `MarkerName`            | 99.89%       |

---

### Next Steps

1. Align EEG, eye-tracking, and event streams using the computed `AbsoluteTime` column
2. Extract clean segments for each gameplay phase
3. Begin calculating and comparing EEG and eye-tracking metrics across phases
4. Confirm the sampling rates of the Emotiv and Tobii devices next week

---

This log details the data cleaning process undertaken, the issues faced and resolved, and outlines the direction for the next phase in the cognitive load analysis of Tetris gameplay.

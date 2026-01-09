# Metadata Extraction and Setup Log

## Purpose of this Script

This script is responsible for extracting structural and session metadata from raw iMotions exports. It prepares the dataset for synchronization and further analysis by:

* Extracting participant details (name, ID, age, gender)
* Capturing session context (study name, calibration quality)
* Identifying the correct header row where the data begins (typically after `#DATA`)
* Locating and extracting the Unix timestamp for time synchronization

## Steps Completed So Far

1. **Defined key metadata to extract**:

   * Study name, respondent name and ID, age, gender, gaze calibration, and Unix time.
   * All values are extracted with fallback defaults if missing or malformed.

2. **Developed `extract_metadata_value()`**:

   * Accepts a line, keyword, and type, and searches for a value using `split(';')`.
   * Returns cleaned values in the appropriate data type.

3. **Built `read_metadata_and_data()`**:

   * Iterates through the header lines of the file.
   * Uses both `startswith()` and `in` checks with `lower()` normalization.
   * Uses regex for robust UUID extraction from "Id:" fields.

4. **Tested edge cases**:

   * Files with missing values, lowercase variations, or extra whitespace.
   * Output verified against multiple .csv files.

5. **Version-controlled changes**:

   * Scripts were added and committed via Git.
   * Learned to `git add`, `commit`, and `push`.
   * Ensured tracking excludes unnecessary files using `.gitignore`.

##  Current Outputs

From each CSV file, the script successfully extracts:

* **Participant ID**: UUID formatted string after "Id:"
* **Participant Name**: e.g., "participant 1"
* **Age**: Integer
* **Gender**: MALE / FEMALE
* **Study Name**: Session or file identifier
* **Gaze Calibration Quality**: e.g., Good
* **Unix Time**: Used to create absolute timestamps
* **Header Row Index**: Indicates where the actual dataset starts

##  Why These Metadata Fields Matter

* **Participant ID / Name**: Grouping and labeling across multiple sessions
* **Age / Gender**: Used for demographic analysis and workload variability
* **Study Name**: Helps track session context and match with subjective assessments (e.g., NASA-TLX)
* **Gaze Calibration**: Quality indicator for Eye-Tracking reliability
* **Unix Time**: Necessary for aligning EEG, Eye-Tracking, and game events
* **Header Row**: Ensures correct DataFrame parsing

##  Issues Faced & Fixes

| Problem                            | Solution                                                             |
| ---------------------------------- | -------------------------------------------------------------------- |
| Varying number of columns per line | Used `split(';')` and regex parsing to isolate meaningful parts      |
| IDs not extracted properly         | Applied regex (`id:\s*([a-f0-9\-]+)`) to reliably capture UUIDs      |
| Missing or empty fields            | Applied fallback defaults and printed debug output for manual review |
| Inconsistent case/spaces           | Lowercased and stripped lines for uniform parsing                    |
| Parsing failures for integers      | Used `expected_type=int` and wrapped extraction in `try-except`      |

##  Next Step: Column Quality Checks

Create a new file `quality_checks.py` and implement a function `inspect_columns(df)` that will:

* Calculate % of missing values per column
* Flag columns with >70% missing data
* Suggest core columns to keep (EEG, Eye-Tracking, Events)
* Identify timestamp and marker columns
* Print summary for visual inspection

This step ensures we retain only meaningful data, simplifies synchronization, and avoids propagating noise into the analysis.

---

This documentation reflects progress up to metadata extraction. Next, we focus on structural validation of columns, followed by data synchronization and segmentation.

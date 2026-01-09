

**May 19–23, 2025**


This week, I focused on completing and validating a full experimental session, updating the experimental timeline, and advancing the data cleaning and preprocessing pipeline for EEG and eye-tracking analysis. I now have three full participant recordings, including my own. These recordings will form the base dataset for computing workload measures across different Tetris gameplay phases for the next few weeks.

## Study Timeline Updates

After reviewing the practical flow and feedback from the first two participants, I planned a revision to the experimental timeline. Based on their feedback that the break felt too long, I intend to reduce the resting break from 2 minutes to 1 minute in future sessions. This adjustment has not yet been implemented but is scheduled for next week. I also finalized the game flow into clearly structured phases:

1. Familiarization (3 minutes)
2. Skill Level Detection (3 minutes)
3. Resting Baseline (2 minutes, EEG only)
4. Starting Level (up to 10 minutes, EEG + Eye Tracking)
5. NASA-TLX (after Starting Level)
6. Break (1 minute)
7. Harder Level (up to 10 minutes, EEG + Eye Tracking)
8. NASA-TLX (after Harder Level)

Key event markers ("GameStart", "LineClear", "EndLevel") were used consistently during recording.

## Recording Setup and Environment

I configured iMotions with the Event Receiving API and structured the sessions for EEG and gaze data recording. However, the recording environment was not fully distraction-free. While I followed the standard setup procedure, noise and interruptions were present, which may affect the physiological signal quality.

I reviewed the real-time sensor preview results **after the sessions**, not during. Participants commented that the game felt relatively easy and the break too long. These comments will be used to fine-tune the study design.

## Data Cleaning and Preprocessing Log

I processed the raw export from iMotions using scripts: `main.py`, `quality_checks.py`, `data_loader.py`, and `delimiter.py`.

### Objective

To prepare the multimodal dataset (EEG + Eye Tracking) for clean, synchronized, and analyzable formats:

* Extract metadata (Unix time, participant ID)
* Validate data structure and completeness
* Compute missing data rates using a per-column strategy
* Shift from category-based summaries to a flat column-wise validation

### Completed Steps

1. Parsed metadata using `read_metadata_and_data()` and correctly extracted header and Unix timestamp, participantID.
2. Verified data integrity with `verify_export_quality()` — file contained 669,142 rows and 149 columns.
3. Assessed missing data using a direct `REQUIRED_COLUMNS` list in `calculate_missing_percentages()`.
4. Confirmed comma as the correct delimiter via `delimiter.py`.

### Issues Encountered and Fixed

* Rewrote loop logic after encountering unpacking errors
* Adjusted output formatting for column-wise reporting
* Fixed UTF-8 encoding issues by specifying `'utf-8-sig'`
* Centralized `REQUIRED_COLUMNS` for consistent reference


### Data Quality Summary

EEG channels like AF3 and F3 had around 33% missing values. Eye tracking modalities showed higher gaps:

* Eye gaze: ~68% missing
* Fixation metrics: ~76%
* Saccade metrics: over 97%
* MarkerName: nearly 100% missing

This suggests EEG is mostly usable, while gaze and marker data may need interpolation or manual correction.

### Next Steps

1. Align EEG, eye-tracking, and event streams to the Unix time using the `AbsoluteTime` field.
2. Extract clean segment windows for each gameplay phase.
3. Begin statistical comparison of EEG and gaze metrics across phases.
4. Verify the sampling rates of Emotiv and Tobii systems — **scheduled for next week**.



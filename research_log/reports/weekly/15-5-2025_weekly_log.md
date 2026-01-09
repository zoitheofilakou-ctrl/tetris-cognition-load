

## What I Did This Week

* Defined AOIs manually in iMotions (Grid, Score, NextPiece, LineClear, Timer)
* Exported full AOI-related eye-tracking data from iMotions:
  - FixationTable.csv
  - SaccadeTable.csv
  - SceneFixationTable.csv
  - SceneSaccadeTable.csv
  - AggregatedAOImetrics.csv
  - IndividualAOImetrics.csv
* Verified AOI labels appear correctly in `FixationTable.csv` (most ET_AOI_Label entries populated)
* Started comparing event marker timestamps (e.g., LineClear, ScoreUpdate) to fixation segments
* Confirmed that AOIs are now visible and correctly aligned in iMotions interface
* Watched iMotions tutorials and read blog posts on:
  - AOI best practices
  - Gaze mapping vs autoAOI
  - Dynamic AOIs for tracking moving objects

## Key Fixes & Discoveries

* Identified that `ScoreUpdate` marker is triggered too frequently — marker logic needs fixing
* Verified that fixation points outside the game screen are correctly labeled as `NA` in AOI column
* Confirmed saccade and fixation indices are not starting from 0 (expected behavior from iMotions)
* Noted that Blink Detection Metrics export is failing — needs troubleshooting

## Open Issues / Questions

* How to export NASA-TLX survey as a single file per participant (currently 3 txt files per session)
* How to export EEG aligned with gaze + markers (still pending)
* Whether I need to use R or keep everything in Python for analysis
* Do I need to process TTFF, dwell index, and transitions now or after EEG is added?

## Next Steps / Goals

* Export EEG sensor data from iMotions for each participant
* Merge NASA-TLX txt files into one CSV file per participant
* Analyze AOI hit counts (e.g., fixations per AOI during LineClear)
* Debug `ScoreUpdate` marker logic in `api.py`
* Begin a short Jupyter Notebook to process and visualize eye-tracking fixation data
* Consider trying automated AOI (dynamic) tools for moving blocks if time allows

---

### Resources Used

* iMotions Docs:
  - [AOI Editor Overview](https://imotions.com/blog/learning/product-news/product-release-new-areas-of-interest-aoi-editor-in-imotions-9-0/)
  - [Gaze Mapping vs AutoAOI](https://imotions.com/blog/insights/research-insights/gaze-mapping-vs-autoaoi/)
  - [AOI Metrics Reference](https://imotions.com/blog/learning/10-terms-metrics-eye-tracking/)
* YouTube iMotions AOI Walkthrough:  
  https://www.youtube.com/watch?v=59K_qVF2R9I&t=648s


Τέλειο — πάμε **τελική, καθαρή, 100% ευθυγραμμισμένη έκδοση**
👉 **χωρίς ERP**,
👉 **μόνο frequency-domain (alpha / theta)**,
👉 **execution-level, marker-only documentation**.

Αυτό που ακολουθεί είναι **ΑΚΡΙΒΩΣ** το κείμενο που πρέπει να βάλεις στο
`Implementation_log_markers_t3imosciences.md`.

Μπορείς να το κάνεις **copy–paste αυτούσιο**.

---

# Implementation Log – Event Markers (EEG–Tetris × iMotions)

This document records the **exact implementation points** of experimental event markers used to synchronize Tetris gameplay with EEG and eye-tracking data in iMotions.
It complements the API reference by documenting **where each marker is triggered in the codebase, when it is sent, and why this design is experiment-safe**.

All markers are transmitted via a unified API (`send_event`) and logged as **momentary sample-based events (M;1)**.
Markers are used exclusively for **temporal segmentation of gameplay phases and conditions** in support of frequency-domain EEG analysis (e.g., alpha and theta power).

---

## Design Principles

All experimental markers follow three strict rules:

1. Each marker is triggered **exactly once**
2. Each marker is sent from the **logical origin of the event**
3. No marker is inferred indirectly from other variables (e.g., score or speed)

Violation of any rule renders the experiment unsafe for EEG and eye-tracking analysis.

---

## Marker Transmission Layer

All communication with iMotions is handled exclusively by:

```python
send_event(sample, value)
```

defined in `tetris_code/api.py`.

No other module opens sockets, formats UDP messages, or sends raw marker strings.

---

## Marker Integration by File

### 1. `menu.py` — Task and Condition Onset

**Markers sent:**

```python
send_event("StartGame", 1)
send_event(f"{level_name}Level", "Start")
```

**Trigger point:**
Immediately before gameplay begins, when the user selects a difficulty level.

**Rationale:**

* `StartGame` marks **task onset**
* `<Level>Level Start` marks **experimental condition onset**
* Explicit onset markers are required for reliable segmentation of EEG and eye-tracking data into task phases and difficulty conditions

Implicit difficulty changes are not experiment-safe.

---

### 2. `grid.py` — Atomic Performance Events

**Marker sent:**

```python
send_event("LineClear", 1)
```

**Trigger point:**
Inside `is_row_full()`, at the exact moment a row-clear condition is detected.

**Rationale:**

* Line clears represent **discrete performance success events**
* They are logged **before** score aggregation or speed changes
* This enables precise segmentation of EEG data for **frequency-domain workload analysis** (e.g., alpha and theta power during successful actions)

Line clears must be logged at detection time and never inferred from score updates.

---

### 3. `main.py` — Task Termination and Outcome

**Markers sent (exactly once per run):**

```python
send_event("FinalScore", score)
send_event("GameOver", termination_reason)
```

**Termination conditions:**

* Time limit reached → `GameOver = "TimeLimit"`
* Block stacking (loss) → `GameOver = "BlockOut"`

A single boolean flag (`task_ended`) enforces one and only one termination event.

**Rationale:**

* Prevents duplicate termination markers
* Makes termination cause explicit
* Defines a clear end of the analysis window for EEG and eye-tracking data
* Protects trial-level segmentation for statistical analysis

No experimental logic exists inside UI-only loops.

---

## Score Semantics

Two distinct score-related markers are enforced:

### `ScoreUpdate`

```python
send_event("ScoreUpdate", current_score)
```

* Sent during gameplay
* Represents **time-varying performance**
* Can be aligned with short EEG windows for exploratory analysis

### `FinalScore`

```python
send_event("FinalScore", final_score)
```

* Sent exactly once at task termination
* Represents **trial-level outcome**

This separation prevents ambiguity between ongoing performance and final results.

---

## Verification Status

* Markers verified live in iMotions Sensor Preview
* Marker format aligned with `eventsource.xml` (**M;1 only**)
* No scene-based markers (`M;2`) are used
* All markers originate from a single API layer
* Markers are used for **temporal segmentation**, not for ERP analysis

---

## Debugging Checklist

If marker timing or presence appears incorrect:

1. Verify `send_event()` usage in the relevant module
2. Confirm the marker is triggered at the logical origin of the event
3. Ensure the marker is not duplicated
4. Ensure no marker is inferred indirectly from other variables
5. Confirm no legacy marker functions or scene logic exist

---

> This implementation ensures scientifically valid synchronization between gameplay events, EEG signals, and eye-tracking data for frequency-domain workload analysis (e.g., alpha and theta power).
> The document serves as a reproducibility record and a precise reference for experimental instrumentation.
## Example Marker Calls
```python
send_event("GameStart", 1)
send_event("LevelStart", 2)
send_event("LineClear", 1)
send_event("FinalScore", 4200)
```


# Tetris-iMotions API Reference

## API Reference – Unified Event Marker Interface (`api.py`)

This file defines the **centralized event communication interface** between the Tetris application and iMotions.
All experimental markers are transmitted via **UDP** using a **single standardized function**, ensuring format consistency, low latency, and reliable synchronization with EEG and eye-tracking data.

The `api.py` module is intentionally minimal and **does not contain game logic**.
It acts as a shared communication layer imported by multiple gameplay modules.

---

## Marker Function

### `send_event(sample, value)`

**Purpose**
Sends a single, momentary experimental event marker (`M;1`) to iMotions.

This is the **only marker-sending function** used in the codebase.

**Format**

```
M;1;<sample>;<value>
```

**Parameters**

* `sample` (string): Event label (e.g., `GameStart`, `LevelStart`, `LineClear`)
* `value` (int | string): Event value or payload

**Example**

```python
send_event("GameStart", 1)
send_event("LevelStart", 2)
send_event("LineClear", 1)
send_event("FinalScore", 4200)
```

Each call sends a single UDP packet to iMotions containing a correctly formatted `M;1` marker.

---

## Design Principles

* All markers use **M;1 sample-based events**
* No scene markers (`M;2`) are used
* No raw UDP messages are sent outside `api.py`
* All event semantics are defined at the caller level
* The API guarantees format consistency across the experiment

This design minimizes error probability, simplifies debugging, and prevents silent data loss caused by incompatible marker formats.

---

## Usage Across Codebase

The `send_event()` function is imported and used by multiple modules:

* `menu.py`
  Used for high-level experimental events (e.g., game start, level start)

* `grid.py`
  Used for atomic gameplay events (e.g., line clears)

* `main.py`
  Used for session termination events (e.g., final score, game end)

All modules communicate with iMotions **exclusively through `api.py`**.

---

## UDP Transmission Details

* **Protocol:** UDP (User Datagram Protocol)
* **Destination:** `127.0.0.1 : 8089`
* **Rationale:**
  UDP is used to minimize latency and preserve accurate temporal alignment between gameplay events, EEG signals, and eye-tracking data.

---

## Maintenance Rule

If event markers stop appearing in iMotions:

1. Check `api.py`
2. Ensure all events are sent via `send_event()`
3. Verify that no legacy marker functions are used

---

## Deprecated Functionality

The following approaches are **no longer used** and must not be reintroduced:

* Multiple marker-sending functions
* Scene-based markers (`M;2`)
* Raw UDP or TCP message sending from other modules
* Hardcoded marker formats outside `api.py`

---

**This file reflects the final, lab-ready event communication design and serves as the single source of truth for experimental marker transmission.**


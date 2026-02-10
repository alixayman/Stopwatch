# Stopwatch (Python + PyQt5)

A simple and responsive **Stopwatch application** built using **Python** and **PyQt5**, featuring start, stop, and reset functionality with millisecond precision.

---

## Features

* ▶️ **Start** the stopwatch
* ⏹️ **Stop** (pause) the stopwatch
* 🔄 **Reset** the time back to zero
* Displays time in the format:

  ```
  HH:MM:SS.ms
  ```
* Smooth updates using a `QTimer` with 10 ms resolution
* Clean and modern UI styled with Qt stylesheets

---

## How It Works

* The stopwatch time is managed using `QTime`
* A `QTimer` triggers updates every **10 milliseconds**
* Time is incremented using `addMSecs()`
* The display is updated dynamically on every timer tick

---

## Technologies Used

* **Python 3**
* **PyQt5**
* Event-driven programming
* Qt layout management (`QVBoxLayout`, `QHBoxLayout`)

---

## How to Run

1. Make sure Python is installed (Python 3.9+ recommended)
2. Install PyQt5 if not already installed:

   ```bash
   pip install PyQt5
   ```
3. Run the application:

   ```bash
   python stopwatch.py
   ```

---

## User Interface

* Large, easy-to-read time display
* Clearly labeled control buttons
* Responsive layout that adapts to window resizing

---


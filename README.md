# 🎥 Face-Aware Video Summarization Tool (CCTV Footage)

A Python-based application that summarizes CCTV or long-duration video footage by extracting only the frames where human faces appear. The summarized video is trimmed to an exact duration (default: 60 seconds), helping users quickly review significant human activity in security footage or other videos.

---

## ✅ Features

- 🔍 Detects human faces using Haar cascade classifiers.
- 🧠 Summarizes **one or more videos** into a single output file.
- ⏱ Ensures **exact fixed duration** (default: 60 seconds).
- 🗂 Easy GUI file selection via **Tkinter**.
- 📦 Automatically saves output to `summarized_video/` folder.

---

## 🧠 How It Works

1. Opens selected video(s) via file dialog.
2. Scans each frame using Haar cascade-based face detection.
3. Stores only those frames that contain at least one face.
4. Combines the top N frames into an output video:
   - `N = target_duration (in seconds) × FPS`
5. Writes output as `front_view_summary.mp4`.

---

## 🧰 Tech Stack

- Python 3.x
- OpenCV – for video processing and face detection
- Tkinter – for GUI-based file selection
- OS – for file management

---

## 📁 Project Structure


---

## 💻 Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/yourusername/face-video-summarizer.git
cd face-video-summarizer

pip install opencv-python

python face_summary.py

summarized_video/front_view_summary.mp4

select_videos_and_summarize(target_duration=90)  # for a 90-second summary


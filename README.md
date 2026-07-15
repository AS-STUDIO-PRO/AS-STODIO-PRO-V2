# 🚀 AS AVATAR STUDIO V2

An upgraded ultra-fast lipsync engine featuring strict original audio removal, dynamic video looping, and inline Gradio preview support.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AS-STUDIO-PRO/AS-STODIO-PRO-V2/blob/main/AS-STODIO-PRO-V2.ipynb)
[![Open In Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/AS-STUDIO-PRO/AS-STODIO-PRO-V2/blob/main/AS-STODIO-PRO-V2.ipynb)

---

## ✨ Key Features

* **🚀 Turbo Engine V2:** Optimized segmented processing with hardware acceleration.
* **🔇 Strict Audio Strip:** Automatically removes any original audio from the target video and replaces it with your driving audio.
* **🔁 Dynamic Video Looping:** Loops the target video infinitely and cuts exactly where the driving audio ends (`-shortest` integration).
* **💾 Disconnect-Safe Backup:** Automatically copies the final rendered video to your Google Drive (`AS_Studio_Outputs`) so you never lose your progress.
* **🎬 Inline Colab Preview:** Interactive Gradio interface launches directly inside your Jupyter/Colab notebook cell.

---

## ⚡ Quick Start Guide

### **Step 1: Install Dependencies**
```python
!git clone [https://github.com/](https://github.com/)AS-STUDIO-PRO/AS-STODIO-PRO-V2.git
%cd AS-STODIO-PRO-V2
!pip install -q gradio librosa
```

### **Step 2: Launch Web UI**
```python
!python demo.py
```

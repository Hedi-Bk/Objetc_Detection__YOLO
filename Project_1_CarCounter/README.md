## 🚗 Car Detection Project — Real-Time Vehicle Counting Using YOLO and SORT

Hi! This project demonstrates a complete pipeline for detecting and tracking cars from a real-world video feed using **YOLO** for object detection and **SORT** for tracking. The goal is to simulate and test how such a system could be used in intelligent traffic monitoring applications.

### 💡 Real-World Applications

This solution addresses the growing need for **smart traffic management** systems. It can be used to:

1. Automatically monitor traffic on roads by placing a camera on a strategic location (bridge, intersection, highway, etc.).
2. Estimate **real-time vehicle density or congestion** on a given road section.
3. Collect useful data for **urban planning**, **traffic flow optimization**, or **automated tolling systems**.

> ⚠️ Before deploying such a system in a real-world setting, it is important to test the solution on recorded videos. This is exactly what we are doing here.

---

### 🔧 Tools & Technologies Used

- **YOLOv8** (Ultralytics) for car detection
- **SORT (Simple Online and Realtime Tracking)**: tracking algorithm to count individual vehicles reliably
  > Source: abewley/sort
- **OpenCV** for video processing and visualization
- **NumPy** for numerical operations
- Python-based pipeline executed in a local environment

---

### 📦 Project Pipeline

```mermaid
mermaid
CopierModifier
graph LR
A[Load Real-Life Video] --> B[Define ROI (Masking)]
B --> C[Specify Detected Object Classes (e.g., only cars)]
C --> D[Run YOLO Inference]
D --> E[Track Vehicles using SORT]
E --> F[Display Real-Time Vehicle Count]

```

### Detailed Steps:

1. **Video Input**: We start with a real-life traffic video.
2. **ROI Masking**: Apply a mask to define the specific zone of interest (ignore irrelevant parts of the frame).
3. **Object Class Filtering**: Focus detection only on relevant classes — e.g., ignore pedestrians, trucks, and motorcycles.
4. **Inference**: Use YOLOv8 to detect vehicles within the masked area.
5. **Tracking**: Use the SORT algorithm to maintain consistent IDs for cars across frames and count them.
6. **Display**: Show the detection boxes and the total car count live on the video.

---

### 🎯 Project Objective

By the end of this project, we aim to:

- Simulate a working **vehicle detection and tracking system** from a recorded video
- Gain insights into the feasibility and precision of such a solution before deploying it in a real-time scenario
- Build a foundation for future enhancements such as speed estimation, multi-lane analysis, or alert systems

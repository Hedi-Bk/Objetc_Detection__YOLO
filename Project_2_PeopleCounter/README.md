### People Detection and Counting on Escalators

**Hi!**

This project focuses on detecting and counting people on escalators in a shopping mall.

The goal is to track individuals going **up** and **down** the escalator for **statistical analysis** and **business insights**.

We aim to distinguish between **ascending** and **descending** people using video input from a fixed camera, with real-time detection and tracking.

---

### Demo 👇

![Demo](../DemoPeople.gif)

### 🔍 Problem Statement

In large public spaces like malls, it's often difficult to:

- Know the **number of visitors** entering and exiting specific areas.
- Understand **traffic direction patterns** (up vs down).
- Optimize **energy usage** and **resource allocation** based on traffic.
- Improve **safety**, detect **congestion**, and make **data-driven decisions**.

This project answers these challenges by providing **automated people detection and movement counting** in both directions on an escalator.

---

### 🧠 Use Cases in the Real World

- 🛍 **Shopping Malls**: understand peak hours, optimize space and promotions.
- 🏬 **Public Facilities**: monitor usage, detect overload or safety issues.
- 🎡 **Theme Parks / Airports**: improve crowd flow and logistics.
- 📊 **Urban Planning**: collect real-time statistics for foot traffic studies.

---

### 🔁 Project Pipeline

1. **Camera Setup**:

   Install a surveillance camera in a fixed position, capturing both **upward** and **downward** movement on the escalator.

2. **Demo Video Collection**:

   Record a representative sample video for initial testing.

3. **Core Objective (This Project)**:

   Apply **real-time people detection and tracking** on the video, using:

   - **YOLOv8 model** for object (person) detection
   - **SORT Algorithm** for object tracking
   - GitHub Repo used: [abewley/sort](https://github.com/abewley/sort)

4. **Deployment Phase**:

   Once the model is verified and validated, install it on a local server linked to the camera.

5. **Result Utilization**:

   Provide statistical dashboards, live insights, and reports for the mall to optimize their:

   - Staff distribution
   - Advertisement placement
   - Emergency protocols
   - ROI and planning strategies

---

### 📦 Tech Stack

- `Python` / `OpenCV`
- `Ultralytics YOLOv8`
- `SORT` tracking algorithm
- `Streamlit` (for demo and visualization)

# Prediction Storage System

## 📌 Overview

This project implements a simple backend system to store and retrieve model predictions using SQLite.

It demonstrates how predictions from an AI/ML model can be persisted and accessed later.

---

## ⚙️ Features

* Store prediction results in database
* Retrieve prediction history
* Lightweight SQLite-based system
* Clean and modular Python structure

---

## 🗂️ Project Structure

```
prediction-storage-system/
│
├── database.py           # Database connection & table creation
├── store_prediction.py   # Insert predictions into DB
├── get_history.py        # Fetch stored predictions
```

---

## 🧪 Usage

### 1. Create Database Table

```
python database.py
```

### 2. Store Prediction

```
python store_prediction.py
```

### 3. Get Prediction History

```
python get_history.py
```

---

## 📊 Example Output

```
(1, 0, '2026-04-18 10:30:00')
(2, 1, '2026-04-18 10:32:10')
```

---

## 🧠 Use Case

This system can be integrated with:

* Machine Learning APIs
* Model inference pipelines
* Backend services for AI applications

---

## 🚀 Future Improvements

* Add user tracking
* Connect with API layer
* Add filtering & pagination
* Replace SQLite with PostgreSQL

---

## 👨‍💻 Author

Built as part of a daily AI engineering practice system.
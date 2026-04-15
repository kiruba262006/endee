# 📄 Resume Analyzer using Endee

## 📌 Overview

This project is a simple AI-based Resume Analyzer built using the Endee vector database.
It analyzes resume text and provides relevant suggestions using semantic search.

---

## 🚀 Features

* Resume text analysis
* Semantic search using Endee
* AI-based suggestions
* Simple command-line interface
* Uses preloaded dataset from Endee

---

## 🛠️ Tech Stack

* Python
* Endee (Vector Database)

---

## 📂 Project Structure

```
resume-analyzer/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Run the application:

```
python app.py
```

---

## 🧠 How it Uses Endee

This project uses Endee's vector search to:

* Convert resume text into embeddings
* Search similar data from the dataset
* Retrieve meaningful suggestions
* Provide feedback based on similarity

---

## 💡 Example

Input:

```
Python developer with basic machine learning skills
```

Output:

```
Suggested Roles: ML Engineer, Data Analyst  
Suggestions: Improve project experience, add certifications  
```

---

## 📸 Demo

You can run the project and input any resume text to see results.

---

## ✅ Conclusion

This project demonstrates a basic Retrieval-Augmented Generation (RAG) approach using Endee for resume analysis and suggestions.

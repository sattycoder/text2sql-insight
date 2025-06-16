# 🧠 Text2SQL Insight

Text2SQL Insight is a simple, interactive Streamlit web app that converts natural language (NLP) queries into SQL statements using Google’s Generative AI API. It then executes the generated SQL on a dataset and displays the output in a readable format.

---

## 🔍 Features

- 🗣️ Convert natural language into SQL queries using Google Generative AI
- 📊 Execute SQL on predefined datasets
- 🧾 Display results in clean, readable format
- 🌐 Web-based UI built with Streamlit

---

## 🚀 How It Works

1. **Text to SQL Conversion**  
   User types a query in plain English. This is sent to the Google Generative AI API, which returns an SQL statement.

2. **Query Execution**  
   The generated SQL query is run on a dataset using SQLite or pandas.

3. **Result Display**  
   Results are rendered in a table using Streamlit, along with original inputs and generated SQL.

---

## 🛠️ Built With

- Python
- Streamlit
- Google Generative AI (Palm2 or Gemini API)
- SQLite / Pandas (for data handling)

---

## 📦 Directory Structure

text2sql-insight/  </br>
├── app.py # Streamlit UI "/n"
├── check.py # Test and Check Functionalities /n
├── sql.py # Executes SQL query to generate a database /n
├── requirements.txt /n
└── student.db # Sample database (optional) 

## ✅ TODO

- [ ] Add support for more databases
- [ ] Add query history feature
- [ ] Add authentication for multi-user access

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 🙌 Acknowledgements

- Google PaLM/Gemini API
- Streamlit team
- Community contributors

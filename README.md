
📌 README.md

# Python Mini Projects (File Handling, OOP, Pandas, API, Encoding)

This repository contains *4  Python projects* that combine *OOP, File Handling, Pandas/Numpy, APIs, and Encoding* concepts.  

---

## 📂 Projects

### 1️⃣ Library Management System (OOP + File Handling)
A simple console-based system to manage books in a library.

*Features:*
- Add new books
- Borrow/return books (updates availability)
- List all books
- Persistent storage using books.json

*How to Run:*
- bash
python library.py

*Sample Output:*

📚 Library Books:
- Python Basics by John Smith (ISBN: 111) → ✅ Available
- Data Science 101 by Alice Brown (ISBN: 222) → ❌ Borrowed
<img width="1920" height="1080" alt="2025-09-07" src="https://github.com/user-attachments/assets/26e600fc-4dad-4de3-8f58-c790e26900a8" />

<img width="1920" height="1080" alt="2025-09-07 (1)" src="https://github.com/user-attachments/assets/23da26fa-8cc9-442f-a452-36cafdf8c1af" />
<img width="1920" height="1080" alt="2025-09-07 (8)" src="https://github.com/user-attachments/assets/afd54913-27b2-42f7-8c7b-da9205a378e2" />


---

#2️⃣ Weather Dashboard (API + JSON + History)

A weather app that fetches real-time weather using OpenWeatherMap API.

Features:

Search current weather by city

Save search history to history.json

Display last 5 searches


*How to Run:*

1. Get a free API key from OpenWeatherMap.


2. Replace "YOUR_API_KEY" in weather_dashboard.py with your key.


3. Run:



python weather_dashboard.py

*Sample Output:*

🌤 Weather in London: 18°C, Clear Sky

📜 Last 5 Searches:
- London: 18°C, Clear Sky
- Paris: 20°C, Clouds
Json file output
<img width="1920" height="1080" alt="2025-09-07 (21)" src="https://github.com/user-attachments/assets/bb8b3c1b-cc8e-4172-bc1d-887ff7f2f012" />



---

#3️⃣ Student Grades Analyzer (CSV + Pandas/NumPy)

Analyzes student grades from a CSV file and provides useful insights.

*Features:*

Load student dataset (students.csv)

Calculate average, highest, lowest scores per subject

Display top 3 students by average score

Add Pass/Fail column (threshold = 40%)


*How to Run:*

python grades_analyzer.py

*Sample Output:*

📘 Math:
   ➡ Average: 64.00
   ➡ Highest: 90
   ➡ Lowest : 30

🏆 Top 3 Students (by Average Score):
    Name  Average
  Charlie    87.33
    Alice    85.00
      Eva    71.67
<img width="1920" height="1080" alt="2025-09-07 (22)" src="https://github.com/user-attachments/assets/d04f1dea-20ef-4252-93a1-14cd87851080" />


---

#4️⃣ Simple Password Manager (File + Encoding)

A console-based password manager that stores website credentials securely.

*Features:*

Store website, username, and password

Save entries in passwords.json

Apply Base64 encoding (simple protection)

View stored logins (decoded)


*How to Run:*

python password_manager.py

*Sample Output:*

🔐 Stored Passwords:
- gmail.com | alice123 | mysecret

<img width="1920" height="1080" alt="2025-09-07 (23)" src="https://github.com/user-attachments/assets/5662b265-e550-4fcb-87a3-486c4f5695fe" />

---


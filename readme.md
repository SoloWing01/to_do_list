# 📝 To-Do List (with SQLite Database)

This is a simple **command-line To-Do List application** built with **Python** and **SQLite3**.  
It supports full CRUD operations:

- ✅ View all tasks  
- ➕ Insert new tasks  
- ✏️ Update tasks  
- ❌ Delete tasks  
- 🚪 Exit the program  

All tasks are stored in a **SQLite database** (`to_do.db`) for persistence.

---

## ⚙️ Features
- Stores tasks in a local database  
- Auto-generates unique IDs for each task  
- Tracks task creation time with a timestamp  
- Boolean status field (completed ✅ or pending ⏳)  
- User-friendly CLI menu  

---

## 📂 Project Structure
.
├── to_do.py # Main Python script
├── to_do.db # SQLite database (auto-created on first run)
└── README.md # Project documentation
---

## 🚀 Getting Started

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/todo-list-database.git
cd todo-list-database

2️⃣ Run the program

Make sure you have Python 3.10+ installed (for match case support).

python to_do.py
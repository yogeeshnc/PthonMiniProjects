# 🎓 Student Management System

A simple **command-line based Student Management System** built with Python using **Object-Oriented Programming (OOP)** concepts. This program allows you to add, view, search, and delete student records interactively.

---

## 📋 Table of Contents

- [About the Project](#-about-the-project)
- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Sample Output](#-sample-output)
- [Concepts Used](#-concepts-used)
- [Author](#-author)

---

## 📖 About the Project

This project demonstrates the use of **Classes and Objects** in Python to manage student data. It provides a simple **menu-driven interface** that runs in the terminal, making it beginner-friendly and easy to understand.

> Perfect for students learning Python OOP concepts for the first time!

---

## ✨ Features

| Feature | Description |
|---|---|
| ➕ Add Student | Enter student details like name, USN, age, and branch |
| 📋 View All Students | Display all stored student records |
| 🔍 Search Student | Find a specific student by their USN |
| 🗑️ Delete Student | Remove a student record using their USN |
| 🚪 Exit | Safely exit the program |

---

## 🛠️ Technologies Used

- **Language:** Python 3.x
- **Paradigm:** Object-Oriented Programming (OOP)
- **Interface:** Command Line Interface (CLI)

---

## 📁 Project Structure

```
student-management-system/
│
├── student_management.py    # Main Python file containing all logic
└── README.md                # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have **Python 3.x** installed on your system.

```bash
python --version
```

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/yogeeshnc/student-management-system.git
```

**2. Navigate to the project directory**

```bash
cd student-management-system
```

**3. Run the program**

```bash
python student_management.py
```

> No external packages needed — runs on pure Python!

---

## 💻 Usage

Once the program starts, you will see the following menu:

```
--- Student Management System ---
1. Add Student
2. View Students
3. Search Student
4. Delete Student
5. Exit
Enter choice:
```

Enter the number corresponding to the action you want to perform and follow the prompts.

---

## 📸 Sample Output

### Adding a Student

```
--- Add Student ---
Enter name   : John Doe
Enter USN    : 1AB22CS001
Enter age    : 20
Enter branch : CSE

Student Added Successfully!
```

### Viewing All Students

```
--- Student List ---
Name   : John Doe
USN    : 1AB22CS001
Age    : 20
Branch : CSE
--------------------
```

### Searching a Student

```
--- Search Student ---
Enter USN to search: 1AB22CS001

Student Found:
Name   : John Doe
USN    : 1AB22CS001
Age    : 20
Branch : CSE
```

### Deleting a Student

```
--- Delete Student ---
Enter USN to delete: 1AB22CS001

Student deleted successfully!
```

---

## 🧠 Concepts Used

| Concept | Description |
|---|---|
| **Class & Object** | Student class is defined with attributes and methods |
| **Constructor (__init__)** | Initializes student attributes when an object is created |
| **Instance Methods** | display() method prints the student details |
| **Lists** | students[] list stores all student objects |
| **Loops** | Used to iterate through student records |
| **Functions** | Separate functions for each operation (add, view, search, delete) |
| **Conditional Statements** | Used for menu navigation and search/delete logic |

---

## 🙋 Author

**Yogeesh N C**

- Email  : yogeeshnc832@gmail.com
- GitHub : https://github.com/yogeeshnc

---

## 📄 License

This project is open source and available under the MIT License.

---

> If you found this project helpful, please give it a star on GitHub!

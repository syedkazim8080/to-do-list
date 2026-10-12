# 📝 To-Do Task Manager

A command-line Python application that helps you **add, view, complete and delete tasks**, and saves them so they are still there the next time you run it.
Built as part of the **Auspify Python Developer Internship**.

---

## 📌 Features

- **Add tasks** – type a task name and it is saved instantly
- **View tasks** – see every task with its number and status (Pending / Done)
- **Mark as completed** – choose a task by number and mark it as done
- **Delete tasks** – remove a task you no longer need
- **Persistent storage** – tasks are saved in `task.txt` and reloaded on startup
- **Input validation** – empty names, letters instead of numbers, and out-of-range numbers never crash the program

---

## 🛠️ Technologies & Skills

| Item | Details |
|------|---------|
| Language | Python 3.6+ |
| Modules | `os` (standard library only) |
| Concepts | Functions, loops, lists and dictionaries, file handling, exception handling, input validation |

No external packages are required.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/syedkazim8080/to-do-list.git
cd to-do-list
```

### 2. Run the program

```bash
python TO-DO-LIST.py
```

---

## 💻 Usage Example

```text
-----SHOW MENU-----
1. Add task
2. View task
3. Mark task as completed
4. Delete task
5. Exit
Enter your option (1-5): 1
Enter your task name: Buy milk
Your task is: Buy milk
Task 'Buy milk' added successfully!

-----SHOW MENU-----
1. Add task
2. View task
3. Mark task as completed
4. Delete task
5. Exit
Enter your option (1-5): 3

------- YOUR TASKS -------
1. Buy milk  -  Pending
Enter the task number to mark as completed: 1
Task 'Buy milk' marked as completed!

-----SHOW MENU-----
1. Add task
2. View task
3. Mark task as completed
4. Delete task
5. Exit
Enter your option (1-5): 2

------- YOUR TASKS -------
1. Buy milk  -  [✔] Done

-----SHOW MENU-----
1. Add task
2. View task
3. Mark task as completed
4. Delete task
5. Exit
Enter your option (1-5): 5
Tasks saved. Goodbye!
```

---

## ⚙️ How It Works

1. On startup, the program reads `task.txt` and loads every saved task into a list of dictionaries.
2. Each task is stored as `{"title": "...", "completed": True/False}`.
3. The menu loop runs until the user chooses Exit.
4. After every change (add, complete, delete) and on exit, all tasks are written back to `task.txt`.

Tasks are saved one per line in this format:

```text
Buy milk | DONE
Finish internship project | PENDING
```

---

## 📂 Project Structure

```text
to-do-list/
├── TO-DO-LIST.py   # Main application
├── task.txt        # Created automatically when you add your first task
└── README.md       # Project documentation
```

---

## 🔮 Future Improvements

- Edit an existing task
- Due dates and priorities
- Search and filter tasks
- Clear all completed tasks at once
- GUI version using Tkinter

---

## 👤 Author

**Syed Kaim Ali Shah**
Python Developer Intern @ Auspify
GitHub: [@syedkazim8080](https://github.com/syedkazim8080)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

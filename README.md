# Smart Student Task Manager

## Project Overview
Smart Student Task Manager is a Python-based productivity application designed to help students organize academic and personal tasks in one place.

The application provides a simple, reliable command-line interface and stores task information locally in JSON format.

## Key Features
- Create and save tasks
- Assign Low, Medium, or High priority
- View all tasks in a structured table
- Mark tasks as completed
- Delete unwanted tasks
- View total, pending, and completed task counts
- Persistent local JSON storage
- Input validation and basic error handling

## Technology Stack
- Python 3.9+
- JSON
- Python Standard Library

## Project Structure
```text
Smart_Student_Task_Manager/
├── app.py
├── requirements.txt
├── README.md
└── project_report.pdf
```

## Installation
No third-party packages are required.

Install Python 3.9 or later and open a terminal in the project folder.

## Execution
Run:

```bash
python app.py
```

On some systems, use:

```bash
python3 app.py
```

## How to Use
1. Select **Add Task** to create a task.
2. Enter the task title.
3. Select Low, Medium, or High priority.
4. Select **View Tasks** to see saved tasks.
5. Select **Complete Task** to update a task.
6. Select **Delete Task** to remove a task.
7. Select **Task Summary** to view progress.
8. Select **Exit** to close the application.

## Data Storage
Task information is stored automatically in `tasks.json` in the same directory. This file is generated when the first task is saved.

## Future Enhancements
- Graphical User Interface
- Web/mobile version
- SQLite or MySQL database
- User authentication
- Deadline and reminder notifications
- Calendar integration
- Task analytics and progress charts
- Cloud synchronization

## Author
**Altaf Bagawan**  
Information Science Engineering  
Bapuji Institute of Engineering & Technology, Davanagere

# Todo List Application

A simple command-line todo list application built in Python with JSON persistence.

## Features

- ✅ Add new tasks
- 📋 View all tasks with status
- ✏️ Update task titles
- ☑️ Toggle task completion status
- 🗑️ Delete tasks
- 💾 Automatic data persistence to JSON file
- 🔄 Load existing tasks on startup

## Installation

No additional dependencies required - uses only Python standard library.

**Requirements:**
- Python 3.6 or higher

## Usage

### Running the Application

```bash
python tempCodeRunnerFile.py
```

### Menu Options

The application provides an interactive menu with the following options:

1. **Add Task** - Create a new task
2. **View Tasks** - Display all tasks with their status
3. **Update Task** - Modify existing tasks
4. **Delete Task** - Remove tasks
5. **Exit** - Close the application

### Example Usage

```
Todo App Menu:
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Exit
Enter your choice: 1
Enter task title: Buy groceries
Task added: Buy groceries (ID: 1)
```

## Data Storage

Tasks are automatically saved to `todos.json` in the same directory. The file structure:

```json
[
    {
        "id": 1,
        "title": "Buy groceries",
        "completed": false
    },
    {
        "id": 2,
        "title": "Walk the dog",
        "completed": true
    }
]
```

## Code Structure

### Classes

#### `Task`
Represents a single todo item with:
- `id`: Unique identifier
- `title`: Task description
- `completed`: Boolean status

**Methods:**
- `to_dict()`: Convert task to dictionary
- `from_dict(data)`: Create task from dictionary

#### `TodoList`
Manages the collection of tasks with:
- `tasks`: List of Task objects
- `filename`: JSON file for persistence
- `next_id`: Auto-incrementing ID counter

**Methods:**
- `add_task(title)`: Add new task
- `view_tasks()`: Display all tasks
- `update_task(task_id, new_title, toggle_complete)`: Modify task
- `delete_task(task_id)`: Remove task
- `save()`: Write tasks to JSON file
- `load()`: Read tasks from JSON file

## Testing

The application includes comprehensive tests:

```bash
# Run all tests
python test_todo_app.py

# Run manual functionality test
python manual_test.py
```

### Test Coverage

- ✅ Task creation and manipulation
- ✅ TodoList operations (add, view, update, delete)
- ✅ Data persistence and loading
- ✅ Edge cases and error handling
- ✅ Complete workflow integration

## Error Handling

The application handles common errors gracefully:

- Invalid task IDs
- Non-existent tasks
- Empty task lists
- File I/O issues
- Invalid user input

## File Structure

```
.
├── todo_App.py    # Main application
├── todos.json              # Data storage (auto-created)
├── test_todo_app.py        # Comprehensive test suite
├── manual_test.py          # Manual testing script
└── README.md              # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Future Enhancements

Potential improvements:
- Due dates for tasks
- Task categories/tags
- Priority levels
- Search functionality
- Export to different formats
- Web interface
- Multiple todo lists

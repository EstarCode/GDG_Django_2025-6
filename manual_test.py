#!/usr/bin/env python3
"""
Manual test script to verify the todo app functionality
"""
from tempCodeRunnerFile import TodoList
import os

def test_manual_operations():
    """Test the todo app with manual operations"""
    
    # Use a test file
    test_file = "test_todos.json"
    
    # Clean up any existing test file
    if os.path.exists(test_file):
        os.remove(test_file)
    
    print("=== Testing Todo List Application ===\n")
    
    # Initialize todo list
    todo = TodoList(filename=test_file)
    print("✓ TodoList initialized successfully")
    
    # Test adding tasks
    print("\n--- Testing Add Task ---")
    todo.add_task("Buy groceries")
    todo.add_task("Walk the dog")
    todo.add_task("Finish Python project")
    
    # Test viewing tasks
    print("\n--- Testing View Tasks ---")
    todo.view_tasks()
    
    # Test updating task title
    print("\n--- Testing Update Task Title ---")
    todo.update_task(2, new_title="Walk the dog in the park")
    
    # Test toggling completion
    print("\n--- Testing Toggle Completion ---")
    todo.update_task(1, toggle_complete=True)
    
    # View updated tasks
    print("\n--- Updated Task List ---")
    todo.view_tasks()
    
    # Test deleting a task
    print("\n--- Testing Delete Task ---")
    todo.delete_task(3)
    
    # Final view
    print("\n--- Final Task List ---")
    todo.view_tasks()
    
    # Test persistence by creating new instance
    print("\n--- Testing Persistence ---")
    new_todo = TodoList(filename=test_file)
    print("Loaded tasks from file:")
    new_todo.view_tasks()
    
    # Test edge cases
    print("\n--- Testing Edge Cases ---")
    print("Trying to update non-existent task:")
    todo.update_task(999, new_title="This won't work")
    
    print("Trying to delete non-existent task:")
    todo.delete_task(999)
    
    # Clean up
    if os.path.exists(test_file):
        os.remove(test_file)
    
    print("\n✓ All manual tests completed successfully!")

if __name__ == "__main__":
    test_manual_operations()
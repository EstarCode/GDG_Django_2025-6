#!/usr/bin/env python3
"""
Comprehensive test suite for the Todo List application
"""
import json
import os
import tempfile
import unittest
from unittest.mock import patch
from tempCodeRunnerFile import Task, TodoList


class TestTask(unittest.TestCase):
    """Test the Task class functionality"""
    
    def test_task_creation(self):
        """Test creating a new task"""
        task = Task(1, "Test task")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test task")
        self.assertFalse(task.completed)
    
    def test_task_creation_with_completed_status(self):
        """Test creating a task with completed status"""
        task = Task(2, "Completed task", completed=True)
        self.assertTrue(task.completed)
    
    def test_task_to_dict(self):
        """Test converting task to dictionary"""
        task = Task(1, "Test task", completed=True)
        expected = {'id': 1, 'title': 'Test task', 'completed': True}
        self.assertEqual(task.to_dict(), expected)
    
    def test_task_from_dict(self):
        """Test creating task from dictionary"""
        data = {'id': 3, 'title': 'From dict task', 'completed': False}
        task = Task.from_dict(data)
        self.assertEqual(task.id, 3)
        self.assertEqual(task.title, 'From dict task')
        self.assertFalse(task.completed)


class TestTodoList(unittest.TestCase):
    """Test the TodoList class functionality"""
    
    def setUp(self):
        """Set up test environment with temporary file"""
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        self.temp_file.close()
        self.todo_list = TodoList(filename=self.temp_file.name)
    
    def tearDown(self):
        """Clean up temporary file"""
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)
    
    def test_empty_todo_list_initialization(self):
        """Test initializing empty todo list"""
        self.assertEqual(len(self.todo_list.tasks), 0)
        self.assertEqual(self.todo_list.next_id, 1)
    
    def test_add_task(self):
        """Test adding a task"""
        with patch('builtins.print') as mock_print:
            self.todo_list.add_task("Test task")
            mock_print.assert_called_with("Task added: Test task (ID: 1)")
        
        self.assertEqual(len(self.todo_list.tasks), 1)
        self.assertEqual(self.todo_list.tasks[0].title, "Test task")
        self.assertEqual(self.todo_list.tasks[0].id, 1)
        self.assertEqual(self.todo_list.next_id, 2)
    
    def test_add_multiple_tasks(self):
        """Test adding multiple tasks"""
        with patch('builtins.print'):
            self.todo_list.add_task("Task 1")
            self.todo_list.add_task("Task 2")
            self.todo_list.add_task("Task 3")
        
        self.assertEqual(len(self.todo_list.tasks), 3)
        self.assertEqual(self.todo_list.next_id, 4)
    
    def test_view_tasks_empty(self):
        """Test viewing tasks when list is empty"""
        with patch('builtins.print') as mock_print:
            self.todo_list.view_tasks()
            mock_print.assert_called_with("No tasks found.")
    
    def test_view_tasks_with_data(self):
        """Test viewing tasks with data"""
        with patch('builtins.print') as mock_print:
            self.todo_list.add_task("Test task")
            mock_print.reset_mock()
            self.todo_list.view_tasks()
            mock_print.assert_called_with("ID: 1 | Title: Test task | Status: Pending")
    
    def test_update_task_title(self):
        """Test updating task title"""
        with patch('builtins.print') as mock_print:
            self.todo_list.add_task("Original title")
            mock_print.reset_mock()
            self.todo_list.update_task(1, new_title="Updated title")
            mock_print.assert_called_with("Task updated: Updated title (ID: 1)")
        
        self.assertEqual(self.todo_list.tasks[0].title, "Updated title")
    
    def test_update_task_toggle_completion(self):
        """Test toggling task completion status"""
        with patch('builtins.print') as mock_print:
            self.todo_list.add_task("Test task")
            mock_print.reset_mock()
            self.todo_list.update_task(1, toggle_complete=True)
            mock_print.assert_called_with("Task updated: Test task (ID: 1)")
        
        self.assertTrue(self.todo_list.tasks[0].completed)
        
        # Toggle back
        with patch('builtins.print'):
            self.todo_list.update_task(1, toggle_complete=True)
        self.assertFalse(self.todo_list.tasks[0].completed)
    
    def test_update_nonexistent_task(self):
        """Test updating a task that doesn't exist"""
        with patch('builtins.print') as mock_print:
            self.todo_list.update_task(999, new_title="New title")
            mock_print.assert_called_with("Task with ID 999 not found.")
    
    def test_delete_task(self):
        """Test deleting a task"""
        with patch('builtins.print') as mock_print:
            self.todo_list.add_task("Task to delete")
            mock_print.reset_mock()
            self.todo_list.delete_task(1)
            mock_print.assert_called_with("Task with ID 1 deleted.")
        
        self.assertEqual(len(self.todo_list.tasks), 0)
    
    def test_delete_nonexistent_task(self):
        """Test deleting a task that doesn't exist"""
        with patch('builtins.print') as mock_print:
            self.todo_list.delete_task(999)
            mock_print.assert_called_with("Task with ID 999 deleted.")
    
    def test_save_and_load_persistence(self):
        """Test saving and loading tasks from file"""
        # Add some tasks
        with patch('builtins.print'):
            self.todo_list.add_task("Task 1")
            self.todo_list.add_task("Task 2")
            self.todo_list.update_task(1, toggle_complete=True)
        
        # Create new TodoList instance with same file
        new_todo_list = TodoList(filename=self.temp_file.name)
        
        # Verify data was loaded correctly
        self.assertEqual(len(new_todo_list.tasks), 2)
        self.assertEqual(new_todo_list.tasks[0].title, "Task 1")
        self.assertTrue(new_todo_list.tasks[0].completed)
        self.assertEqual(new_todo_list.tasks[1].title, "Task 2")
        self.assertFalse(new_todo_list.tasks[1].completed)
        self.assertEqual(new_todo_list.next_id, 3)


class TestIntegration(unittest.TestCase):
    """Integration tests for the complete workflow"""
    
    def setUp(self):
        """Set up test environment"""
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        self.temp_file.close()
        self.todo_list = TodoList(filename=self.temp_file.name)
    
    def tearDown(self):
        """Clean up"""
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)
    
    def test_complete_workflow(self):
        """Test a complete workflow of operations"""
        with patch('builtins.print'):
            # Add tasks
            self.todo_list.add_task("Buy groceries")
            self.todo_list.add_task("Walk the dog")
            self.todo_list.add_task("Finish project")
            
            # Complete one task
            self.todo_list.update_task(2, toggle_complete=True)
            
            # Update task title
            self.todo_list.update_task(3, new_title="Finish Python project")
            
            # Delete a task
            self.todo_list.delete_task(1)
        
        # Verify final state
        self.assertEqual(len(self.todo_list.tasks), 2)
        
        # Find remaining tasks
        remaining_tasks = {task.id: task for task in self.todo_list.tasks}
        
        # Task 2 should be completed
        self.assertTrue(remaining_tasks[2].completed)
        self.assertEqual(remaining_tasks[2].title, "Walk the dog")
        
        # Task 3 should have updated title
        self.assertEqual(remaining_tasks[3].title, "Finish Python project")
        self.assertFalse(remaining_tasks[3].completed)


if __name__ == '__main__':
    # Run the tests
    unittest.main(verbosity=2)
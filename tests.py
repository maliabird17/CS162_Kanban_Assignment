# Import required packages 
import os
import unittest
from app import app, db

# Class for running all unit tests of Kanban's functionalities 
class KanbanTests(unittest.TestCase):
    # Setting up the Kanban for testing (execute before testing) 
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite'
        self.app = app.test_client()
        
        app.app_context().push()
        db.drop_all()
        db.create_all()

        self.assertEqual(app.debug, False)

    # Tearing down anything created during testing (for after testing) 
    def tearDown(self):
        pass

    # Test main page 
    def test_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    ## Testing the addition of each type of task (todo, doing & done tasks)
    # Add a task to the Todo column of the Kanban
    def test_addtodotask(self):
        # Fake task inputs used for testing 
        task_info = dict(content = "Test Task for Todo", status = 1) # status = Todo
        # App posts new task and response is stored 
        response = self.app.post(
            '/add_task/1',
            data = task_info,
            follow_redirects=True)
        
        # Check the request's response was a success 
        self.assertEqual(response.status_code, 200)

    # Add a task to the Doing column of the Kanban
    def test_adddoingtask(self):
        task_info = dict(content = "Test Task for Doing", status = 2) # status = Doing 
        response = self.app.post(
            '/add_task/2',
            data = task_info,
            follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)

    # Add a task to the Done column of the Kanban
    def test_adddonetask(self):
        task_info = dict(content = "Test Task for Done", status = 3) # status = Done
        response = self.app.post(
            '/add_task/3',
            data = task_info,
            follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)

    # Testing that task statuses can be updated 
    def test_update(self):
        self.test_addtodotask() # add a new todo task 
        response = self.app.get(
            "/update/3/1", 
            follow_redirects=True) # move the todo task to done
        
        self.assertEqual(response.status_code, 200)

    # Testing that tasks can be deleted 
    def test_deletetask(self):
        self.test_addtodotask() # add a new doing task 
        response = self.app.get(
            "/delete_task/1", 
            follow_redirects=True) 
        
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
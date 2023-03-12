# Import required packages 
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Flask Configuration 
app = Flask(__name__)

# Create database to store tasks using SQLlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

# Class of Tasks to be used in the database
class Task(db.Model):
    # Task Parameters set automatically: id & date_created
    id = db.Column(db.Integer, primary_key = True) # unique ids for each task
    date_created = db.Column(db.DateTime, default=datetime.utcnow) # 
    # Task Parameters to be specified: content & status
    content = db.Column(db.String(200)) # content describing task
    status = db.Column(db.Integer) # integer refering to todo, doing, done

    # Defining task representation
    def __repr__(self):
        return '<Task %r>' % self.id

# Main page to visualize Kanban Board
@app.route('/') # just using GET method
def index():
    # Retrieve all tasks from the database, according to status and ordered by date created 
    todo_tasks = Task.query.filter_by(status = 1).order_by(Task.date_created).all()
    doing_tasks = Task.query.filter_by(status = 2).order_by(Task.date_created).all()
    done_tasks = Task.query.filter_by(status = 3).order_by(Task.date_created).all()
    
    # Render HTML template, using sectioned versions of the database
    return render_template('index.html', todo_tasks = todo_tasks, doing_tasks = doing_tasks, done_tasks = done_tasks)


# Add Tasks anywhere on the Kanban Board 
# Route using task status (required to know where to add the task)
@app.route('/add_task/<int:task_status>', methods = ['POST']) # just using POST
def add_task(task_status): 
    '''
    To add tasks to the kanban board of the specified status. 
    '''
    # Get description of the task from form
    content = request.form.get("content")

    # Create a new Task instance with content and status as specified in url
    new_task = Task(content = content, status = task_status)
    db.session.add(new_task) # add task to database
    db.session.commit() # commit modifications
    return redirect(url_for('index')) 


# Change a Task's Status 
# Route using task status and ID (required to know what task to move & where)
@app.route('/update/<int:task_status>/<int:task_id>', methods = ['GET'])
def update(task_status, task_id):
    '''
    Update the status (todo, doing, done) of a task as specified. 
    '''
    # Get task instance corresponding to given task id
    task = Task.query.filter_by(id = task_id).first()
    
    # Update status value depending on new status specified in the url
    if task_status == 1: # New status is Todo
        task.status = 1 # change instance attribute
    if task_status == 2: # status = Doing  
        task.status = 2
    if task_status == 3: # status = Done
        task.status = 3 
    
    db.session.commit() # commit database modifications
    return redirect(url_for('index')) # redirect back to main page


# Delete a Task from the Kanban Board
# Route using task id (required to know which task to delete from db)
@app.route('/delete_task/<int:task_id>') # using only GET method
def delete_task(task_id):
    """
    Delete a task from the Kanban Board. 
    """
    # Get task instance corresponding to given task id
    task = Task.query.filter_by(id= task_id).first()
    
    # Remove task instance from database
    db.session.delete(task)

    db.session.commit() # commit modifications to database
    return redirect(url_for('index')) # redirect back to main page


# Command to run the application with debug 
if __name__ == "__main__":
    app.app_context().push()
    db.create_all()
    app.run(debug=True, port = 7000) # run app using port 7000 
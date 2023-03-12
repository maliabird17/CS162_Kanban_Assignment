# C162 Web Application Assignment: Malia's Kanban

## **Kanban Demo:**

See the video linked here for an overview of the web application's functionality: 

<a href="https://ibb.co/gDgmKss"><img src="https://i.ibb.co/9qYc5RR/Screenshot-2023-03-12-at-13-43-30.png" alt="Screenshot-2023-03-12-at-13-43-30" border="0"></a>

## **Code Overview:**

The code from this project is organized within this repo into the following categories and files (excluding this README):

- `static`: this folder contains all static files including: 
    - `kanban_title_art.png`: image used for the title art design
    - `main.css`: CSS code used as the style sheet

- `templates`: this folder contains all HTML files used for the web applications including: 
    - `base.html`: for all basic specifications of the HTML file (including head)
    - `index.html`: design of the kanban board

- `app.py`: python code utilizing Flask and SQL to create kanban application's functionality 

- `tests.py`: python code for running unit tests of kanban application

- `requirements.txt`: required package versions 

## **Installation Instructions:**

To get the application running, follow the steps below for your system: 

**macOS**

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 app.py
```

**Windows**

```bash
python3 -m venv venv
venv\Scripts\activate.bat
pip3 install -r requirements.txt
python3 app.py
```

And to test the app's functionality using the specified unti tests, run: 

```bash
python3 -m unittest discover
```
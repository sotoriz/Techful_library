# I assume you're looking for a sample project that demonstrates the use of Flask and Tkinter together. Here's a simple one that displays a Tkinter window that allows the user to enter a name, which Flask then displays on a webpage.


from flask import Flask, render_template, request
import tkinter as tk

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def form_data():
    name = request.form['name']
    return render_template('index.html', message='Hello, %s!' % name)

def tkinter_window():
    window = tk.Tk()

    # set the window title
    window.title('Flask-Tkinter App')

    # set the window size
    window.geometry('300x150')

    # add a label and entry field to the window
    name_label = tk.Label(window, text='Enter your name:', font=('Arial', 12))
    name_label.pack(pady=10)

    name_entry = tk.Entry(window)
    name_entry.pack()

    # add a button to submit the form
    submit_button = tk.Button(window, text='Submit', command=lambda: submit_form(name_entry.get()))
    submit_button.pack(pady=10)

    window.mainloop()

def submit_form(name):
    with app.test_client() as c:
        c.post('/', data={'name': name})
        response = c.get('/')
        print(response.data)

if __name__ == '__main__':
    app.run()


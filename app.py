# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Harshita Bhatia" # write your name
    age = "14" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/mother")
def mother_webpage():
    name = "Rachna Bhatia"
    age = "45"
    return render_template('mother.html' , name = name , age = age)

# define the route to mother webpage
@app.route("/father")
def father_webpage():
    name = "Naveen Bhatia"
    age = "50"
    return render_template('father.html' , name = name , age = age)

# define the route to friends webpage
@app.route("/friend")
def friend_webpage():
    name = "Kriti"
    age = "14"
    return render_template('friend.html' , name = name , age = age)

app.run(debug = True)

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)

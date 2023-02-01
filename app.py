from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    # html_welcome = """
    #         <html>
    #             <h1>Welcome</h1>
    #             <p>This is the Welcome Page </p>
                             
    #         </html>
    #         """
    # return html_welcome
    return "welcome"

@app.route('/welcome/home')
def welcome_home():
    # html_welcome_home = """
    #         <html>
    #             <h1>Welcome Home</h1>
    #             <p>This is the Welcome Home Page </p>
                             
    #         </html>
    #         """
    # return html_welcome_home
    return "welcome home"

@app.route('/welcome/back')
def welcome_back():
    # html_welcome_back = """
    #         <html>
    #             <h1>Welcome Back</h1>
    #             <p>This is the Welcome Back Page </p>
                             
    #         </html>
    #         """
    # return html_welcome_back
    return "welcome back"


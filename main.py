from flask import Flask, render_template
app = Flask(__name__, template_folder='79m/templates')

@app.route('/')
def home_page():
    # return render_template("test_file.html")
    return "Hello world!"

if __name__ == '__main__':
    app.run(debug= True)
from flask import Flask, render_template,jsonify,request

myapp = Flask(__name__)


@myapp.route('/')
def hello():
    return "Hello From My app"


@myapp.route('/hcl')
def index():
    return "Hello HCL Developers"


@myapp.route('/home')
def home():
   return render_template("home.html")
@myapp.route('/demo')
def demo():
    return jsonify(name="Manjusha", place="Guntur", role="Tester")
@myapp.route('/emp')
def emp():
    return render_template("emp.html")
@myapp.route('/result',methods=['GET','POST'])
def result():
    if request.method=='POST':
        result=request.form
        return render_template("result.html",result=result)
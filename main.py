from flask import Flask, render_template, request, redirect
import pollingDB

app = Flask(__name__)

validResourcePaths:set = {"index/index.js", "index/style.css"}

@app.route('/')
def landingPage() -> str:
    return render_template('index/index.html')
    

@app.route('/resource/<path:path>')
def resource(path: str) -> str:
    if path in validResourcePaths:
        return render_template(path)
    else:
        return render_template("noResource/noResource.html")
    
    return resourceFile


@app.route('/<path:path>')
def catchAll(path: str) -> redirect:
    return redirect("/")

app.run()

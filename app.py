from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>DevOps Page</title>
</head>
<body style="font-family: Arial; text-align: center; margin-top: 50px;">

    <h1>{{ message }}</h1>

    <form method="post">
        <button type="submit">Academy</button>
    </form>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        message = "Have a nice day"
    else:
        message = "Hello DevOpsGroup"
    return render_template_string(HTML, message=message)


# only used if running python app.py locally (NOT in Docker)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
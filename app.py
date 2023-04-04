from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    make_response,
    jsonify,
    send_from_directory,
)
from data_manager import DataManager
from notification_manager import NotificationManager
from helpers import get_random_token
from flight_data import FlightData

app = Flask(__name__)
app.secret_key = "test"

dm = DataManager()
notification_manager = NotificationManager()
fd = FlightData()


@app.route("/")
def index():
    cookie = request.cookies.get("web")
    if cookie:
        return render_template("index.html")
    return render_template("main.html")


@app.route("/", methods=["GET", "POST"])
def get_email():
    if request.method == "POST":
        email = request.form.get("email")
        token = get_random_token()
        print(email, token)
        if email != "" and token != "":
            try:
                if not dm.validate_user(email):
                    dm.add_user(email, token)
                    notification_manager.send_welcome_deals(email)
                    response = make_response(render_template("main.html"))
                    response.set_cookie("token", token, 365)
                    return response
                else:
                    response = make_response(render_template("main.html"))
                    return response
            except Exception as e:
                print(e)
    return render_template("main.html")


@app.route("/contact")
def get_message():
    return render_template("contact.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        email = request.form.get("email")
        message = request.form.get("message")
        name = request.form.get("name")
        if name != "" and message != "" and email != "":
            print(message, name, email)
            try:
                notification_manager.notify_me(name, email, message)
            except Exception as e:
                print(e)
        else:
            print("failed")
    return ("", 204)


@app.route("/about")
def about_us():
    return render_template("about.html")


@app.route("/main")
def main_page():
    return render_template("index.html", token="hello world")


@app.route("/remove_user", methods=["GET", "POST"])
def remove_cookie():
    if request.method == "POST":
        email = request.form.get("email")
        if email != "":
            dm.delete_user(email)
            response = make_response(redirect(url_for("get_email")))
            response.set_cookie("cookie-consent", "", max_age=0)
            response.set_cookie("web", "", max_age=0)
            response.set_cookie("excel", "", max_age=0)
            response.set_cookie("token", "", max_age=0)
            response.set_cookie("no_cookies", "", max_age=0)
        return response
    return render_template("remove_user.html")


@app.route("/flights")
def get_the_flights():
    data = fd.web_deals()
    return jsonify(data)


@app.route("/images/<path:filename>")
def serve_image(filename):
    return send_from_directory("static/res/cities", filename)


if __name__ == "__main__":
    app.run(debug=True)

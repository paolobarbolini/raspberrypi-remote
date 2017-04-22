import flask
import RPi.GPIO as GPIO

PIN = 8

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)

app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template("index.html", on=GPIO.input(PIN))


@app.route("/switch", methods=["POST"])
def switch():
    GPIO.output(PIN, GPIO.LOW if GPIO.input(PIN) else GPIO.HIGH)

    return flask.redirect(flask.url_for("index"))

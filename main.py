import flask
import RPi.GPIO as GPIO


PINS = [
    8,
    36,
    13,
    15
]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
for pin in PINS:
    GPIO.setup(pin, GPIO.OUT)

app = flask.Flask(__name__)


@app.route("/")
def index():
    states = []
    for pin in PINS:
        states.append({
            "id": pin,
            "state": bool(GPIO.input(pin)),
        })

    return flask.render_template("index.html", states=states)


@app.route("/switch/<int:id>", methods=["POST"])
def switch(id):
    if id not in PINS:
        return flask.jsonify({
            "success": False
        }), 403

    GPIO.output(id, GPIO.LOW if GPIO.input(id) else GPIO.HIGH)

    return flask.jsonify({
        "success": True
    })

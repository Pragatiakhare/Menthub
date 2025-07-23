from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from models import db, User, MentorshipRequest
from ml.matcher import match_mentees_to_mentors


app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:anusha@localhost/Menthub'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/match", methods=["GET"])
def match():
    mentees = User.query.filter_by(role='mentee').all()
    mentors = User.query.filter_by(role='mentor').all()

    match_result = match_mentees_to_mentors(mentees, mentors)

    return jsonify(match_result)


if __name__ == "__main__":
    app.run(debug=True)
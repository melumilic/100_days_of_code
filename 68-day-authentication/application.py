from fileinput import filename
from flask import (
    Flask,
    render_template,
    request,
    url_for,
    redirect,
    flash,
    abort,
    send_from_directory,
)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    login_required,
    current_user,
    logout_user,
)
from urllib.parse import urlparse, urljoin
from flask import request, url_for

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc


app = Flask(__name__)
# Set the secret key to some random bytes. Keep this really secret!
# refer to https://flask.palletsprojects.com/en/2.1.x/quickstart/#sessions
# to generate an actual key
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.config["SECRET_KEY"] = "any-secret-key-you-choose"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

app.config["UPLOAD_FOLDER"] = "static/files"

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))



# Line below only required once, when creating DB.
# db.create_all()

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        new_user = User(
            email=request.form.get("email"),
            name=request.form.get("name"),
            password=generate_password_hash(
                password=request.form.get("password"),
                method="pbkdf2:sha256",
                salt_length=8
            ),
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("secrets"))

    return render_template("register.html")


@app.route("/login", methods=["POST","GET"])
def login():
    if request.method=="POST":
        user_to_login = db.session.query(User).filter_by(email=request.form.get("email")).first()
        if user_to_login:
            if check_password_hash(pwhash=user_to_login.password,password=request.form.get("password")):
                login_user(user_to_login)
                flash('Logged in successfully.')
                next = request.args.get("next")
                if not is_safe_url(next):
                    return abort(400)
                return redirect(next or url_for('secrets'))
    return render_template('login.html')



@app.route("/secrets")
@login_required
def secrets():
    return render_template("secrets.html",name=current_user.name)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/download", methods=["GET"])
@login_required
def download():
    return send_from_directory(
        directory=app.config["UPLOAD_FOLDER"], path="cheat_sheet.pdf"
    )


if __name__ == "__main__":
    app.run(debug=True)

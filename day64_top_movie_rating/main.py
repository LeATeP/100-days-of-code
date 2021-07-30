from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movie-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)


api_key = "7256dfecd66c1bd10fb98d2e5d4028da"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"


class MyForm(FlaskForm):
    rating = StringField('rating')
    review = StringField('review')
    submit = SubmitField("Done")
    
class add_movie_form(FlaskForm):
    title = StringField('title')
    submit = SubmitField("Add")


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=False)
    rating = db.Column(db.Float(120), unique=False, nullable=True)
    ranking = db.Column(db.Integer, unique=False, nullable=True)
    review = db.Column(db.String(240), unique=False, nullable=True)
    img_url = db.Column(db.String(240), unique=False, nullable=False)

    def __repr__(self):
        return f'{self.title}'
    
    
db.create_all()


@app.route("/")
def home():
    all_movie = Movie.query.all()
    all_movie.sort(key=lambda x: x.rating, reverse=True)
    
    for movie in all_movie:
        movie.ranking = all_movie.index(movie) + 1
    db.session.commit()
    return render_template("index.html", movies=all_movie)


@app.route("/add", methods=["GET", "POST"])
def add():
    add_form = add_movie_form()
    
    if add_form.validate_on_submit():
        title = add_form.title.data
        return redirect(url_for("select", title=title))
    return render_template('add.html', add_form=add_form)


@app.route("/select", methods=["GET", "POST"])
def select():
    r = requests.get("https://api.themoviedb.org/3/search/movie", params={
    'api_key': "7256dfecd66c1bd10fb98d2e5d4028da",
    'query': request.args.get("title"),})
    r.raise_for_status()
    all_movies = r.json()['results']
    
    return render_template('select.html', movies=all_movies)


@app.route("/find_movie", methods=["GET", "POST"])
def find_movie():
    movie_api_id = request.args.get('id')
    if movie_api_id:
        request_url = f'{MOVIE_DB_INFO_URL}/{movie_api_id}'
        response = requests.get(request_url, params={'api_key': "7256dfecd66c1bd10fb98d2e5d4028da"})
        data = response.json()
        new_book = Movie(title = data['title'],
                        year = data['release_date'].split("-")[0], 
                        description = data['overview'],
                        img_url = f'{MOVIE_DB_IMAGE_URL}{data["poster_path"]}',)
        db.session.add(new_book)
        db.session.commit()
        
        return redirect(url_for('edit', movie_id=new_book.id))
        
        
@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = MyForm()
    movie_id = request.args.get("movie_id")
    movie = Movie.query.get(movie_id)
    
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete", methods=["GET", "POST"])
def delete():
    book_id = request.args.get('movie_id')
    book = Movie.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)

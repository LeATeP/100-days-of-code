#%%
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    author = db.Column(db.String(120), unique=False, nullable=False)
    rating = db.Column(db.String(120), unique=False, nullable=False)

    def __str__(self):
        return f'{self.title} {self.author} {self.rating}'
    
db.create_all()


@app.route('/', methods=["GET", "POST"])
def home():
    all_books = Book.query.all()
    
    return render_template('index.html', books=all_books)



@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(title=request.form.get('book'), 
                        author=request.form.get('author'), 
                        rating=request.form.get('rating'))

        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form.get('id')
        book = Book.query.get(book_id)
        
        book.rating = request.form.get('new_rating')
        db.session.commit()
        return redirect(url_for('home'))
    
    book_id = request.args.get('book_id')
    book = Book.query.get(book_id)
    return render_template('edit.html', book=book)


@app.route("/delete")
def delete():
    book_id = request.args.get('book_id')
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)


# %%

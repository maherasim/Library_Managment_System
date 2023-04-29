from flask import Blueprint, render_template, redirect, url_for, request, flash
import json
from app.auth import DBSession
from .models import Books  
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from . import Session
from . import *
session=Session(bind=engine)
app = Blueprint('name', __name__)

@app.route('/show_books')
def index():
    
    query = session.query(Books)
    book_id = request.args.get('id')
    if book_id:
        query = query.filter(Books.id == book_id)
    results = query.all()
    added_books = session.query(Books).count()
    checked_out_books = session.query(Books).filter(Books.checked_out == True).count()
    checked_in_books = session.query(Books).filter(Books.checked_out == True).count()
    fig = make_subplots(rows=1, cols=3, shared_yaxes=True, horizontal_spacing=0.1, subplot_titles=('Added Books', 'Checked Out Books', 'Checked In Books'))
    fig.add_trace(go.Bar(x=[added_books], y=['Books Added'], orientation='h', showlegend=False), row=1, col=1)
    fig.add_trace(go.Bar(x=[checked_out_books], y=['Books Checked Out'], orientation='h', showlegend=False), row=1, col=2)
    fig.add_trace(go.Bar(x=[checked_in_books], y=['Books Checked In'], orientation='h', showlegend=False), row=1, col=3)
    fig.update_layout(title='Book Status', height=400, margin=dict(l=50, r=50, b=50, t=50))
    graph_html = fig.to_html(full_html=False)
    return render_template('show_books.html', results=results, graph=graph_html)




    
@app.route('/add_book')
def addbook():
    return render_template('add_books.html')

@app.route('/add_book', methods=['POST'])
def add_book():
    if(request.method=='POST'):
        name = request.form.get('name')
        description = request.form.get('description')
        pub_by = request.form.get('pub_by')
        copies = request.form.get('copies')
        session = DBSession()
        entry = Books(name=name, description=description, pub_by=pub_by, copies=copies)
        session.add(entry)
        session.commit()
        flash('Book successfully Added')
        
    return redirect('show_books')

@app.route('/edit_book/<int:id>', methods=['GET', 'POST'])
def edit_book(id):
    session = DBSession()
    book = session.query(Books).filter_by(id=id).one()

    if request.method == 'POST':
        book.name = request.form.get('name')
        book.description = request.form.get('description')
        book.pub_by = request.form.get('pub_by')
        book.copies = request.form.get('copies')
        session.commit()
        flash('Book successfully Edited')
        return redirect(url_for('name.index'))

    return render_template('edit_books.html', book=book)
@app.route('/delete_book/<int:id>')
def delete_book(id):
    session = DBSession()
    book = session.query(Books).filter_by(id=id).one()
    session.delete(book)
    session.commit()
    flash('Book successfully deleted')
    return redirect(url_for('name.index'))

@app.route('/checkout_book/<int:id>', methods=['GET', 'POST'])
def checkout_book(id):
    session = DBSession()
    book = session.query(Books).filter_by(id=id).one()

    if request.method == 'POST':
        borrower_name = request.form.get('borrower_name')
        book.checked_out = True
        book.checked_out_by1 = borrower_name
        session.commit()
        flash(f'Book {book.name} checked out by {borrower_name}')


    return render_template('checkout_book.html', id=id)



@app.route('/checkin_book/<int:id>')
def checkin_book(id):
    session = DBSession()
    book = session.query(Books).filter_by(id=id).one()
    book.checked_out = False
    book.checked_out_by1 = None
    session.commit()
    flash('Book successfully checked in')
    return redirect(url_for('name.checkout_book', id=id))

 
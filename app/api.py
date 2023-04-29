from flask import jsonify
from books import *

@app.route('/books', methods=['GET'])
def get_books():
    '''Function to get all the movies in the database'''
    return jsonify({'index': index.get_all_books()})
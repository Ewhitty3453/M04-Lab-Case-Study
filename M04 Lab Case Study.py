from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (can be replaced with a database)
books = [
    {"id": 1, "book_name": "Book 1", "author": "Author 1", "publisher": "Publisher 1"},
    {"id": 2, "book_name": "Book 2", "author": "Author 2", "publisher": "Publisher 2"},
    {"id": 3, "book_name": "Book 3", "author": "Author 3", "publisher": "Publisher 3"}
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return jsonify(book)
    return jsonify({'error': 'Book not found'}), 404

@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.json
    if 'book_name' in new_book and 'author' in new_book and 'publisher' in new_book:
        new_book['id'] = len(books) + 1
        books.append(new_book)
        return jsonify(new_book), 201
    else:
        return jsonify({'error': 'Incomplete book information'}), 400

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    for book in books:
        if book['id'] == book_id:
            updated_book = request.json
            book.update(updated_book)
            return jsonify(book)
    return jsonify({'error': 'Book not found'}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for i, book in enumerate(books):
        if book['id'] == book_id:
            del books[i]
            return jsonify({'message': 'Book deleted successfully'})
    return jsonify({'error': 'Book not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
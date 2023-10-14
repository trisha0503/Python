from flask import flask, request, jsonify

# Create a Flask application
app = flask(__name__)

# Sample data (you can replace this with your own data)
data = {
    '1': 'Item 1',
    '2': 'Item 2',
    '3': 'Item 3',
}

# Define a route for GET requests
@app.route('/items/<item_id>', methods=['GET'])
def get_item(item_id):
    if item_id in data:
        return jsonify({item_id: data[item_id]})
    else:
        return jsonify({'error': 'Item not found'}), 404

# Define a route for POST requests
@app.route('/items', methods=['POST'])
def create_item():
    if not request.is_json:
        return jsonify({'error': 'Data must be in JSON format'}), 400

    item_data = request.get_json()
    if 'id' not in item_data or 'name' not in item_data:
        return jsonify({'error': 'Missing required fields'}), 400

    new_id = str(len(data) + 1)
    data[new_id] = item_data['name']

    return jsonify({'id': new_id, 'name': item_data['name']}), 201

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify, request
import requests, pymongo, json

app = Flask(__name__)

dev_api_admin_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1YmVmMDljZTc0YWFlZjJjNGQ5YWE3MTIiLCJlbWFpbCI6ImFkbWluQGFsZ29yaXRobS5hZSIsInJvbGVzIjpbImFkbWluIl0sImlhdCI6MTU0NjI0OTE4MH0.SvooehBDn00uIu1f0obXGd3r41ZLh58XCIqerdVS9YU'
parameters_book, parameters_order = None, None
test_object = {"name": "sulum", "address": {"country": "5b72ec8bee60314fd9910bca", "city": "5b72ec8bee60314fd9910bcb",
                                            "area": "5b72ec8bee60314fd9910bcc", "street": "street1", "location":
                                                {"type": "Point", "coordinates": [20.5, 20.6]}}}


def auth_and_extract_data():
    server_token = "sulumelprinceYN@hop8"
    token = request.args.get('token')

    if not token or server_token != token:
        return jsonify({'message': 'Token is invalid!'}), 403
    # data has keys number_book, seats_type, restaurant_name', 'tim_booking'
    data = json.loads(request.get_data())
    attributes = data['result']['parameters']
    return attributes


@app.route('/book', methods=['GET', 'POST'])
def book():
    parameters_book = auth_and_extract_data()
    print(parameters_book)
    # ------------contacting back-end API ---------------------------------------------------#
    if parameters_book:
        response = requests.post('https://api-dev.bites.vip/malls', headers={'Authorization': dev_api_admin_token},
                                     json=test_object)
        print(response.text)
        print(response.status_code)
        # the bot expects to see an array of objects called response 'bot response' of type 'text'
        return jsonify({'responses': [{'type': 'text', 'elements': ["THANKS AGAIN !!!!!!"]}]})

@app.route('/order', methods=['GET', 'POST'])
def order():
    parameters_order = auth_and_extract_data()
    print(parameters_order)
    # the bot expects to see an array of objects called response 'bot response' of type 'text'
    return jsonify({'responses': [{'type': 'text', 'elements': ["THANKS AGAIN !!!!!!"]}]})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7777, debug=True)  # choosing a port other than 3000 as api of dev is on this port

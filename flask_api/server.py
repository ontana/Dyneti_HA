import base64
from io import BytesIO

from PIL import Image
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from sqlalchemy import create_engine

from tensorflow_model import interpreter, input_details, output_details
import numpy as np

# init app
app = Flask(__name__)
api = Api(app)

db_connect = create_engine('sqlite:///dyneti.db')
conn = db_connect.connect()


class Classification(Resource):
    def get(self):
        # List result
        pass

    def post(self):
        # Send image
        req = request.get_json()
        res = {
            'message': None
        }
        base64_image = req.get('image')
        if not base64_image:
            return {'message': 'Image is required'}, 400

        image_data = base64.b64decode(base64_image)
        with Image.open(BytesIO(image_data)) as image:
            input_data = np.array(image)
            interpreter.set_tensor(input_details[0]['index'], input_data)
            interpreter.invoke()
            output_data = interpreter.get_tensor(output_details[0]['index'])
            res.update({
                'message': output_data
            })

        return jsonify(res)


api.add_resource(Classification, '/classification')

if __name__ == '__main__':
    app.run()

import base64
from io import BytesIO

from PIL import Image
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from sqlalchemy import create_engine

from flask_api.handler.tensorflow_model import TensorflowModel

# init app
app = Flask(__name__)
api = Api(app)

db_connect = create_engine('sqlite:///db/dyneti.db')
conn = db_connect.connect()

ts_model = TensorflowModel("config/model.tflite")


class Classification(Resource):
    def get(self):
        # List result
        pass

    def post(self):
        # Send image
        req = request.get_json()
        res = {
            'result': None,
            'message': None
        }
        base64_image = req.get('image')
        if not base64_image:
            return {'message': 'Image is required'}, 400

        image_data = base64.b64decode(base64_image)
        with Image.open(BytesIO(image_data)) as image:
            prediction = ts_model.predict(image)

            if not prediction:
                return {'message': 'Prediction failed'}, 400

        return jsonify(res)


api.add_resource(Classification, '/classification')

if __name__ == '__main__':
    app.run()

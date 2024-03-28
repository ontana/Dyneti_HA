import base64
import uuid
from io import BytesIO

from PIL import Image
from flask import Flask, request
from flask_restful import Api, Resource
from models.result import db, Result

from flask_api.handler.classification import AnimalDetection
from flask_api.handler.tensorflow_model import TensorflowModel

# init app
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dyneti.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Create the database tables
with app.app_context():
    db.create_all()

ts_model = TensorflowModel("config/model.tflite")
detection = AnimalDetection()


class Classification(Resource):
    def get(self):
        # List result
        pass

    def post(self):
        # Send image
        req = request.get_json()
        base64_image = req.get('image')
        name = req.get('name') or str(uuid.uuid4())

        # Should receive the highest possible result instead of set of result
        single_result = str((req.get('single_result') or 'false')).lower() == 'true'

        if not base64_image:
            return {'message': 'Image is required'}, 400

        image_data = base64.b64decode(base64_image)
        with Image.open(BytesIO(image_data)) as image:
            prediction = ts_model.predict(image)

            if not prediction:
                return {'message': 'Prediction failed'}, 400

            print(f'name: {name}, prediction_score: {prediction}')
            _results, error = detection.predict(prediction)
            if error and not _results:
                return {'message': error}, 400

            self.save_result(name, _results)

            if single_result:
                return {'prediction': _results[0]}, 200

            return {'prediction': _results}, 200

    def save_result(self, name, _results):
        result = Result(name=name, prediction=_results)
        db.session.add(result)
        db.session.commit()


api.add_resource(Classification, '/classification')

if __name__ == '__main__':
    app.run()

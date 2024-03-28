import numpy as np
import tensorflow as tf
from PIL import Image


class TensorflowModel:
    def __init__(self, model_path):
        # model_path="./handler.tflite"
        self.interpreter = tf.lite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()

    def predict(self, image: Image) -> list:
        # Pre resize image
        try:
            image = image.resize((224, 224))
            input_data = np.expand_dims(image, axis=0)
            input_data = input_data / 255.0

            self.interpreter.set_tensor(input_details[0]['index'], np.float32(input_data))
            self.interpreter.invoke()
            output_data = self.interpreter.get_tensor(output_details[0]['index'])
            return np.squeeze(output_data).tolist()
        except Exception as e:
            print(f"Prediction error: {str(e)}")
            raise RuntimeError("Can't predict image")

import json
from typing import List, Any, Tuple


class AnimalDetection:
    def __init__(self):
        with open('config/config.json', 'r') as ifile:
            config = json.load(ifile)
            self.model = config.get('score_config')

    def predict(self, model_res: list) -> tuple[None, str] | tuple[list[list[Any] | Any], None]:
        result = []

        if not model_res:
            return None, 'Not found prediction result'

        if not self.model:
            return None, 'Config not found'

        for animal, config in self.model.items():
            model_idx = config.get('model_idx')
            threshold = config.get('threshold')

            if not model_idx or not threshold:
                return None, 'Config not found'

            if len(model_res) > model_idx and model_res[model_idx] > threshold:
                result.append({
                    'class': animal,
                    'score': model_res[model_idx]
                })
        result = sorted(result, key=lambda x: x['score'], reverse=True)
        return [x['class'] for x in result], None
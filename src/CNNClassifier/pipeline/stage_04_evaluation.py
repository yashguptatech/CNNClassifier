from CNNClassifier.config import ConfigurationManager
from CNNClassifier.components import Evaluation
from CNNClassifier import logger

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_evaluation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluate()
        evaluation.save_score()

"""
Single Responsibility Principle
"""

from typing import Any


class DLModel:
    """
    Class that represents Deep Learning Model
    """

    @staticmethod
    def train(features: list[Any]) -> list[Any]:
        """
        here goes training code
        :param features: The list of features to train
        :type features: list
        :return: The list of features
        :rtype: list
        """
        print("Model has been trained")
        return features


class Preprocessor:
    """
    Class that represents Preprocessor
    """

    @staticmethod
    def preprocess(features: list[Any]) -> None:
        """
        here goes preprocessing code
        :param features: The features to preprocess
        :type features: list
        :return: None
        :rtype: NoneType
        """
        print("Features have been preprocessed:", features)


class DlEvaluator:
    """
    Class that represents Deep Learning Evaluator
    """

    @staticmethod
    def evaluate(model: DLModel) -> None:
        """
        here goes evaluation code
        :param model: The model to be evaluated
        :type model: DLModel
        :return: None
        :rtype: NoneType
        """
        print("Model has been evaluated", model)


if __name__ == "__main__":
    my_features: list[list[int]] = [[0, 1, 2], [1, 2, 3]]
    my_model: DLModel = DLModel()
    preprocessor: Preprocessor = Preprocessor()
    evaluator: DlEvaluator = DlEvaluator()
    preprocessor.preprocess(my_features)
    my_model.train(my_features)
    evaluator.evaluate(my_model)

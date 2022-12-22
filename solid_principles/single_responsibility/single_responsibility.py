"""
Single Responsibility Principle
"""


class DLModel:
    """
    Class that represents Deep Learning Model
    """

    def train(self, features: list) -> list:
        """
        here goes training code
        :param features:
        :type features: list
        :return:
        :rtype: list
        """
        print("Model has been trained")
        return features


class Preprocessor:
    """
    Class that represents Preprocessor
    """

    def preprocess(self, features: list) -> None:
        """
        here goes preprocessing code
        :param features:
        :type features: list
        :return: None
        :rtype: NoneType
        """
        print("Features have been preprocessed:", features)


class DlEvaluator:
    """
    Class that represents Deep Learning Evaluator
    """

    def evaluate(self, model: DLModel) -> None:
        """
        here goes evaluation code
        :param model:
        :type model:
        :return: None
        :rtype: NoneType
        """
        print("Model has been evaluated", model)


if __name__ == "__main__":
    my_features: list[list[int]] = [
        [0, 1, 2],
        [1, 2, 3]
    ]
    my_model: DLModel = DLModel()
    preprocessor: Preprocessor = Preprocessor()
    evaluator: DlEvaluator = DlEvaluator()
    preprocessor.preprocess(my_features)
    my_model.train(my_features)
    evaluator.evaluate(my_model)

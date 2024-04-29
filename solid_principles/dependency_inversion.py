"""
Dependency Inversion Principle
"""

from abc import ABC, abstractmethod

# # Dependency Inversion Violation
# class TensorFlowEvaluator:
#
#     def evaluate(self):
#         print("Evaluating with TensorFlow.")
#
#
# class MLPipeline:
#
#     def __init__(self):
#         self.evaluator = TensorFlowEvaluator()
#
#     def evaluate(self):
#         self.evaluator.evaluate()
#
#
# if __name__ == "__main__":
#     ml_pipeline = MLPipeline()
#     ml_pipeline.evaluate()


class Evaluator(ABC):
    """
    Evaluator abstract class
    """

    @abstractmethod
    def evaluate(self) -> None:
        """
        Evaluate abstract method
        :return: None
        :rtype: NoneType
        """


class TensorFlowEvaluator(Evaluator):
    """
    Tensorflow Evaluator class
    """

    def evaluate(self) -> None:
        print("Evaluating with TensorFlow.")


class PytorchEvaluator(Evaluator):
    """
    Pytorch Evaluator class
    """

    def evaluate(self) -> None:
        print("Evaluating with PyTorch.")


class MLPipeline:
    """
    Machine Learning Pipeline class
    """

    def __init__(self, evaluator: Evaluator) -> None:
        self.evaluator = evaluator

    def evaluate(self) -> None:
        """
        Evaluate method within the ML Pipeline with an Evaluator.
        :return: None
        :rtype: NoneType
        """
        self.evaluator.evaluate()


if __name__ == "__main__":
    pytorch_evaluator: PytorchEvaluator = PytorchEvaluator()
    ml_pipeline: MLPipeline = MLPipeline(pytorch_evaluator)
    ml_pipeline.evaluate()

"""
Open-Closed Principle
"""
from abc import abstractmethod, ABC

# # OCP violation
# class Extractor:
#
#     def extract_spectrogram(self, data):
#         print("Extracted spectrogram")
#
#     def extract_mfcc(self, data):
#         print("Extracted MFCCs")
#
#     def extract_mel_spectrogram(self, data):
#         print("Extracted mel spectrogram")
#
#
# class DLPipeline:
#
#     def __init__(self, extractor, feature_type):
#         self.extractor = extractor
#         self.feature_type = feature_type
#
#     def run(self, data):
#         print("Running DL pipeline")
#         features = self._extract(data)
#         # Implementation of DL steps go here
#
#     def _extract(self, data):
#         if self.feature_type == "spectrogram":
#             self.extractor.extract_spectrogram(data)
#         elif self.feature_type == "mfcc":
#             self.extractor.extract_mfcc(data)
#         elif self.feature_type == "melspectrogram":
#             self.extractor.extract_melspectrogram(data)
#
#
# if __name__ == "__main__":
#     data = [1, 2, 3]
#     extractor = Extractor()
#     dl_pipeline = DLPipeline(extractor, "spectrogram")
#     dl_pipeline.run(data)


class Extractor(ABC):
    """
    Feature Extractor class
    """

    @abstractmethod
    def extract(self, data: list[int]) -> None:
        """
        Extract abstract method for Extractor object
        :param data:
        :type data:
        :return: None
        :rtype: NoneType
        """


class SpectrogramExtractor(Extractor):
    """
    SpectrogramExtractor class inherits from :class:`Extractor`
    """

    def extract(self, data: list[int]) -> None:
        print("Extracted spectrogram")


class MFCCExtractor(Extractor):
    """
    MFCCExtractor class inherits from :class:`Extractor`
    """

    def extract(self, data: list[int]) -> None:
        print("Extracted MFCC")


class MelSpectrogramExtractor(Extractor):
    """
    MelSpectrogramExtractor class inherits from :class:`Extractor`
    """

    def extract(self, data: list[int]) -> None:
        print("Extracted mel spectrogram")


class DLPipeline:
    """
    Deep Learning Pipeline class
    """

    def __init__(self, extractor: Extractor) -> None:
        self.extractor: Extractor = extractor

    def run(self, data: list[int]) -> None:
        """
        Run method for Deep Learning Pipeline
        :param data:
        :type data: list[int]
        :return: None
        :rtype: NoneType
        """
        print("Running DL pipeline")
        self._extract(data)
        # Implementation of DL steps go here

    def _extract(self, data: list[int]) -> None:
        """
        Private method to extract data for DLPipeline
        :param data:
        :type data: list[int]
        :return: None
        :rtype: NoneType
        """
        self.extractor.extract(data)


if __name__ == "__main__":
    my_data: list[int] = [1, 2, 3]
    my_extractor: SpectrogramExtractor = SpectrogramExtractor()
    dl_pipeline: DLPipeline = DLPipeline(my_extractor)
    dl_pipeline.run(my_data)

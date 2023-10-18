"""
Liskov Substitution Principle
"""
from abc import ABC, abstractmethod
from typing import Any

# # LSP violation
# class Extractor(ABC):
#
#     @abstractmethod
#     def extract(self, data):
#         pass
#
#
# class MelSpectrogramExtractor(Extractor):
#
#     def extract(self, data):
#         print("Extracted spectrogram")
#
#
# class MFCCExtractor(Extractor):
#
#     def extract(self, data, num_mfccs):
#         print("Extracted MFCC")
#
#
# if __name__ == "__main__":
#     dummy_data = [1, 2, 3]
#     mfcc_extractor = MFCCExtractor()
#     mfcc_extractor.extract(dummy_data, 10)


class Extractor(ABC):
    """
    Extractor abstract class
    """

    @abstractmethod
    def extract(self, data: list[int]) -> None:
        """
        Extract abstract method
        :param data:
        :type data: list[int]
        :return: None
        :rtype: NoneType
        """


class MelSpectrogramExtractor(Extractor):
    """
    Mel Spectrogram Extractor class that inherits from Extractor
    """

    def __init__(self, mels: Any) -> None:
        self.mfcss: Any = mels

    def extract(self, data: list[int]) -> None:
        print("Extracted spectrogram")


class MFCCExtractor(Extractor):
    """
    MFCC Extractor class that inherits from Extractor
    """

    def __init__(self, mfcss: Any) -> None:
        self.mfcss: Any = mfcss

    def extract(self, data: list[int]) -> None:
        print("Extracted MFCC")


if __name__ == "__main__":
    dummy_data: list[int] = [1, 2, 3]
    mfcc_extractor: MFCCExtractor = MFCCExtractor(13)
    mfcc_extractor.extract(dummy_data)

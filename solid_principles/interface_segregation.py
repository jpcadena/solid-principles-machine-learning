"""
Interface Segregation Principle
"""
from abc import ABC, abstractmethod
from typing import Any

# # Violates ISP
# class Recommender(ABC):
#
#     @abstractmethod
#     def get_closest_items(self, item):
#         pass
#
#     @abstractmethod
#     def get_personalised_recommendations(self, user):
#         pass
#
#
# class CollaborativeFilteringRecommender(Recommender):
#
#     def get_closest_items(self, item):
#         print("Recommended closest items")
#
#     def get_personalised_recommendations(self, user):
#         print("Provided personalised recommendations")
#
#
# class DLRecommender(Recommender):
#
#     def get_closest_items(self, item):
#         print("Recommended closest items")
#
#     def get_personalised_recommendations(self, user):
#         print("Provided personalised recommendations")
#
#
# class NearestNeighbourRecommender(Recommender):
#
#     def get_closest_items(self, item):
#         print("Recommended closest items")
#
#     def get_personalised_recommendations(self, user):
#         raise Exception("NearestNeighbourRecommender can't provide
#         personalised recommendations")

# Single Inheritance
# class Recommender(ABC):
#
#     @abstractmethod
#     def get_closest_items(self, item):
#         pass
#
#
# class PersonalisedRecommender(Recommender):
#
#     @abstractmethod
#     def get_personalised_recommendations(self, user):
#         pass
#
#
# class CollaborativeFilteringRecommender(PersonalisedRecommender):
#
#     def get_closest_items(self, item):
#         print("Recommended closest items")
#
#     def get_personalised_recommendations(self, user):
#         print("Provided personalised recommendations")
#
#
# class DLRecommender(PersonalisedRecommender):
#
#     def get_closest_items(self, item):
#         print("Recommended closest items")
#
#     def get_personalised_recommendations(self, user):
#         print("Provided personalised recommendations")
#
#
# class NearestNeighbourRecommender(Recommender):
#
#     def get_closest_items(self, item):
#        print("Recommended closest items")

# Multiple Inheritance


class ItemRecommender(ABC):
    """
    Item Recommender abstract class
    """

    @abstractmethod
    def get_closest_items(self, item: Any) -> None:
        """
        Get the closest items abstract method
        :param item: The item to get the closest items from
        :type item: Any
        :return: None
        :rtype: NoneType
        """


class PersonalisedRecommender(ABC):
    """
    Personalised Recommender abstract class
    """

    @abstractmethod
    def get_personalised_recommendations(self, user: Any) -> None:
        """
        Get personalised recommendations abstract method
        :param user: The user to get personalises recommendations from
        :type user: Any
        :return: None
        :rtype: NoneType
        """


class CollaborativeFilteringRecommender(
    ItemRecommender, PersonalisedRecommender
):
    """
    Collaborative Filtering Recommender class that inherits from
     ItemRecommender and PersonalisedRecommender
    """

    def get_closest_items(self, item: Any) -> None:
        print("Recommended closest items")

    def get_personalised_recommendations(self, user: Any) -> None:
        print("Provided personalised recommendations")


class DLRecommender(ItemRecommender, PersonalisedRecommender):
    """
    Deep Learning Recommender class that inherits from
     ItemRecommender and PersonalisedRecommender
    """

    def get_closest_items(self, item: Any) -> None:
        print("Recommended closest items")

    def get_personalised_recommendations(self, user: Any) -> None:
        print("Provided personalised recommendations")


class NearestNeighbourRecommender(ItemRecommender):
    """
    Nearest Neighbour Recommender class that inherits from
    ItemRecommender
    """

    def get_closest_items(self, item: Any) -> None:
        print("Recommended closest items")

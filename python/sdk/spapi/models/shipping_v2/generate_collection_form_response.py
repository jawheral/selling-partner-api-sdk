# coding: utf-8

"""
    Amazon Shipping API

    The Amazon Shipping API is designed to support outbound shipping use cases both for orders originating on Amazon-owned marketplaces as well as external channels/marketplaces. With these APIs, you can request shipping rates, create shipments, cancel shipments, and track shipments.

    The version of the OpenAPI document: v2
    Contact: swa-api-core@amazon.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import pprint
import re  # noqa: F401

import six

from spapi.configuration import Configuration


class GenerateCollectionFormResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'collections_form_document': 'CollectionsFormDocument',
    }

    attribute_map = {
        'collections_form_document': 'collectionsFormDocument',
    }

    def __init__(self, collections_form_document=None, _configuration=None):  # noqa: E501
        """GenerateCollectionFormResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._collections_form_document = None
        self.discriminator = None

        if collections_form_document is not None:
            self.collections_form_document = collections_form_document

    @property
    def collections_form_document(self):
        """Gets the collections_form_document of this GenerateCollectionFormResponse.  # noqa: E501


        :return: The collections_form_document of this GenerateCollectionFormResponse.  # noqa: E501
        :rtype: CollectionsFormDocument
        """
        return self._collections_form_document

    @collections_form_document.setter
    def collections_form_document(self, collections_form_document):
        """Sets the collections_form_document of this GenerateCollectionFormResponse.


        :param collections_form_document: The collections_form_document of this GenerateCollectionFormResponse.  # noqa: E501
        :type: CollectionsFormDocument
        """

        self._collections_form_document = collections_form_document

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GenerateCollectionFormResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GenerateCollectionFormResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GenerateCollectionFormResponse):
            return True

        return self.to_dict() != other.to_dict()

# coding: utf-8

"""
    The Selling Partner API for FBA inbound operations.

    The Selling Partner API for Fulfillment By Amazon (FBA) Inbound. The FBA Inbound API enables building inbound workflows to create, manage, and send shipments into Amazon's fulfillment network. The API has interoperability with the Send-to-Amazon user interface.

    The version of the OpenAPI document: 2024-03-20
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import pprint
import re  # noqa: F401

import six

from spapi.configuration import Configuration


class GeneratePlacementOptionsRequest(object):
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
        'custom_placement': 'List[CustomPlacementInput]',
    }

    attribute_map = {
        'custom_placement': 'customPlacement',
    }

    def __init__(self, custom_placement=None, _configuration=None):  # noqa: E501
        """GeneratePlacementOptionsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._custom_placement = None
        self.discriminator = None

        if custom_placement is not None:
            self.custom_placement = custom_placement

    @property
    def custom_placement(self):
        """Gets the custom_placement of this GeneratePlacementOptionsRequest.  # noqa: E501

        Custom placement options you want to add to the plan. This is only used for the India (IN - A21TJRUUN4KGV) marketplace.  # noqa: E501

        :return: The custom_placement of this GeneratePlacementOptionsRequest.  # noqa: E501
        :rtype: List[CustomPlacementInput]
        """
        return self._custom_placement

    @custom_placement.setter
    def custom_placement(self, custom_placement):
        """Sets the custom_placement of this GeneratePlacementOptionsRequest.

        Custom placement options you want to add to the plan. This is only used for the India (IN - A21TJRUUN4KGV) marketplace.  # noqa: E501

        :param custom_placement: The custom_placement of this GeneratePlacementOptionsRequest.  # noqa: E501
        :type: List[CustomPlacementInput]
        """

        self._custom_placement = custom_placement

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
        if issubclass(GeneratePlacementOptionsRequest, dict):
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
        if not isinstance(other, GeneratePlacementOptionsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GeneratePlacementOptionsRequest):
            return True

        return self.to_dict() != other.to_dict()

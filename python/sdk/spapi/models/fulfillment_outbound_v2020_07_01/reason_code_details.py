# coding: utf-8

"""
    Selling Partner APIs for Fulfillment Outbound

    The Selling Partner API for Fulfillment Outbound lets you create applications that help a seller fulfill Multi-Channel Fulfillment orders using their inventory in Amazon's fulfillment network. You can get information on both potential and existing fulfillment orders.

    The version of the OpenAPI document: 2020-07-01
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import pprint
import re  # noqa: F401

import six

from spapi.configuration import Configuration


class ReasonCodeDetails(object):
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
        'return_reason_code': 'str',
        'description': 'str',
        'translated_description': 'str',
    }

    attribute_map = {
        'return_reason_code': 'returnReasonCode',
        'description': 'description',
        'translated_description': 'translatedDescription',
    }

    def __init__(self, return_reason_code=None, description=None, translated_description=None, _configuration=None):  # noqa: E501
        """ReasonCodeDetails - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._return_reason_code = None
        self._description = None
        self._translated_description = None
        self.discriminator = None

        self.return_reason_code = return_reason_code
        self.description = description
        if translated_description is not None:
            self.translated_description = translated_description

    @property
    def return_reason_code(self):
        """Gets the return_reason_code of this ReasonCodeDetails.  # noqa: E501

        A code that indicates a valid return reason.  # noqa: E501

        :return: The return_reason_code of this ReasonCodeDetails.  # noqa: E501
        :rtype: str
        """
        return self._return_reason_code

    @return_reason_code.setter
    def return_reason_code(self, return_reason_code):
        """Sets the return_reason_code of this ReasonCodeDetails.

        A code that indicates a valid return reason.  # noqa: E501

        :param return_reason_code: The return_reason_code of this ReasonCodeDetails.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and return_reason_code is None:
            raise ValueError("Invalid value for `return_reason_code`, must not be `None`")  # noqa: E501

        self._return_reason_code = return_reason_code

    @property
    def description(self):
        """Gets the description of this ReasonCodeDetails.  # noqa: E501

        A human readable description of the return reason code.  # noqa: E501

        :return: The description of this ReasonCodeDetails.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ReasonCodeDetails.

        A human readable description of the return reason code.  # noqa: E501

        :param description: The description of this ReasonCodeDetails.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def translated_description(self):
        """Gets the translated_description of this ReasonCodeDetails.  # noqa: E501

        A translation of the description. The translation is in the language specified in the Language request parameter.  # noqa: E501

        :return: The translated_description of this ReasonCodeDetails.  # noqa: E501
        :rtype: str
        """
        return self._translated_description

    @translated_description.setter
    def translated_description(self, translated_description):
        """Sets the translated_description of this ReasonCodeDetails.

        A translation of the description. The translation is in the language specified in the Language request parameter.  # noqa: E501

        :param translated_description: The translated_description of this ReasonCodeDetails.  # noqa: E501
        :type: str
        """

        self._translated_description = translated_description

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
        if issubclass(ReasonCodeDetails, dict):
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
        if not isinstance(other, ReasonCodeDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReasonCodeDetails):
            return True

        return self.to_dict() != other.to_dict()

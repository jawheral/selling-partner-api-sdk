# coding: utf-8

"""
    Selling Partner API for Retail Procurement Shipments

    The Selling Partner API for Retail Procurement Shipments provides programmatic access to retail shipping data for vendors.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import pprint
import re  # noqa: F401

import six

from spapi.configuration import Configuration


class ShipmentDetails(object):
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
        'pagination': 'Pagination',
        'shipments': 'List[Shipment]',
    }

    attribute_map = {
        'pagination': 'pagination',
        'shipments': 'shipments',
    }

    def __init__(self, pagination=None, shipments=None, _configuration=None):  # noqa: E501
        """ShipmentDetails - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._pagination = None
        self._shipments = None
        self.discriminator = None

        if pagination is not None:
            self.pagination = pagination
        if shipments is not None:
            self.shipments = shipments

    @property
    def pagination(self):
        """Gets the pagination of this ShipmentDetails.  # noqa: E501


        :return: The pagination of this ShipmentDetails.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this ShipmentDetails.


        :param pagination: The pagination of this ShipmentDetails.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

    @property
    def shipments(self):
        """Gets the shipments of this ShipmentDetails.  # noqa: E501

        A list of one or more shipments with underlying details.  # noqa: E501

        :return: The shipments of this ShipmentDetails.  # noqa: E501
        :rtype: List[Shipment]
        """
        return self._shipments

    @shipments.setter
    def shipments(self, shipments):
        """Sets the shipments of this ShipmentDetails.

        A list of one or more shipments with underlying details.  # noqa: E501

        :param shipments: The shipments of this ShipmentDetails.  # noqa: E501
        :type: List[Shipment]
        """

        self._shipments = shipments

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
        if issubclass(ShipmentDetails, dict):
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
        if not isinstance(other, ShipmentDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ShipmentDetails):
            return True

        return self.to_dict() != other.to_dict()

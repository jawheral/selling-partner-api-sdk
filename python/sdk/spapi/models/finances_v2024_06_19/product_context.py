# coding: utf-8

"""
    The Selling Partner API for Finances

    The Selling Partner API for Finances helps you obtain financial information relevant to a seller's business. You can obtain financial events for a given order or date range without having to wait until a statement period closes.

    The version of the OpenAPI document: 2024-06-19
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import pprint
import re  # noqa: F401

import six

from spapi.configuration import Configuration


class ProductContext(object):
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
        'asin': 'str',
        'sku': 'str',
        'quantity_shipped': 'int',
        'fulfillment_network': 'str',
    }

    attribute_map = {
        'asin': 'asin',
        'sku': 'sku',
        'quantity_shipped': 'quantityShipped',
        'fulfillment_network': 'fulfillmentNetwork',
    }

    def __init__(self, asin=None, sku=None, quantity_shipped=None, fulfillment_network=None, _configuration=None):  # noqa: E501
        """ProductContext - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._asin = None
        self._sku = None
        self._quantity_shipped = None
        self._fulfillment_network = None
        self.discriminator = None

        if asin is not None:
            self.asin = asin
        if sku is not None:
            self.sku = sku
        if quantity_shipped is not None:
            self.quantity_shipped = quantity_shipped
        if fulfillment_network is not None:
            self.fulfillment_network = fulfillment_network

    @property
    def asin(self):
        """Gets the asin of this ProductContext.  # noqa: E501

        Amazon Standard Identification Number (ASIN) of the item.  # noqa: E501

        :return: The asin of this ProductContext.  # noqa: E501
        :rtype: str
        """
        return self._asin

    @asin.setter
    def asin(self, asin):
        """Sets the asin of this ProductContext.

        Amazon Standard Identification Number (ASIN) of the item.  # noqa: E501

        :param asin: The asin of this ProductContext.  # noqa: E501
        :type: str
        """

        self._asin = asin

    @property
    def sku(self):
        """Gets the sku of this ProductContext.  # noqa: E501

        Stock keeping unit (SKU) of the item.  # noqa: E501

        :return: The sku of this ProductContext.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this ProductContext.

        Stock keeping unit (SKU) of the item.  # noqa: E501

        :param sku: The sku of this ProductContext.  # noqa: E501
        :type: str
        """

        self._sku = sku

    @property
    def quantity_shipped(self):
        """Gets the quantity_shipped of this ProductContext.  # noqa: E501

        Quantity of the item shipped.  # noqa: E501

        :return: The quantity_shipped of this ProductContext.  # noqa: E501
        :rtype: int
        """
        return self._quantity_shipped

    @quantity_shipped.setter
    def quantity_shipped(self, quantity_shipped):
        """Sets the quantity_shipped of this ProductContext.

        Quantity of the item shipped.  # noqa: E501

        :param quantity_shipped: The quantity_shipped of this ProductContext.  # noqa: E501
        :type: int
        """

        self._quantity_shipped = quantity_shipped

    @property
    def fulfillment_network(self):
        """Gets the fulfillment_network of this ProductContext.  # noqa: E501

        Fulfillment network of the item.  # noqa: E501

        :return: The fulfillment_network of this ProductContext.  # noqa: E501
        :rtype: str
        """
        return self._fulfillment_network

    @fulfillment_network.setter
    def fulfillment_network(self, fulfillment_network):
        """Sets the fulfillment_network of this ProductContext.

        Fulfillment network of the item.  # noqa: E501

        :param fulfillment_network: The fulfillment_network of this ProductContext.  # noqa: E501
        :type: str
        """

        self._fulfillment_network = fulfillment_network

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
        if issubclass(ProductContext, dict):
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
        if not isinstance(other, ProductContext):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProductContext):
            return True

        return self.to_dict() != other.to_dict()

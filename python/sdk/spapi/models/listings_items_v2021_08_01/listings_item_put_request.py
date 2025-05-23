# coding: utf-8

"""
    Selling Partner API for Listings Items

    The Selling Partner API for Listings Items (Listings Items API) provides programmatic access to selling partner listings on Amazon. Use this API in collaboration with the Selling Partner API for Product Type Definitions, which you use to retrieve the information about Amazon product types needed to use the Listings Items API.  For more information, see the [Listings Items API Use Case Guide](https://developer-docs.amazon.com/sp-api/docs/listings-items-api-v2021-08-01-use-case-guide).

    The version of the OpenAPI document: 2021-08-01
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import pprint
import re  # noqa: F401

import six

from spapi.configuration import Configuration


class ListingsItemPutRequest(object):
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
        'product_type': 'str',
        'requirements': 'str',
        'attributes': 'Dict[str, object]',
    }

    attribute_map = {
        'product_type': 'productType',
        'requirements': 'requirements',
        'attributes': 'attributes',
    }

    def __init__(self, product_type=None, requirements=None, attributes=None, _configuration=None):  # noqa: E501
        """ListingsItemPutRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._product_type = None
        self._requirements = None
        self._attributes = None
        self.discriminator = None

        self.product_type = product_type
        if requirements is not None:
            self.requirements = requirements
        self.attributes = attributes

    @property
    def product_type(self):
        """Gets the product_type of this ListingsItemPutRequest.  # noqa: E501

        The Amazon product type of the listings item.  # noqa: E501

        :return: The product_type of this ListingsItemPutRequest.  # noqa: E501
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this ListingsItemPutRequest.

        The Amazon product type of the listings item.  # noqa: E501

        :param product_type: The product_type of this ListingsItemPutRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and product_type is None:
            raise ValueError("Invalid value for `product_type`, must not be `None`")  # noqa: E501

        self._product_type = product_type

    @property
    def requirements(self):
        """Gets the requirements of this ListingsItemPutRequest.  # noqa: E501

        The name of the requirements set for the provided data.  # noqa: E501

        :return: The requirements of this ListingsItemPutRequest.  # noqa: E501
        :rtype: str
        """
        return self._requirements

    @requirements.setter
    def requirements(self, requirements):
        """Sets the requirements of this ListingsItemPutRequest.

        The name of the requirements set for the provided data.  # noqa: E501

        :param requirements: The requirements of this ListingsItemPutRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["LISTING", "LISTING_PRODUCT_ONLY", "LISTING_OFFER_ONLY"]  # noqa: E501
        if (self._configuration.client_side_validation and
                requirements not in allowed_values):
            raise ValueError(
                "Invalid value for `requirements` ({0}), must be one of {1}"  # noqa: E501
                .format(requirements, allowed_values)
            )

        self._requirements = requirements

    @property
    def attributes(self):
        """Gets the attributes of this ListingsItemPutRequest.  # noqa: E501

        A JSON object containing structured listings item attribute data keyed by attribute name.  # noqa: E501

        :return: The attributes of this ListingsItemPutRequest.  # noqa: E501
        :rtype: Dict[str, object]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this ListingsItemPutRequest.

        A JSON object containing structured listings item attribute data keyed by attribute name.  # noqa: E501

        :param attributes: The attributes of this ListingsItemPutRequest.  # noqa: E501
        :type: Dict[str, object]
        """
        if self._configuration.client_side_validation and attributes is None:
            raise ValueError("Invalid value for `attributes`, must not be `None`")  # noqa: E501

        self._attributes = attributes

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
        if issubclass(ListingsItemPutRequest, dict):
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
        if not isinstance(other, ListingsItemPutRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListingsItemPutRequest):
            return True

        return self.to_dict() != other.to_dict()

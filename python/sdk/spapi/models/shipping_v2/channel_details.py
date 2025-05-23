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


class ChannelDetails(object):
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
        'channel_type': 'ChannelType',
        'amazon_order_details': 'AmazonOrderDetails',
        'amazon_shipment_details': 'AmazonShipmentDetails',
    }

    attribute_map = {
        'channel_type': 'channelType',
        'amazon_order_details': 'amazonOrderDetails',
        'amazon_shipment_details': 'amazonShipmentDetails',
    }

    def __init__(self, channel_type=None, amazon_order_details=None, amazon_shipment_details=None, _configuration=None):  # noqa: E501
        """ChannelDetails - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._channel_type = None
        self._amazon_order_details = None
        self._amazon_shipment_details = None
        self.discriminator = None

        self.channel_type = channel_type
        if amazon_order_details is not None:
            self.amazon_order_details = amazon_order_details
        if amazon_shipment_details is not None:
            self.amazon_shipment_details = amazon_shipment_details

    @property
    def channel_type(self):
        """Gets the channel_type of this ChannelDetails.  # noqa: E501


        :return: The channel_type of this ChannelDetails.  # noqa: E501
        :rtype: ChannelType
        """
        return self._channel_type

    @channel_type.setter
    def channel_type(self, channel_type):
        """Sets the channel_type of this ChannelDetails.


        :param channel_type: The channel_type of this ChannelDetails.  # noqa: E501
        :type: ChannelType
        """
        if self._configuration.client_side_validation and channel_type is None:
            raise ValueError("Invalid value for `channel_type`, must not be `None`")  # noqa: E501

        self._channel_type = channel_type

    @property
    def amazon_order_details(self):
        """Gets the amazon_order_details of this ChannelDetails.  # noqa: E501


        :return: The amazon_order_details of this ChannelDetails.  # noqa: E501
        :rtype: AmazonOrderDetails
        """
        return self._amazon_order_details

    @amazon_order_details.setter
    def amazon_order_details(self, amazon_order_details):
        """Sets the amazon_order_details of this ChannelDetails.


        :param amazon_order_details: The amazon_order_details of this ChannelDetails.  # noqa: E501
        :type: AmazonOrderDetails
        """

        self._amazon_order_details = amazon_order_details

    @property
    def amazon_shipment_details(self):
        """Gets the amazon_shipment_details of this ChannelDetails.  # noqa: E501


        :return: The amazon_shipment_details of this ChannelDetails.  # noqa: E501
        :rtype: AmazonShipmentDetails
        """
        return self._amazon_shipment_details

    @amazon_shipment_details.setter
    def amazon_shipment_details(self, amazon_shipment_details):
        """Sets the amazon_shipment_details of this ChannelDetails.


        :param amazon_shipment_details: The amazon_shipment_details of this ChannelDetails.  # noqa: E501
        :type: AmazonShipmentDetails
        """

        self._amazon_shipment_details = amazon_shipment_details

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
        if issubclass(ChannelDetails, dict):
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
        if not isinstance(other, ChannelDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChannelDetails):
            return True

        return self.to_dict() != other.to_dict()

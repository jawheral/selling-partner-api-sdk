# coding: utf-8

"""
    Selling Partner API for Direct Fulfillment Orders

    The Selling Partner API for Direct Fulfillment Orders provides programmatic access to a direct fulfillment vendor's order data.

    The version of the OpenAPI document: 2021-12-28
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import pprint
import re  # noqa: F401

import six

from spapi.configuration import Configuration


class ScheduledDeliveryShipment(object):
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
        'scheduled_delivery_service_type': 'str',
        'earliest_nominated_delivery_date': 'datetime',
        'latest_nominated_delivery_date': 'datetime',
    }

    attribute_map = {
        'scheduled_delivery_service_type': 'scheduledDeliveryServiceType',
        'earliest_nominated_delivery_date': 'earliestNominatedDeliveryDate',
        'latest_nominated_delivery_date': 'latestNominatedDeliveryDate',
    }

    def __init__(self, scheduled_delivery_service_type=None, earliest_nominated_delivery_date=None, latest_nominated_delivery_date=None, _configuration=None):  # noqa: E501
        """ScheduledDeliveryShipment - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._scheduled_delivery_service_type = None
        self._earliest_nominated_delivery_date = None
        self._latest_nominated_delivery_date = None
        self.discriminator = None

        if scheduled_delivery_service_type is not None:
            self.scheduled_delivery_service_type = scheduled_delivery_service_type
        if earliest_nominated_delivery_date is not None:
            self.earliest_nominated_delivery_date = earliest_nominated_delivery_date
        if latest_nominated_delivery_date is not None:
            self.latest_nominated_delivery_date = latest_nominated_delivery_date

    @property
    def scheduled_delivery_service_type(self):
        """Gets the scheduled_delivery_service_type of this ScheduledDeliveryShipment.  # noqa: E501

        Scheduled delivery service type.  # noqa: E501

        :return: The scheduled_delivery_service_type of this ScheduledDeliveryShipment.  # noqa: E501
        :rtype: str
        """
        return self._scheduled_delivery_service_type

    @scheduled_delivery_service_type.setter
    def scheduled_delivery_service_type(self, scheduled_delivery_service_type):
        """Sets the scheduled_delivery_service_type of this ScheduledDeliveryShipment.

        Scheduled delivery service type.  # noqa: E501

        :param scheduled_delivery_service_type: The scheduled_delivery_service_type of this ScheduledDeliveryShipment.  # noqa: E501
        :type: str
        """

        self._scheduled_delivery_service_type = scheduled_delivery_service_type

    @property
    def earliest_nominated_delivery_date(self):
        """Gets the earliest_nominated_delivery_date of this ScheduledDeliveryShipment.  # noqa: E501

        Earliest nominated delivery date for the scheduled delivery.  # noqa: E501

        :return: The earliest_nominated_delivery_date of this ScheduledDeliveryShipment.  # noqa: E501
        :rtype: datetime
        """
        return self._earliest_nominated_delivery_date

    @earliest_nominated_delivery_date.setter
    def earliest_nominated_delivery_date(self, earliest_nominated_delivery_date):
        """Sets the earliest_nominated_delivery_date of this ScheduledDeliveryShipment.

        Earliest nominated delivery date for the scheduled delivery.  # noqa: E501

        :param earliest_nominated_delivery_date: The earliest_nominated_delivery_date of this ScheduledDeliveryShipment.  # noqa: E501
        :type: datetime
        """

        self._earliest_nominated_delivery_date = earliest_nominated_delivery_date

    @property
    def latest_nominated_delivery_date(self):
        """Gets the latest_nominated_delivery_date of this ScheduledDeliveryShipment.  # noqa: E501

        Latest nominated delivery date for the scheduled delivery.  # noqa: E501

        :return: The latest_nominated_delivery_date of this ScheduledDeliveryShipment.  # noqa: E501
        :rtype: datetime
        """
        return self._latest_nominated_delivery_date

    @latest_nominated_delivery_date.setter
    def latest_nominated_delivery_date(self, latest_nominated_delivery_date):
        """Sets the latest_nominated_delivery_date of this ScheduledDeliveryShipment.

        Latest nominated delivery date for the scheduled delivery.  # noqa: E501

        :param latest_nominated_delivery_date: The latest_nominated_delivery_date of this ScheduledDeliveryShipment.  # noqa: E501
        :type: datetime
        """

        self._latest_nominated_delivery_date = latest_nominated_delivery_date

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
        if issubclass(ScheduledDeliveryShipment, dict):
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
        if not isinstance(other, ScheduledDeliveryShipment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScheduledDeliveryShipment):
            return True

        return self.to_dict() != other.to_dict()

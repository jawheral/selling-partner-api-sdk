# coding: utf-8

"""
    Selling Partner API for Services

    With the Services API, you can build applications that help service providers get and modify their service orders and manage their resources.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import pprint
import re  # noqa: F401

import six

from spapi.configuration import Configuration


class AppointmentTimeInput(object):
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
        'start_time': 'datetime',
        'duration_in_minutes': 'int',
    }

    attribute_map = {
        'start_time': 'startTime',
        'duration_in_minutes': 'durationInMinutes',
    }

    def __init__(self, start_time=None, duration_in_minutes=None, _configuration=None):  # noqa: E501
        """AppointmentTimeInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._start_time = None
        self._duration_in_minutes = None
        self.discriminator = None

        self.start_time = start_time
        if duration_in_minutes is not None:
            self.duration_in_minutes = duration_in_minutes

    @property
    def start_time(self):
        """Gets the start_time of this AppointmentTimeInput.  # noqa: E501

        The date, time in UTC for the start time of an appointment in ISO 8601 format.  # noqa: E501

        :return: The start_time of this AppointmentTimeInput.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this AppointmentTimeInput.

        The date, time in UTC for the start time of an appointment in ISO 8601 format.  # noqa: E501

        :param start_time: The start_time of this AppointmentTimeInput.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and start_time is None:
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501

        self._start_time = start_time

    @property
    def duration_in_minutes(self):
        """Gets the duration_in_minutes of this AppointmentTimeInput.  # noqa: E501

        The duration of an appointment in minutes.  # noqa: E501

        :return: The duration_in_minutes of this AppointmentTimeInput.  # noqa: E501
        :rtype: int
        """
        return self._duration_in_minutes

    @duration_in_minutes.setter
    def duration_in_minutes(self, duration_in_minutes):
        """Sets the duration_in_minutes of this AppointmentTimeInput.

        The duration of an appointment in minutes.  # noqa: E501

        :param duration_in_minutes: The duration_in_minutes of this AppointmentTimeInput.  # noqa: E501
        :type: int
        """

        self._duration_in_minutes = duration_in_minutes

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
        if issubclass(AppointmentTimeInput, dict):
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
        if not isinstance(other, AppointmentTimeInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppointmentTimeInput):
            return True

        return self.to_dict() != other.to_dict()

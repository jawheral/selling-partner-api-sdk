# coding: utf-8

"""
    Selling Partner API for Retail Procurement Orders

    The Selling Partner API for Retail Procurement Orders provides programmatic access to vendor orders data.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import pprint
import re  # noqa: F401

import six

from spapi.configuration import Configuration


class OrderItemStatusAcknowledgementStatus(object):
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
        'confirmation_status': 'str',
        'accepted_quantity': 'ItemQuantity',
        'rejected_quantity': 'ItemQuantity',
        'acknowledgement_status_details': 'List[AcknowledgementStatusDetails]',
    }

    attribute_map = {
        'confirmation_status': 'confirmationStatus',
        'accepted_quantity': 'acceptedQuantity',
        'rejected_quantity': 'rejectedQuantity',
        'acknowledgement_status_details': 'acknowledgementStatusDetails',
    }

    def __init__(self, confirmation_status=None, accepted_quantity=None, rejected_quantity=None, acknowledgement_status_details=None, _configuration=None):  # noqa: E501
        """OrderItemStatusAcknowledgementStatus - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._confirmation_status = None
        self._accepted_quantity = None
        self._rejected_quantity = None
        self._acknowledgement_status_details = None
        self.discriminator = None

        if confirmation_status is not None:
            self.confirmation_status = confirmation_status
        if accepted_quantity is not None:
            self.accepted_quantity = accepted_quantity
        if rejected_quantity is not None:
            self.rejected_quantity = rejected_quantity
        if acknowledgement_status_details is not None:
            self.acknowledgement_status_details = acknowledgement_status_details

    @property
    def confirmation_status(self):
        """Gets the confirmation_status of this OrderItemStatusAcknowledgementStatus.  # noqa: E501

        Confirmation status of line item.  # noqa: E501

        :return: The confirmation_status of this OrderItemStatusAcknowledgementStatus.  # noqa: E501
        :rtype: str
        """
        return self._confirmation_status

    @confirmation_status.setter
    def confirmation_status(self, confirmation_status):
        """Sets the confirmation_status of this OrderItemStatusAcknowledgementStatus.

        Confirmation status of line item.  # noqa: E501

        :param confirmation_status: The confirmation_status of this OrderItemStatusAcknowledgementStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACCEPTED", "PARTIALLY_ACCEPTED", "REJECTED", "UNCONFIRMED"]  # noqa: E501
        if (self._configuration.client_side_validation and
                confirmation_status not in allowed_values):
            raise ValueError(
                "Invalid value for `confirmation_status` ({0}), must be one of {1}"  # noqa: E501
                .format(confirmation_status, allowed_values)
            )

        self._confirmation_status = confirmation_status

    @property
    def accepted_quantity(self):
        """Gets the accepted_quantity of this OrderItemStatusAcknowledgementStatus.  # noqa: E501


        :return: The accepted_quantity of this OrderItemStatusAcknowledgementStatus.  # noqa: E501
        :rtype: ItemQuantity
        """
        return self._accepted_quantity

    @accepted_quantity.setter
    def accepted_quantity(self, accepted_quantity):
        """Sets the accepted_quantity of this OrderItemStatusAcknowledgementStatus.


        :param accepted_quantity: The accepted_quantity of this OrderItemStatusAcknowledgementStatus.  # noqa: E501
        :type: ItemQuantity
        """

        self._accepted_quantity = accepted_quantity

    @property
    def rejected_quantity(self):
        """Gets the rejected_quantity of this OrderItemStatusAcknowledgementStatus.  # noqa: E501


        :return: The rejected_quantity of this OrderItemStatusAcknowledgementStatus.  # noqa: E501
        :rtype: ItemQuantity
        """
        return self._rejected_quantity

    @rejected_quantity.setter
    def rejected_quantity(self, rejected_quantity):
        """Sets the rejected_quantity of this OrderItemStatusAcknowledgementStatus.


        :param rejected_quantity: The rejected_quantity of this OrderItemStatusAcknowledgementStatus.  # noqa: E501
        :type: ItemQuantity
        """

        self._rejected_quantity = rejected_quantity

    @property
    def acknowledgement_status_details(self):
        """Gets the acknowledgement_status_details of this OrderItemStatusAcknowledgementStatus.  # noqa: E501

        Details of item quantity confirmed.  # noqa: E501

        :return: The acknowledgement_status_details of this OrderItemStatusAcknowledgementStatus.  # noqa: E501
        :rtype: List[AcknowledgementStatusDetails]
        """
        return self._acknowledgement_status_details

    @acknowledgement_status_details.setter
    def acknowledgement_status_details(self, acknowledgement_status_details):
        """Sets the acknowledgement_status_details of this OrderItemStatusAcknowledgementStatus.

        Details of item quantity confirmed.  # noqa: E501

        :param acknowledgement_status_details: The acknowledgement_status_details of this OrderItemStatusAcknowledgementStatus.  # noqa: E501
        :type: List[AcknowledgementStatusDetails]
        """

        self._acknowledgement_status_details = acknowledgement_status_details

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
        if issubclass(OrderItemStatusAcknowledgementStatus, dict):
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
        if not isinstance(other, OrderItemStatusAcknowledgementStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrderItemStatusAcknowledgementStatus):
            return True

        return self.to_dict() != other.to_dict()

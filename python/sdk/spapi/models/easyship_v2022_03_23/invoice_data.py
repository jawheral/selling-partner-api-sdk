# coding: utf-8

"""
    Selling Partner API for Easy Ship

    Use the Selling Partner API for Easy Ship to build applications for sellers to manage and ship Amazon Easy Ship orders. With this API, you can get available time slots, schedule and reschedule Easy Ship orders, and print shipping labels, invoices, and warranties. To review the differences in Easy Ship operations by marketplace, refer to [Marketplace support](https://developer-docs.amazon.com/sp-api/docs/easyship-api-v2022-03-23-use-case-guide#marketplace-support).

    The version of the OpenAPI document: 2022-03-23
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import pprint
import re  # noqa: F401

import six

from spapi.configuration import Configuration


class InvoiceData(object):
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
        'invoice_number': 'str',
        'invoice_date': 'datetime',
    }

    attribute_map = {
        'invoice_number': 'invoiceNumber',
        'invoice_date': 'invoiceDate',
    }

    def __init__(self, invoice_number=None, invoice_date=None, _configuration=None):  # noqa: E501
        """InvoiceData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._invoice_number = None
        self._invoice_date = None
        self.discriminator = None

        self.invoice_number = invoice_number
        if invoice_date is not None:
            self.invoice_date = invoice_date

    @property
    def invoice_number(self):
        """Gets the invoice_number of this InvoiceData.  # noqa: E501

        A string of up to 255 characters.  # noqa: E501

        :return: The invoice_number of this InvoiceData.  # noqa: E501
        :rtype: str
        """
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        """Sets the invoice_number of this InvoiceData.

        A string of up to 255 characters.  # noqa: E501

        :param invoice_number: The invoice_number of this InvoiceData.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and invoice_number is None:
            raise ValueError("Invalid value for `invoice_number`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                invoice_number is not None and len(invoice_number) > 255):
            raise ValueError("Invalid value for `invoice_number`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                invoice_number is not None and len(invoice_number) < 1):
            raise ValueError("Invalid value for `invoice_number`, length must be greater than or equal to `1`")  # noqa: E501

        self._invoice_number = invoice_number

    @property
    def invoice_date(self):
        """Gets the invoice_date of this InvoiceData.  # noqa: E501

        A datetime value in ISO 8601 format.  # noqa: E501

        :return: The invoice_date of this InvoiceData.  # noqa: E501
        :rtype: datetime
        """
        return self._invoice_date

    @invoice_date.setter
    def invoice_date(self, invoice_date):
        """Sets the invoice_date of this InvoiceData.

        A datetime value in ISO 8601 format.  # noqa: E501

        :param invoice_date: The invoice_date of this InvoiceData.  # noqa: E501
        :type: datetime
        """

        self._invoice_date = invoice_date

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
        if issubclass(InvoiceData, dict):
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
        if not isinstance(other, InvoiceData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InvoiceData):
            return True

        return self.to_dict() != other.to_dict()

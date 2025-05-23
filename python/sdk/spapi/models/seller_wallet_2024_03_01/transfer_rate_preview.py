# coding: utf-8

"""
    The Selling Partner API for Amazon Seller Wallet Open Banking API

    The Selling Partner API for Seller Wallet (Seller Wallet API) provides financial information that is relevant to a seller's Seller Wallet account. You can obtain financial events, balances, and transfer schedules for Seller Wallet accounts. You can also schedule and initiate transactions.

    The version of the OpenAPI document: 2024-03-01
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import pprint
import re  # noqa: F401

import six

from spapi.configuration import Configuration


class TransferRatePreview(object):
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
        'base_amount': 'Currency',
        'fx_rate_details': 'FxRateDetails',
        'transfer_amount': 'Currency',
        'fees': 'List[Fee]',
    }

    attribute_map = {
        'base_amount': 'baseAmount',
        'fx_rate_details': 'fxRateDetails',
        'transfer_amount': 'transferAmount',
        'fees': 'fees',
    }

    def __init__(self, base_amount=None, fx_rate_details=None, transfer_amount=None, fees=None, _configuration=None):  # noqa: E501
        """TransferRatePreview - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._base_amount = None
        self._fx_rate_details = None
        self._transfer_amount = None
        self._fees = None
        self.discriminator = None

        self.base_amount = base_amount
        self.fx_rate_details = fx_rate_details
        self.transfer_amount = transfer_amount
        self.fees = fees

    @property
    def base_amount(self):
        """Gets the base_amount of this TransferRatePreview.  # noqa: E501


        :return: The base_amount of this TransferRatePreview.  # noqa: E501
        :rtype: Currency
        """
        return self._base_amount

    @base_amount.setter
    def base_amount(self, base_amount):
        """Sets the base_amount of this TransferRatePreview.


        :param base_amount: The base_amount of this TransferRatePreview.  # noqa: E501
        :type: Currency
        """
        if self._configuration.client_side_validation and base_amount is None:
            raise ValueError("Invalid value for `base_amount`, must not be `None`")  # noqa: E501

        self._base_amount = base_amount

    @property
    def fx_rate_details(self):
        """Gets the fx_rate_details of this TransferRatePreview.  # noqa: E501


        :return: The fx_rate_details of this TransferRatePreview.  # noqa: E501
        :rtype: FxRateDetails
        """
        return self._fx_rate_details

    @fx_rate_details.setter
    def fx_rate_details(self, fx_rate_details):
        """Sets the fx_rate_details of this TransferRatePreview.


        :param fx_rate_details: The fx_rate_details of this TransferRatePreview.  # noqa: E501
        :type: FxRateDetails
        """
        if self._configuration.client_side_validation and fx_rate_details is None:
            raise ValueError("Invalid value for `fx_rate_details`, must not be `None`")  # noqa: E501

        self._fx_rate_details = fx_rate_details

    @property
    def transfer_amount(self):
        """Gets the transfer_amount of this TransferRatePreview.  # noqa: E501


        :return: The transfer_amount of this TransferRatePreview.  # noqa: E501
        :rtype: Currency
        """
        return self._transfer_amount

    @transfer_amount.setter
    def transfer_amount(self, transfer_amount):
        """Sets the transfer_amount of this TransferRatePreview.


        :param transfer_amount: The transfer_amount of this TransferRatePreview.  # noqa: E501
        :type: Currency
        """
        if self._configuration.client_side_validation and transfer_amount is None:
            raise ValueError("Invalid value for `transfer_amount`, must not be `None`")  # noqa: E501

        self._transfer_amount = transfer_amount

    @property
    def fees(self):
        """Gets the fees of this TransferRatePreview.  # noqa: E501

        A list of fees.  # noqa: E501

        :return: The fees of this TransferRatePreview.  # noqa: E501
        :rtype: List[Fee]
        """
        return self._fees

    @fees.setter
    def fees(self, fees):
        """Sets the fees of this TransferRatePreview.

        A list of fees.  # noqa: E501

        :param fees: The fees of this TransferRatePreview.  # noqa: E501
        :type: List[Fee]
        """
        if self._configuration.client_side_validation and fees is None:
            raise ValueError("Invalid value for `fees`, must not be `None`")  # noqa: E501

        self._fees = fees

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
        if issubclass(TransferRatePreview, dict):
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
        if not isinstance(other, TransferRatePreview):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransferRatePreview):
            return True

        return self.to_dict() != other.to_dict()

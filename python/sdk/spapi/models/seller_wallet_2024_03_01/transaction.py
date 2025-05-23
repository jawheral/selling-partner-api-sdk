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


class Transaction(object):
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
        'transaction_id': 'str',
        'transaction_type': 'TransactionType',
        'transaction_status': 'TransactionStatus',
        'transaction_request_date': 'datetime',
        'expected_completion_date': 'datetime',
        'transaction_actual_completion_date': 'datetime',
        'last_update_date': 'datetime',
        'requester_name': 'str',
        'transaction_requester_source': 'str',
        'transaction_description': 'str',
        'transaction_source_account': 'TransactionAccount',
        'transaction_destination_account': 'TransactionAccount',
        'transaction_request_amount': 'Currency',
        'transfer_rate_details': 'TransferRatePreview',
        'transaction_final_amount': 'Currency',
        'transaction_failure_reason': 'str',
    }

    attribute_map = {
        'transaction_id': 'transactionId',
        'transaction_type': 'transactionType',
        'transaction_status': 'transactionStatus',
        'transaction_request_date': 'transactionRequestDate',
        'expected_completion_date': 'expectedCompletionDate',
        'transaction_actual_completion_date': 'transactionActualCompletionDate',
        'last_update_date': 'lastUpdateDate',
        'requester_name': 'requesterName',
        'transaction_requester_source': 'transactionRequesterSource',
        'transaction_description': 'transactionDescription',
        'transaction_source_account': 'transactionSourceAccount',
        'transaction_destination_account': 'transactionDestinationAccount',
        'transaction_request_amount': 'transactionRequestAmount',
        'transfer_rate_details': 'transferRateDetails',
        'transaction_final_amount': 'transactionFinalAmount',
        'transaction_failure_reason': 'transactionFailureReason',
    }

    def __init__(self, transaction_id=None, transaction_type=None, transaction_status=None, transaction_request_date=None, expected_completion_date=None, transaction_actual_completion_date=None, last_update_date=None, requester_name=None, transaction_requester_source=None, transaction_description=None, transaction_source_account=None, transaction_destination_account=None, transaction_request_amount=None, transfer_rate_details=None, transaction_final_amount=None, transaction_failure_reason=None, _configuration=None):  # noqa: E501
        """Transaction - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._transaction_id = None
        self._transaction_type = None
        self._transaction_status = None
        self._transaction_request_date = None
        self._expected_completion_date = None
        self._transaction_actual_completion_date = None
        self._last_update_date = None
        self._requester_name = None
        self._transaction_requester_source = None
        self._transaction_description = None
        self._transaction_source_account = None
        self._transaction_destination_account = None
        self._transaction_request_amount = None
        self._transfer_rate_details = None
        self._transaction_final_amount = None
        self._transaction_failure_reason = None
        self.discriminator = None

        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.transaction_status = transaction_status
        self.transaction_request_date = transaction_request_date
        if expected_completion_date is not None:
            self.expected_completion_date = expected_completion_date
        if transaction_actual_completion_date is not None:
            self.transaction_actual_completion_date = transaction_actual_completion_date
        self.last_update_date = last_update_date
        if requester_name is not None:
            self.requester_name = requester_name
        self.transaction_requester_source = transaction_requester_source
        self.transaction_description = transaction_description
        self.transaction_source_account = transaction_source_account
        self.transaction_destination_account = transaction_destination_account
        self.transaction_request_amount = transaction_request_amount
        self.transfer_rate_details = transfer_rate_details
        if transaction_final_amount is not None:
            self.transaction_final_amount = transaction_final_amount
        if transaction_failure_reason is not None:
            self.transaction_failure_reason = transaction_failure_reason

    @property
    def transaction_id(self):
        """Gets the transaction_id of this Transaction.  # noqa: E501

        The unique identifier provided by Amazon to the transaction.  # noqa: E501

        :return: The transaction_id of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this Transaction.

        The unique identifier provided by Amazon to the transaction.  # noqa: E501

        :param transaction_id: The transaction_id of this Transaction.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and transaction_id is None:
            raise ValueError("Invalid value for `transaction_id`, must not be `None`")  # noqa: E501

        self._transaction_id = transaction_id

    @property
    def transaction_type(self):
        """Gets the transaction_type of this Transaction.  # noqa: E501


        :return: The transaction_type of this Transaction.  # noqa: E501
        :rtype: TransactionType
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this Transaction.


        :param transaction_type: The transaction_type of this Transaction.  # noqa: E501
        :type: TransactionType
        """
        if self._configuration.client_side_validation and transaction_type is None:
            raise ValueError("Invalid value for `transaction_type`, must not be `None`")  # noqa: E501

        self._transaction_type = transaction_type

    @property
    def transaction_status(self):
        """Gets the transaction_status of this Transaction.  # noqa: E501


        :return: The transaction_status of this Transaction.  # noqa: E501
        :rtype: TransactionStatus
        """
        return self._transaction_status

    @transaction_status.setter
    def transaction_status(self, transaction_status):
        """Sets the transaction_status of this Transaction.


        :param transaction_status: The transaction_status of this Transaction.  # noqa: E501
        :type: TransactionStatus
        """
        if self._configuration.client_side_validation and transaction_status is None:
            raise ValueError("Invalid value for `transaction_status`, must not be `None`")  # noqa: E501

        self._transaction_status = transaction_status

    @property
    def transaction_request_date(self):
        """Gets the transaction_request_date of this Transaction.  # noqa: E501

        The date on which the transaction was initiated.  # noqa: E501

        :return: The transaction_request_date of this Transaction.  # noqa: E501
        :rtype: datetime
        """
        return self._transaction_request_date

    @transaction_request_date.setter
    def transaction_request_date(self, transaction_request_date):
        """Sets the transaction_request_date of this Transaction.

        The date on which the transaction was initiated.  # noqa: E501

        :param transaction_request_date: The transaction_request_date of this Transaction.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and transaction_request_date is None:
            raise ValueError("Invalid value for `transaction_request_date`, must not be `None`")  # noqa: E501

        self._transaction_request_date = transaction_request_date

    @property
    def expected_completion_date(self):
        """Gets the expected_completion_date of this Transaction.  # noqa: E501

        The expected completion date of the transaction.  # noqa: E501

        :return: The expected_completion_date of this Transaction.  # noqa: E501
        :rtype: datetime
        """
        return self._expected_completion_date

    @expected_completion_date.setter
    def expected_completion_date(self, expected_completion_date):
        """Sets the expected_completion_date of this Transaction.

        The expected completion date of the transaction.  # noqa: E501

        :param expected_completion_date: The expected_completion_date of this Transaction.  # noqa: E501
        :type: datetime
        """

        self._expected_completion_date = expected_completion_date

    @property
    def transaction_actual_completion_date(self):
        """Gets the transaction_actual_completion_date of this Transaction.  # noqa: E501

        The transaction's completion date.  # noqa: E501

        :return: The transaction_actual_completion_date of this Transaction.  # noqa: E501
        :rtype: datetime
        """
        return self._transaction_actual_completion_date

    @transaction_actual_completion_date.setter
    def transaction_actual_completion_date(self, transaction_actual_completion_date):
        """Sets the transaction_actual_completion_date of this Transaction.

        The transaction's completion date.  # noqa: E501

        :param transaction_actual_completion_date: The transaction_actual_completion_date of this Transaction.  # noqa: E501
        :type: datetime
        """

        self._transaction_actual_completion_date = transaction_actual_completion_date

    @property
    def last_update_date(self):
        """Gets the last_update_date of this Transaction.  # noqa: E501

        The date of the most recent account balance update.  # noqa: E501

        :return: The last_update_date of this Transaction.  # noqa: E501
        :rtype: datetime
        """
        return self._last_update_date

    @last_update_date.setter
    def last_update_date(self, last_update_date):
        """Sets the last_update_date of this Transaction.

        The date of the most recent account balance update.  # noqa: E501

        :param last_update_date: The last_update_date of this Transaction.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and last_update_date is None:
            raise ValueError("Invalid value for `last_update_date`, must not be `None`")  # noqa: E501

        self._last_update_date = last_update_date

    @property
    def requester_name(self):
        """Gets the requester_name of this Transaction.  # noqa: E501

        The Amazon Seller Wallet customer who requested the transaction.  # noqa: E501

        :return: The requester_name of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._requester_name

    @requester_name.setter
    def requester_name(self, requester_name):
        """Sets the requester_name of this Transaction.

        The Amazon Seller Wallet customer who requested the transaction.  # noqa: E501

        :param requester_name: The requester_name of this Transaction.  # noqa: E501
        :type: str
        """

        self._requester_name = requester_name

    @property
    def transaction_requester_source(self):
        """Gets the transaction_requester_source of this Transaction.  # noqa: E501

        The transaction initiation source. This value could be the Amazon portal or PISP name that the customer used to start the transaction.  # noqa: E501

        :return: The transaction_requester_source of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._transaction_requester_source

    @transaction_requester_source.setter
    def transaction_requester_source(self, transaction_requester_source):
        """Sets the transaction_requester_source of this Transaction.

        The transaction initiation source. This value could be the Amazon portal or PISP name that the customer used to start the transaction.  # noqa: E501

        :param transaction_requester_source: The transaction_requester_source of this Transaction.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and transaction_requester_source is None:
            raise ValueError("Invalid value for `transaction_requester_source`, must not be `None`")  # noqa: E501

        self._transaction_requester_source = transaction_requester_source

    @property
    def transaction_description(self):
        """Gets the transaction_description of this Transaction.  # noqa: E501

        The description provided by the requester in the transaction request at time of transaction initiation.  # noqa: E501

        :return: The transaction_description of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._transaction_description

    @transaction_description.setter
    def transaction_description(self, transaction_description):
        """Sets the transaction_description of this Transaction.

        The description provided by the requester in the transaction request at time of transaction initiation.  # noqa: E501

        :param transaction_description: The transaction_description of this Transaction.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and transaction_description is None:
            raise ValueError("Invalid value for `transaction_description`, must not be `None`")  # noqa: E501

        self._transaction_description = transaction_description

    @property
    def transaction_source_account(self):
        """Gets the transaction_source_account of this Transaction.  # noqa: E501


        :return: The transaction_source_account of this Transaction.  # noqa: E501
        :rtype: TransactionAccount
        """
        return self._transaction_source_account

    @transaction_source_account.setter
    def transaction_source_account(self, transaction_source_account):
        """Sets the transaction_source_account of this Transaction.


        :param transaction_source_account: The transaction_source_account of this Transaction.  # noqa: E501
        :type: TransactionAccount
        """
        if self._configuration.client_side_validation and transaction_source_account is None:
            raise ValueError("Invalid value for `transaction_source_account`, must not be `None`")  # noqa: E501

        self._transaction_source_account = transaction_source_account

    @property
    def transaction_destination_account(self):
        """Gets the transaction_destination_account of this Transaction.  # noqa: E501


        :return: The transaction_destination_account of this Transaction.  # noqa: E501
        :rtype: TransactionAccount
        """
        return self._transaction_destination_account

    @transaction_destination_account.setter
    def transaction_destination_account(self, transaction_destination_account):
        """Sets the transaction_destination_account of this Transaction.


        :param transaction_destination_account: The transaction_destination_account of this Transaction.  # noqa: E501
        :type: TransactionAccount
        """
        if self._configuration.client_side_validation and transaction_destination_account is None:
            raise ValueError("Invalid value for `transaction_destination_account`, must not be `None`")  # noqa: E501

        self._transaction_destination_account = transaction_destination_account

    @property
    def transaction_request_amount(self):
        """Gets the transaction_request_amount of this Transaction.  # noqa: E501


        :return: The transaction_request_amount of this Transaction.  # noqa: E501
        :rtype: Currency
        """
        return self._transaction_request_amount

    @transaction_request_amount.setter
    def transaction_request_amount(self, transaction_request_amount):
        """Sets the transaction_request_amount of this Transaction.


        :param transaction_request_amount: The transaction_request_amount of this Transaction.  # noqa: E501
        :type: Currency
        """
        if self._configuration.client_side_validation and transaction_request_amount is None:
            raise ValueError("Invalid value for `transaction_request_amount`, must not be `None`")  # noqa: E501

        self._transaction_request_amount = transaction_request_amount

    @property
    def transfer_rate_details(self):
        """Gets the transfer_rate_details of this Transaction.  # noqa: E501


        :return: The transfer_rate_details of this Transaction.  # noqa: E501
        :rtype: TransferRatePreview
        """
        return self._transfer_rate_details

    @transfer_rate_details.setter
    def transfer_rate_details(self, transfer_rate_details):
        """Sets the transfer_rate_details of this Transaction.


        :param transfer_rate_details: The transfer_rate_details of this Transaction.  # noqa: E501
        :type: TransferRatePreview
        """
        if self._configuration.client_side_validation and transfer_rate_details is None:
            raise ValueError("Invalid value for `transfer_rate_details`, must not be `None`")  # noqa: E501

        self._transfer_rate_details = transfer_rate_details

    @property
    def transaction_final_amount(self):
        """Gets the transaction_final_amount of this Transaction.  # noqa: E501


        :return: The transaction_final_amount of this Transaction.  # noqa: E501
        :rtype: Currency
        """
        return self._transaction_final_amount

    @transaction_final_amount.setter
    def transaction_final_amount(self, transaction_final_amount):
        """Sets the transaction_final_amount of this Transaction.


        :param transaction_final_amount: The transaction_final_amount of this Transaction.  # noqa: E501
        :type: Currency
        """

        self._transaction_final_amount = transaction_final_amount

    @property
    def transaction_failure_reason(self):
        """Gets the transaction_failure_reason of this Transaction.  # noqa: E501

        The reason the transaction failed, if applicable.  # noqa: E501

        :return: The transaction_failure_reason of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._transaction_failure_reason

    @transaction_failure_reason.setter
    def transaction_failure_reason(self, transaction_failure_reason):
        """Sets the transaction_failure_reason of this Transaction.

        The reason the transaction failed, if applicable.  # noqa: E501

        :param transaction_failure_reason: The transaction_failure_reason of this Transaction.  # noqa: E501
        :type: str
        """

        self._transaction_failure_reason = transaction_failure_reason

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
        if issubclass(Transaction, dict):
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
        if not isinstance(other, Transaction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Transaction):
            return True

        return self.to_dict() != other.to_dict()

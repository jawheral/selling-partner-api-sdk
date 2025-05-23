# coding: utf-8

"""
    Selling Partner API for Retail Procurement Payments

    The Selling Partner API for Retail Procurement Payments provides programmatic access to vendors payments data.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import pprint
import re  # noqa: F401

import six

from spapi.configuration import Configuration


class CreditNoteDetails(object):
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
        'reference_invoice_number': 'str',
        'debit_note_number': 'str',
        'returns_reference_number': 'str',
        'goods_return_date': 'datetime',
        'rma_id': 'str',
        'coop_reference_number': 'str',
        'consignors_reference_number': 'str',
    }

    attribute_map = {
        'reference_invoice_number': 'referenceInvoiceNumber',
        'debit_note_number': 'debitNoteNumber',
        'returns_reference_number': 'returnsReferenceNumber',
        'goods_return_date': 'goodsReturnDate',
        'rma_id': 'rmaId',
        'coop_reference_number': 'coopReferenceNumber',
        'consignors_reference_number': 'consignorsReferenceNumber',
    }

    def __init__(self, reference_invoice_number=None, debit_note_number=None, returns_reference_number=None, goods_return_date=None, rma_id=None, coop_reference_number=None, consignors_reference_number=None, _configuration=None):  # noqa: E501
        """CreditNoteDetails - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._reference_invoice_number = None
        self._debit_note_number = None
        self._returns_reference_number = None
        self._goods_return_date = None
        self._rma_id = None
        self._coop_reference_number = None
        self._consignors_reference_number = None
        self.discriminator = None

        if reference_invoice_number is not None:
            self.reference_invoice_number = reference_invoice_number
        if debit_note_number is not None:
            self.debit_note_number = debit_note_number
        if returns_reference_number is not None:
            self.returns_reference_number = returns_reference_number
        if goods_return_date is not None:
            self.goods_return_date = goods_return_date
        if rma_id is not None:
            self.rma_id = rma_id
        if coop_reference_number is not None:
            self.coop_reference_number = coop_reference_number
        if consignors_reference_number is not None:
            self.consignors_reference_number = consignors_reference_number

    @property
    def reference_invoice_number(self):
        """Gets the reference_invoice_number of this CreditNoteDetails.  # noqa: E501

        Original Invoice Number when sending a credit note relating to an existing invoice. One Invoice only to be processed per Credit Note. This is mandatory for AP Credit Notes.  # noqa: E501

        :return: The reference_invoice_number of this CreditNoteDetails.  # noqa: E501
        :rtype: str
        """
        return self._reference_invoice_number

    @reference_invoice_number.setter
    def reference_invoice_number(self, reference_invoice_number):
        """Sets the reference_invoice_number of this CreditNoteDetails.

        Original Invoice Number when sending a credit note relating to an existing invoice. One Invoice only to be processed per Credit Note. This is mandatory for AP Credit Notes.  # noqa: E501

        :param reference_invoice_number: The reference_invoice_number of this CreditNoteDetails.  # noqa: E501
        :type: str
        """

        self._reference_invoice_number = reference_invoice_number

    @property
    def debit_note_number(self):
        """Gets the debit_note_number of this CreditNoteDetails.  # noqa: E501

        Debit Note Number as generated by Amazon. Recommended for Returns and COOP Credit Notes.  # noqa: E501

        :return: The debit_note_number of this CreditNoteDetails.  # noqa: E501
        :rtype: str
        """
        return self._debit_note_number

    @debit_note_number.setter
    def debit_note_number(self, debit_note_number):
        """Sets the debit_note_number of this CreditNoteDetails.

        Debit Note Number as generated by Amazon. Recommended for Returns and COOP Credit Notes.  # noqa: E501

        :param debit_note_number: The debit_note_number of this CreditNoteDetails.  # noqa: E501
        :type: str
        """

        self._debit_note_number = debit_note_number

    @property
    def returns_reference_number(self):
        """Gets the returns_reference_number of this CreditNoteDetails.  # noqa: E501

        Identifies the Returns Notice Number. Mandatory for all Returns Credit Notes.  # noqa: E501

        :return: The returns_reference_number of this CreditNoteDetails.  # noqa: E501
        :rtype: str
        """
        return self._returns_reference_number

    @returns_reference_number.setter
    def returns_reference_number(self, returns_reference_number):
        """Sets the returns_reference_number of this CreditNoteDetails.

        Identifies the Returns Notice Number. Mandatory for all Returns Credit Notes.  # noqa: E501

        :param returns_reference_number: The returns_reference_number of this CreditNoteDetails.  # noqa: E501
        :type: str
        """

        self._returns_reference_number = returns_reference_number

    @property
    def goods_return_date(self):
        """Gets the goods_return_date of this CreditNoteDetails.  # noqa: E501

        Defines a date and time according to ISO8601.  # noqa: E501

        :return: The goods_return_date of this CreditNoteDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._goods_return_date

    @goods_return_date.setter
    def goods_return_date(self, goods_return_date):
        """Sets the goods_return_date of this CreditNoteDetails.

        Defines a date and time according to ISO8601.  # noqa: E501

        :param goods_return_date: The goods_return_date of this CreditNoteDetails.  # noqa: E501
        :type: datetime
        """

        self._goods_return_date = goods_return_date

    @property
    def rma_id(self):
        """Gets the rma_id of this CreditNoteDetails.  # noqa: E501

        Identifies the Returned Merchandise Authorization ID, if generated.  # noqa: E501

        :return: The rma_id of this CreditNoteDetails.  # noqa: E501
        :rtype: str
        """
        return self._rma_id

    @rma_id.setter
    def rma_id(self, rma_id):
        """Sets the rma_id of this CreditNoteDetails.

        Identifies the Returned Merchandise Authorization ID, if generated.  # noqa: E501

        :param rma_id: The rma_id of this CreditNoteDetails.  # noqa: E501
        :type: str
        """

        self._rma_id = rma_id

    @property
    def coop_reference_number(self):
        """Gets the coop_reference_number of this CreditNoteDetails.  # noqa: E501

        Identifies the COOP reference used for COOP agreement. Failure to provide the COOP reference number or the Debit Note number may lead to a rejection of the Credit Note.  # noqa: E501

        :return: The coop_reference_number of this CreditNoteDetails.  # noqa: E501
        :rtype: str
        """
        return self._coop_reference_number

    @coop_reference_number.setter
    def coop_reference_number(self, coop_reference_number):
        """Sets the coop_reference_number of this CreditNoteDetails.

        Identifies the COOP reference used for COOP agreement. Failure to provide the COOP reference number or the Debit Note number may lead to a rejection of the Credit Note.  # noqa: E501

        :param coop_reference_number: The coop_reference_number of this CreditNoteDetails.  # noqa: E501
        :type: str
        """

        self._coop_reference_number = coop_reference_number

    @property
    def consignors_reference_number(self):
        """Gets the consignors_reference_number of this CreditNoteDetails.  # noqa: E501

        Identifies the consignor reference number (VRET number), if generated by Amazon.  # noqa: E501

        :return: The consignors_reference_number of this CreditNoteDetails.  # noqa: E501
        :rtype: str
        """
        return self._consignors_reference_number

    @consignors_reference_number.setter
    def consignors_reference_number(self, consignors_reference_number):
        """Sets the consignors_reference_number of this CreditNoteDetails.

        Identifies the consignor reference number (VRET number), if generated by Amazon.  # noqa: E501

        :param consignors_reference_number: The consignors_reference_number of this CreditNoteDetails.  # noqa: E501
        :type: str
        """

        self._consignors_reference_number = consignors_reference_number

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
        if issubclass(CreditNoteDetails, dict):
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
        if not isinstance(other, CreditNoteDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreditNoteDetails):
            return True

        return self.to_dict() != other.to_dict()

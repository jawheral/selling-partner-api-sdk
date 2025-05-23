# coding: utf-8

"""
    Selling Partner API for A+ Content Management

    Use the A+ Content API to build applications that help selling partners add rich marketing content to their Amazon product detail pages. Selling partners can use A+ content to share their brand and product story, which helps buyers make informed purchasing decisions. Selling partners use content modules to add images and text.

    The version of the OpenAPI document: 2020-11-01
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import pprint
import re  # noqa: F401

import six

from spapi.configuration import Configuration


class StandardTechSpecsModule(object):
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
        'headline': 'TextComponent',
        'specification_list': 'List[StandardTextPairBlock]',
        'table_count': 'int',
    }

    attribute_map = {
        'headline': 'headline',
        'specification_list': 'specificationList',
        'table_count': 'tableCount',
    }

    def __init__(self, headline=None, specification_list=None, table_count=None, _configuration=None):  # noqa: E501
        """StandardTechSpecsModule - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._headline = None
        self._specification_list = None
        self._table_count = None
        self.discriminator = None

        if headline is not None:
            self.headline = headline
        self.specification_list = specification_list
        if table_count is not None:
            self.table_count = table_count

    @property
    def headline(self):
        """Gets the headline of this StandardTechSpecsModule.  # noqa: E501


        :return: The headline of this StandardTechSpecsModule.  # noqa: E501
        :rtype: TextComponent
        """
        return self._headline

    @headline.setter
    def headline(self, headline):
        """Sets the headline of this StandardTechSpecsModule.


        :param headline: The headline of this StandardTechSpecsModule.  # noqa: E501
        :type: TextComponent
        """

        self._headline = headline

    @property
    def specification_list(self):
        """Gets the specification_list of this StandardTechSpecsModule.  # noqa: E501

        The specification list.  # noqa: E501

        :return: The specification_list of this StandardTechSpecsModule.  # noqa: E501
        :rtype: List[StandardTextPairBlock]
        """
        return self._specification_list

    @specification_list.setter
    def specification_list(self, specification_list):
        """Sets the specification_list of this StandardTechSpecsModule.

        The specification list.  # noqa: E501

        :param specification_list: The specification_list of this StandardTechSpecsModule.  # noqa: E501
        :type: List[StandardTextPairBlock]
        """
        if self._configuration.client_side_validation and specification_list is None:
            raise ValueError("Invalid value for `specification_list`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                specification_list is not None and len(specification_list) > 16):
            raise ValueError("Invalid value for `specification_list`, number of items must be less than or equal to `16`")  # noqa: E501
        if (self._configuration.client_side_validation and
                specification_list is not None and len(specification_list) < 4):
            raise ValueError("Invalid value for `specification_list`, number of items must be greater than or equal to `4`")  # noqa: E501

        self._specification_list = specification_list

    @property
    def table_count(self):
        """Gets the table_count of this StandardTechSpecsModule.  # noqa: E501

        The number of tables you want present. Features are evenly divided between the tables.  # noqa: E501

        :return: The table_count of this StandardTechSpecsModule.  # noqa: E501
        :rtype: int
        """
        return self._table_count

    @table_count.setter
    def table_count(self, table_count):
        """Sets the table_count of this StandardTechSpecsModule.

        The number of tables you want present. Features are evenly divided between the tables.  # noqa: E501

        :param table_count: The table_count of this StandardTechSpecsModule.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                table_count is not None and table_count > 2):  # noqa: E501
            raise ValueError("Invalid value for `table_count`, must be a value less than or equal to `2`")  # noqa: E501
        if (self._configuration.client_side_validation and
                table_count is not None and table_count < 1):  # noqa: E501
            raise ValueError("Invalid value for `table_count`, must be a value greater than or equal to `1`")  # noqa: E501

        self._table_count = table_count

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
        if issubclass(StandardTechSpecsModule, dict):
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
        if not isinstance(other, StandardTechSpecsModule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StandardTechSpecsModule):
            return True

        return self.to_dict() != other.to_dict()

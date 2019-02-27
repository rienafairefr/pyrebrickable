# coding: utf-8

import pprint
import re  # noqa: F401

import six


class AllPart(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'color': 'Color',
        'part': 'Part',
        'quantity': 'Integer'
    }

    attribute_map = {
        'color': 'color',
        'part': 'part',
        'quantity': 'quantity'
    }

    def __init__(self, color=null, part=null, quantity=null):  # noqa: E501
        """AllPart - a model defined in OpenAPI"""  # noqa: E501

        self._color = None
        self._part = None
        self._quantity = None
        self.discriminator = None

        if color is not None:
            self.color = color
        if part is not None:
            self.part = part
        if quantity is not None:
            self.quantity = quantity

    @property
    def color(self):
        """Gets the color of this AllPart.  # noqa: E501


        :return: The color of this AllPart.  # noqa: E501
        :rtype: Color
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this AllPart.


        :param color: The color of this AllPart.  # noqa: E501
        :type: Color
        """

        self._color = color

    @property
    def part(self):
        """Gets the part of this AllPart.  # noqa: E501


        :return: The part of this AllPart.  # noqa: E501
        :rtype: Part
        """
        return self._part

    @part.setter
    def part(self, part):
        """Sets the part of this AllPart.


        :param part: The part of this AllPart.  # noqa: E501
        :type: Part
        """

        self._part = part

    @property
    def quantity(self):
        """Gets the quantity of this AllPart.  # noqa: E501


        :return: The quantity of this AllPart.  # noqa: E501
        :rtype: Integer
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this AllPart.


        :param quantity: The quantity of this AllPart.  # noqa: E501
        :type: Integer
        """

        self._quantity = quantity

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AllPart):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
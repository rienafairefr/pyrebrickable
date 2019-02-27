# coding: utf-8

import pprint
import re  # noqa: F401

import six


class InventoryPart(object):
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
        'id': 'Integer',
        'invUnderscorepartUnderscoreid': 'Integer',
        'part': 'Part'
    }

    attribute_map = {
        'color': 'color',
        'id': 'id',
        'invUnderscorepartUnderscoreid': 'inv_part_id',
        'part': 'part'
    }

    def __init__(self, color=null, id=null, invUnderscorepartUnderscoreid=null, part=null):  # noqa: E501
        """InventoryPart - a model defined in OpenAPI"""  # noqa: E501

        self._color = None
        self._id = None
        self._invUnderscorepartUnderscoreid = None
        self._part = None
        self.discriminator = None

        if color is not None:
            self.color = color
        if id is not None:
            self.id = id
        if invUnderscorepartUnderscoreid is not None:
            self.invUnderscorepartUnderscoreid = invUnderscorepartUnderscoreid
        if part is not None:
            self.part = part

    @property
    def color(self):
        """Gets the color of this InventoryPart.  # noqa: E501


        :return: The color of this InventoryPart.  # noqa: E501
        :rtype: Color
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this InventoryPart.


        :param color: The color of this InventoryPart.  # noqa: E501
        :type: Color
        """

        self._color = color

    @property
    def id(self):
        """Gets the id of this InventoryPart.  # noqa: E501


        :return: The id of this InventoryPart.  # noqa: E501
        :rtype: Integer
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InventoryPart.


        :param id: The id of this InventoryPart.  # noqa: E501
        :type: Integer
        """

        self._id = id

    @property
    def invUnderscorepartUnderscoreid(self):
        """Gets the invUnderscorepartUnderscoreid of this InventoryPart.  # noqa: E501


        :return: The invUnderscorepartUnderscoreid of this InventoryPart.  # noqa: E501
        :rtype: Integer
        """
        return self._invUnderscorepartUnderscoreid

    @invUnderscorepartUnderscoreid.setter
    def invUnderscorepartUnderscoreid(self, invUnderscorepartUnderscoreid):
        """Sets the invUnderscorepartUnderscoreid of this InventoryPart.


        :param invUnderscorepartUnderscoreid: The invUnderscorepartUnderscoreid of this InventoryPart.  # noqa: E501
        :type: Integer
        """

        self._invUnderscorepartUnderscoreid = invUnderscorepartUnderscoreid

    @property
    def part(self):
        """Gets the part of this InventoryPart.  # noqa: E501


        :return: The part of this InventoryPart.  # noqa: E501
        :rtype: Part
        """
        return self._part

    @part.setter
    def part(self, part):
        """Sets the part of this InventoryPart.


        :param part: The part of this InventoryPart.  # noqa: E501
        :type: Part
        """

        self._part = part

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
        if not isinstance(other, InventoryPart):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
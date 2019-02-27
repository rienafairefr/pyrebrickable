# coding: utf-8

import pprint
import re  # noqa: F401

import six


class Color(object):
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
        'externalUnderscoreids': 'ExternalColorIds',
        'id': 'Integer',
        'isUnderscoretrans': 'Boolean',
        'name': 'String',
        'rgb': 'String'
    }

    attribute_map = {
        'externalUnderscoreids': 'external_ids',
        'id': 'id',
        'isUnderscoretrans': 'is_trans',
        'name': 'name',
        'rgb': 'rgb'
    }

    def __init__(self, externalUnderscoreids=null, id=null, isUnderscoretrans=null, name=null, rgb=null):  # noqa: E501
        """Color - a model defined in OpenAPI"""  # noqa: E501

        self._externalUnderscoreids = None
        self._id = None
        self._isUnderscoretrans = None
        self._name = None
        self._rgb = None
        self.discriminator = None

        if externalUnderscoreids is not None:
            self.externalUnderscoreids = externalUnderscoreids
        if id is not None:
            self.id = id
        if isUnderscoretrans is not None:
            self.isUnderscoretrans = isUnderscoretrans
        if name is not None:
            self.name = name
        if rgb is not None:
            self.rgb = rgb

    @property
    def externalUnderscoreids(self):
        """Gets the externalUnderscoreids of this Color.  # noqa: E501


        :return: The externalUnderscoreids of this Color.  # noqa: E501
        :rtype: ExternalColorIds
        """
        return self._externalUnderscoreids

    @externalUnderscoreids.setter
    def externalUnderscoreids(self, externalUnderscoreids):
        """Sets the externalUnderscoreids of this Color.


        :param externalUnderscoreids: The externalUnderscoreids of this Color.  # noqa: E501
        :type: ExternalColorIds
        """

        self._externalUnderscoreids = externalUnderscoreids

    @property
    def id(self):
        """Gets the id of this Color.  # noqa: E501


        :return: The id of this Color.  # noqa: E501
        :rtype: Integer
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Color.


        :param id: The id of this Color.  # noqa: E501
        :type: Integer
        """

        self._id = id

    @property
    def isUnderscoretrans(self):
        """Gets the isUnderscoretrans of this Color.  # noqa: E501


        :return: The isUnderscoretrans of this Color.  # noqa: E501
        :rtype: Boolean
        """
        return self._isUnderscoretrans

    @isUnderscoretrans.setter
    def isUnderscoretrans(self, isUnderscoretrans):
        """Sets the isUnderscoretrans of this Color.


        :param isUnderscoretrans: The isUnderscoretrans of this Color.  # noqa: E501
        :type: Boolean
        """

        self._isUnderscoretrans = isUnderscoretrans

    @property
    def name(self):
        """Gets the name of this Color.  # noqa: E501


        :return: The name of this Color.  # noqa: E501
        :rtype: String
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Color.


        :param name: The name of this Color.  # noqa: E501
        :type: String
        """

        self._name = name

    @property
    def rgb(self):
        """Gets the rgb of this Color.  # noqa: E501


        :return: The rgb of this Color.  # noqa: E501
        :rtype: String
        """
        return self._rgb

    @rgb.setter
    def rgb(self, rgb):
        """Sets the rgb of this Color.


        :param rgb: The rgb of this Color.  # noqa: E501
        :type: String
        """

        self._rgb = rgb

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
        if not isinstance(other, Color):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
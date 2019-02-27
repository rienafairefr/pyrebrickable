# coding: utf-8

import pprint
import re  # noqa: F401

import six


class ExternalColorIds(object):
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
        'BrickLink': 'ExternalColorId',
        'BrickOwl': 'ExternalColorId',
        'LDraw': 'ExternalColorId',
        'LEGO': 'ExternalColorId',
        'Peeron': 'ExternalColorId'
    }

    attribute_map = {
        'BrickLink': 'BrickLink',
        'BrickOwl': 'BrickOwl',
        'LDraw': 'LDraw',
        'LEGO': 'LEGO',
        'Peeron': 'Peeron'
    }

    def __init__(self, BrickLink=null, BrickOwl=null, LDraw=null, LEGO=null, Peeron=null):  # noqa: E501
        """ExternalColorIds - a model defined in OpenAPI"""  # noqa: E501

        self._BrickLink = None
        self._BrickOwl = None
        self._LDraw = None
        self._LEGO = None
        self._Peeron = None
        self.discriminator = None

        if BrickLink is not None:
            self.BrickLink = BrickLink
        if BrickOwl is not None:
            self.BrickOwl = BrickOwl
        if LDraw is not None:
            self.LDraw = LDraw
        if LEGO is not None:
            self.LEGO = LEGO
        if Peeron is not None:
            self.Peeron = Peeron

    @property
    def BrickLink(self):
        """Gets the BrickLink of this ExternalColorIds.  # noqa: E501


        :return: The BrickLink of this ExternalColorIds.  # noqa: E501
        :rtype: ExternalColorId
        """
        return self._BrickLink

    @BrickLink.setter
    def BrickLink(self, BrickLink):
        """Sets the BrickLink of this ExternalColorIds.


        :param BrickLink: The BrickLink of this ExternalColorIds.  # noqa: E501
        :type: ExternalColorId
        """

        self._BrickLink = BrickLink

    @property
    def BrickOwl(self):
        """Gets the BrickOwl of this ExternalColorIds.  # noqa: E501


        :return: The BrickOwl of this ExternalColorIds.  # noqa: E501
        :rtype: ExternalColorId
        """
        return self._BrickOwl

    @BrickOwl.setter
    def BrickOwl(self, BrickOwl):
        """Sets the BrickOwl of this ExternalColorIds.


        :param BrickOwl: The BrickOwl of this ExternalColorIds.  # noqa: E501
        :type: ExternalColorId
        """

        self._BrickOwl = BrickOwl

    @property
    def LDraw(self):
        """Gets the LDraw of this ExternalColorIds.  # noqa: E501


        :return: The LDraw of this ExternalColorIds.  # noqa: E501
        :rtype: ExternalColorId
        """
        return self._LDraw

    @LDraw.setter
    def LDraw(self, LDraw):
        """Sets the LDraw of this ExternalColorIds.


        :param LDraw: The LDraw of this ExternalColorIds.  # noqa: E501
        :type: ExternalColorId
        """

        self._LDraw = LDraw

    @property
    def LEGO(self):
        """Gets the LEGO of this ExternalColorIds.  # noqa: E501


        :return: The LEGO of this ExternalColorIds.  # noqa: E501
        :rtype: ExternalColorId
        """
        return self._LEGO

    @LEGO.setter
    def LEGO(self, LEGO):
        """Sets the LEGO of this ExternalColorIds.


        :param LEGO: The LEGO of this ExternalColorIds.  # noqa: E501
        :type: ExternalColorId
        """

        self._LEGO = LEGO

    @property
    def Peeron(self):
        """Gets the Peeron of this ExternalColorIds.  # noqa: E501


        :return: The Peeron of this ExternalColorIds.  # noqa: E501
        :rtype: ExternalColorId
        """
        return self._Peeron

    @Peeron.setter
    def Peeron(self, Peeron):
        """Sets the Peeron of this ExternalColorIds.


        :param Peeron: The Peeron of this ExternalColorIds.  # noqa: E501
        :type: ExternalColorId
        """

        self._Peeron = Peeron

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
        if not isinstance(other, ExternalColorIds):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
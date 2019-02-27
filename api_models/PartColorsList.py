# coding: utf-8

import pprint
import re  # noqa: F401

import six


class PartColorsList(object):
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
        'colorUnderscoreid': 'Integer',
        'colorUnderscorename': 'String',
        'elements': 'List',
        'numUnderscoresetUnderscoreparts': 'Integer',
        'numUnderscoresets': 'Integer',
        'partUnderscoreimgUnderscoreurl': 'String'
    }

    attribute_map = {
        'colorUnderscoreid': 'color_id',
        'colorUnderscorename': 'color_name',
        'elements': 'elements',
        'numUnderscoresetUnderscoreparts': 'num_set_parts',
        'numUnderscoresets': 'num_sets',
        'partUnderscoreimgUnderscoreurl': 'part_img_url'
    }

    def __init__(self, colorUnderscoreid=null, colorUnderscorename=null, elements=null, numUnderscoresetUnderscoreparts=null, numUnderscoresets=null, partUnderscoreimgUnderscoreurl=null):  # noqa: E501
        """PartColorsList - a model defined in OpenAPI"""  # noqa: E501

        self._colorUnderscoreid = None
        self._colorUnderscorename = None
        self._elements = None
        self._numUnderscoresetUnderscoreparts = None
        self._numUnderscoresets = None
        self._partUnderscoreimgUnderscoreurl = None
        self.discriminator = None

        if colorUnderscoreid is not None:
            self.colorUnderscoreid = colorUnderscoreid
        if colorUnderscorename is not None:
            self.colorUnderscorename = colorUnderscorename
        if elements is not None:
            self.elements = elements
        if numUnderscoresetUnderscoreparts is not None:
            self.numUnderscoresetUnderscoreparts = numUnderscoresetUnderscoreparts
        if numUnderscoresets is not None:
            self.numUnderscoresets = numUnderscoresets
        if partUnderscoreimgUnderscoreurl is not None:
            self.partUnderscoreimgUnderscoreurl = partUnderscoreimgUnderscoreurl

    @property
    def colorUnderscoreid(self):
        """Gets the colorUnderscoreid of this PartColorsList.  # noqa: E501


        :return: The colorUnderscoreid of this PartColorsList.  # noqa: E501
        :rtype: Integer
        """
        return self._colorUnderscoreid

    @colorUnderscoreid.setter
    def colorUnderscoreid(self, colorUnderscoreid):
        """Sets the colorUnderscoreid of this PartColorsList.


        :param colorUnderscoreid: The colorUnderscoreid of this PartColorsList.  # noqa: E501
        :type: Integer
        """

        self._colorUnderscoreid = colorUnderscoreid

    @property
    def colorUnderscorename(self):
        """Gets the colorUnderscorename of this PartColorsList.  # noqa: E501


        :return: The colorUnderscorename of this PartColorsList.  # noqa: E501
        :rtype: String
        """
        return self._colorUnderscorename

    @colorUnderscorename.setter
    def colorUnderscorename(self, colorUnderscorename):
        """Sets the colorUnderscorename of this PartColorsList.


        :param colorUnderscorename: The colorUnderscorename of this PartColorsList.  # noqa: E501
        :type: String
        """

        self._colorUnderscorename = colorUnderscorename

    @property
    def elements(self):
        """Gets the elements of this PartColorsList.  # noqa: E501


        :return: The elements of this PartColorsList.  # noqa: E501
        :rtype: List
        """
        return self._elements

    @elements.setter
    def elements(self, elements):
        """Sets the elements of this PartColorsList.


        :param elements: The elements of this PartColorsList.  # noqa: E501
        :type: List
        """

        self._elements = elements

    @property
    def numUnderscoresetUnderscoreparts(self):
        """Gets the numUnderscoresetUnderscoreparts of this PartColorsList.  # noqa: E501


        :return: The numUnderscoresetUnderscoreparts of this PartColorsList.  # noqa: E501
        :rtype: Integer
        """
        return self._numUnderscoresetUnderscoreparts

    @numUnderscoresetUnderscoreparts.setter
    def numUnderscoresetUnderscoreparts(self, numUnderscoresetUnderscoreparts):
        """Sets the numUnderscoresetUnderscoreparts of this PartColorsList.


        :param numUnderscoresetUnderscoreparts: The numUnderscoresetUnderscoreparts of this PartColorsList.  # noqa: E501
        :type: Integer
        """

        self._numUnderscoresetUnderscoreparts = numUnderscoresetUnderscoreparts

    @property
    def numUnderscoresets(self):
        """Gets the numUnderscoresets of this PartColorsList.  # noqa: E501


        :return: The numUnderscoresets of this PartColorsList.  # noqa: E501
        :rtype: Integer
        """
        return self._numUnderscoresets

    @numUnderscoresets.setter
    def numUnderscoresets(self, numUnderscoresets):
        """Sets the numUnderscoresets of this PartColorsList.


        :param numUnderscoresets: The numUnderscoresets of this PartColorsList.  # noqa: E501
        :type: Integer
        """

        self._numUnderscoresets = numUnderscoresets

    @property
    def partUnderscoreimgUnderscoreurl(self):
        """Gets the partUnderscoreimgUnderscoreurl of this PartColorsList.  # noqa: E501


        :return: The partUnderscoreimgUnderscoreurl of this PartColorsList.  # noqa: E501
        :rtype: String
        """
        return self._partUnderscoreimgUnderscoreurl

    @partUnderscoreimgUnderscoreurl.setter
    def partUnderscoreimgUnderscoreurl(self, partUnderscoreimgUnderscoreurl):
        """Sets the partUnderscoreimgUnderscoreurl of this PartColorsList.


        :param partUnderscoreimgUnderscoreurl: The partUnderscoreimgUnderscoreurl of this PartColorsList.  # noqa: E501
        :type: String
        """

        self._partUnderscoreimgUnderscoreurl = partUnderscoreimgUnderscoreurl

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
        if not isinstance(other, PartColorsList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
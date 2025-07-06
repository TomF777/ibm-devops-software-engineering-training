import connexion
import six

from swagger_server import util


def items_get():  # noqa: E501
    """Returns a list of items

    Returns items  # noqa: E501


    :rtype: None
    """
    items = {
        "item01" : "AABW23",
        "item02" : "EIRJ23",
        "item03" : "asdE#3"
    }

    return items

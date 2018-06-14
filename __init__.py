# -*- coding: utf-8 -*-
"""
/***************************************************************************
 test_plug
                                 A QGIS plugin
 test_plug
                             -------------------
        begin                : 2018-06-14
        copyright            : (C) 2018 by boulecafe
        email                : info@boulecafe.de
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load test_plug class from file test_plug.

    :param iface: A QGIS interface instance.
    :type iface: QgisInterface
    """
    #
    from .test_plug import test_plug
    return test_plug(iface)

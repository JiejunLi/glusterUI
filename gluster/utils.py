#!/usr/bin/env python
# encoding=utf-8

# Copyright (C) 2015 Alljun Lee, CT
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA
#
# Refer to the README and COPYING files for full details of the license


def new_attr(obj, attr_name, attr_value):
    """ 
    create a attribute 'attr_name' with value 'attr_value'
    to instance then return the attr_value
    """
    obj.__setattr__(attr_name, attr_value)
    return obj.__getattribute__(attr_name)
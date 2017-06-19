#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Tang
import math
def area(radius):
    """ Return the area of a circle with 
	the given radius.
	for example:
	>>> area(5.5)
	95.0331
	"""
    return math.pi*radius**2

print(area(5.5))
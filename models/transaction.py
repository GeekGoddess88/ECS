#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 12:20:45 2026

@author: user
"""


class Transaction:
    def __init__(self, employee, equipment, returned):
        self.employee = employee
        self.equipment = equipment
        self.returned = False

    def mark_returned(self):
        self.returned = True

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 12:20:45 2026

@author: user
"""


class Equipment:
    def __init__(self, item_id, name, required_skill):
        self.item_id = item_id
        self.name = name
        self.required_skill = required_skill
        self.available = True
        


    def mark_checked_out(self):
        self.available = False

    def mark_returned(self):
        self.available = True

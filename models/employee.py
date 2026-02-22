#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 12:20:45 2026

@author: user
"""


class Employee:
    def __init__(self, employee_id, name, skill, role):
        self.employee_id = employee_id
        self.name = name
        self.skill = skill
        self.role = role

    def request_checkout(self, equipment, inventory_system):
        inventory_system.process_checkout(self, equipment)

    def request_return(self, equipment, inventory_system):
        inventory_system.process_return(self, equipment)

    def view_transactions(self, report):
        report = report.generate_employee_report()

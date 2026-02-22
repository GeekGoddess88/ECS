#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 12:20:45 2026

@author: user
"""
from models.employee import Employee


class Manager(Employee):
    def __init__(self, employee_id, name, skill, role):
        super().__init__(employee_id, name, skill, role)

    def exception_report(self, report):
        report.generate_exception_report()

    def usage_analysis(self, report):
        report.generate_usage_analysis()

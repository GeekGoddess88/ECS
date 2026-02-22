#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 12:20:45 2026

@author: user
"""


class Report:
    def __init__(self, transactions):
        self.transactions = transactions

    def generate_employee_report(self, employee):
        print("Employee Report:")
        print("No data at this time.")
        report_lines = []
        for t in self.transactions:
            if t.employee == employee:
                report_lines.append(f"{t.equipment.name}")
                print(f"{t.equipment.name} returned: {t.returned}.")
        return "\n".join(report_lines)

    def generate_exception_report(self):
        # report_lines = []
        # for t in self.transacitons:
            # if t.employee.employee_id == employee.employee_id:
                #report_lines.append(f"{t.employee.name}")
        # return "\n".join(report_lines)
        print("Exception Report:")
        print("No outstanding transactions.")
        # 
            # if not t.returned:
                # print(f"Outstanding: {employee.name} has {t.equipment.name}.")

    def generate_usage_analysis(self):
        print("Equipment Usage Analysis:")
        usage_count = {}
        for t in self.transactions:
            name = t.equipment.name
            usage_count[name] = usage_count.get(name, 0) + 1

        for equipment, count in usage_count.items():
            print(f"{equipment} has been used: {count} times.")

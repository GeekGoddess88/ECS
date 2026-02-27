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
        #print("No data at this time.")
        print("Employee Report:")
        print("Report Generated.")
        results = []
        for t in self.transactions:
            if t.employee == employee:
                results.append(f"{t.equipment.name}")
                print(f"{t.employee.name} returned: {t.returned}.")
        return "\n".join(results)
        

    def generate_exception_report(self):
        print("Exception Report:")
        print("Report Generated.")
        report_lines = []
        for t in self.transactions:
            report_lines.append(f"{t.employee.name}")
            return "\n".join(report_lines)
        
        # 
            # if not t.returned:
                # print(f"Outstanding: {employee.name} has {t.equipment.name}.")

    def generate_usage_analysis(self):
        print("Equipment Usage Analysis:")
        print("Report Generated.")
        usage_count = {}
        for t in self.transactions:
            name = t.equipment.name
            usage_count[name] = usage_count.get(name, 0) + 1
        for equipment, count in usage_count.items():
            print(f"{name} has been used: {count} times.")
        
        

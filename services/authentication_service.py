#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 12:20:45 2026

@author: user
"""
from models.skill import Skill
from models.employee import Employee
from models.manager import Manager


class AuthenticationService:
    def __init__(self, filename):
        self.employees = self.load_employees(filename)

    def load_employees(self, filename):
        employees = []
        with open(filename, "r") as file:
            for line in file:
                employee_id, name, skill_class, role = line.strip().split(",")
                skill = Skill(skill_class)

                if role == "Manager":
                    employee = Manager(int(employee_id), name, skill, role)
                else:
                    employee = Employee(int(employee_id), name, skill, role)

                employees.append(employee)

        return employees

    def login(self, employee_id):
        for emp in self.employees:
            if emp.employee_id == int(employee_id):
                print("Authentication successful.")
                return emp

        print("Authentication failed.")
        return None

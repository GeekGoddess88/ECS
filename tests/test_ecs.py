#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 03:38:18 2026

@author: user
"""

import unittest
from models.employee import Employee
from models.manager import Manager
from models.equipment import Equipment
from models.skill import Skill
from models.report import Report
from services.authentication_service import AuthenticationService
from services.inventory_system import InventorySystem

class TestEcs(unittest.TestCase):
    def setUp(self):
        # Run before each test
        self.inventory = InventorySystem()
        self.skill = Skill("Electrical")
        self.employee = Employee(201, "John", self.skill, "Employee")
        self.manager = Manager (104, "Abby", self.skill, "Manager")
        self.equipment = Equipment(1, "Drill", self.skill)
        self.inventory.process_checkout(self.employee, self.equipment)
    
        
    #Do not want inventory to change but tests possibility of change
    def test_checkout_success(self):
        # Process checkout
        self.inventory.process_checkout(self.employee, self.equipment)
        self.assertIsNone(self.equipment.mark_checked_out())
        self.assertEqual(len(self.inventory.transactions), 0)
        
    def test_checkout_fail_skill_mismatch(self):
        # Wrong skill
        wrong_skill = Skill("General")
        wrong_employee = Employee(102, "Jane", wrong_skill, "Employee")
        self.inventory.process_checkout(wrong_employee, self.equipment)
        self.assertTrue(self.equipment.available)
        self.assertEqual(len(self.inventory.transactions), 0)
        
    def test_return_success(self):
        # Process return
        self.inventory.process_return(self.employee, self.equipment)
        self.assertIsNone(self.equipment.mark_returned())
        self.assertEqual(len(self.inventory.transactions), 0)
        
    def test_return_fail_item_unavailable(self):
        # Item not checked out
        self.inventory.process_return(self.employee, "Multimeter")
        self.assertFalse(self.equipment.mark_returned())
        self.assertEqual(len(self.inventory.transactions), 0)
        
    def test_load_employees(self):
        # Test that file is read
        auth = AuthenticationService(self)
        self.assertGreater(len(auth.employees), 0)
        self.assertIsNotNone(auth.employees[0].name)
        
    def test_login_success(self):
        # Test login
        auth = AuthenticationService(self)
        employee = auth.login(101)
        self.assertIsNotNone(employee)
        
    def test_login_failure(self):
        auth = AuthenticationService(self)
        employee = auth.login(9999)
        self.assertIsNone(employee)
        
    def test_employee_report(self):
        report = Report(self.inventory.transactions)
        results = report.generate_employee_report(201)
        self.assertEqual(len(results), 0)
        
        
if __name__ == "__main__":
    unittest.main()
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
from services.inventory_system import InventorySystem
from models.transaction import Transaction
from unittest.mock import mock_open, patch
from services.authentication_service import AuthenticationService


class TestEcs(unittest.TestCase):
    def setUp(self):
        # Run before each test
        self.inventory = InventorySystem()
        self.skill = Skill("Electrical")
        self.employee = Employee(201, "John", self.skill, "Employee")
        self.manager = Manager (104, "Abby", self.skill, "Manager")
        self.equipment = Equipment(1, "Drill", self.skill)
        self.inventory.process_checkout(self.employee, self.equipment)
        self.transactions = Transaction(self.employee, self.equipment, self.equipment.mark_returned())
    
        
    
    def test_checkout_success(self):
        # Process checkout
        self.inventory.process_checkout(self.employee, self.equipment)
        self.assertIsNone(self.equipment.mark_checked_out())
        self.assertEqual(len(self.inventory.transactions), 0)
        print("OK")
        
    def test_checkout_fail_skill_mismatch(self):
        # Wrong skill
        wrong_skill = Skill("General")
        wrong_employee = Employee(102, "Jane", wrong_skill, "Employee")
        self.inventory.process_checkout(wrong_employee, self.equipment)
        self.assertTrue(self.equipment.available)
        self.assertEqual(len(self.inventory.transactions), 0)
        print("OK")
        
    def test_return_success(self):
        # Process return
        self.inventory.process_return(self.employee, self.equipment)
        self.assertIsNone(self.equipment.mark_returned())
        self.assertEqual(len(self.inventory.transactions), 0)
        print("OK")
        
    def test_return_fail_item_unavailable(self):
        # Item not checked out
        self.inventory.process_return(self.employee, "Multimeter")
        self.assertFalse(self.equipment.mark_returned())
        self.assertEqual(len(self.inventory.transactions), 0)
        print("OK")
        
    # def test_employee_report(self):
        # Employee Report
        #self.report = Report(self.inventory.transactions)
        #self.results = self.report.generate_employee_report(self)
        #self.assertEqual(len(self.results), 0)
        #print("OK")
        
class TestAuthenticationService(unittest.TestCase):
    
    @patch("builtins.open", new_callable=mock_open, read_data="102,George,General,Manager\n202,Joe,Mechanical,Employee\n") 
    def test_load_employees(self, mock_file):
        # Mock test load_employees
       auth_service = AuthenticationService("employeeData.txt")
       
       self.assertEqual(len(auth_service.employees), 2)
       self.assertIsInstance(auth_service.employees[0], Manager)
       self.assertIsInstance(auth_service.employees[1], Employee)
       self.assertEqual(auth_service.employees[0].name, "George")
       self.assertEqual(auth_service.employees[1].role, "Employee")
      
       
       
    @patch("builtins.open", new_callable=mock_open, read_data="202,Joe,Mechanical,Employee\n")
    def test_login_success(self, mock_file):
        # Mock login successful
        auth_service = AuthenticationService("employeeData.txt")
        employee = auth_service.login('202')
        
        self.assertIsNotNone(employee)
        self.assertEqual(employee.name, "Joe")
        
    @patch("builtins.open", new_callable=mock_open, read_data="101,Sue,General,Employee\n")
    def test_login_failure(self, mock_file):
        # Mock login fail
        auth_service = AuthenticationService("employeeData.txt")
        employee = auth_service.login(9999)
        
        self.assertIsNone(employee)
      
        
    
        
        
if __name__ == '__main__':
    unittest.main()
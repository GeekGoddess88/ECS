#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 12:27:26 2026

@author: user
"""
from models.transaction import Transaction

class InventorySystem:
    def __init__(self):
        self.transactions = []         
              
    def process_checkout(self, employee, equipment):
        if equipment.available and employee.skill.skill_class == equipment.required_skill:
            equipment.mark_checked_out()
            transaction = Transaction(employee, equipment)
            self.transactions.append(transaction)
            employee.view_transactions.append(transaction)
            print(f"{employee.name} successfully checked out {equipment.name}.")
            return
        else:
            #print("Checkout failed: Skill mismatch or equipment unavailable.")
            return

    def process_return(self, employee, equipment):
        for t in self.transactions:
            if t.employee == employee and t.equipment == equipment and not t.returned:
                t.mark_returned()
                equipment.mark_returned()
                print(f"{employee.name} returned {equipment.name}.")
                return

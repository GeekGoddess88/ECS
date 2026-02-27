from services.inventory_system import InventorySystem
from services.authentication_service import AuthenticationService
from models.skill import Skill
from models.report import Report
from models.equipment import Equipment
from models.transaction import Transaction
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 12:38:07 2026

@author: user
"""


def main():
    # Load employees
    auth_service = AuthenticationService("employeeData.txt")
    inventory_system = InventorySystem()
    report = Report(inventory_system.transactions)
    # Login
    employee = auth_service.login(input("Enter your Employee ID: "))
    if not employee:
        print("Login failed.")
        return
    print(f"Welcome {employee.name} from {employee.skill.skill_class}.")
    # Create inventory system
    if employee.role == "Manager":
        menu_choice = input(
            "Enter 1 to print exception report\nEnter 2 to print usage analytics report: ")
        if menu_choice == "1":
            report.generate_exception_report()
        elif menu_choice == "2":
            report.generate_usage_analysis()
        else:
            print("Incorrect entry.")
    elif employee.role == "Employee":
        menu_choice = input(
            "Enter 1 to print employee report\nEnter 2 to checkout equipment\nEnter 3 to return equipment: ")
        if menu_choice == "1":
            report.generate_employee_report(employee)
        elif menu_choice == "2":
            if employee.skill.skill_class == "Electrical":
                available_equipment = (
                    [Equipment(1, "Drill", Skill("Electrical"))])
            elif employee.skill.skill_class == "General":
                available_equipment = (
                    [Equipment(2, "Hammer", Skill("General"))])
            elif employee.skill.skill_class == "Mechanical":
                available_equipment = (
                    [Equipment(3, "Wrench", Skill("Mechanical"))])

            for i, eq in enumerate(available_equipment):
                print(f"{i + 1}. {eq.name}.")

            choice = int(input("Select equipment to checkout: ")) - 1 
            selected_equipment = available_equipment[choice]
            print("Item checked out.")
            inventory_system.process_checkout(employee, selected_equipment)
        elif menu_choice == "3":
            inventory_system.process_return(employee, "Screwdriver")
            print("Item returned.")
        else:
            print("Invalid entry.")
    else:
        print("Employee not found. Please try again.")



if __name__ == "__main__":
    main()

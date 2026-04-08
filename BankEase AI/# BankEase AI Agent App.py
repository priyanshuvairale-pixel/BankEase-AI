# BankEase AI Agent App
# Author: Priyanshu
# Purpose: Book bank appointments and handle small banking services

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

class BankEaseAgent:
    def __init__(self, user_name):
        self.user_name = user_name
        self.appointments = []
        self.requests = []

    def book_appointment(self, branch, date, time, mode="Physical"):
        appointment = {
            "branch": branch,
            "date": date,
            "time": time,
            "mode": mode,
            "status": "Confirmed"
        }
        self.appointments.append(appointment)
        return f"✅ {mode} appointment booked at {branch} on {date} at {time}."

    def apply_debit_card(self, account_number):
        request = {
            "service": "Debit Card Application",
            "account_number": account_number,
            "status": "Submitted",
            "tracking_id": f"DC{len(self.requests)+1:04d}"
        }
        self.requests.append(request)
        return f"💳 Debit card request submitted. Tracking ID: {request['tracking_id']}."

    def request_passbook(self, account_number):
        request = {
            "service": "Passbook Request",
            "account_number": account_number,
            "status": "Submitted",
            "tracking_id": f"PB{len(self.requests)+1:04d}"
        }
        self.requests.append(request)
        return f"📘 Passbook request submitted. Tracking ID: {request['tracking_id']}."

    def update_kyc(self, account_number, documents):
        request = {
            "service": "KYC Update",
            "account_number": account_number,
            "documents": documents,
            "status": "Submitted",
            "tracking_id": f"KYC{len(self.requests)+1:04d}"
        }
        self.requests.append(request)
        return f"📝 KYC update submitted. Tracking ID: {request['tracking_id']}."

    def view_status(self):
        if not self.requests:
            return "No active service requests."
        status_list = [f"{req['service']} - {req['status']} (ID: {req['tracking_id']})" for req in self.requests]
        return "\n".join(status_list)


def main():
    print("=== Welcome to BankEase AI Agent ===")
    user_name = input("Enter your name: ")
    agent = BankEaseAgent(user_name)

    while True:
        print("\nChoose an option:")
        print("1. Book Physical Appointment")
        print("2. Book Online Appointment")
        print("3. Apply for Debit Card")
        print("4. Request Passbook")
        print("5. Update KYC")
        print("6. View Service Status")
        print("7. Exit")

        choice = input("Enter choice (1-7): ")

        if choice == "1":
            branch = input("Enter branch name: ")
            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time (e.g., 11:00 AM): ")
            print(agent.book_appointment(branch, date, time, mode="Physical"))

        elif choice == "2":
            branch = input("Enter branch name (for online service center): ")
            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time (e.g., 11:00 AM): ")
            print(agent.book_appointment(branch, date, time, mode="Online"))

        elif choice == "3":
            acc = input("Enter account number: ")
            print(agent.apply_debit_card(acc))

        elif choice == "4":
            acc = input("Enter account number: ")
            print(agent.request_passbook(acc))

        elif choice == "5":
            acc = input("Enter account number: ")
            docs = input("Enter documents (comma separated): ").split(",")
            print(agent.update_kyc(acc, docs))

        elif choice == "6":
            print("\nService Status:\n", agent.view_status())

        elif choice == "7":
            print("Thank you for using BankEase AI Agent. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
    
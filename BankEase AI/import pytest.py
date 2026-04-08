import pytest
from bankease_agent import BankEaseAgent

def test_book_physical_appointment():
    agent = BankEaseAgent("Priyanshu")
    result = agent.book_appointment("Main Branch", "2026-04-10", "11:00 AM", mode="Physical")
    assert "Physical appointment booked" in result
    assert agent.appointments[0]["mode"] == "Physical"

def test_book_online_appointment():
    agent = BankEaseAgent("Priyanshu")
    result = agent.book_appointment("Online Service Center", "2026-04-11", "02:00 PM", mode="Online")
    assert "Online appointment booked" in result
    assert agent.appointments[0]["mode"] == "Online"

def test_apply_debit_card():
    agent = BankEaseAgent("Priyanshu")
    result = agent.apply_debit_card("123456")
    assert "Debit card request submitted" in result
    assert agent.requests[0]["service"] == "Debit Card Application"

def test_request_passbook():
    agent = BankEaseAgent("Priyanshu")
    result = agent.request_passbook("123456")
    assert "Passbook request submitted" in result
    assert agent.requests[0]["service"] == "Passbook Request"

def test_update_kyc():
    agent = BankEaseAgent("Priyanshu")
    result = agent.update_kyc("123456", ["PAN", "Aadhar"])
    assert "KYC update submitted" in result
    assert agent.requests[0]["service"] == "KYC Update"

def test_view_status_empty():
    agent = BankEaseAgent("Priyanshu")
    assert agent.view_status() == "No active service requests."
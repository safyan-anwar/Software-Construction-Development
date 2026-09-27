import unittest
def is_bonus_eligible(employee):
    is_active = employee["active"]
    has_required_service = employee["months_employed"] >= 12
    has_good_performance = employee["performance_rating"] >= 4
    has_clean_record = not employee["disciplinary_action"]
    has_good_attendance = employee["attendance_percentage"] >= 90
    return(
        is_active
        and has_required_service
        and has_good_performance
        and has_clean_record
        and has_good_attendance
    )
def test_normal_case():
    employee = {
        "active": True,
        "months_employed": 18,
        "performance_rating": 5,
        "disciplinary_action": False,
        "attendance_percentage": 95
    }
    assert is_bonus_eligible(employee) == True
def test_boundary_case():
    employee = {
        "active": True,
        "months_employed": 12,
        "performance_rating": 4,
        "disciplinary_action": False,
        "attendance_percentage": 90
    }
    assert is_bonus_eligible(employee) == True
def test_inactive_employee():
    employee = {
        "active": False,
        "months_employed": 18,
        "performance_rating": 5,
        "disciplinary_action": False,
        "attendance_percentage": 95
    }
    assert is_bonus_eligible(employee) == False
def test_less_than_12_months():
    employee = {
        "active": True,
        "months_employed": 11,
        "performance_rating": 5,
        "disciplinary_action": False,
        "attendance_percentage": 95
    }
    assert is_bonus_eligible(employee) == False
def test_low_performance():
    employee ={
        "active": True,
        "months_employed": 18,
        "performance_rating": 3,
        "disciplinary_action": False,
        "attendance_percentage": 95
    }

    assert is_bonus_eligible(employee) == False
def test_disciplinary_action():
    employee = {
        "active": True,
        "months_employed": 18,
        "performance_rating": 5,
        "disciplinary_action": True,
        "attendance_percentage": 95
    }
    assert is_bonus_eligible(employee) == False
def test_low_attendance():
    employee = {
        "active": True,
        "months_employed": 18,
        "performance_rating": 5,
        "disciplinary_action": False,
        "attendance_percentage": 89
    }

    assert is_bonus_eligible(employee) == False
tests =[
    test_normal_case,
    test_boundary_case,
    test_inactive_employee,
    test_less_than_12_months,
    test_low_performance,
    test_disciplinary_action,
    test_low_attendance
]
for test in tests:
    test()
print('all tests has passed...')
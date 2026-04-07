from employee import EmployeeApi


base_url = "http://5.101.50.27:8000"

def test_create_employee():
    employee_json = {
            "first_name": "Who",
            "last_name": "Ami",
            "middle_name": "Nona",
            "company_id": 29,
            "email": "user@example.com",
            "phone": "+156",
            "birthdate": "2026-03-18",
            "is_active": True
    }

    api = EmployeeApi(base_url)  # Инициализация API-клиента
    # 1. Получаем текущий список компаний
    emp_before = api.create_employ(data_json=employee_json)

    print(emp_before)

    # assert
def test_get_employee():
    api = EmployeeApi(base_url)
    employee_info = api.get_employee_by_id(1)

    assert employee_info["first_name"] == "Иван"
    # 2. Создаём новую компанию

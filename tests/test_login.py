import json
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.config import BASE_URL
from utils.helpers import screenshot_path

with open("data/users.json") as file:
    users = json.load(file)

# @pystest.mark.smoke
@pytest.mark.parametrize("user_key, expected_success", [
    ("valid", True),
    ("locked", False),
    ("invalid", False)
])
def test_login_variantes(page, user_key,expected_success):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    try:
        login.goto(BASE_URL)
        creds = users[user_key]
        login.login(creds["username"], creds["password"])

        if expected_success:
            assert inventory.is_loaded(), "No se cargó la lista de productos"
        else:
            assert not inventory.is_loaded(), "No debería loguear"
            assert login.error_message() != "", "Se esperaba mensaje de error"
    except Exception:
        page.screenshot(path=screenshot_path(f"login_{user_key}_fail"))
        raise
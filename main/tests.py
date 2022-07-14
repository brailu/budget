from django.core.exceptions import ValidationError
from django.test import TestCase
from django.contrib.auth.models import User
from main.models import (
    Category,
    Account
)
from main.forms import (
    AccountUpdateForm
)

class CategoryTest(TestCase):
   
    def test_if_name_category_is_uppercase(self):
        test_category = Category(name="test")
        test_category.full_clean()
        self.assertEqual(test_category.name, "TEST")


class AccountTest(TestCase):

    def test_if_account_name_is_uppercase(self):
        test_account = Account(name="test", balance=100.0, type='checking')
        test_account.full_clean()
        self.assertEqual(test_account.name, "TEST")


class AccountUpdateFormTest(TestCase):

    def test_if_type_and_balance_are_disabled(self):
        test_account_update_form = AccountUpdateForm()
        self.assertNotIn('type', test_account_update_form.fields)
        self.assertNotIn('balance', test_account_update_form.fields)
    

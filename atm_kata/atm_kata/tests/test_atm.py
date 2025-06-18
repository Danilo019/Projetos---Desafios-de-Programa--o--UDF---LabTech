import unittest

class TestATM(unittest.TestCase):
    def test_withdraw_simple_example(self):
        from atm.atm import ATM
        atm = ATM()
        result = atm.withdraw(30)
        expected_output = [
            "1 billete de 20",
            "1 billete de 10"
        ]
        self.assertEqual(result, expected_output)

    def test_withdraw_iteration_2_example_1725(self):
        from atm.atm import ATM
        atm = ATM()
        result = atm.withdraw(1725)
        expected_output = [
            "2 billetes de 500",
            "3 billetes de 200",
            "1 billete de 100",
            "1 billete de 20",
            "1 billete de 5"
        ]
        self.assertEqual(result, expected_output)

    def test_withdraw_insufficient_funds(self):
        from atm.atm import ATM
        atm = ATM()
        atm.denominations_available = {500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}
        with self.assertRaisesRegex(ValueError, "El cajero automático no dispone de dinero suficiente, por favor acuda al cajero automático más cercano"):
            atm.withdraw(1000)

    def test_initial_atm_state_and_withdrawal(self):

        from atm.atm import ATM
        atm = ATM()
        result = atm.withdraw(1725)
        expected_output = [
            "2 billetes de 500",
            "3 billetes de 200",
            "1 billete de 100",
            "1 billete de 20",
            "1 billete de 5"
        ]
        self.assertEqual(result, expected_output)
        expected_denominations_after_withdrawal = {
            500: 0,
            200: 0,
            100: 4,
            50: 12,
            20: 19,
            10: 50,
            5: 99,
            2: 250,
            1: 500
        }
        self.assertEqual(atm.denominations_available, expected_denominations_after_withdrawal)

    def test_another_withdrawal_after_first(self):
        from atm.atm import ATM
        atm = ATM()
        atm.withdraw(1725)

        result = atm.withdraw(1825)
        expected_output = [
            "4 billetes de 100",
            "12 billetes de 50",
            "19 billetes de 20",
            "44 billetes de 10",
            "1 billete de 5"
        ]
        self.assertEqual(result, expected_output)
        expected_denominations_after_second_withdrawal = {
            500: 0,
            200: 0,
            100: 0,
            50: 0,
            20: 0,
            10: 6,
            5: 98,
            2: 250,
            1: 500
        }
        self.assertEqual(atm.denominations_available, expected_denominations_after_second_withdrawal)



import unittest
from decimal import Decimal
# Assuming a Python wrapper 'legacy_bridge' allows calling the COBOL shared library
# or a modernized microservice endpoint.
from legacy_bridge import calculate_payroll 

class TestPayrollCalculation(unittest.TestCase):

    def test_basic_salary_no_tax(self):
        """
        Test Case 1: Low income below tax threshold.
        Input: Salary 1500.00, 0 Dependents.
        Expected: Tax 0.00.
        """
        result = calculate_payroll(gross_salary=1500.00, dependents=0)
        self.assertEqual(result['tax_amt'], Decimal('0.00'))
        self.assertEqual(result['return_code'], 0)

    def test_standard_tax_bracket(self):
        """
        Test Case 2: Middle income bracket (e.g., 15% tax).
        Input: Salary 5000.00, 0 Dependents.
        Expected: Calculated tax should match legacy logic hardcoded values.
        """
        result = calculate_payroll(gross_salary=5000.00, dependents=0)
        # Assuming 15% rate minus deductible base
        expected_tax = (Decimal('5000.00') * Decimal('0.15')) - Decimal('350.00')
        self.assertEqual(result['tax_amt'], expected_tax)

    def test_dependent_deduction(self):
        """
        Test Case 3: Verify logic for dependent deductions.
        Input: Salary 5000.00, 2 Dependents.
        """
        result_no_dep = calculate_payroll(gross_salary=5000.00, dependents=0)
        result_with_dep = calculate_payroll(gross_salary=5000.00, dependents=2)
        
        # Tax should be lower with dependents
        self.assertTrue(result_with_dep['tax_amt'] < result_no_dep['tax_amt'])

    def test_invalid_negative_salary(self):
        """
        Test Case 4: Validation logic for negative input.
        Input: Salary -100.00.
        Expected: Error Code 99.
        """
        result = calculate_payroll(gross_salary=-100.00, dependents=0)
        self.assertEqual(result['return_code'], 99)

    def test_y2k_date_windowing_risk(self):
        """
        Test Case 5: Simulating the 'Year 50' pivot risk identified in List 3.
        This test checks if a hire date of '51' is interpreted as 1951, not 2051.
        """
        # This function tests the utils module separately
        from legacy_bridge import convert_date_yy_to_yyyy
        
        # '51' should satisfy logic < 50 check? No, logic was > 50 = 19xx
        year_1951 = convert_date_yy_to_yyyy('510101') 
        self.assertEqual(year_1951[:4], '1951')
        
        # '49' should be 2049
        year_2049 = convert_date_yy_to_yyyy('490101')
        self.assertEqual(year_2049[:4], '2049')

if __name__ == '__main__':
    unittest.main()

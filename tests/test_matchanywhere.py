import unittest
import pandas as pd
from IndicPy import RuleEngine, MatchAnyWhere, run_indicators

class TestIndicators(unittest.TestCase):
    def setUp(self):
        """
        Configuración inicial para los tests.
        Crea el dataframe y el RuleEngine.
        """
        self.hosp_dataframe = pd.DataFrame({
            'episode_id': [1, 2, 3],
            'age': [45, 60, 32],
            'sex': ["M", "F", "M"],
            'diagnosis1': ["F10.10", "I20", "I60"],
            'diagnosis2': ["E11", "J45", "I25"],
            'diagnosis3': ["I60", "K35", "F10.120"],
            'present_on_admission_d1': ["Yes", "No", "No"],
            'present_on_admission_d2': ["No", "Yes", "No"],
            'present_on_admission_d3': ["No", "Yes", "Yes"]
        })
        self.reng = RuleEngine(self.hosp_dataframe, "episode_id",)

    def test_matchanywhere_no_regex(self):
        """
        Test para MatchAnyWhere con regex_prefix_search=False.
        """
        target_columns = ['diagnosis1', 'diagnosis2', 'diagnosis3']
        filter_columns = ['present_on_admission_d1', 'present_on_admission_d2', 'present_on_admission_d3']
        lookup_values = ['Yes']
        definition_codes = ['F10.10', 'I60']

        scenario1 = MatchAnyWhere(
            self.reng,
            "scenario1",
            target_columns,
            definition_codes,
            filter_columns=filter_columns,
            lookup_values=lookup_values
        )


        """
        Test MatchAnyWhere with regex_prefix_search=True
        """
        target_columns = ['diagnosis1', 'diagnosis2', 'diagnosis3']
        filter_columns = ['present_on_admission_d1', 'present_on_admission_d2', 'present_on_admission_d3']
        lookup_values = ['Yes']
        definition_codes = ['F10.1', 'I']

        scenario2 = MatchAnyWhere(
            self.reng,
            "scenario2",
            target_columns,
            definition_codes,
            filter_columns=filter_columns,
            lookup_values=lookup_values,
            regex_prefix_search=True
        )

        list_scenarios = [scenario1,scenario2]
        result = run_indicators(self.reng, list_scenarios, append_results=False)
        result_scenario1 = result[['episode_id', 'scenario1']]
        result_scenario2 = result[['episode_id', 'scenario2']]
        expected_result1 = pd.DataFrame({
            'episode_id': [1, 3],
            'scenario1': [True, False]
        })
        expected_result2 = pd.DataFrame({
            'episode_id': [1, 3],
            'scenario2': [True, True]
        })

        pd.testing.assert_frame_equal(expected_result1, result_scenario1)
        pd.testing.assert_frame_equal(expected_result2, result_scenario2)


if __name__ == "__main__":
    unittest.main()

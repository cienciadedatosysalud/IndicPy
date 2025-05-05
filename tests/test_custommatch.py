import unittest
import pandas as pd
from indicpy4health import RuleEngine, MatchAny, CustomMatch, run_indicators


class TestIndicators(unittest.TestCase):
    def setUp(self):
        """
        Configuración inicial para los tests.
        Se crea un DataFrame simulado y un RuleEngine basado en él.
        """
        self.hosp_dataframe = pd.DataFrame({
            'episode_id': [1, 2, 3],
            'age': [45, 60, 32],
            'sex': ["M", "F", "M"],
            'diagnosis1': ["F10.10", "I20", "I60"],
            'diagnosis2': ["E11", "J45", "I25"],
            'diagnosis3': ["I60", "K35", "F10.120"],
            'present_on_admission_d1': [True, False, False],
            'present_on_admission_d2': [False, True, False],
            'present_on_admission_d3': [False, True, True]
        })
        self.reng = RuleEngine(self.hosp_dataframe, "episode_id")

    def test_indicators(self):
        """
        Test para verificar el comportamiento de MatchAny y CustomMatch.
        """
        # Configuración de escenarios
        target_columns = ['diagnosis1', 'diagnosis2', 'diagnosis3']
        definition_codes = ['I']

        # Escenario 1: MatchAny con regex_prefix_search=True
        scenario1 = MatchAny(self.reng, "scenario1", target_columns, definition_codes, regex_prefix_search=True)

        # Escenario 2: CustomMatch basado en scenario1 y filtro por sexo masculino
        scenario2 = CustomMatch("scenario2custom", "scenario1 and sex = 'M'")

        # Escenario 3: CustomMatch basado en scenario1 y filtro por sexo femenino
        scenario3 = CustomMatch("scenario3custom", "scenario1 and sex = 'F'")

        # Ejecutar los escenarios
        list_scenarios = [scenario1, scenario2, scenario3]
        result = run_indicators(self.reng, list_scenarios, append_results=False)

        # Ordenar el resultado por episode_id
        result = result.sort_values(by='episode_id').reset_index(drop=True)

        # Resultados por escenario
        result_scenario1 = result[['episode_id', 'scenario1']]
        result_scenario2 = result[['episode_id', 'scenario2custom']]
        result_scenario3 = result[['episode_id', 'scenario3custom']]

        # Resultados esperados
        expected_result1 = pd.DataFrame({
            'episode_id': [1, 2, 3],
            'scenario1': [True, True, True]
        })

        expected_result2 = pd.DataFrame({
            'episode_id': [1, 2, 3],
            'scenario2custom': [True, False, True]
        })

        expected_result3 = pd.DataFrame({
            'episode_id': [1, 2, 3],
            'scenario3custom': [False, True, False]
        })

        # Verificaciones
        pd.testing.assert_frame_equal(expected_result1, result_scenario1)
        pd.testing.assert_frame_equal(expected_result2, result_scenario2)
        pd.testing.assert_frame_equal(expected_result3, result_scenario3)


if __name__ == "__main__":
    unittest.main()

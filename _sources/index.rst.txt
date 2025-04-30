.. IndicPy documentation master file, created by
   sphinx-quickstart on Mon Apr 28 10:32:09 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

IndicPy
=====================

**IndicPy** is a Lightweight, Fast, and Intuitive Indicator Calculations Python Library for Health.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules

How to use:

.. code-block:: python

   import pandas as pd
   import IndicPy

   hosp_dataframe = pd.DataFrame({
      "episode_id": [1, 2, 3],
      "age": [45, 60, 32],
      "diagnosis1": ["F10.10", "I20", "I60"],
      "diagnosis2": ["E11", "J45", "I25"],
      "diagnosis3": ["I60", "K35", "F10.120"],
      "present_on_admission_d1": [False, False, False],
      "present_on_admission_d2": [False, True, False],
      "present_on_admission_d3": [False, True, True],
  })

  reng = RuleEngine(hosp_dataframe, "episode_id")

  target_columns = ["diagnosis2", "diagnosis3"]

  definition_codes = ["F10.10", "F10.11", "F10.120", "F10.121"]

  filter_columns = ["present_on_admission_d2", "present_on_admission_d3"]

  lookup_values = ["true"]

  alcohol_indicator_poa = MatchAnyWhere(
      reng,
      "alcohol_i_poa",
      target_columns,
      definition_codes,
      filter_columns,
      lookup_values
  )

  alcohol_i_regex_poa = MatchAnyWhere(
      reng,
      "alcohol_i_regex_poa",
      target_columns,
      ["F10"],
      filter_columns,
      lookup_values,
      regex_prefix_search=True
  )

  # Include the indicators in a list and apply them
  indicators_list = [alcohol_indicator_poa, alcohol_i_regex_poa]

  run_indicators(self.reng,
      indicators_list,
      append_results=False,
      csv_path="./results.csv"
   )


GitHub Repository
=================

You can find the source code on GitHub:

`🚀 IndicPy on GitHub <https://github.com/cienciadedatosysalud/IndicPy>`_


IndicPy for R
=============

IndicPy is also available for **R** under the name `IndicR`_, offering similar functionality for processing data.

You can find and use IndicR in its official repository:

`🚀 IndicR on GitHub <https://github.com/cienciadedatosysalud/IndicR>`_

.. _IndicR: https://cienciadedatosysalud.github.io/IndicR/





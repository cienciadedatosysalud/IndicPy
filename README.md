# IndicPy4Health

<!-- [![CRAN
status](https://www.r-pkg.org/badges/version/)](https://CRAN.R-project.org/package="package"/)-->
[![GitHub
version](https://img.shields.io/badge/GitHub-0.1.2-blue)](https://github.com/cienciadedatosysalud/IndicPy4Health)
[![Codecov test coverage](https://codecov.io/gh/cienciadedatosysalud/IndicPy4Health/graph/badge.svg)](https://app.codecov.io/gh/cienciadedatosysalud/IndicPy4Health)
[![Lifecycle:
stable](https://lifecycle.r-lib.org/articles/figures/lifecycle-stable.svg)](https://lifecycle.r-lib.org/articles/stages.html#stable/)
[![DOI](https://zenodo.org/badge/974787529.svg)](https://doi.org/10.5281/zenodo.15343177)

<!-- badges: end -->

**IndicPy4Health** is a Lightweight, Fast, and Intuitive Indicator Calculations Python Library from Health data.


## Example

``` py
import pandas as pd
from indicpy4health import RuleEngine, MatchAnyWhere, run_indicators

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

```

## IndicatorBuilder

Effortlessly generate indicator calculation script templates using 'IndicatorBuilder'. This web tool reads a CSV file, where each column represents an indicator by including its respective definition codes, and outputs a script template ready to be copied and used in R or Python. You can streamline your data analysis workflow with 'IndicatorBuilder'.
 
The use of 'IndicatorBuilder' complements the Python library [IndicPy4Health](https://cienciadedatosysalud.github.io/IndicPy4Health/#) and the R package [IndicR4Health](https://cienciadedatosysalud.github.io/IndicR4Health/), providing an easy-to-use tool scripting the definition of any indicator within your preferred programming environment.



## 📜 Disclaimer

This software is provided "as is," without any warranties of any kind, express or implied, including but not limited to warranties of merchantability, fitness for a particular purpose, and non-infringement.

In no event shall the authors, contributors, or maintainers be liable for any direct, indirect, incidental, special, exemplary, or consequential damages (including but not limited to loss of use, data, or profits), regardless of the cause and under any liability theory, whether in contract, strict liability, or tort (including negligence or any other cause), arising in any way from the use of this software, even if advised of the possibility of such damages.

The user assumes full responsibility for the use of this library, including evaluating its suitability and safety in the context of their application.

# Author: MD. SABBIR HOSEN HOOWLADER
# Website: https://sabbir28.github.io/

__author__ = "MD. SABBIR HOSEN HOOWLADER"
__author_website__ = "https://sabbir28.github.io/"
__version__ = "1.0.0"

# Minimum Python version required
__minimum_python_version__ = '3.6'

# Check if the current Python version meets the requirement
import sys

if sys.version_info < tuple(map(int, __minimum_python_version__.split('.'))):
    raise ImportError(f"This module requires Python >= {__minimum_python_version__}. Current Python version is {sys.version}.")

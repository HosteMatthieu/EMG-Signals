import sys
import subprocess

try:
	subprocess.check_call([sys.executable, "-m", "pip", "install", "nbformat"])
except subprocess.CalledProcessError as e:
	print(f"Failed to install nbformat: {e}")
	sys.exit(1)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, butter, filtfilt, iirnotch
from io import StringIO
import io
from nbformat import read
from unittest.mock import patch
from IPython.display import display
import scipy.stats as stats
import seaborn as sns
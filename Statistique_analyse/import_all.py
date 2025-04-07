import sys
import subprocess
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data_normal(notebook_files,variable_to_find):
	results={}

	for file_name in notebook_files:
		try:
			# Load the .ipynb file
			with open("../Normal_analyse/"+file_name, 'r', encoding='utf-8') as f:
				notebook = read(f, as_version=4)
			print(f"Notebook {file_name} imported successfully.")
		except FileNotFoundError:
			print(f"Error: The file '{file_name}' was not found. Please ensure it exists in the current directory.")
			continue

		# Dictionnaire pour stocker les variables
		global_vars = {}

		# Sauvegarde stdout et stderr pour masquer l'affichage
		stdout_backup = sys.stdout
		stderr_backup = sys.stderr
		sys.stdout = io.StringIO()  # Capture la sortie standard
		sys.stderr = io.StringIO()  # Capture les erreurs

		# Désactiver l'affichage interactif de Matplotlib
		plt.ioff()

		# Redéfinir `plt.show()` et `display()` pour bloquer les affichages
		with patch("matplotlib.pyplot.show"), patch("IPython.display.display"):
			# Exécuter toutes les cellules de code sans affichage
			for cell in notebook.cells:
				if cell.cell_type == "code":
					exec(cell.source, global_vars)

		# Rétablir la sortie normale
		sys.stdout = stdout_backup
		sys.stderr = stderr_backup
		plt.ion()  # Réactiver l'affichage interactif
		plt.close("all")  # Fermer toutes les figures en mémoire

		# Récupérer uniquement `average_cycle_time`
		data = global_vars.get(variable_to_find, "Variable non trouvée")
		results[file_name] = data

	return results


try:
	subprocess.check_call([sys.executable, "-m", "pip", "install", "nbformat"])
except subprocess.CalledProcessError as e:
	print(f"Failed to install nbformat: {e}")
	sys.exit(1)

import numpy as np
import pandas as pd
from scipy.signal import find_peaks, butter, filtfilt, iirnotch
from io import StringIO
import io
from nbformat import read
from unittest.mock import patch
from IPython.display import display
import scipy.stats as stats
import seaborn as sns
Analyse des Signaux EMG — Comparaison Patients / Sujets Sains

🧠 Présentation

Ce projet vise à analyser les signaux électromyographiques (EMG) enregistrés au niveau des muscles du genou, afin de distinguer des sujets sains de patients potentiellement atteints d’une pathologie articulaire ou musculaire.
Le but est de comparer les signaux EMG, d’en extraire des paramètres pertinents, d’effectuer une analyse statistique approfondie et de concevoir un modèle d’intelligence artificielle pour la détection automatique.


💡 Objectifs du Projet

Analyser les signaux EMG pour 11 sujets sains et 11 patients.
Extraire et comparer 5 paramètres clés : RMS, fréquence moyenne (MNF), fréquence médiane (MDF), fréquence de pic, et énergie.
Réaliser une analyse statistique comparative grâce au test de Mann-Whitney.
Créer un modèle de Machine Learning (SVM) capable de différencier un patient d’un sujet sain.

📁 Organisation du Projet
EMG-Signal-Analysis/
├── Analyse_Sujets_Normaux/
│   └── Analyse des 11 sujets sains
│
├── Analyse_Patients/
│   └── Analyse des 11 patients
│
├── Statistique_Analyse/
│   └── Comparaison de tous les paramètres avec Mann Whitney
│   └── Graphiques/
│       └── Histogrammes
│       └── Boxplots
│
├── Model_IA/
│   └── SVM_Model.py  # Modèle SVM pour classification patients/sujets sains│

⚙️ Fonctionnalités

Tous les codes sont commentés pour faciliter la compréhension des fonctions et méthodes utilisées.
Chaque sujet (normal ou patient) est traité selon une méthodologie identique.
Le sujet sain dispose d’un code détaillé avec explications, servant d’exemple pour les 21 autres
L’analyse statistique utilise le test de Mann-Whitney pour comparer les groupes.
Les résultats sont visualisés via des histogrammes et boxplots.
Un modèle SVM a été développé pour classifier automatiquement les signaux entre patients et sujets sains.


🚀 Technologies Utilisées

Python 🐍
Numpy, Pandas
SciPy
Matplotlib, Seaborn
Scikit-Learn
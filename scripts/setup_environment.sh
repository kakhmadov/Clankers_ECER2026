#!/bin/bash
# setup_environment.sh
# Dieses Skript richtet die Python-Umgebung für alle Teammitglieder gleich ein

echo "=== ECER2026 Python Setup ==="
echo "Team: Clankers, TGM 3. Jahrgang"

# 1. Virtuelle Python-Umgebung erstellen
echo "1. Erstelle virtuelle Umgebung..."
python3 -m venv venv

# 2. Virtuelle Umgebung aktivieren
echo "2. Aktiviere virtuelle Umgebung..."
source venv/bin/activate  # Für Linux/Mac
# Für Windows: venv\Scripts\activate

# 3. Dependencies installieren
echo "3. Installiere Abhängigkeiten..."
pip install --upgrade pip
pip install -r requirements.txt

# 4. Pre-commit hooks installieren
echo "4. Installiere Pre-commit hooks..."
pre-commit install

echo "=== Setup abgeschlossen! ==="
echo "Um die Umgebung zu aktivieren:"
echo "  source venv/bin/activate   # Linux/Mac"
echo "  venv\Scripts\activate      # Windows"

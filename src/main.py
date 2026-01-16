#!/usr/bin/env python3
"""
ECER 2026 - Team Clankers
TGM 3. Jahrgang - Robotik Wettbewerb

Hauptprogramm für Robotik-System
"""

import logging
import sys

# Logging konfigurieren
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('clankers.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

def print_banner():
    """Gibt Banner aus"""
    banner = """
    ╔══════════════════════════════════════════════╗
    ║          ECER 2026 - TEAM CLANKERS           ║
    ║          TGM 3. Jahrgang - Robotik           ║
    ║                                              ║
    ║         Python Robotik Framework             ║
    ╚══════════════════════════════════════════════╝
    """
    print(banner)

def main():
    """Hauptfunktion"""
    print_banner()
    logger.info("Starte Clankers Robotik System")
    
    # Hier kommt später eure Logik
    print("\nModi:")
    print("1. Simulation starten")
    print("2. Tests ausführen")
    print("3. Beenden")
    
    choice = input("\nAuswahl (1-3): ")
    
    if choice == "1":
        logger.info("Starte Simulationsmodus")
        start_simulation()
    elif choice == "2":
        logger.info("Starte Testmodus")
        run_tests()
    else:
        logger.info("Programm beendet")
        
    return 0

def start_simulation():
    """Startet die Simulation"""
    print("\n--- Simulationsmodus ---")
    print("Noch nicht implementiert")
    print("TODO: PyGame Simulation einbinden")
    
def run_tests():
    """Führt Tests aus"""
    print("\n--- Testmodus ---")
    
    # Einfache Funktionsprüfung
    print("1. Teste Grundfunktionen...")
    
    try:
        # Test ob Module importierbar sind
        import src.robot as robot_module
        print("✅ Robot-Module importierbar")
    except ImportError as e:
        print(f"❌ Import-Fehler: {e}")
        
    print("\n✅ Basis-Tests abgeschlossen")
    
if __name__ == "__main__":
    sys.exit(main())

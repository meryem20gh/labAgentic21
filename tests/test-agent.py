import os
import json
import pytest
from dotenv import load_dotenv
from pymongo import MongoClient

# Charge dynamiquement les variables du fichier .env local
load_dotenv()

def test_environment_variables_are_set():
    """Vérifie que les clés secrètes sont chargées dynamiquement et ne sont pas vides."""
    assert os.getenv("JIGSAWSTACK_API_KEY") is not None, "La clé JIGSAWSTACK_API_KEY n'est pas chargée !"
    assert os.getenv("DATABASE_URI") is not None, "Le lien DATABASE_URI n'est pas chargé !"

def test_workflow_json_presence():
    """Vérifie que le workflow JSON est bien présent dans le projet pour GitHub."""
    workflow_path = "j18-VOCR (1).json"
    assert os.path.exists(workflow_path), "Le fichier du workflow doit être présent dans le dépôt !"
    
    with open(workflow_path, 'r') as f:
        content = f.read()
        # Sécurité : On s'assure qu'aucune vraie clé secrète n'a été écrite en dur par erreur
        assert "jigsaw_" not in content, "ATTENTION : Une clé JigsawStack semble être écrite en dur dans le JSON !"
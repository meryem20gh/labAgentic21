# CI/CD Agents Containerization Pipeline

Ce dépôt contient l'architecture conteneurisée et sécurisée d'un système multi-agents basé sur **Agentic Fusion AI**. Ce pipeline combine l'extraction de documents complexes par vision (VOCR), l'interrogation de bases de données NoSQL (FusionDB Query) et l'exécution d'actions via des outils avancés (Composio Gmail & MCP Tools).

## 🚀 Architecture Globale

Le projet est conçu selon un flux de traitement à deux niveaux :
1. **Extraction & Structuration (VOCR)** : Analyse des documents via l'API vLLM fine-tunée de *JigsawStack*, suivie d'une conversion de type.
2. **Requêtage & Routage Métier (FusionDB)** : Analyse de l'extraction par un LLM pour générer des requêtes structurées destinées à l'instance MongoDB (*FusionDB*), avant de passer la main aux agents d'exécution dotés de capacités d'action (Gmail / Model Context Protocol).

## 📁 Structure du Projet

```text
├── .github/workflows/
│   └── agent.yml        # Pipeline de CI/CD (Tests, Linting Bandit, Docker Build)
├── src/
│   └── custom_nodes.py  # Code source et nœuds personnalisés
├── tests/
│   └── test-agent.py    # Suite de tests d'intégration (Validation JSON & SecEnv)
├── .env.example         # Modèle des variables d'environnement requises
├── .gitignore           # Exclusion des secrets et des caches locaux
├── Dockerfile           # Conteneurisation multi-étape isolée pour la production
├── j18-VOCR (1).json    # Graphe logique complet du workflow (Variables dynamiques)
├── README.md            # Guide d'introduction et d'installation
├── RUNBOOK.md           # Guide d'exploitation, de monitoring et d'observabilité
└── AGENT-CARD.md        # Spécifications de sécurité, alignement et gouvernance
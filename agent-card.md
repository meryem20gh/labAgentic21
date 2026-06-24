# Agent Card : Spécifications de Sécurité & Gouvernance

## 🔍 Identité de l'Agent
- **Nom** : Security & Observability Orchestrator Agent
- **Architecture** : Pipeline séquentiel et multi-agents intégrant JigsawStack (Vision), FusionDB (Persistance) et Composio/MCP (Actionneurs).
- **Version du Graphe** : v1.7.0 (Spécifiée dans `j18-VOCR (1).json`)

## 🎯 Mission & Alignement Systémique
L'agent est conçu exclusivement pour automatiser l'ingestion de données documentaires, exécuter des requêtes de diagnostic sur la base de données FusionDB et interagir avec des outils de communication.

> ⚠️ **Limitation stricte du périmètre** : Cet agent est un assistant de maintenance technique et de fiabilité système. Il n'est pas habilité à effectuer des analyses cliniques de santé, des décisions RH autonomes ou des transactions financières. Ses actions de communication (via Composio Gmail) doivent se limiter au reporting technique.

## 🛡️ Guardrails & Guardrails de Sécurité

### 1. Gestion des Identités et Habilitations (No-Session Rule)
Pour des raisons de sécurité renforcée et de confidentialité des données, l'agent n'utilise **aucune authentification basée sur les sessions persistantes**. 
- Chaque accès à des informations sensibles ou exécution de requêtes restrictives nécessite la saisie et la **vérification manuelle de l'identifiant employé** (Employee ID) de l'utilisateur au cours du prompt, agissant comme une barrière d'accès explicite (*Human-in-the-Loop*).

### 2. Protection contre les Injections de Prompts (Prompt Injection)
Les entrées issues des documents analysés par le composant `JigsawStackVOCR` sont traitées comme des chaînes de caractères brutes (données non fiables) par le composant `TypeConverterComponent` avant d'être envoyées aux LLM (`LanguageModelComponent` / `GroqModel`). 
- Le système applique un nettoyage des balises d'instructions pour empêcher qu'un texte malveillant caché dans un document n'altère le comportement de l'agent ou ne détourne l'outil de messagerie Gmail.

### 3. Isolation des Clés Secrètes
Le graphe de l'agent stocké dans GitHub est totalement agnostique de l'infrastructure cible. Les jetons critiques (`JIGSAWSTACK_API_KEY`, `DATABASE_URI`) ne sont jamais écrits en dur et sont injectés exclusivement au démarrage via l'environnement Docker ou les secrets chiffrés de GitHub, prévenant toute fuite d'informations sur les dépôts publics.
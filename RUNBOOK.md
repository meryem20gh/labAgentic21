---

### 2. `RUNBOOK.md`
Ce document sert de guide d'exploitation pour l'équipe technique pour le monitoring et la maintenance de la fiabilité système.

```markdown
# Runbook de Production : Observabilité & Fiabilité Système

**Statut du Document** : Opérationnel  
**Périmètre** : Maintenance technique et surveillance des capteurs/interfaces réseau.  
**Cible** : Équipe d'ingénierie DevOps / MLOps.

---

## 📊 Stratégie d'Observabilité

Pour garantir la résilience du système multi-agents, l'observabilité repose sur l'injection de traçabilité à travers tout le graphe d'exécution.

### 1. Suivi par ID de Corrélation (Correlation ID)
Chaque requête initiée par l'extraction VOCR génère un `Correlation ID` unique. Cet identifiant est transmis à travers :
- Le composant `JigsawStackVOCR`
- Le convertisseur de type (`TypeConverterComponent`)
- La passerelle de requêtage `MongoDBQuery`

*En cas d'anomalie, filtrez les journaux système à l'aide de cet ID pour isoler le parcours exact de la donnée.*

### 2. Télémétrie et Alertes
Si `TELEMETRY_LOGGING=true` est activé dans l'environnement, les métriques d'exécution (temps de réponse JigsawStack, latence d'exécution de la requête FusionDB) sont historisées.

---

## 🛠️ Résolution des Incidents Communs (Troubleshooting)

### Incident A : Échec de connexion à FusionDB (MongoDB Query Component)
- **Symptôme** : Le nœud `MongoDBQuery-yKPJA` renvoie une erreur de type `ConnectionError` ou `serverSelectionTimeoutMS`.
- **Actions** :
  1. Vérifier que la variable `DATABASE_URI` dans le `.env` ou les secrets GitHub est correctement formatée et que les identifiants n'ont pas expiré.
  2. Valider les règles de pare-feu (Whitelisting IP) du cluster FusionDB pour autoriser les requêtes provenant du conteneur Docker ou des runners GitHub Actions.

### Incident B : Erreur de parsing ou clé manquante JigsawStack
- **Symptôme** : Le nœud `JigsawStackVOCR-CufZC` renvoie `success: false` ou une erreur d'authentification.
- **Actions** :
  1. Confirmer la validité du jeton dans `JIGSAWSTACK_API_KEY`.
  2. Vérifier l'accessibilité de l'URL contenue dans `VOCR_DOCUMENT_URL`. Si le document est sur Google Drive, assurez-vous que le lien est en accès public direct (`export=download`).

### Incident C : Alerte de sécurité Bandit en CI/CD
- **Symptôme** : Le pipeline GitHub Actions échoue lors de l'étape `Run Security Linter`.
- **Actions** :
  1. Consulter les logs de l'action GitHub pour identifier la ligne de code incriminée.
  2. Corriger l'usage de fonctions non sécurisées ou s'assurer qu'aucun mot de passe n'a été inséré par inadvertance dans le code source (`src/`).
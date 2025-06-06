# 🤖 Workshop Discord Bot en Python

Bienvenue dans ce workshop de 2h dédié à la création d’un bot Discord avec Python et `discord.py`.

---

## 🎯 Objectifs

- Créer un bot fonctionnel avec des commandes de base
- Utiliser des Cogs pour structurer le code
- Interagir avec des API externes
- Envoyer des messages enrichis (embeds)
- Gérer les erreurs et les événements

---

## 🧠 Prérequis

- Python 3.8 ou plus
- Connaissances solides en Python (fonctions, classes, exceptions)
- Savoir utiliser une API
- Avoir un serveur Discord pour tester le bot
- Créer une application sur [Discord Developer Portal](https://discord.com/developers/applications) et récupérer un token

---

## 📁 Arborescence du workshop

```
discord-workshop/
├── bot.py
├── .env
├── requirements.txt
├── README.md
└── cogs/
    ├── hello.py
    ├── maths.py
    └── api.py
```

---

## 🧰 Installation

### 1. Cloner le repo

```bash
git clone https://github.com/ton-utilisateur/discord-workshop.git
cd discord-workshop
```

## 2. Installer les dépendances
```bash
pip install -r requirements.txt
```
## 3. Ajouter votre token dans un fichier

```.env
DISCORD_TOKEN=collez_votre_token_ici
```

## 🚀 Lancer le bot
test :
```bash
python bot.py
```

## 💪 Exercices :

### ✅ Partie 1 : Commandes simples (cogs/hello.py)

- Ajouter une commande `!hello`
- Ajouter une commande `!say` qui répète le message

### ✅ Partie 2 : Maths (cogs/maths.py)

- Créer une commande `!sub` pour la soustraction
- Ajouter `!div a b` avec gestion de la division par zéro

### ✅ Partie 3 : API externe (cogs/api.py)

- Ajouter `!crypto BTC` qui renvoie le prix du BTC depuis [CoinGecko](https://www.coingecko.com/)
- Ajouter `!weather Paris` en utilisant une API météo (ex: [OpenWeatherMap](https://openweathermap.org/api))

### ✅ Partie 4 : Bonus (cogs/bonus.py)

- Créer un mini-jeu `!guess` où l’utilisateur devine un nombre entre 1 et 10
- Ajouter une commande `!poll` qui lance un sondage avec réactions 👍👎





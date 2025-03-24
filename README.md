# 👾 Alien Invasion Game

## 🎮 Description

A fun arcade-style **Alien Invasion** game built with **Pygame**.  
Pilot your spaceship, shoot down alien fleets, and level up as the game speeds up! 🚀👽

---

## 🕹️ How to Play

- Click the **Play** button to start the game.
- Use **left** and **right arrow keys** to move your ship horizontally.
- Press **Spacebar** to shoot bullets.
- Press **Q** on the keyboard or click the window's **X** button to exit the game.

---

## 💡 Game Rules

- You have **3 lives**, shown as ships in the top-left corner.
- The **current score** is shown in the top-right corner, and the **level number** is right below it.
- The **highest score** is displayed at the top center of the screen.

---

## 🛸 Gameplay Details

- The ship can move only left and right, and cannot go beyond screen boundaries.
- An **alien fleet** (flot) is formed by multiple alien images.
- You can have a maximum of **3 bullets** on screen at any time.
- A bullet disappears when it:
  - Hits an alien (both bullet and alien vanish).
  - Reaches the top edge of the screen without hitting anything.

---

## 👽 Alien Fleet Movement

- The fleet moves **horizontally**.
- When it reaches the screen edge:
  - It **drops down** and **changes direction**.
- This continues until:
  - All aliens are destroyed → **Next level starts**.
  - An alien reaches the **bottom of the screen** or **collides with your ship** → You lose a life.

---

## 📈 Scoring & Levels

- The game becomes **faster** with each level.
- You earn **more points** per alien as you advance.
  - For example: Level 1 = *50 points per alien*.

---

## 🧠 Requirements

- Python 3.x
- Pygame

---

## 📸 Screenshots

(Add screenshots of your game screen here, if you have any.)

---

## 🛠️ Setup

```bash
# Install dependencies
pip install pygame

# Run the game
python alien_invasion.py

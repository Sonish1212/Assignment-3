**Question_number_1**

# (Tkinter Chat Application)

## Overview

This Tkinter Chat Application is designed with a focus on object-oriented programming principles, including multiple inheritance, encapsulation, polymorphism, and method overriding.
The application facilitates communication between users in a room-based environment. The code structure is modular, ensuring clean and organized implementation.

## Features
Server-Client Architecture:
Utilizes a server-client architecture allowing unlimited users to connect and chat in various rooms.

**Object-Oriented Programming Concepts:**

**Encapsulation**: Bundles related functionality and data within classes for better organization.

**Polymorphism**: Demonstrated through methods like send_message and receive_message tailored for server and client classes.

**Method Overriding**: Custom methods overridden in server and client classes based on specific requirements.

**Multiple Inheritance**: Inherits from Tkinter classes for GUI and socket-related classes for networking.

**Unlimited Users and Chat Rooms:**

Users can join chat rooms without limitations, fostering multiple discussions simultaneously.

## Usage
Clone the repository: git clone https://github.com/Sonish1212/Assignment-3/tree/main/Chat-bot

**Run the server script**:
First  we have to run the server.py file to establish the connection 
python server.py
After running the file the server is activated and we have to run client script
**Run the client script:**
python client.py
Enter a username and select a chat room.

Start chatting with other users in the same room.

## Code Explanation
Server and Client Classes:
-The Server and Client classes encapsulate server and client functionalities separately.
-Polymorphism is evident in methods like send_message and receive_message implemented differently for server and client.

**Socket Connections:**
-Utilizes socket programming for communication, showcasing multiple inheritance for handling GUI and networking aspects.

## Output image


![WhatsApp Image 2024-02-11 at 6 27 15 PM](https://github.com/Sonish1212/Assignment-3/assets/150264109/24ebe2fd-8f5e-4187-af35-02cc51bc43a5)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Question number 2 (PyGame)** 

# Side-Scrolling 2D Game with Pygame

## Overview

This project is a simple side-scrolling 2D game developed using Pygame. It features a player character with the ability to run, jump, and shoot projectiles. The game includes enemies, collectibles, 3 levels, a scoring system, health, and lives. Additionally, a dynamic camera follows the player smoothly for an enhanced gaming experience.

## Game Ideas

Choose one of the following themes:
- A game with human-like characters (hero, enemy)
- A game with a soldier and human characters (Enemy) with good graphs and various obstacles like water.
- A game is made more beautiful using the mountains and  trees  so the UI looks great. 
- A game have several buttons restart, start and exit
- A game is operated using the keys A and D for direction W to Jump and Space to shoot.

## Features

- **Player Class:**
  - Movements, speed, jump, health, lives.
  - Methods for player actions.

- **Projectile Class:**
  - Movements, speed, damage.
  - Methods for projectile actions.

- **Enemy Class:**
  - Placeholder for enemy-related methods.

- **Collectible Class:**
  - Health boost, life, Ammo etc.

- **Level Design:**
  - 3 Levels.
  - Boss enemy at the end of each level.

- **Scoring System:**
  - Based on enemies defeated and collectibles collected.

- **Health Bar:**
  - Display for player and enemy health.

- **Game Over Screen:**
  - Option to restart.

- **Bonus:**
  - Dynamic camera that smoothly follows the player.

## Installation and usage

1. Clone the repository:

   ```bash
   git clone https://github.com/Sonish1212/Assignment-3/tree/main/pygame_soldier

2. Install the required dependencies
    pip install pygame

3. Run the main game script:
    python main.py

4. A game is operated using the keys Such as; A and D for direction and running W to Jump and Space to shoot.


## Output images 
<img width="598" alt="image" src="https://github.com/Sonish1212/Assignment-3/assets/150264109/27792367-bd45-4f12-b08f-0a17a76642e9">
<img width="602" alt="image" src="https://github.com/Sonish1212/Assignment-3/assets/150264109/07f3fa37-2c70-45e4-9713-1e474f933e1f">
<img width="601" alt="image" src="https://github.com/Sonish1212/Assignment-3/assets/150264109/a5cc2b9e-fc37-4599-8b44-3a354180cfa3">
<img width="602" alt="image" src="https://github.com/Sonish1212/Assignment-3/assets/150264109/1deffad1-af57-4d31-baf3-fabcdbb67575">
<img width="601" alt="image" src="https://github.com/Sonish1212/Assignment-3/assets/150264109/2fe9cfb9-339b-46c9-bcce-64135364185f">







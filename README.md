# Python pygame platformer
A simple collision detection game created with Python's Pygame library. There's enemies moving around the screen and 
the player needs to avoid hitting the enemies by moving with the arrow keys or with WASD.

This project currently contains only dummy code that shows the conventions used when coding with Python (and more 
specifically, Pygame).

## Up & running 
### Installation Pygame
- Download Python from [Python website](https://www.python.org/downloads/)
- Install pygame: <br> ```pip install pygame```

### Installation project
- Clone the repository: <br> ```git clone https://github.com/username/project-name.git```
- Navigate to project directory: <br> ```cd assignment-1-ryanv```
- Install dependencies: <br>```pip install -r requirements.txt```

### Run project
- Navigate to src directory: <br> ```cd src```
- Run ```python main.py```

## Project structure
assignment-2-RyanVankriekinge/
│
├── assets/                    # Directory for all asset files (images, sounds, etc.)
│   ├── dynamics/              # Subdirectory for dynamic assets
│   │   ├── player.png         # Player image asset
│   │   └── enemy.png          # Enemy image asset
│   └── levels/                # Subdirectory for game levels
│       ├── level1.json        # JSON file defining level 1
│       └── level2.json        # JSON file defining level 2
│
├── src/                       # Source code directory
│   ├── __init__.py            # Initialization for package
│   ├── assets.py              # Module for handling assets
│   ├── enemy.py               # Module for enemy logic
│   ├── game.py                # Game logic
│   ├── main.py                # Entry point of the application
│   ├── player.py              # Module for player logic
│   └── settings.py            # Game settings
│
├── .gitignore                 # Specifies files to be ignored by Git
├── LICENSE                    # License information
├── README.md                  # Project documentation
├── requirements.txt           # List of Python dependencies


## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Sources 
- [Pygame Installation Guide](https://www.pygame.org/wiki/GettingStarted) used to install Pygame
- [Pygame newbie guide](https://www.pygame.org/docs/tut/newbieguide.html)
- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/) correct use of style conventions in project in src > *
- [Pygame Quick start](https://www.pygame.org/docs/) used to create main game loop in src > main.py 17-53
- [Moving player with pygame](https://opensource.com/article/17/12/game-python-moving-player) used to move player in src > player.py 33-75
- [Bouncing enemies off wall](https://wall-ball.readthedocs.io/en/latest/steps/step01.html) used to reverse enemy direction when they hit the wall in src > enemy.py 43-47
- [Choose a license - MIT license](https://choosealicense.com/licenses/mit/) used to create MIT license
- [Python programming: Docstrings](https://www.programiz.com/python-programming/docstrings) used to document functions and classes with docstrings in src > *
- [ChatGPT](https://chatgpt.com/share/671626a0-2670-8002-838d-dc274be10d10) used to generate Project structure for README
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT

FPS = 120

CAPTION = "Gunther McShooty: Alien Hunter"

TILE_WIDTH = 64
TILE_HEIGHT = 64
TILE_SIZE = TILE_WIDTH, TILE_HEIGHT

# Physics parameters
GRAVITY = 800                   # pixels/s^2
DRAG = 0.1                      # 1/s
TERMINAL_VELOCITY = 500
VERTICAL_RESTITUTION = 0.0
HORIZONTAL_RESTITUTION = 0.2
TANGENTIAL_RESTITUTION = 1      # unitless
V_MIN_BOUNCE = 25               # pixels/s

FRICTION = 10                   # grounded friction time constant in 1/s
V_MIN_SLIDE = 5                 # minimum sliding velocity in pixels/s

# Zombie parameters
ZOMBIE_SPEED = 25               # zombie walking speed in pixels/s
ZOMBIE_KNOCKBACK = 500          # zombie attack impulse on hero in pixels/s
ZOMBIE_COOLDOWN = 0.5           # time between attacks in s

# Hero parameters
RECOIL = 10                     # gun knockback in pixels/s
HERO_COOLDOWN = 0.5             # time between shots in s
HERO_AIM_TIME = 1               # time to hold aim steady before shooting
TARGET_PRIORITY = 0.7           # amount to prioritize switching to a closer target (0 to 1)
SWIVEL_SPEED = 1.3                # gun aiming speed in rad/s
SHOT_JITTER = 5                # maximum projectile initial offset in pixels
SHOT_SPREAD = 15                # maximum projectile spread in degrees
HERO_SPEED = 100                # hero walking speed in pixels/s
HERO_JUMP = 500                 # hero jump speed in pixels/s

# Projectile parameters
BULLET_SPEED = 1500             # bullet speed in pixels/s
BULLET_FORCE = 0.05             # bullet mass to zombie mass ratio

# Level parameters
SPAWN_RATE = 1                  # seconds between zombie spawns

# Direction constants
UP_LEFT = (-1, -1)
UP = (0, -1)
UP_RIGHT = (1, -1)
LEFT = (-1, 0)
SELF = (0, 0)
RIGHT = (1, 0)
DOWN_LEFT = (-1, 1)
DOWN = (0, 1)
DOWN_RIGHT = (1, 0)

# Upgrades
HEALTH = 0
RATE_OF_FIRE = 1
ACCURACY = 2
LEFTY = 3
WALK_SPEED = 4
PIERCE = 5
KNOCK = 6

UPGRADE_NAMES = {
    HEALTH: "Thick skin",
    RATE_OF_FIRE: "Trigger lubricant",
    ACCURACY: "Contact lenses",
    LEFTY: "Lefty",
    WALK_SPEED: "Comfy footwear",
    PIERCE: "Sharpened bullets",
    KNOCK: "High caliber"
}

UPGRADE_DESCRIPTIONS = {
    HEALTH: "The hero's health is increased.",
    RATE_OF_FIRE: "The hero shoots more rapidly.",
    ACCURACY: "The hero's shots are more accurate.",
    LEFTY: "More dangerous with left hand;\nless dangerous with right.",
    WALK_SPEED: "The hero can move faster.",
    PIERCE: "Shots can pierce through monsters.",
    KNOCK: "Shots launch zombies further."
}
MAX_LEVEL = 5

from tod.common.constant import constant
from tod.common.game import game
from tod.common.game import string
import arcade
import random

# Constants
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN_TITLE = constant.__project__

# Constants used to scale our sprites from their original size
ROOT_DIR = "C:/src/tod-git/"
IMAGES_DIR = f"{ROOT_DIR}tod/resources/images/"
BATTLE_IMG = f"{IMAGES_DIR}battle.png"
DUNGEON_IMG = f"{IMAGES_DIR}dungeon.png"
DRAGON1_IMG = f"{IMAGES_DIR}dragon1.png"
DRAGON2_IMG = f"{IMAGES_DIR}dragon2.png"
CHEST_IMG = f"{IMAGES_DIR}chest.png"
BACKGROUND_COLOR = arcade.csscolor.PALE_GREEN
BATTLE_SIZE = 240
DUNGEON_WIDTH = 640
DUNGEON_HEIGHT = 425
DUNGEON_SCALING = 1.55
CHARACTER_SIZE = 30
BORDER_SIZE = 10
SCALING = SCREEN_HEIGHT / BATTLE_SIZE * 2 / 3
TEXT_COLOR = arcade.csscolor.BLACK
FONT_SIZE = 18
BATTLE_MODE = "battle"
SHOP_MODE = "shop"
DUNGEON_MODE = "dungeon"


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # self.mode = BATTLE_MODE
        # self.mode = SHOP_MODE
        self.mode = DUNGEON_MODE

        # These are 'lists' that keep track of our sprites. Each sprite should go into a list.
        self.background_list = None
        self.item_list = None
        self.monster_count = None
        self.monster_list = None
        self.hero_list = None

        # Separate variables that hold the sprites
        self.battle_sprite = None
        self.dungeon_sprite = None
        self.blank_sprite = None
        self.item_sprite = None
        self.monster_sprite = None
        self.hero_sprite = None

        arcade.set_background_color(BACKGROUND_COLOR)

    def setup(self):
        if self.mode == SHOP_MODE:
            self.setup_shop()

        elif self.mode == DUNGEON_MODE:
            self.setup_dungeon()

        else:
            self.setup_battle()

    def setup_battle(self):
        """ Set up the game here. Call this function to restart the game. """

        # Create the sprite lists
        self.background_list = arcade.SpriteList()
        self.item_list = arcade.SpriteList(use_spatial_hash=True)
        self.monster_list = arcade.SpriteList(use_spatial_hash=True)
        self.hero_list = arcade.SpriteList(use_spatial_hash=True)

        # Create the background
        self.battle_sprite = arcade.Sprite(BATTLE_IMG, SCALING)
        self.battle_sprite = arcade.Sprite(BATTLE_IMG, SCALING)
        self.battle_sprite.center_x = BATTLE_SIZE / 2 * SCALING + BORDER_SIZE
        self.battle_sprite.center_y = SCREEN_HEIGHT - BATTLE_SIZE / 2 * SCALING - BORDER_SIZE
        self.background_list.append(self.battle_sprite)

        # Set up the items, specifically placing them at these coordinates.
        item_list = list()
        item_list.append([random.randint(1, 6), 6])

        for item in item_list:
            self.item_sprite = arcade.Sprite(CHEST_IMG, SCALING)
            self.item_sprite.center_x = (item[0] * CHARACTER_SIZE + CHARACTER_SIZE / 2) * SCALING + BORDER_SIZE
            self.item_sprite.center_y = SCREEN_HEIGHT - (item[1] * CHARACTER_SIZE + CHARACTER_SIZE / 2) * SCALING - BORDER_SIZE
            self.item_list.append(self.item_sprite)

        # Set up the monsters, specifically placing them at these coordinates.
        monster_list = list()
        self.monster_count = random.randint(1, 4)

        for _ in range(0, self.monster_count):
            monster_list.append([random.randint(1, 6), random.randint(2, 5)])

        for monster in monster_list:
            if monster == monster_list[0]:
                self.monster_sprite = arcade.Sprite(DRAGON2_IMG, SCALING)

            else:
                self.monster_sprite = arcade.Sprite(DRAGON1_IMG, SCALING)

            self.monster_sprite.center_x = (monster[0] * CHARACTER_SIZE + CHARACTER_SIZE / 2) * SCALING + BORDER_SIZE
            self.monster_sprite.center_y = SCREEN_HEIGHT - (
                        monster[1] * CHARACTER_SIZE + CHARACTER_SIZE / 2) * SCALING - BORDER_SIZE
            self.hero_list.append(self.monster_sprite)

        # Set up the heroes, specifically placing them at these coordinates.
        for hero in game.party:
            self.hero_sprite = arcade.Sprite(f"{IMAGES_DIR}{game.party[hero]['images'][0]}", SCALING)
            self.hero_sprite.center_x = (game.party[hero]["x"] * CHARACTER_SIZE + CHARACTER_SIZE / 2) * SCALING + BORDER_SIZE
            self.hero_sprite.center_y = SCREEN_HEIGHT - (game.party[hero]["y"] * CHARACTER_SIZE + CHARACTER_SIZE / 2) * SCALING - BORDER_SIZE
            self.hero_list.append(self.hero_sprite)

        # Status screen
        y = 0

        for hero in game.party:
            # Hero sprites
            self.hero_sprite = arcade.Sprite(f"{IMAGES_DIR}{game.party[hero]['images'][0]}", SCALING)
            self.hero_sprite.center_x = (BATTLE_SIZE + CHARACTER_SIZE / 2) * SCALING + BORDER_SIZE * 2
            self.hero_sprite.center_y = SCREEN_HEIGHT - (y * CHARACTER_SIZE + CHARACTER_SIZE / 2) * SCALING * 2 - BORDER_SIZE
            self.hero_list.append(self.hero_sprite)
            y += 1

    def draw_status(self):
        y = 0

        for hero in game.party:
            # Draw blank squares
            center_x = (BATTLE_SIZE + CHARACTER_SIZE) * SCALING - BORDER_SIZE / 2
            center_y = SCREEN_HEIGHT - (y * CHARACTER_SIZE + CHARACTER_SIZE / 2) * 2 * SCALING - BORDER_SIZE
            width = CHARACTER_SIZE * SCALING
            height = CHARACTER_SIZE * SCALING
            color = arcade.color.WHITE
            arcade.draw_rectangle_filled(center_x, center_y, width, height,color)

            # Draw status text
            text = f'{game.party[hero]["name"]}, the {game.party[hero]["class"]}' \
                   f'\nHP: {game.party[hero]["hp"]} / {game.party[hero]["hp_max"]}' \
                   f'\nXP: {game.party[hero]["xp"]}' \
                   f'\nLevel {game.party[hero]["lv"]}'
            start_x = (BATTLE_SIZE + CHARACTER_SIZE) * SCALING + 4 * BORDER_SIZE
            start_y = SCREEN_HEIGHT - (y * CHARACTER_SIZE + CHARACTER_SIZE / 1.25) * 2 * SCALING - BORDER_SIZE
            color = TEXT_COLOR
            font_size = FONT_SIZE
            arcade.draw_text(text, start_x, start_y, color, font_size)
            y += 1

        # Draw battle text
        text = f"{self.monster_count} {string.pluralize('Dragon', self.monster_count)}"
        start_x = BORDER_SIZE
        start_y = SCREEN_HEIGHT - BATTLE_SIZE * SCALING - 4 * BORDER_SIZE
        color = TEXT_COLOR
        font_size = FONT_SIZE
        arcade.draw_text(text, start_x, start_y, color, font_size)

    def setup_shop(self):
        self.background_list = arcade.SpriteList()

    def setup_dungeon(self):
        # Create the sprite lists
        self.background_list = arcade.SpriteList()
        self.monster_list = arcade.SpriteList()

        # Create the background
        self.dungeon_sprite = arcade.Sprite(DUNGEON_IMG, DUNGEON_SCALING)
        self.dungeon_sprite.center_x = DUNGEON_WIDTH * DUNGEON_SCALING / 2 + BORDER_SIZE
        self.dungeon_sprite.center_y = SCREEN_HEIGHT - DUNGEON_HEIGHT * DUNGEON_SCALING / 2 - BORDER_SIZE
        self.background_list.append(self.dungeon_sprite)

    @staticmethod
    def draw_direction():
        # Draw dungeon text
        text = "S"
        start_x = SCREEN_WIDTH / 2 - 3 * BORDER_SIZE
        start_y = SCREEN_HEIGHT - 10 * BORDER_SIZE
        color = TEXT_COLOR
        font_size = 4 * FONT_SIZE
        arcade.draw_text(text, start_x, start_y, color, font_size)

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()

        # Draw our sprites

        if self.mode == SHOP_MODE:
            self.background_list.draw()
            self.draw_status()

        elif self.mode == BATTLE_MODE:
            self.background_list.draw()
            self.draw_status()
            self.item_list.draw()
            self.monster_list.draw()
            self.hero_list.draw()

        else:
            self.background_list.draw()
            self.draw_direction()
            self.monster_list.draw()


def main():
    """ Main method """

    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

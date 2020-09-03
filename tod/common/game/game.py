import arcade

party = {
    0: {
        "name": "David",
        "class": "Traveller",
        "color": "red",
        "images": ["traveller1.png", "traveller2.png"],
        "hp": 24,
        "hp_max": 24,
        "xp": 0,
        "lv": 1,
        "bonus": 0,
        "weapons": [
            {"Sword": {"damage": 8, "cost": 50}},
            {"None": {"damage": 2, "cost": 0}},
        ],
        "armor": {"Ring Mail": {"protection": 4, "cost": 50}},
        "shield": {"None": {"protection": 0, "cost": 0}},
        "unusable": [],
        "items": [
            {"Lightning Rod": {"type": "wand", "effect": "Decreases monster hit points", "use": 6}}
        ],
        "x": 3,
        "y": 1
    },
    1: {
        "name": "Eric Seablade",
        "class": "Fighter",
        "color": "blue",
        "images": ["fighter1.png", "fighter2.png"],
        "hp": 20,
        "hp_max": 20,
        "xp": 0,
        "lv": 1,
        "bonus": 0,
        "weapons": [
            {"Hand Ax": {"damage": 6, "cost": 30}},
            {"Short Bow": {"damage": 6, "cost": 30, "ranged": True, "ammo": 120}}
        ],
        "armor": {"Plate Mail": {"protection": 6, "cost": 100}},
        "shield": {"Shield": {"protection": 1, "cost": 10}},
        "unusable": [],
        "items": [],
        "x": 4,
        "y": 1
    },
    2: {
        "name": "Mauve d'Orm-Mul",
        "class": "Rogue",
        "color": "purple",
        "images": ["rogue1.png", "rogue2.png"],
        "hp": 18,
        "hp_max": 18,
        "xp": 0,
        "lv": 1,
        "bonus": 0,
        "weapons": [
            {"Dagger": {"damage": 4, "cost": 10}},
            {"Crossbow": {"damage": 8, "cost": 60, "ranged": True, "ammo": 120}}
        ],
        "armor": {"Leather": {"protection": 2, "cost": 20}},
        "shield": {"None": {"protection": 0, "cost": 0}},
        "unusable": {"Ring Mail", "Plate Mail", "Shield"},
        "items": [],
        "x": 3,
        "y": 0
    },
    3: {
        "name": "Forestall Grimm",
        "class": "Wizard",
        "color": "green",
        "images": ["wizard1.png", "wizard2.png"],
        "hp": 15,
        "hp_max": 15,
        "xp": 0,
        "lv": 1,
        "bonus": 0,
        "weapons": [
            {"Dagger": {"damage": 4, "cost": 10}},
            {"Sling": {"damage": 2, "cost": 10, "ranged": True, "ammo": None}}
        ],
        "armor": {"Leather": {"protection": 2, "cost": 20}},
        "shield": {"None": {"protection": 0, "cost": 0}},
        "unusable": {"Hand Ax", "Sword", "Short Bow", "Crossbow", "Ring Mail", "Plate Mail", "Shield"},
        "items": [
            {"Protection": {"type": "scroll", "effect": "Decreases monster attack class", "use": 4}}
        ],
        "x": 4,
        "y": 0
    }
}


def start_render(screen_width, screen_height, title, background_color):
    # Open the window. Set the window title and dimensions (width and height)
    arcade.open_window(screen_width, screen_height, title)

    # Set the background color to white.
    # For a list of named colors see:
    # http://arcade.academy/arcade.color.html
    # Colors can also be specified in (red, green, blue) format and
    # (red, green, blue, alpha) format.
    arcade.set_background_color(background_color)

    # Start the render process. This must be done before any drawing commands.
    arcade.start_render()


def finish_render():
    # Finish drawing and display the result
    arcade.finish_render()

    # Keep the window open until the user hits the 'close' button
    arcade.run()


def draw_pine_tree(x, y, size):
    """ This function draws a pine tree at the specified location. """

    # Draw the triangle on top of the trunk.
    # We need three x, y points for the triangle.
    arcade.draw_triangle_filled(x + size, y,
                                x, y - 2.5 * size,
                                x + 2 * size, y - 2.5 * size,
                                arcade.color.DARK_GREEN)

    # Draw the trunk
    arcade.draw_lrtb_rectangle_filled(x + 0.75 * size, x + 1.25 * size, y - 2.5 * size, y - 3.5 * size, arcade.color.DARK_BROWN)


def draw_smiley_face(x, y, radius):
    # Draw the face
    arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)

    # Draw the left eye
    arcade.draw_circle_filled(x - radius / 3, y + radius / 3, radius / 10, arcade.color.BLACK)

    # Draw the right eye
    arcade.draw_circle_filled(x + radius / 3, y + radius / 3, radius / 10, arcade.color.BLACK)

    # Draw the smile
    arcade.draw_arc_outline(x, y - radius / 10, radius, radius, arcade.color.BLACK, 360 / 2, 360, radius / 20)

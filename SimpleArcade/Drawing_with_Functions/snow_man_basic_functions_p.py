import arcade


WIDTH = 800
HEIGHT = 600


def draw_grass():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, WIDTH, HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)


def draw_snow_person(x, y):
    """ Draw a snow person """

    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)

    # Snow
    arcade.draw_circle_filled(300 + x, 200 + y, 60, arcade.color.RED_DEVIL)
    arcade.draw_circle_filled(300 + x, 280 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(300 + x, 340 + y, 40, arcade.color.ROYAL_BLUE)

    # Eyes
    arcade.draw_circle_filled(285 + x, 350 + y, 5, arcade.color.YELLOW)
    arcade.draw_circle_filled(315 + x, 350 + y, 5, arcade.color.YELLOW)

def on_update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    # Draw in here...
    draw_grass()
    draw_snow_person(50, 50)
    draw_snow_person(175, 50)
    draw_snow_person(325, 50)



def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.schedule(on_update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()

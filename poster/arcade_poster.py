import arcade
import webbrowser

WIDTH = 1048
HEIGHT = 768
start_x = 0
start_y = 700
x_move = 1
stop_value = 300

def on_update(delta_time):
    global start_x
    global x_move

    start_x += x_move
    if start_x > stop_value:
        x_move = 0


def on_draw():

    # arcade.draw_rectangle_outline(x coord,y coord, width, height, arcade.color.color, thick

    arcade.start_render()
    # Draw in here...
    arcade.draw_rectangle_outline(450,710, 400, 100, arcade.color.BLACK,)

    arcade.draw_text("Smart Phone Addiction!", start_x, start_y, arcade.color.BLACK, 20)
    arcade.draw_text("Nomophobia—an abbreviation of “no-mobile-phone-phobia.", 67, 550, arcade.color.BLACK, 13)
    arcade.draw_text("Cell phones used to just be communication tools. Now, they’re GPS, cameras, and the list goes on. ", 67, 500, arcade.color.BLACK, 13)
    arcade.draw_text("Mobile phone overuse is a proposed form of psychological or behavioural dependence on cell phones, closely related to", 67, 450, arcade.color.BLACK, 12)
    arcade.draw_text("other forms of digital media overuse such as social media addiction or internet addiction disorder.", 67, 400, arcade.color.BLACK, 12)

    texture =arcade.load_texture("0_J7vwt-FyYYhVRPxM.jpg")
    scale= .5
    arcade.draw_texture_rectangle(500, 170, scale * texture.width,
                                  scale * texture.height, texture, 0)

def on_key_press(key, modifiers):

    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
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

import arcade

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN_TITLE = "Stopwatch"

class Stopwatch_Game(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.color.AMAZON)
    
    def setup(self):
        """Set up the game here, Call this function to reset it."""
        pass

    def on_draw(self):
        """render the screen"""

        #clear the screen
        self.clear()
    
    def on_mouse_press(self, x, y, button, key_modifiers):
        """ called when user presses mouse button"""
        pass

    def on_mouse_release(self, x: float, y:float, button: int, modifiers: int):
        """called when user releases mouse button"""
        pass

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """User moves mouse"""
        pass


def main():
    window = Stopwatch_Game()
    window.setup()
    arcade.run()
    

if __name__ == "__main__":
    main()

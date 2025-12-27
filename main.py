import arcade
from physics import *
from pseudo3D import *
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "GAS"

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.setup()
        
    def setup(self):
        arcade.set_background_color(arcade.color.WHITE)

        self.room_size = [300, 200, 400]
        self.room = Room(200, 500, self.room_size, "Ne")
        self.meas: dict[str:float]
        self.T = 300
    
    def on_draw(self):
        self.clear()
        arcade.draw_text(f"P(посчитанное): {self.meas["P"]}", 200, 550, arcade.color.BLACK, 24)
        arcade.draw_text(f"P(по формуле): {self.T*len(self.room.molecules)/(self.room_size[0]*self.room_size[1]*self.room_size[2])*BOLZMAN_K}", 
        200, 500, arcade.color.BLACK, 24)
        arcade.draw_text(f"T: {self.T}", 200, 450, arcade.color.BLACK, 24)
        
        h_delta = -SCREEN_HEIGHT/3
        w_delta = -SCREEN_WIDTH/3
                
        coords = self.room_size
        walls = [
            [[0, 0, 0], [0, 0, coords[2]], [0, coords[1], coords[2]], [0, coords[1], 0], [0, 0, 0]],
            [[0, 0, 0], [0, coords[1], 0], [coords[0], coords[1], 0], [coords[0], 0, 0], [0, 0, 0]],
            [[0, 0, 0], [coords[0], 0, 0], [coords[0], 0, coords[2]], [0, 0, coords[2]], [0, 0, 0]]
        ]
        for wall in walls:
            arcade.draw_line_strip([vector_to_screen(point, h_delta, w_delta) 
                                    for point in wall], arcade.color.BLACK, 2)
        
        for m in self.room.molecules:
            draw_molecule(m, h_delta, w_delta)

        walls = [
            [[coords[0], coords[1], coords[2]], [0, coords[1], coords[2]], 
             [0, 0, coords[2]], [coords[0], 0, coords[2]], 
             [coords[0], coords[1], coords[2]]],
            [[coords[0], coords[1], coords[2]], [0, coords[1], coords[2]], 
             [0, coords[1], 0], [coords[0], coords[1], 0], 
             [coords[0], coords[1], coords[2]]]
        ]
        for wall in walls:
            arcade.draw_line_strip([vector_to_screen(point, h_delta, w_delta) 
                                    for point in wall], arcade.color.BLACK, 2)
    def on_update(self, delta_time):
        self.meas = self.room.tick()
    def on_key_press(self, key, modifier):
        if key == arcade.key.UP:
            self.room.dt *= 1.2
        if key == arcade.key.DOWN:
            self.room.dt /= 1.2

def main():
    window = GameWindow()
    arcade.run()

if __name__ == "__main__":
    main()

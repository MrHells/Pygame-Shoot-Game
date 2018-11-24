import sys
import math
import pygame as pg


def out_of_bounds(position):
    """Check if the position of a projectile is out of bounds.

    Args:
        position (list): The coordinates of the projectile.

    Returns:
        bool: True if out of bounds, False if not.
    """
    x, y = position  # You can unpack a list or tuple like so.
    return x < -40 or x > 500 or y < -40 or y > 400


pg.init()

screen = pg.display.set_mode((640, 480))

PLAYER_IMG = pg.Surface((50, 30), pg.SRCALPHA)
pg.draw.polygon(PLAYER_IMG, (30, 150, 90), ((0, 0), (50, 15), (0, 30)))
DAGGER_IMG = pg.Surface((30, 20), pg.SRCALPHA)
pg.draw.polygon(DAGGER_IMG, (190, 150, 90), ((0, 0), (30, 10), (0, 20)))

# Player variables. I store the position in a rect.
player = pg.Rect(200, 275, 50, 30)
velocity_x = 0  # The x-speed of the player.
velocity_y = 0  # The y-speed of the player.
angle = 0
# In this list I'll store the data for the projectiles,
# i.e. lists of the positions and the velocities.
daggers = []

clock = pg.time.Clock()  # Use a clock to limit the frame rate.
x = pygame.
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        # Move the player.
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                velocity_x -= 5
            elif event.key == pg.K_RIGHT:
                velocity_x += 5
            elif event.key == pg.K_UP:
                velocity_y -= 5
            elif event.key == pg.K_DOWN:
                velocity_y += 5
        elif event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                velocity_x = 0
            elif event.key == pg.K_UP or event.key == pg.K_DOWN:
                velocity_y = 0
        # Here I create the projectiles and add them to the daggers list.
        elif event.type == pg.MOUSEBUTTONDOWN:
            # Use sine and cosine to get the velocity of the projectile.
            # To make it move faster, you need to scale the velocity
            # (i.e. multiply it by a number).
            vel_x = math.cos(angle) * 3
            vel_y = math.sin(angle) * 3
            # Now rotate the original image by the negative angle (because
            # pygame's y-axis is flipped).
            dagger_img = pg.transform.rotate(DAGGER_IMG, -math.degrees(angle))
            width, height = dagger_img.get_size()
            # The projectile data consists of position, velocity and the
            # rotated image. -width/2 and -height/2 to center them.
            daggers.append(
                [[player.centerx-width/2, player.centery-height/2],  # Pos
                 [vel_x, vel_y],  # Velocity
                 dagger_img  # Image
                 ])

    # Update the game.
    # Move the player by adding the velocity to the x- and y-coords
    # of the player rect.
    player.x += velocity_x
    player.y += velocity_y
    # Rotate player toward the mouse.
    mouse_position = pg.mouse.get_pos()
    # Distances to the mouse position.
    rise = mouse_position[1] - player.centery
    run = mouse_position[0] - player.centerx
    angle = math.atan2(rise, run)  # atan2 gives you the angle to the target.
    # Rotate the player image.
    player_rotated = pg.transform.rotate(PLAYER_IMG, -math.degrees(angle))
    player = player_rotated.get_rect(center=player.center)

    # Filter the daggers list.
    filtered_daggers = []
    for shot in daggers:
        if not out_of_bounds(shot[0]):
            filtered_daggers.append(shot)
    daggers = filtered_daggers
    # The 5 lines above can be reduced to this list comprehension.
    # daggers = [shot for shot in daggers if not out_of_bounds(shot[0])]

    # Move the daggers by adding the velocity to the position.
    # shot[0] is the pos, shot[1] the velocity.
    for shot in daggers:
        shot[0][0] += shot[1][0]
        shot[0][1] += shot[1][1]

    # Draw everything.
    screen.fill((30, 40, 50))
    screen.blit(player_rotated, player)
    # Blit the projectiles in a for loop.
    for shot in daggers:
        screen.blit(shot[2], shot[0])

    pg.display.update()
    clock.tick(30)  # Limit frame rate to 30 fps.

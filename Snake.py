import pygame,random

Length, Width = 500, 500

white = (255,255,255)
position_x = 0
position_y = 0
velocity = 1

snake_segments = [(position_x, position_y)]

def draw_square():
    global position_x,position_y,velocity,snake_segments
    for segment in snake_segments:
        pygame.draw.rect(screen, white, (segment[0], segment[1], 30, 30))
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            velocity = 1
        if event.key == pygame.K_LEFT:
            velocity = 2
        if event.key == pygame.K_DOWN:
            velocity = 3
        if event.key == pygame.K_UP:
            velocity = 4

def set_velocity():
    global position_x,position_y,velocity,snake_segments
    if velocity == 1:
        position_x += 10
    if velocity == 2:
        position_x -= 10
    if velocity == 3:
        position_y += 10
    if velocity == 4:
        position_y -= 10

    snake_segments.insert(0, (position_x, position_y))

def out_of_bounds():
    global position_x,position_y,done
    if position_x > Length - 30 or position_x < 0 or position_y > Width - 30 or position_y < 0:
        done = True

def check_collision():
    global position_x,position_y,done,snake_segments
    for i in range(1, len(snake_segments)):
        if snake_segments[i] == (position_x, position_y):
            done = True
def set_food():
    global food_x,food_y
    food_x = random.randint(0, Length - 30)
    food_y = random.randint(0, Width - 30)

def spawn_food():
    pygame.draw.rect(screen,white,(food_x,food_y,30,30))
    pygame.display.flip()

screen = pygame.display.set_mode((Length,Width))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
count = 0

food_x = Length/2
food_y = Width/2

done = False
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0,0,0))

    clock.tick(30)

    draw_square()

    set_velocity()
    
    out_of_bounds()
    
    check_collision()

    pygame.draw.rect(screen, white, (food_x, food_y, 30, 30))
    
    if position_x > food_x - 25 and position_x < food_x + 25 and position_y > food_y - 25 and position_y < food_y + 25:
        set_food()
        spawn_food()
    else:
        snake_segments.pop()

    pygame.display.flip()

pygame.quit()
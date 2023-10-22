import pygame
import sys

# 初期化
pygame.init()

# 画面の幅と高さ
width, height = 400, 400

# 画面の初期化
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Virtual Joystick")

# 色
background_color = (255, 255, 255)
base_color = (200, 200, 200)
knob_color = (255, 0, 0)

# FPS設定
FPS = 60
wait_time = 1000 // FPS
print(wait_time)

# メインループ
running = True
try:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(background_color)
        pygame.draw.circle(screen, base_color, (width // 2, height // 2), 10)
        pygame.display.flip()
        pygame.time.delay(wait_time)

except Exception as e:
    print(e)
except KeyboardInterrupt as k:
    print()
finally:
    pygame.quit()
    sys.exit()

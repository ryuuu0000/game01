import pygame
import sys
import math

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

# ジョイスティックのベースとノブの初期位置
base_x, base_y = width // 2, height // 2
base_radius = 100
knob_x, knob_y = base_x, base_y
knob_radius = 30

# ジョイスティックの移動範囲
joystick_range = base_radius - knob_radius

# ドラッグ中かどうか
dragging = False

# メインループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                # マウスクリックの位置からノブの中心までの距離を計算
                distance = math.hypot(x - knob_x, y - knob_y)
                if distance <= knob_radius:
                    dragging = True
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                x, y = event.pos
                # ノブがベースの範囲内に収まるように制限
                distance = math.hypot(x - base_x, y - base_y)
                if distance <= joystick_range:
                    knob_x, knob_y = x, y
                else:
                    angle = math.atan2(y - base_y, x - base_x)
                    knob_x = int(base_x + joystick_range * math.cos(angle))
                    knob_y = int(base_y + joystick_range * math.sin(angle))
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragging = False
                knob_x, knob_y = base_x, base_y

    screen.fill(background_color)
    pygame.draw.circle(screen, base_color, (base_x, base_y), base_radius)
    pygame.draw.circle(screen, knob_color, (knob_x, knob_y), knob_radius)

    pygame.display.flip()

pygame.quit()
sys.exit()

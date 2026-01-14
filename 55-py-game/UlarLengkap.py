import pygame
import random

# 1. Init
pygame.init()
clock = pygame.time.Clock()

# Membuat display surface object
windowLebar = 600
windowPanjang = 600
window = pygame.display.set_mode((windowLebar, windowPanjang))
pygame.display.set_caption("Snake Game: Tembus Dinding")

# 2. Variabel Game
ukuran_blok = 20
x = 300
y = 300
x_speed = 0
y_speed = 0

badan_ular = []
panjang_ular = 1

# Posisi Umpan
umpan_x = round(random.randrange(0, windowLebar - ukuran_blok) / 20.0) * 20.0
umpan_y = round(random.randrange(0, windowPanjang - ukuran_blok) / 20.0) * 20.0

score = 0
font_style = pygame.font.SysFont("bahnschrift", 25)

def tampil_skor(pilih_skor):
    value = font_style.render("Skor: " + str(pilih_skor), True, (0, 0, 0))
    window.blit(value, [10, 10])

isRun = True
while isRun:
    # 3. User Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x_speed == 0:
                x_speed = -ukuran_blok
                y_speed = 0
            elif event.key == pygame.K_RIGHT and x_speed == 0:
                x_speed = ukuran_blok
                y_speed = 0
            elif event.key == pygame.K_UP and y_speed == 0:
                y_speed = -ukuran_blok
                x_speed = 0
            elif event.key == pygame.K_DOWN and y_speed == 0:
                y_speed = ukuran_blok
                x_speed = 0

    # 4. Logika Tembus Dinding (Ganti ke Sebelahnya)
    x += x_speed
    y += y_speed

    if x >= windowLebar:
        x = 0
    elif x < 0:
        x = windowLebar - ukuran_blok
    
    if y >= windowPanjang:
        y = 0
    elif y < 0:
        y = windowPanjang - ukuran_blok
    
    window.fill((210, 210, 210))

    # 5. Logika Makan Umpan
    pygame.draw.rect(window, (255, 0, 0), (umpan_x, umpan_y, ukuran_blok, ukuran_blok))
    
    if x == umpan_x and y == umpan_y:
        umpan_x = round(random.randrange(0, windowLebar - ukuran_blok) / 20.0) * 20.0
        umpan_y = round(random.randrange(0, windowPanjang - ukuran_blok) / 20.0) * 20.0
        panjang_ular += 1
        score += 10

    # 6. Logika Badan Ular
    kepala_ular = [x, y]
    badan_ular.append(kepala_ular)
    
    if len(badan_ular) > panjang_ular:
        del badan_ular[0]

    for bagian in badan_ular[:-1]:
        if bagian == kepala_ular:
            isRun = False 

    for bagian in badan_ular:
        pygame.draw.rect(window, (0, 150, 0), (bagian[0], bagian[1], ukuran_blok, ukuran_blok))

    # 7. Render & Kecepatan Dinamis
    tampil_skor(score)
    pygame.display.update()
    
    # LOGIKA KECEPATAN: Mulai dari 8 (santai) dan bertambah seiring panjang ular
    kecepatan_sekarang = 8 + (panjang_ular // 2) 
    clock.tick(kecepatan_sekarang)

pygame.quit()
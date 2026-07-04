import pygame

# Init
pygame.init()
isRun = True
clock = pygame.time.Clock() # Tambahkan ini untuk mengatur FPS

# Membuat display surface object
windowLebar = 900
windowPanjang = 900
window = pygame.display.set_mode((windowLebar, windowPanjang))

# Object game
x = 450
y = 450
panjang = 20
lebar = 20
speed = 10

while isRun:
    pygame.time.delay(10)
    # 1. User input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
    
    keys = pygame.key.get_pressed()

    # PERBAIKAN LOGIKA DI SINI:
    # Ke kiri
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed

    # Ke kanan (Batasnya adalah lebar jendela dikurangi lebar kotak)
    if keys[pygame.K_RIGHT] and x < windowLebar - lebar:
        x += speed

    # Ke atas
    if keys[pygame.K_UP] and y > 0:
        y -= speed

    # Ke bawah (Batasnya adalah panjang jendela dikurangi panjang kotak)
    if keys[pygame.K_DOWN] and y < windowPanjang - panjang:
        y += speed

    # 2. Update asset
    window.fill((255, 255, 255)) # Warna background putih
    pygame.draw.rect(window, (255, 120, 0), (x, y, lebar, panjang))

    # 3. Render ke display
    pygame.display.update()
    
    # Atur kecepatan loop (60 FPS) agar gerakan halus
    clock.tick(60)

pygame.quit()
import pygame

pygame.init()
window = pygame.display.set_mode((1280, 720))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(0)

    rect = pygame.Rect(window.get_rect().center, (0, 0)).inflate(*([min(window.get_size())//2]*2))

    pixel_array = pygame.PixelArray(window)

    for x in range(20):
        u = x / (20 - 1)
        color = (round(u*255), 0, round((1-u)*255))
        pixel_array[rect.left + x, rect.top:rect.bottom] = color

    pixel_array.close()

    pygame.display.flip()

pygame.quit()
exit()

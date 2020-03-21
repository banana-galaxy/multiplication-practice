import pygame, random, pyautogui
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 

height = int(pyautogui.size()[1]/3)
size = (height, int(height/1.5))
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Multiplication with Bongo Cat")
 

done = False
new = True
right = False
user = '__'
k = {pygame.K_0:'0', pygame.K_1:'1', pygame.K_2:'2', pygame.K_3:'3', pygame.K_4:'4', pygame.K_5:'5', pygame.K_6:'6', pygame.K_7:'7', pygame.K_8:'8', pygame.K_9:'9'}
kp = {pygame.K_KP0:'0', pygame.K_KP1:'1', pygame.K_KP2:'2', pygame.K_KP3:'3', pygame.K_KP4:'4', pygame.K_KP5:'5', pygame.K_KP6:'6', pygame.K_KP7:'7', pygame.K_KP8:'8', pygame.K_KP9:'9'}
bongo_img = pygame.transform.scale(pygame.image.load("bongoyes.png"), (int(height/3), int(height/5)))
check_img = pygame.transform.scale(pygame.image.load("check.png"), (int(height/5), int(height/5)))
imgs = [bongo_img, check_img]
show_check = False
transparency = 255
alphav = 1
 

clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                if user == '__':
                    continue

                user = list(user)
                count = 0
                while count < 2:
                    try:
                        int(user[count])
                    except ValueError:
                        user.pop(count)
                    count += 1
                user = ''.join(user)
                if int(user) == number:
                    new = True
                    right = True
                else:
                    user = '__'
            if event.key == pygame.K_BACKSPACE:
                user = list(user)
                for i in range(2):
                    try:
                        int(user[1-i])
                        user[1-i] = '_'
                        break
                    except ValueError:
                        pass
                user = ''.join(user)
            for key in k:
                if event.key == key:
                    user = list(user)
                    for char in range(len(user)):
                        try:
                            int(user[char])
                        except ValueError:
                            user[char] = k[key]
                            break
                    user = ''.join(user)
            for key in kp:
                if event.key == key:
                    user = list(user)
                    for char in range(len(user)):
                        try:
                            int(user[char])
                        except ValueError:
                            user[char] = kp[key]
                            break
                    user = ''.join(user)
            
                        
 
    # --- Game logic should go here
    if new:
        user = '__'
        nums = [0,0,0]
        skip = random.randint(0,2)
        nums[0] = random.randint(2,9)
        nums[1] = random.randint(2,9)
        nums[2] = nums[0]*nums[1]
        number = nums[skip]
        nums[skip] = '?'
        way = random.randint(0,1)
        new = False
    if right:
        img = random.choice(imgs)
        show_check = True
        transparency = 255
        right = False

    
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here

    # font, size, bold, italics
    font = pygame.font.SysFont('Calibri', int(size[0]/10), True, False)
    # text, anti-aliased, color
    if way:
        text = font.render(f"{nums[0]} x {nums[1]} = {nums[2]}",True,BLACK)
    else:
        text = font.render(f"{nums[2]} = {nums[1]} x {nums[0]}",True,BLACK)
    # Put the image of the text on the screen at 250x250
    screen.blit(text, [int(size[0]/3), int(size[1]/3)])


    # font, size, bold, italics
    font = pygame.font.SysFont('Calibri', int(size[0]/10), True, False)
    # text, anti-aliased, color
    text = font.render(user,True,BLACK)
    # Put the image of the text on the screen at 250x250
    screen.blit(text, [int(size[0]/2.2), int(size[1]/1.7)])

    # check
    if show_check:
        check_img.set_alpha(transparency)
        screen.blit(img, (int(size[0]/1.35), int(size[1]/3)))
        transparency -= alphav
        alphav = alphav*1.06
        if transparency < 0:
            transparency = 255
            alphav = 1
            show_check = False
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
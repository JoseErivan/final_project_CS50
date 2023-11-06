import pygame
from player import Player
from enemy import Enemy
import random

def main(status, score):
    pygame.init() # Initializing the pygame.

    # Defining the game's font.
    font = pygame.font.Font(None, 50)

    # Creating the dimensions from screen.
    screen_width = 500
    screen_height = 700
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Putting the title from the game.
    pygame.display.set_caption("Runner Taxi Game")

    # Variable to main loop.
    running = True

    # Creating the game score.
    score = score

    # Status from application.
    starting_status = 0
    credit_status = 1
    playing_status = 2
    gameover_status = 3
    game_status = status

    # The main loop from the game.
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if game_status == starting_status:
            # Defining the menu content.
            play_text = font.render("Play", True, (255, 255, 255))
            credit_text = font.render("Credits", True, (255, 255, 255))

            # Creating rectangles to verify the clicks.
            play_rect = play_text.get_rect(center=(250, 500))
            credit_rect = credit_text.get_rect(center=(250, 550))

            # Main loop for the starting screen.
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:# Checking the mouse click.
                        if play_rect.collidepoint(event.pos):
                            game_status = main(playing_status, 0)
                        elif credit_rect.collidepoint(event.pos):
                            game_status = main(credit_status, 0)

                # Cleaning the screen.
                screen.fill((0,0,0))

                # Putting the menu in screen.
                screen.blit(play_text, play_rect)
                screen.blit(credit_text, credit_rect)
        
                # Updating the game window.
                pygame.display.update()

        elif game_status == playing_status:
            # Creating the player and enemy.
            player = Player(screen)

            # Creating the enemies array.
            enemies = []

            # Defining the timer from enemies.
            enemy_timer = pygame.time.get_ticks()
            enemy_delay = random.randint(500, 3000)

            # Main loop for the game.
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                
                # Putting the logic from movimentation.
                keys = pygame.key.get_pressed()
                player.move(keys)
                player.out()

                # Cleaning the screen.
                screen.fill((0,0,0))

                # Putting the player in screen.
                player.draw()

                # Creating the enemies with time condition.
                if pygame.time.get_ticks() - enemy_timer > enemy_delay:
                    create_enemy(screen, enemies)
                    enemy_timer = pygame.time.get_ticks()

                # Drawing and moving the enemies on screen.
                for enemy in enemies:
                    enemy.move()
                    if enemy.out():
                        score += 1
                        enemies.remove(enemy)
                        continue
                    enemy.draw()

                    # Checking the collision with enemies.
                    if player.rect.colliderect(enemy.rect):
                        pygame.time.delay(500)
                        game_status = main(gameover_status, score)

                # Showing the score in screen.
                score_text = font.render(f"Score: {score}", True, (255, 255, 255))
                screen.blit(score_text, (10, 10))
        
                # Updating the game window.
                pygame.display.update()
    
        elif game_status == credit_status:
            # Defining the menu content.
            credits_text = font.render("Made by José Erivan", True, (255, 255, 255))
            credits_text_02 = font.render("to CS50", True, (255, 255, 255))
            back_text = font.render("Return", True, (255, 255, 255))

            # Creating rectangles to verify the clicks.
            credits_rect = credits_text.get_rect(center=(250, 400))
            credits_rect_02 = credits_text_02.get_rect(center=(250, 450))
            back_rect = back_text.get_rect(center=(250, 600))

            # Main loop for the starting screen.
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:# Checking the mouse click.
                        if back_rect.collidepoint(event.pos):
                            game_status = main(starting_status, 0)
                        
                # Cleaning the screen.
                screen.fill((0,0,0))

                # Putting the menu in screen.
                screen.blit(credits_text, credits_rect)
                screen.blit(credits_text_02, credits_rect_02)
                screen.blit(back_text, back_rect)
        
                # Updating the game window.
                pygame.display.update()
        
        elif game_status == gameover_status:
            # Defining the menu content.
            gameover_text = font.render("GAME OVER", True, (255, 255, 255))
            play_again_text = font.render("Play Again", True, (255, 255, 255))
            quit_text = font.render("Quit", True, (255, 255, 255))
            gameover_score_text = font.render(f"Score: {score}", True, (255, 255, 255))

            # Creating rectangles to verify the clicks.
            gameover_rect = gameover_text.get_rect(center=(250, 400))
            gameover_score_rect = gameover_score_text.get_rect(center=(250, 500))
            play_again_rect = play_again_text.get_rect(center=(250, 600))
            quit_rect = quit_text.get_rect(center=(250, 650))

            # Main loop for the starting screen.
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:# Checking the mouse click.
                        if play_again_rect.collidepoint(event.pos):
                            game_status = main(playing_status, 0)
                        elif quit_rect.collidepoint(event.pos):
                            running = False
                        
                # Cleaning the screen.
                screen.fill((0,0,0))

                # Putting the menu in screen.
                screen.blit(gameover_text, gameover_rect)
                screen.blit(gameover_score_text, gameover_score_rect)
                screen.blit(play_again_text, play_again_rect)
                screen.blit(quit_text, quit_rect)
        
                # Updating the game window.
                pygame.display.update()
    
    pygame.quit() # Closing the pygame.

def create_enemy(screen, enemies):
    # Creating enemies to game.
    enemy = Enemy(random.randint(50, 350), random.randint(0, 0), screen)
    enemies.append(enemy)
    return enemy

# Executing the main function for the first time.
if __name__ == "__main__":
    main(0, 0)
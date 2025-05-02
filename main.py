"""
Nom: Nicolas Rodriguez
Groupe: 406
Description: Jeu de Roche, Papier, Ciseaux
"""
from game_state import GameState
from attack_animation import AttackType, AttackAnimation
from random import randint
import time

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Roche, Papier, Ciseaux"


class Game(arcade.Window):
    """
    Classe du jeu de roche, papier, ciseaux
    """
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.game_state = GameState.NOT_STARTED
        self.winner = str
        self.com_win = "L'ordinateur à"
        self.player_win = "Vous avez"
        self.draw_win = "Personne à"
        self.com_rand = int
        self.com_counter = 0
        self.player_counter = 0
        self.com_selected = None
        self.player_selected = None

        self.player_attack_type = {
            AttackType.ROCK: False,
            AttackType.PAPER: False,
            AttackType.SCISSORS: False
        }

        self.com_attack_type = {
            AttackType.ROCK: False,
            AttackType.PAPER: False,
            AttackType.SCISSORS: False
        }

        self.draw_icons = arcade.SpriteList()
        self.face = arcade.Sprite("assets/faceBeard.png", scale=0.25)
        self.draw_icons.append(self.face)
        self.com = arcade.Sprite("assets/compy.png", scale=1.2)
        self.draw_icons.append(self.com)

        self.face.center_x = 220
        self.face.center_y = 225

        self.com.center_x = 640
        self.com.center_y = 225

        self.draw_player_rock = arcade.SpriteList()
        self.player_rock = AttackAnimation(AttackType.ROCK)
        self.draw_player_rock.append(self.player_rock)

        self.draw_player_paper = arcade.SpriteList()
        self.player_paper = AttackAnimation(AttackType.PAPER)
        self.draw_player_paper.append(self.player_paper)

        self.draw_player_scissors = arcade.SpriteList()
        self.player_scissors = AttackAnimation(AttackType.SCISSORS)
        self.draw_player_scissors.append(self.player_scissors)

        self.player_rock.center_x = 130
        self.player_rock.center_y = 140

        self.player_paper.center_x = 330
        self.player_paper.center_y = 140

        self.player_scissors.center_x = 220
        self.player_scissors.center_y = 140

        self.draw_com_rock = arcade.SpriteList()
        self.com_rock = AttackAnimation(AttackType.ROCK)
        self.draw_com_rock.append(self.com_rock)

        self.draw_com_paper = arcade.SpriteList()
        self.com_paper = AttackAnimation(AttackType.PAPER)
        self.draw_com_paper.append(self.com_paper)

        self.draw_com_scissors = arcade.SpriteList()
        self.com_scissors = AttackAnimation(AttackType.SCISSORS)
        self.draw_com_scissors.append(self.com_scissors)

        self.com_rock.center_x = 640
        self.com_rock.center_y = 140

        self.com_paper.center_x = 640
        self.com_paper.center_y = 140

        self.com_scissors.center_x = 640
        self.com_scissors.center_y = 140

    def setup(self):
        """
        Rien
        """

    def on_draw(self):
        """
        Affiche les graphiques du jeu
        """
        self.clear()

        arcade.set_background_color(arcade.color.BLACK)
        title = arcade.Text("Roche, Papier, Ciseaux", 40, 500, arcade.color.RUSTY_RED, 60)
        title.draw()

        arcade.draw_lbwh_rectangle_outline(80, 100, 80, 80, arcade.color.RUSTY_RED)
        arcade.draw_lbwh_rectangle_outline(180, 100, 80, 80, arcade.color.RUSTY_RED)
        arcade.draw_lbwh_rectangle_outline(280, 100, 80, 80, arcade.color.RUSTY_RED)
        arcade.draw_lbwh_rectangle_outline(600, 100, 80, 80, arcade.color.RUSTY_RED)

        self.draw_icons.draw()

        if self.game_state == GameState.NOT_STARTED:
            insruction_text = arcade.Text("Appuyez sur 'espace' pour commencer la partie", 150, 450,
                                          arcade.color.ANTI_FLASH_WHITE, 20)
            insruction_text.draw()

            self.draw_player_rock.draw()
            self.draw_player_paper.draw()
            self.draw_player_scissors.draw()

        elif self.game_state == GameState.ROUND_ACTIVE:
            insruction_text = arcade.Text("Appuyez sur une icône pour faire une attaque!", 150, 450,
                                          arcade.color.ANTI_FLASH_WHITE, 20)
            insruction_text.draw()

            if self.player_selected and self.com_selected:
                if self.player_attack_type[AttackType.ROCK]:
                    self.draw_player_rock.draw()

                elif self.player_attack_type[AttackType.PAPER]:
                    self.draw_player_paper.draw()

                elif self.player_attack_type[AttackType.SCISSORS]:
                    self.draw_player_scissors.draw()

                if self.com_attack_type[AttackType.ROCK]:
                    self.draw_com_rock.draw()

                elif self.com_attack_type[AttackType.PAPER]:
                    self.draw_com_paper.draw()

                elif self.com_attack_type[AttackType.SCISSORS]:
                    self.draw_com_scissors.draw()

            else:
                self.draw_player_rock.draw()
                self.draw_player_paper.draw()
                self.draw_player_scissors.draw()

        elif self.game_state == GameState.ROUND_DONE:
            insruction_text = arcade.Text("Appuyez sur 'espace' pour commencer la prochaine ronde", 125, 450,
                                          arcade.color.ANTI_FLASH_WHITE, 20)
            insruction_text.draw()

            win_text = arcade.Text(f"{self.winner} gagné la ronde", 270, 425,
                                   arcade.color.ANTI_FLASH_WHITE, 20)
            win_text.draw()

            player_score = arcade.Text(f"Score: {self.player_counter}", 600, 265,
                                       arcade.color.ANTI_FLASH_WHITE, 20)
            player_score.draw()

            com_score = arcade.Text(f"Score: {self.com_counter}", 180, 265,
                                    arcade.color.ANTI_FLASH_WHITE, 20)
            com_score.draw()

            if self.player_selected and self.com_selected:
                if self.player_attack_type[AttackType.ROCK]:
                    self.draw_player_rock.draw()

                elif self.player_attack_type[AttackType.PAPER]:
                    self.draw_player_paper.draw()

                elif self.player_attack_type[AttackType.SCISSORS]:
                    self.draw_player_scissors.draw()

                if self.com_attack_type[AttackType.ROCK]:
                    self.draw_com_rock.draw()

                elif self.com_attack_type[AttackType.PAPER]:
                    self.draw_com_paper.draw()

                elif self.com_attack_type[AttackType.SCISSORS]:
                    self.draw_com_scissors.draw()

        elif self.game_state == GameState.GAME_OVER:
            insruction_text = arcade.Text("Appuyez sur 'espace' pour commencer la prochaine partie", 125, 450,
                                          arcade.color.ANTI_FLASH_WHITE, 20)
            insruction_text.draw()

            win_text = arcade.Text(f"{self.winner} gagné la partie", 270, 425,
                                   arcade.color.ANTI_FLASH_WHITE, 20)
            win_text.draw()

            player_score = arcade.Text(f"Score: {self.player_counter}", 600, 265,
                                       arcade.color.ANTI_FLASH_WHITE, 20)
            player_score.draw()

            com_score = arcade.Text(f"Score: {self.com_counter}", 180, 265,
                                    arcade.color.ANTI_FLASH_WHITE, 20)
            com_score.draw()

            if self.player_selected and self.com_selected:
                if self.player_attack_type[AttackType.ROCK]:
                    self.draw_player_rock.draw()

                elif self.player_attack_type[AttackType.PAPER]:
                    self.draw_player_paper.draw()

                elif self.player_attack_type[AttackType.SCISSORS]:
                    self.draw_player_scissors.draw()

                if self.com_attack_type[AttackType.ROCK]:
                    self.draw_com_rock.draw()

                elif self.com_attack_type[AttackType.PAPER]:
                    self.draw_com_paper.draw()

                elif self.com_attack_type[AttackType.SCISSORS]:
                    self.draw_com_scissors.draw()

    def on_update(self, delta_time):
        """
        Permet l'ordinateur de selectionner son attaque et de déterminer le gagnant
        """
        if self.game_state == GameState.ROUND_ACTIVE:
            # L'ordinateur sélectionne son attaque selon la valeur de la variable com_rand
            # (0 = roche, 1 = papier, 2 = ciseaux)
            if self.com_rand == 0:
                self.com_attack_type[AttackType.ROCK] = True
                self.com_selected = True

            elif self.com_rand == 1:
                self.com_attack_type[AttackType.PAPER] = True
                self.com_selected = True

            elif self.com_rand == 2:
                self.com_attack_type[AttackType.SCISSORS] = True
                self.com_selected = True

            if self.player_selected and self.com_selected:
                if self.player_attack_type[AttackType.ROCK]:
                    if self.com_attack_type[AttackType.ROCK]:
                        self.winner = self.draw_win

                    elif self.com_attack_type[AttackType.PAPER]:
                        self.winner = self.com_win
                        self.com_counter += 1

                    elif self.com_attack_type[AttackType.SCISSORS]:
                        self.winner = self.player_win

                elif self.player_attack_type[AttackType.PAPER]:
                    if self.com_attack_type[AttackType.ROCK]:
                        self.winner = self.player_win
                        self.player_counter += 1

                    elif self.com_attack_type[AttackType.PAPER]:
                        self.winner = self.draw_win

                    elif self.com_attack_type[AttackType.SCISSORS]:
                        self.winner = self.com_win
                        self.com_counter += 1

                elif self.player_attack_type[AttackType.SCISSORS]:
                    if self.com_attack_type[AttackType.ROCK]:
                        self.winner = self.com_win
                        self.com_counter += 1

                    elif self.com_attack_type[AttackType.PAPER]:
                        self.winner = self.player_win
                        self.player_counter += 1

                    if self.com_attack_type[AttackType.SCISSORS]:
                        self.winner = self.draw_win

                self.game_state = GameState.ROUND_DONE

        if self.player_counter == 3:
            self.game_state = GameState.GAME_OVER

        elif self.com_counter == 3:
            self.game_state = GameState.GAME_OVER

    def on_key_press(self, key, key_modifiers):
        """
        Permet le joueur de passer à la prochaine ronde
        """
        if key == arcade.key.SPACE:
            if self.game_state == GameState.NOT_STARTED:
                self.com_rand = randint(0, 2)
                self.game_state = GameState.ROUND_ACTIVE

            elif self.game_state == GameState.ROUND_DONE:
                self.player_attack_type[AttackType.ROCK] = False
                self.player_attack_type[AttackType.PAPER] = False
                self.player_attack_type[AttackType.SCISSORS] = False
                self.com_attack_type[AttackType.ROCK] = False
                self.com_attack_type[AttackType.PAPER] = False
                self.com_attack_type[AttackType.SCISSORS] = False
                self.player_selected = False
                self.com_selected = False
                self.com_rand = randint(0, 2)
                self.game_state = GameState.ROUND_ACTIVE

            elif self.game_state == GameState.GAME_OVER:
                self.player_attack_type[AttackType.ROCK] = False
                self.player_attack_type[AttackType.PAPER] = False
                self.player_attack_type[AttackType.SCISSORS] = False
                self.com_attack_type[AttackType.ROCK] = False
                self.com_attack_type[AttackType.PAPER] = False
                self.com_attack_type[AttackType.SCISSORS] = False
                self.player_selected = False
                self.com_selected = False
                self.player_counter = 0
                self.com_counter = 0
                self.com_rand = randint(0, 2)
                self.game_state = GameState.ROUND_ACTIVE

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Permet le joueur de selectioner son attaque
        """
        if self.game_state == GameState.ROUND_ACTIVE:
            if self.player_rock.collides_with_point((x, y)):
                self.player_attack_type[AttackType.ROCK] = True
                self.player_selected = True

            elif self.player_paper.collides_with_point((x, y)):
                self.player_attack_type[AttackType.PAPER] = True
                self.player_selected = True

            elif self.player_scissors.collides_with_point((x, y)):
                self.player_attack_type[AttackType.SCISSORS] = True
                self.player_selected = True


def main():
    """ Main method """
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()

"""
Nom: Nicolas Rodriguez
Groupe: 406
Description: Roche, Papier, Ciseaux
"""
from game_state import GameState
from attack_animation import AttackType, AttackAnimation
from random import randint

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Roche, Papier, Ciseaux"


class Game(arcade.Window):
    """
    La classe principale de l'application
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.game_state = None
        self.winner = None
        self.com_win = "L'ordinateur à"
        self.player_win = "Vous avez"
        self.draw = "Personne à"
        self.com_rand = None
        self.attack_selected = None
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

        self.draw_rock = arcade.SpriteList()
        self.rock = AttackAnimation(AttackType.ROCK)
        self.draw_rock.append(self.rock)

        self.draw_paper = arcade.SpriteList()
        self.paper = AttackAnimation(AttackType.PAPER)
        self.draw_paper.append(self.paper)

        self.draw_scissors = arcade.SpriteList()
        self.scissors = AttackAnimation(AttackType.SCISSORS)
        self.draw_scissors.append(self.scissors)

        self.face.center_x = 220
        self.face.center_y = 225

        self.com.center_x = 640
        self.com.center_y = 225

    def setup(self):
        """
        Rien
        """

    def on_draw(self):
        """
        Met l'écran à jour
        """
        self.clear()

        self.rock.center_x = 640
        self.rock.center_y = 140

        self.paper.center_x = 640
        self.paper.center_y = 140

        self.scissors.center_x = 640
        self.scissors.center_y = 140

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

            self.draw_scissors.draw()
            self.draw_paper.draw()
            self.draw_scissors.draw()

        elif self.game_state == GameState.ROUND_ACTIVE:
            insruction_text = arcade.Text("Appuyez sur une icône pour faire une attaque!", 150, 450,
                                          arcade.color.ANTI_FLASH_WHITE, 20)
            insruction_text.draw()

            if self.attack_selected:
                self.rock.center_x = 640
                self.rock.center_y = 140

                self.paper.center_x = 640
                self.paper.center_y = 140

                self.scissors.center_x = 640
                self.scissors.center_y = 140

                if self.com_attack_type[AttackType.ROCK]:
                    self.draw_rock.draw()

                elif self.com_attack_type[AttackType.PAPER]:
                    self.draw_paper.draw()

                elif self.com_attack_type[AttackType.SCISSORS]:
                    self.draw_scissors.draw()

                self.rock.center_x = 130
                self.rock.center_y = 140

                self.paper.center_x = 330
                self.paper.center_y = 140

                self.scissors.center_x = 220
                self.scissors.center_y = 140

                if self.player_attack_type[AttackType.ROCK]:
                    self.draw_rock.draw()

                elif self.player_attack_type[AttackType.PAPER]:
                    self.draw_paper.draw()

                elif self.player_attack_type[AttackType.SCISSORS]:
                    self.draw_scissors.draw()

                self.attack_selected = False

            else:

                self.draw_rock.draw()
                self.draw_paper.draw()
                self.draw_scissors.draw()

        elif self.game_state == GameState.ROUND_DONE:
            insruction_text = arcade.Text("Appuyez sur 'espace' pour commencer la prochaine ronde", 125, 450,
                                          arcade.color.ANTI_FLASH_WHITE, 20)
            insruction_text.draw()

            win_text = arcade.Text(f"{self.winner} gagné la ronde", 100, 425,
                                   arcade.color.ANTI_FLASH_WHITE, 20)
            win_text.draw()

        elif self.game_state == GameState.GAME_OVER:
            insruction_text = arcade.Text("Appuyez sur 'espace' pour commencer la prochaine partie", 125, 450,
                                          arcade.color.ANTI_FLASH_WHITE, 20)
            insruction_text.draw()

            win_text = arcade.Text(f"{self.winner} gagné la partie", 100, 425,
                                   arcade.color.ANTI_FLASH_WHITE, 20)
            win_text.draw()

    def on_update(self, delta_time):
        """
        Opérations du Jeu
        """
        self.com_rand = randint(0, 2)

        if self.game_state == GameState.ROUND_ACTIVE:
            if self.com_rand == AttackType.ROCK:
                self.com_attack_type[AttackType.ROCK] = True

            elif self.com_rand == AttackType.PAPER:
                self.com_attack_type[AttackType.PAPER] = True

            elif self.com_rand == AttackType.SCISSORS:
                self.com_attack_type[AttackType.SCISSORS] = True

            if self.attack_selected:
                if self.player_attack_type == self.com_attack_type:
                    self.winner = self.draw

                elif self.player_attack_type[AttackType.ROCK]:
                    if self.com_attack_type[AttackType.PAPER]:
                        self.winner = self.com_win
                        self.com_counter += 1

                    elif self.com_attack_type[AttackType.SCISSORS]:
                        self.winner = self.player_win

                elif self.player_attack_type[AttackType.PAPER]:
                    if self.com_attack_type[AttackType.ROCK]:
                        self.winner = self.player_win
                        self.player_counter += 1

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

                if self.player_counter == 3:
                    self.game_state = GameState.GAME_OVER
                    self.winner = self.player_win

                elif self.com_counter == 3:
                    self.game_state = GameState.GAME_OVER
                    self.winner = self.com_win

                self.game_state = GameState.ROUND_DONE

    def on_key_press(self, key, key_modifiers):
        """
        Permet de changer de GameState
        """
        if key == arcade.key.SPACE:
            if self.game_state == GameState.NOT_STARTED:
                self.game_state = GameState.ROUND_ACTIVE

            elif self.game_state == GameState.ROUND_DONE:
                self.player_attack_type[AttackType.ROCK] = False
                self.player_attack_type[AttackType.PAPER] = False
                self.player_attack_type[AttackType.SCISSORS] = False
                self.com_attack_type[AttackType.ROCK] = False
                self.com_attack_type[AttackType.PAPER] = False
                self.com_attack_type[AttackType.SCISSORS] = False
                self.game_state = GameState.ROUND_ACTIVE

            elif self.game_state == GameState.GAME_OVER:
                self.player_attack_type[AttackType.ROCK] = False
                self.player_attack_type[AttackType.PAPER] = False
                self.player_attack_type[AttackType.SCISSORS] = False
                self.com_attack_type[AttackType.ROCK] = False
                self.com_attack_type[AttackType.PAPER] = False
                self.com_attack_type[AttackType.SCISSORS] = False
                self.game_state = GameState.ROUND_ACTIVE

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Permet de selectioner l'attaque
        """
        if self.game_state == GameState.ROUND_ACTIVE:
            if self.rock.collides_with_point((x, y)):
                self.player_attack_type[AttackType.ROCK] = True

            elif self.paper.collides_with_point((x, y)):
                self.player_attack_type[AttackType.PAPER] = True

            elif self.scissors.collides_with_point((x, y)):
                self.player_attack_type[AttackType.SCISSORS] = True

            self.attack_selected = True


def main():
    """ Main method """
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()

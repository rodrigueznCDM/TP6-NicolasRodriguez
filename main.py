"""
Nom: Nicolas Rodriguez
Groupe: 406
Description: Roche, Papier, Ciseaux
"""
from game_state import GameState
from attack_animation import AttackType, AttackAnimation
from enum import Enum

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Roche, Papier, Ciseaux"


class Game(arcade.Window):
    """
    La classe principale de l'application

    NOTE: Vous pouvez effacer les méthodes que vous n'avez pas besoin.
    Si vous en avez besoin, remplacer le mot clé "pass" par votre propre code.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.game_state = GameState
        self.winner = None

        self.player_attack_type = {
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

        self.rock.center_x = 130
        self.rock.center_y = 140

        self.paper.center_x = 330
        self.paper.center_y = 140

        self.scissors.center_x = 220
        self.scissors.center_y = 140

    def setup(self):
        """
        Configurer les variables de votre jeu ici. Il faut appeler la méthode une nouvelle
        fois si vous recommencer une nouvelle partie.
        """
        # C'est ici que vous allez créer vos listes de sprites et vos sprites.
        # C'est aussi ici que vous charger les sons de votre jeu.
        self.game_state = self.game_state.NOT_STARTED

    def on_draw(self):
        """
        Met l'écran à jour
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

        if self.game_state.NOT_STARTED:
            insruction_text = arcade.Text("Appuyez sur 'espace' pour commencer la partie", 150, 450,
                                          arcade.color.ANTI_FLASH_WHITE, 20)
            insruction_text.draw()

            self.draw_rock.draw()

            self.draw_paper.draw()

            self.draw_scissors.draw()

        elif self.game_state.ROUND_ACTIVE:
            if self.player_attack_type[AttackType.ROCK]:
                self.draw_rock.draw()

            elif self.player_attack_type[AttackType.PAPER]:
                self.draw_paper.draw()

            elif self.player_attack_type[AttackType.SCISSORS]:
                self.draw_scissors.draw()

        elif self.game_state.ROUND_DONE:
            insruction_text = arcade.Text("Appuyez sur 'espace' pour commencer la prochaine ronde", 125, 450,
                                          arcade.color.ANTI_FLASH_WHITE, 20)
            insruction_text.draw()

            winner_text = arcade.Text(f"{self.winner} à gagné la ronde", 100, 425,
                                      arcade.color.ANTI_FLASH_WHITE, 20)
            winner_text.draw()

        elif self.game_state.GAME_OVER:
            win_text = arcade.Text(f"{self.winner} à gagné la partie", 100, 425,
                                   arcade.color.ANTI_FLASH_WHITE, 20)
            win_text.draw()

    def on_update(self, delta_time):
        """
        Opérations du Jeu
        """

    def on_key_press(self, key, key_modifiers):
        """
        Permet de changer de GameState
        """
        if key == arcade.key.SPACE:
            if self.game_state == self.game_state.NOT_STARTED:
                self.game_state = self.game_state.ROUND_ACTIVE

            elif self.game_state == self.game_state.ROUND_DONE:
                self.game_state = self.game_state.ROUND_ACTIVE

            elif self.game_state == self.game_state.GAME_OVER:
                self.player_attack_type[AttackType.ROCK] = False
                self.player_attack_type[AttackType.PAPER] = False
                self.player_attack_type[AttackType.SCISSORS] = False

                self.game_state = self.game_state.ROUND_ACTIVE

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Permet de selectioner l'attaque
        """
        if self.game_state == self.game_state.ROUND_ACTIVE:
            if self.rock.collides_with_point((130, 140)):
                self.player_attack_type[AttackType.ROCK] = True
                self.player_attack_type[AttackType.PAPER] = False
                self.player_attack_type[AttackType.SCISSORS] = False

            if self.paper.collides_with_point((330, 140)):
                self.player_attack_type[AttackType.ROCK] = False
                self.player_attack_type[AttackType.PAPER] = True
                self.player_attack_type[AttackType.SCISSORS] = False

            if self.scissors.collides_with_point((330, 140)):
                self.player_attack_type[AttackType.ROCK] = False
                self.player_attack_type[AttackType.PAPER] = False
                self.player_attack_type[AttackType.SCISSORS] = True


def main():
    """ Main method """
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()

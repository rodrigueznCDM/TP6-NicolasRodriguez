"""
Nom: Nicolas Rodriguez
Groupe: 406
Description: Roche, Papier, Ciseaux
"""
from abc import ABC

from game_state import GameState
from attack_animation import AttackType, AttackAnimation

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

        self.player_attack_type = {
            AttackType.ROCK: False,
            AttackType.PAPER: False,
            AttackType.SCISSORS: False
        }

        self.sprites = arcade.SpriteList()
        # Si vous avez des listes de sprites, il faut les créer ici et les
        # initialiser à None.

    def game_screen(self):
        """
        Déssine les écrans affichés (sans les sprites)
        """
        arcade.set_background_color(arcade.color.BLACK)

        title = arcade.Text("Roche, Papier, Ciseaux", 40, 500, arcade.color.RUSTY_RED, 60)
        title.draw()
        arcade.draw_lbwh_rectangle_outline(80, 100, 80, 80, arcade.color.COPPER_RED)
        arcade.draw_lbwh_rectangle_outline(180, 100, 80, 80, arcade.color.COPPER_RED)
        arcade.draw_lbwh_rectangle_outline(280, 100, 80, 80, arcade.color.COPPER_RED)
        arcade.draw_lbwh_rectangle_outline(600, 100, 80, 80, arcade.color.COPPER_RED)

        if self.game_state.NOT_STARTED:
            insruction_text = arcade.Text("Appuyez sur 'espace' pour commencer la partie", 100, 450, arcade.color.ANTI_FLASH_WHITE, 20)
            insruction_text.draw()

        elif self.game_state.ROUND_DONE:
            insruction_text = arcade.Text("Appuyez sur 'espace' pour commencer la prochaine ronde", 100, 450,
                                          arcade.color.ANTI_FLASH_WHITE, 20)
            insruction_text.draw()

            winner_text = arcade.Text(f"{} à gagné la ronde", 100, 425,
                                      arcade.color.ANTI_FLASH_WHITE, 20)
            winner_text.draw()

        elif self.game_state.ROUND_ACTIVE:
            pass

        elif self.game_state.GAME_OVER:
            pass

    def setup(self):
        """
        Configurer les variables de votre jeu ici. Il faut appeler la méthode une nouvelle
        fois si vous recommencer une nouvelle partie.
        """
        # C'est ici que vous allez créer vos listes de sprites et vos sprites.
        # C'est aussi ici que vous charger les sons de votre jeu.
        pass

    def on_draw(self):
        """
        C'est la méthode que Arcade invoque à chaque "frame" pour afficher les éléments
        de votre jeu à l'écran.
        """
        self.clear()

        self.game_screen()

    def on_update(self, delta_time):
        """
        Toute la logique pour déplacer les objets de votre jeu et de
        simuler sa logique vont ici. Normalement, c'est ici que
        vous allez invoquer la méthode "update()" sur vos listes de sprites.
        Paramètre:
            - delta_time : le nombre de milliseconde depuis le dernier update.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Cette méthode est invoquée à chaque fois que l'usager tape une touche
        sur le clavier.
        Paramètres:
            - key: la touche enfoncée
            - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?

        Pour connaître la liste des touches possibles:
        http://arcade.academy/arcade.key.html
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Méthode invoquée lorsque l'usager clique un bouton de la souris.
        Paramètres:
            - x, y: coordonnées où le bouton a été cliqué
            - button: le bouton de la souris appuyé
            - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?
        """
        pass


def main():
    """ Main method """
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()

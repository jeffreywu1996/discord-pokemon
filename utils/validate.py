from poke_client import pokepy_client
import beckett.exceptions

from config.whitelist import admin_whitelist


def validate_pokemon(pokemon_name):
    """Checks if pokemon_name is actually a pokemon.

        Args:
            pokemon_name (str): name of pokemon

        Returns:
            True if valid, False otherwise.
    """
    # Edge case when adding "4" would be valid pokemon
    if pokemon_name.isdigit():
        return False

    try:
        pokepy_client.get_pokemon(pokemon_name)
        return True
    except beckett.exceptions.InvalidStatusCodeError:
        return False


def validate_admin(message_author_id):
    """Checks if the message author has the privilege to use an admin command

        Args:
            message_author_id (int): message author's discord account id

        Returns:
            True if valid, False otherwise.
    """
    return message_author_id in admin_whitelist

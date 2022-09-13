import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class PokeDB(object):
    def __init__(self):
        """Initializes db client to firestore with credentials
        """
        cred = credentials.Certificate('config/pokedb-cred.prod.json')
        firebase_admin.initialize_app(cred)

        self.db = firestore.client()

    def get_users(self):
        """Gets all the users on firebase

        Returns:
            list of usernames in firebase
        """
        users = []
        doc_iter = self.db.collection('users').list_documents()
        for doc in doc_iter:
            users.append(doc.id)

        return users

    def has_account(self, username):
        """Checks if a username is registered on firestore already

        Args:
            username (str): discord username

        Returns:
            True if exists, False otherwise.
        """
        return self.db.collection('users').document(username).get().exists

    def add_user(self, username, start_pokemon):
        """Adds a user (along with a starting pokemon) into firestore

        Args:
            username (str): discord username
            start_pokemon_id (int): starting pokemon id

        Returns:
            The write result corresponding to the committed document.
            (object from firestore)
        """
        data = {
            'username': username,
            'pokemons': {
                start_pokemon: 1
                }
            }

        return self.db.collection('users').document(username).set(data)

    def add_pokemon(self, username, pokemon):
        """Adds a pokemon to the collection for a user in firestore

        Args:
            username (str): discord username
            pokemon_id (int): pokemon id to add

        Returns:
            The write result corresponding to the committed document.
            (object from firestore)
        """
        pokemons = self.get_pokemon(username)

        if pokemon in pokemons:
            pokemons[pokemon] += 1
        else:
            pokemons[pokemon] = 1

        user_ref = self.db.collection('users').document(username)
        return user_ref.update({'pokemons': pokemons})

    def get_pokemon(self, username):
        """Get the collection of pokemons from user in firestore

        Args:
            username (str): discord username

        Returns:
            The write result corresponding to the committed document.
            (object from firestore)
        """

        user_ref = self.db.collection('users').document(username)
        data = user_ref.get().to_dict()

        return data['pokemons']

    def add_spawn(self, pokemon, amount=1):
        """Adds a pokemon into spawn zone in firestore.

        Args:
            pokemon (str): pokemon name
            amount (int): the amount of pokemon to add into spawn

        Returns:
            the total count of that pokemon in db
        """
        spawn_ref = self.db.collection('spawn').document(pokemon)

        # if exist, increment pokemon count by amount
        if spawn_ref.get().exists:
            data = spawn_ref.get().to_dict()
            amount = data['count'] + amount

        data = {
            'count': amount,
            }

        spawn_ref.set(data)

        return amount

    def remove_spawn(self, pokemon):
        """Removes a pokemon into spawn zone in firestore.

        Args:
            pokemon (str): pokemon name

        Returns:
            the total count of that pokemon in db
        """
        spawn_ref = self.db.collection('spawn').document(pokemon)

        if not spawn_ref.get().exists:
            return 0

        data = spawn_ref.get().to_dict()
        amount = data['count']

        if amount > 1:
            spawn_ref.update({
                'count': amount - 1,
                })
        else:
            spawn_ref.delete()

        return amount

    def get_spawns(self):
        """Gets all the users on firebase

        Returns:
            list of usernames in firebase
        """
        users = []
        doc_iter = self.db.collection('spawn').list_documents()
        for doc in doc_iter:
            users.append(doc.id)

        return users


if __name__ == "__main__":
    pokedb = PokeDB()

    # Test for accounts
    # print(pokedb.get_users())
    # print(pokedb.has_account('chickenKatsu'))
    # print(pokedb.get_pokemon('chickenKatsu'))
    # print(pokedb.add_user('testuser4', 'poke1'))
    # print(pokedb.get_pokemon('chickenKatsu'))

    # Test for spawn
    print(pokedb.add_spawn('eevee'))
    print(pokedb.add_spawn('dweeb'))
    print(pokedb.add_spawn('eevee', amount=5))

    print(pokedb.remove_spawn('eevee'))
    print(pokedb.remove_spawn('eevee'))
    print(pokedb.remove_spawn('eevee'))
    print(pokedb.remove_spawn('eevee'))
    print(pokedb.remove_spawn('eevee'))

    print(pokedb.get_spawns())
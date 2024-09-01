"""
Define database logic for WIPE.
"""

import redis

AUTHORIZED_METHODS = {
    'get': 'customer', 
    'set': 'producer'
}

class WIPEDB(object):
    """
    A class to handle database operations for WIPE.
    
    Attributes:
    ----------
    server : redis.Redis
        The Redis database connection.
        
    Methods:
    -------
    get_article(id, role)
        Retrieves an article from the database.
    set_article(id, role)
        Sets an article in the database.
    """

    def __init__(self, db_config: dict):
        """
        Initializes the WIPEDB object.
        
        Parameters:
        ----------
        db_config : dict
            A dictionary containing the Redis database configuration.
        """
        self.server = self.__set_db_connection(db_config)

    def get_article(self, id: str, role: str) -> str:
        """
        Retrieves an article from the database.
        
        Parameters:
        ----------
        id : str
            The ID of the article to retrieve.
        role : str
            The role of the user requesting the article.
        
        Returns:
        -------
        str
            The article content if the user is authorized, otherwise None.
        """
        if role != AUTHORIZED_METHODS['get']:
            return None
        try:
            return self.server.get(id)
        except redis.exceptions.RedisError as e:
            raise e

    def set_article(self, id: str, role: str, content: str) -> bool:
        """
        Sets an article in the database.
        
        Parameters:
        ----------
        id : str
            The ID of the article to set.
        role : str
            The role of the user setting the article.
        content : str
            The content of the article.
        
        Returns:
        -------
        bool
            True if the article was set successfully, otherwise False.
        """
        if role != AUTHORIZED_METHODS['set']:
            return False
        try:
            self.server.set(id, content)
            return True
        except redis.exceptions.RedisError as e:
            raise e

    def __set_db_connection(self, db_config: dict) -> redis.Redis:
        """
        Establishes a connection to the Redis database.
        
        Parameters:
        ----------
        db_config : dict
            A dictionary containing the Redis database configuration.
        
        Returns:
        -------
        redis.Redis
            The Redis database connection.
        """
        try:
            server = redis.Redis(**db_config)
            return server
        except redis.ConnectionError as r_ce:
            raise r_ce
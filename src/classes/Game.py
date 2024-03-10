class Game:
    """
    A singleton class used to represent the state of the fact-or-fiction game. 
    
    ...

    Private Fields
    --------------------------------
    __instance : Game
        The singleton instance of this class.

    __is_game_over: bool
        The state of the game and whether the game is over.

    __score: int
        The player's score.

    __lives: int
        The number of lives the player has. 

    Methods
    --------------------------------
    get_score(): int
        Returns the player's score.

    get_lives(): int
        Returns the number of lives the player has.

    increment_score(): void
        Increments the player's score.

    decrement_lives(): void
        Decrements the number of lives the player has.

    check_game_over(): bool
        Checks the state of the game.

    reset_game(): void
        Resets the game.

    """

    __instance = None

    def __new__(cls):
        if(cls.__instance is None):
            cls.__instance = super(Game, cls).__new__(cls)
            cls.__is_game_over = False
            cls.__score = 0
            cls.__lives = 3
        return cls.__instance

    def get_score(self):
        """
        Returns the player's score.

        """
        return self.__score
    
    def get_lives(self):
        """
        Returns the number of lives the player has.

        """
        return self.__lives
    
    def increment_score(self):
        """
        Increments the player's score.

        """
        if not((self.__is_game_over)):
            self.__score += 1

    def decrement_lives(self):
        """
        Decrements the number of lives the player has.

        """
        if not((self.__is_game_over)):
            self.__lives -= 1
    
    def check_game_over(self):
        """
        Checks the state of the game.

        Returns
        -------
        True if the game is over,
        False otherwise.

        """
        if self.__lives <= 0:
            self.__is_game_over = True
            
        return self.__is_game_over

    def reset_game(self):
        """
        Resets the game state.

        """

        self.__instance = None

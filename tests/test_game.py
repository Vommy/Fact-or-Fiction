from src.classes import Game

def test_singleton():
    """
    Tests that the Game class acts as a Singleton and is the same object
    
    """
    s1 = Game.Game()
    s2 = Game.Game()
    assert s1 == s2 

def test_increment_score():
    """
    Tests that the increment_score() method works correctly.

    """

    #Testing increment_score() on a single singleton.
    s1 = Game.Game()
    assert s1.get_lives() == 3
    assert s1.check_game_over() == False
    s1.increment_score()
    assert s1.get_score() == 1

    #Testing that increment_score() works across multiple instances.
    s2 = Game.Game()
    s2.increment_score()
    assert s2.get_score() == 2

    #Explicitly testing that incrementing the score of one instance leads to the same score across all existing instances.
    s1.increment_score()
    assert s1.get_score() == s2.get_score()

def test_decrement_lives():
    """
    Tests that the decrement_lives() method works correctly.

    """
    
    #Testing decrement_lives() on a single instance.
    s1 = Game.Game()
    s1.decrement_lives()
    assert s1.get_lives() == 2

    #Testing decrement lives on another instance.
    s2 = Game.Game()
    s2.decrement_lives()
    s2.get_lives() == 1

    #Explicitly testing that decrement lives updates across all singleton instances
    #Also tests that the game ends when lives reach 0.
    s1.decrement_lives()
    assert s1.get_lives() == s2.get_lives()
    assert s1.check_game_over() == True

    s1.decrement_lives()
    s1.get_lives() == 0

def test_check_game_over():
    """
    Tests that the check_game_over() method works correctly.
    
    """

    s1 = Game.Game()
    for i in range(3):
        s1.decrement_lives()
    s2 = Game.Game()
    assert s1.get_lives() == 0
    assert s1.check_game_over() == True
    assert s2.check_game_over() == s1.check_game_over()
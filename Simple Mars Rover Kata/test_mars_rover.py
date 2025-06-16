import pytest
from mars_rover import MarsRover

def test_rover_initial_position():
    rover = MarsRover()
    assert rover.execute("") == "0:0:N"
def test_turn_left_from_north():
    rover = MarsRover()
    assert rover.execute("L") == "0:0:W"
def test_turn_left_from_west():
    rover = MarsRover()
    rover.direction = 'W'
    assert rover.execute("L") == "0:0:S"
def test_turn_left_from_south():
    rover = MarsRover()
    rover.direction = 'S'
    assert rover.execute("L") == "0:0:E"
def test_turn_left_from_east():
    rover = MarsRover()
    rover.direction = 'E'
    assert rover.execute("L") == "0:0:N"
def test_turn_right_from_north():
    rover = MarsRover()
    assert rover.execute("R") == "0:0:E"
def test_turn_right_from_east():
    rover = MarsRover()
    rover.direction = 'E'
    assert rover.execute("R") == "0:0:S"
def test_turn_right_from_south():
    rover = MarsRover()
    rover.direction = 'S'
    assert rover.execute("R") == "0:0:W"
def test_turn_right_from_west():
    rover = MarsRover()
    rover.direction = 'W'
    assert rover.execute("R") == "0:0:N"
def test_move_forward_north():
    rover = MarsRover()
    assert rover.execute("M") == "0:1:N"
def test_move_forward_south():
    rover = MarsRover()
    rover.y = 1
    rover.direction = 'S'
    assert rover.execute("M") == "0:0:S"
def test_move_forward_east():
    rover = MarsRover()
    rover.x = 0
    rover.direction = 'E'
    assert rover.execute("M") == "1:0:E"
def test_move_forward_west():
    rover = MarsRover()
    rover.x = 1
    rover.direction = 'W'
    assert rover.execute("M") == "0:0:W"
def test_wrap_around_north_boundary():
    rover = MarsRover()
    rover.y = 9
    rover.direction = 'N'
    assert rover.execute("M") == "0:0:N"
def test_wrap_around_south_boundary():
    rover = MarsRover()
    rover.y = 0
    rover.direction = 'S'
    assert rover.execute("M") == "0:9:S"
def test_wrap_around_east_boundary():
    rover = MarsRover()
    rover.x = 9
    rover.direction = 'E'
    assert rover.execute("M") == "0:0:E"
def test_wrap_around_west_boundary():
    rover = MarsRover()
    rover.x = 0
    rover.direction = 'W'
    assert rover.execute("M") == "9:0:W"
def test_complex_command_mmrmmlm():
    rover = MarsRover()
    assert rover.execute("MMRMMLM") == "2:3:N"
def test_complex_command_mmmmmmmmmm():
    rover = MarsRover()
    assert rover.execute("MMMMMMMMMM") == "0:0:N"



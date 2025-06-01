"""Test for Chapter 1 of the book."""

import pytest

from effective.chap01 import item009


def test_extracting_one_move_from_directions():
    directions = "Go up by 11 steps"
    expected = item009.Move("up", 11)
    actual = item009.extract_move_from_directions(directions)
    assert expected == actual


def test_extracting_multiple_moves_from_directions():
    directions = "Go left by 10 steps then go right by 3 steps, finally go up by 4 steps"
    expected = [item009.Move("left", 10), item009.Move("right", 3), item009.Move("up", 4)]
    actual = item009.extract_move_from_directions(directions)
    assert expected == actual


def test_extracting_moves_raises_when_there_are_no_matches():
    directions = "Go left by ten steps"
    with pytest.raises(ValueError, match="Incorrect match"):
        _ = item009.extract_move_from_directions(directions)

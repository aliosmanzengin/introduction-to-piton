"""
    Every professional traveler must know how to do three things: fix the fire, find the water and extract useful
    information from the nature around him. Programming won't help you with the fire and water, but when it comes to
    information extraction - it might be the thing you need.

    Your task is to find the angle of the sun above the horizon knowing the time of the day. The sun rises in the East at
    6:00 AM, which corresponds to an angle of 0 degrees. At 12:00 PM the sun reaches its zenith, which means that the
    angle equals 90 degrees. 6:00 PM is the time of the sunset so the angle is 180 degrees. If the input will be the time
    of the night (before 6:00 AM or after 6:00 PM), your function should return - "I don't see the sun!".
    Example:

    sun_angle("07:00") == 15
    sun_angle("12:15"] == 93.75
    sun_angle("01:23") == "I don't see the sun!"

"""
import pytest


def calculate_angle(time_entry: str) -> str | int:
    hour, minute = map(int, time_entry.split(":"))
    if hour >= 18 or hour < 6:
        return "I don't see the sun!"
    angle = ((hour - 6) * 60 + minute) / 4

    return angle


def test_calculate():
    angle = calculate_angle("02:15")
    assert angle == 93.75



# Difficulty: Medium
# Tags: difference array

# Problem
# You are on a street with street lights, represented by an array lights. Each light is given as [position, radius], which means that the light is located at position, and shines to the left and right at a distance of radius. Let's say the brightest spot on the street is the spot where the most lights are shining. Return any such position.
# Note that the street is extremely long - position <= 10^18.

# Solution
# We create an array of lights changes. Each element is a change at a given position. So, change[pos[i]-radius] = 1 and change[pos[i]+radius+1] = -1, meaning that when the light starts the change is 1, when it ends the change is -1. Then we sort this array and check prefix sums for the maximum lighted area and return its position.

def find_brightest_position(lights: list[list[int]]) -> int:
    change = []
    for position, radius in lights:
        change.append([position - radius, 1])
        change.append([position + radius + 1, -1])

    change.sort()
    ans = curr = brightest = 0
    for position, value in change:
        curr += value
        if curr > brightest:
            brightest = curr
            ans = position

    return ans

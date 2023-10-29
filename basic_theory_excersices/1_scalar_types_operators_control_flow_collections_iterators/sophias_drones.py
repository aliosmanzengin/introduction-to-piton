"""Sophia's drones are not soulless and stupid drones; they can make and have friends. In fact, they already are
working for their own social network for drones! Sophia has received the data about the connections between drones.
She wants to know more about relations between them. We have an array of straight connections between drones. Each
connection is represented as a string with two names of friends separated by a hyphen. For example: "dr101-mr99"
means that the dr101 and mr99 are friends. Implement a function that allows us to determine more complex connections
between drones. You are given two names also. Try to determine if they are related through common bonds by any depth.
For example: if two drones have common friends or friends who have common friends and so on.


Let's look at examples:

scout2 and scout3 have the common friend scout1 so they are related. super and scout2 are related through sscout,
scout4, and scout1. But dr101 and sscout are not related.

Input: three arguments: Information about friends as a tuple of strings; first name as a string; second name as a string.
Output: Are these drones related or not as a boolean.
Example:
        check_connection(
          ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
           "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
          "scout2", "scout3") == True
        check_connection(
          ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
           "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
          "dr101", "sscout") == False
"""
#
# from collections import deque
#
#
# def check_connection(friendships, drone1, drone2):
#     # Initialize an empty adjacency list to represent the graph
#     graph = {}
#
#     # Populate the graph with the friendships information
#     for friendship in friendships:
#         a, b = friendship.split("-")
#         if a not in graph:
#             graph[a] = []
#         if b not in graph:
#             graph[b] = []
#         graph[a].append(b)
#         graph[b].append(a)
#
#     # Initialize a queue for BFS and a set to keep track of visited nodes
#     queue = deque([drone1])
#     visited = set([drone1])
#
#     # Perform BFS to find a path from drone1 to drone2
#     while queue:
#         current_drone = queue.popleft()
#         if current_drone == drone2:
#             return True
#         for neighbor in graph.get(current_drone, []):
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 queue.append(neighbor)
#
#     return False
#
#
# # Test the function with example cases
# print(check_connection(
#     ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
#      "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
#     "scout2", "scout3"))  # Should return True
#
# print(check_connection(
#     ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
#      "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
#     "dr101", "sscout"))  # Should return False


def check_connection_iterative(friendships, drone1, drone2):
    # Initialize an empty adjacency list to represent the graph
    graph = {}

    # Populate the graph with the friendships information
    for friendship in friendships:
        a, b = friendship.split("-")
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    # Initialize lists to keep track of nodes to visit and visited nodes
    to_visit = [drone1]
    visited = []

    # Perform DFS iteratively
    while to_visit:
        current_drone = to_visit.pop()  # Remove and return the last element from the list
        if current_drone == drone2:
            return True
        visited.append(current_drone)
        for neighbor in graph.get(current_drone, []):
            if neighbor not in visited and neighbor not in to_visit:
                to_visit.append(neighbor)

    return False


# Test the function with example cases
print(check_connection_iterative(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    "sscout", "scout3"))  # Should return True

print(check_connection_iterative(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    "dr101", "sscout"))  # Should return False

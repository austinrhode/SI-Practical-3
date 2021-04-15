"""
Write a class to Represent a message.
A message should consist of a sender, receiver, and text

Each attribute should have an getter (accessor).

A message should also be able to tell if two people are messaging
if the sender is the receiver of the other message and the receiver is the sender of
the other message.

You will also need to implement a string to be printed to the user as well as string that
is printed to the developer. This can be whatever you want.

Two messages are considers equal if the they have the same sender, receiver, and text.
This should be represented in your class.

Lastly, a message needs to be hashable. The hash function should be the sum of
the hash value of the sender, receiver, and text.
Hint: use the built in hash function to get somethings hash value. 
"""
class Message:
    pass
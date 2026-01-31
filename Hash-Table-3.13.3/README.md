HashTable Problem Statement

Description

Implement a HashTable class in Python that stores key-value pairs using a hash of the key. The hash table should handle collisions using nested dictionaries.

⸻

Requirements
	1.	The class should have a collection attribute initialized as an empty dictionary.
	2.	hash(key)
	•	Takes a string key.
	•	Returns a hashed value computed as the sum of ASCII values of each character in the string.
	3.	add(key, value)
	•	Adds a key-value pair to the hash table.
	•	Uses the hash of the key to store the pair in the collection.
	•	Handles collisions by storing multiple keys with the same hash in a nested dictionary.
	4.	remove(key)
	•	Deletes the key and its value from the hash table safely.
	5.	lookup(key)
	•	Returns the value associated with the key.
	•	Returns None if the key is not present.
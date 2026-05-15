Problem 1 (Easy): Music Player Song Class
Create a simple music library system by defining a Song class that stores basic information about music tracks.

Requirements:

1. Define a class named Song with an __init__ method that takes three parameters: title, artist, and duration (in minutes)
2. Store these parameters as instance variables: self.title, self.artist, and self.duration
3. Create a method named display_info() that prints song details in this exact format: "Title: {title}, Artist: {artist}, Duration: {duration} min"
4. Create a method named get_duration_seconds() that returns the duration converted to seconds (duration × 60)
5. Create two Song objects with the test data provided below
6. Call display_info() on both songs
7. Print the duration in seconds for the second song using get_duration_seconds()
Input

```First song: "Yesterday", "The Beatles", 2.5
Second song: "Bohemian Rhapsody", "Queen", 6.0```

Expected Output
```Title: Yesterday, Artist: The Beatles, Duration: 2.5 min
Title: Bohemian Rhapsody, Artist: Queen, Duration: 6.0 min
360```
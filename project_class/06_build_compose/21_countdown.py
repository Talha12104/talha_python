class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start + 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current

# Example usage
for num in Countdown(5):
    print(num)  # Outputs: 5, 4, 3, 2, 1, 0
class Walk:
    def move(self):
        return "Walking"

class Swim:
    def move(self):
        return "Swimming"

# Duck inherits from both Walk and Swim
class Duck(Walk, Swim):
    def action(self):
        # Calls the first 'move' found in the MRO
        return f"Land: {self.move()}" 

print("=== 1. Basic Multiple Inheritance ===")
donald = Duck()
print(donald.action())  # Uses Walk.move() because Walk is listed first
print(f"MRO: {[cls.__name__ for cls in Duck.__mro__]}")
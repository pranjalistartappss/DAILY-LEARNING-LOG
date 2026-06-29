#Write a closure that stores a secret message and provides access to it only through an inner function.

def secret(msg):
    def show():
        return msg
    return show

s = secret("Python")
print(s())
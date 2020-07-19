# pip allows us to install packages from the pypi.org official website and use in our programs

import pyjokes

joke = pyjokes.get_joke("en", "neutral")
print(joke)

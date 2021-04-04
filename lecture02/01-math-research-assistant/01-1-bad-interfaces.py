### Lecture 2. Inversion of Control
### 01-1. Bad Interfaces

### SRP violated
### Not consistent
### Redundant
### Not documented
### Verbose

import sys
import random

import requests

class Natural():

    def get_name(self):
        return "Natural number"

    def get_description(self):
        return "Natural is an integer number between 0 and infinity."

    ### Redundancy: get_sample, get_random_sample
    ### Strange method with strange result.
    def get_sample(self):
        return 42

    def get_random_sample(self):
        return random.randrange(0, 100)

    ### Redundancy: get_wikipedia_link, get_wikipedia_page
    ### Invalid responsibility (why it knows about Wikipedia?)
    def get_wikipedia_link(self):
        return "https://en.wikipedia.org/wiki/Natural_number"

    ### Invalid responsibility (the definition class should not interact with the internet)
    ### Invalid responsibility (why it knows about Wikipedia?)
    ### Duplicated code across classes
    def get_wikipedia_page(self):
        r = requests.get(self.get_wikipedia_link())
        return r.content

### ------------------------------------------------------------------------

class Prime():

    def get_name(self):
        return "Prime number"

    def get_description(self):
        return """A prime number (or a prime) is a natural number greater
than 1 that cannot be formed by multiplying two smaller natural numbers."""

    ### Redundancy: get_sample, get_random_sample
    ### Strange method with strange result.
    def get_sample(self):
        return 7;

    def get_random_sample(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                  43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        return primes[random.randrange(0, 25)]

    ### Redundancy: get_wikipedia_link, get_wikipedia_page
    ### Invalid responsibility (why it knows about Wikipedia?)
    def get_wikipedia_link(self):
        return "https://en.wikipedia.org/wiki/Prime_number"

    ### Invalid responsibility (the definition class should not interact with the internet)
    ### Invalid responsibility (why it knows about Wikipedia?)
    ### Duplicated code across classes
    def get_wikipedia_page(self):
        r = requests.get(self.get_wikipedia_link())
        return r.content

### ------------------------------------------------------------------------

class Number:

    def get_name(self):
        return "Number"

    def get_description(self):
        return "A number is a mathematical object used to count, measure, and label."

    ### Redundancy: get_sample, get_random_sample
    ### Strange method with strange result.
    def get_sample(self):
        return 7

    def get_random_sample(self):
        return random.randrange(0, 100)

    ### Redundancy: get_wikipedia_link, get_wikipedia_page
    ### Invalid responsibility (why it knows about Wikipedia?)
    def get_wikipedia_link(self):
        return "https://en.wikipedia.org/wiki/Number"

    ### Invalid responsibility (the definition class should not interact with the internet)
    ### Invalid responsibility (why it knows about Wikipedia?)
    ### Duplicated code across classes
    def get_wikipedia_page(self):
        r = requests.get(self.get_wikipedia_link())
        return r.content


if __name__ == "__main__":
    print("Math Research Assistant")

    nat = Natural()
    print(nat.get_description())
    print(nat.get_sample())
    print(nat.get_random_sample())
    print(nat.get_wikipedia_link())

    ### Heavy operation
    # print(nat.get_wikipedia_page())

    prime = Prime()
    print(prime.get_description())
    print(prime.get_sample())
    print(prime.get_random_sample())
    print(prime.get_wikipedia_link())

    ### Heavy operation
    # print(prime.get_wikipedia_page())

    num = Number()
    print(num.get_description())
    print(num.get_sample())
    print(num.get_random_sample())
    print(num.get_wikipedia_link())

    ### Heavy operation
    # print(num.get_wikipedia_page())

#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The runtime complexity is O(n). As the input n increases, the runtime increases at a proportional rate of n * n²

b) The runtime complexity is O(nlog(n)). The for loop is a O(n) operation that iterates through each value, but the while loop, which is a O(log(n)) operation, is executed for each n and runtime increases at a slightly slower rate as the input size increases.

c) The runtime complexity is O(n). The function is called recursively n times before it reaches the base case.

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudo-code AND give the runtime complexity of your solution.

I would implement a binary search to determine the value of floor f. I would determine the ground floor to be floor 0 and test with the n-th floor being the top floor. By starting from the middle floor, I would drop an egg to see if it cracks, signaling that I am above floor f. By cutting down the midpoints between the floors, I am able to locate floor f while dropping/breaking more eggs than if I had gone through each floor and dropped an egg. THe runtime complexity of a binary search is O(log(n)).

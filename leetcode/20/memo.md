# step 1

- approach 1: Remove valid bracket pairs one by one
	- Time complexity: O(n^3)
		- 1. Each step removes 2 brackets.
		- 2. We iterate through the entire string for each step.
		- 3. String concatenation involves copying, which adds overhead.
	- Space complexity: O(n^2) (I'm not very confident)
		- Call stack usage: O(n), since we can have up to n/2 recursive calls.
		- Each recursive calls create a new string: O(n) space per call.
		- Therefore, the cumulative space could reach O(n^2)
- approach 2. Use a stack to match brackets
	- Time complexity: O(n), as we scan the string once.
	- Space complexity: O(n), since at most `n` brackets will be stored on the stack.

# step 2

- Since Python dictionaries are mutable, naming a local dictionary `BRACKET_PAIRS` in all caps might be misleading, as all-caps typically implies a global constant.
- Use early `return` or `continue` statements to reduce nesting and improve readability (?) in Python code.

# step 3

class Solution:
    def isValid(self, s: str) -> bool:
        opening = {"(", "[", "{"}
        closing = {")": "(", "]": "[", "}": "{"}
        stack: list[str] = []

        for bracket in s:
            if bracket in opening:
                stack.append(bracket)
            elif not stack or stack.pop() != closing[bracket]:
                return False

        return not stack

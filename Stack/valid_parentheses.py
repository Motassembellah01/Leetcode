class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "]": "[", "}":"{"}
        for charac in s:
            if charac in closeToOpen:
                if stack and stack[-1] == closeToOpen[charac]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(charac)

        return len(stack) == 0
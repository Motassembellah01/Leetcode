class Solution:
    def lengthLongestPath(self, input: str) -> int:
        # Stack[i] will store the total path length up to depth i
        # Example: ["dir", "subdir"] → stack = [3, 3+1+6]
        stack = []
        maximLen = 0  # Stores the longest absolute file path found

        # Split input into lines (each line = file or directory)
        for line in input.split('\n'):
            # Depth = number of leading tabs → indicates level in hierarchy
            depth = line.count('\t')

            # Extract actual file/directory name (remove leading tabs)
            name = line.strip('\t')
            
            # Ensure stack represents the correct parent path
            # If current depth is smaller, pop until matching parent level
            while len(stack) > depth:
                stack.pop()
            
            # Compute current path length:
            # If there's a parent, add "/" (+1) and current name length
            if stack:
                current_length = stack[-1] + len(name) + 1
            else:
                # Root level (no parent)
                current_length = len(name)
            
            # If it's a file (contains '.'), update max length
            if '.' in name:
                maximLen = max(maximLen, current_length)
            
            # Push current path length to stack (for future children)
            stack.append(current_length)

        return maximLen
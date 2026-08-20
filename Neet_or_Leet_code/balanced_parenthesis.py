# checking for the balanced paranthesis
def is_balanced(strs):
    stack = []
    par = {")": "(", "}": "{", "]": "["}

    for c in strs:
        if c in par.values():
            stack.append(c)
        elif c in par:
            if not stack or stack.pop() != par[c]:
                return False
    return len(stack) == 0

print(is_balanced("{[({})]}"))

class Stack :
    def __init__(self):
        self.top = []

    def size(self):
        return len(self.top)

    def isEmpty(self) :
        return self.size() == 0

    def clear(self) :
        self.top = []

    def push(self, item):
        self.top.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)

    def peek(self):
        if not self.isEmpty() :
            return self.top[-1]


def isValidSource(srcfile):
    stack = Stack()
    lcnt = 1
    ccnt = 0
    eCode = 0
    for line in srcfile: 
        for ch in line:
            if ch == '\n': lcnt += 1
            ccnt += 1

            if ch in ("'"):
                if(stack.peek() in ("'")) :
                    stack.pop()
                    continue
                else:
                    stack.push(ch)
                    continue
            if stack.peek() == "'":
                continue;

            if ch in ("{[(") :
                stack.push(ch)
            elif ch in ("}])"):
                if stack.isEmpty() :
                    eCode = 2
                    return eCode, lcnt, ccnt
                    
                else :
                    left = stack.pop()
                    if (ch == "}" and left != "{") or \
                    (ch == "]" and left != "[") or \
                    (ch == ")" and left != "(") :
                        eCode = 3
                        return eCode, lcnt, ccnt
                        
    if stack.isEmpty() != True: eCode = 1
    return eCode, lcnt, ccnt

}
]]]]
// 주 함수
void main()
{
	CheckMatching("ArrayStack.h");
	CheckMatching("03장-CheckBracketMain.cpp");
}
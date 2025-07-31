class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for char in s:
            if char=="(" or char=="{" or char=="[":
                st.append(char)
            else:
                if(len(st)==0):
                    return False
                if((char=="}" and st[-1]=="{") or (char=="]" and st[-1]=="[") or(char==")" and st[-1]=="(")):
                    st.pop()
                else:
                    return False
        return len(st)==0
        
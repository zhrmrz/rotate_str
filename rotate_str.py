class Sol:
    def rotate_str(self,goal,s):
        if len(goal)!=len(s):
            return False
        return s in goal*2

if __name__ == '__main__':
    p=Sol()
    print(p.rotate_str(goal='cdeab',s='abcde'))

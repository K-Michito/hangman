def hangman(word):
    wrong=0
    stages=["",
            "_______      ",
            "|            ",
            "|      |     ",
            "|      |     ",
            "|      |     ",
            "|      |     ",
            "|      0     ",
            "|     /|>    ",
            "|     //     ",
            "|            ",
            ]
    rletters=list(word)
    board=["_"] * len(word)
    #alph=[a,b,c,d,e,,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,z]
    #アルファベットを数字に割り当てて、距離を定義したい
    win=False
    print("Welcome to Hangman!")
    print(" ".join(board))
    while wrong<len(stages)-1:
        print("\n")
        msg="1文字予想してください。"
        char=input(msg)
        if char in rletters:
            cind=rletters.index(char)
            board[cind]=char
            rletters[cind]='$'
        else:
            wrong+=1
        print(" ".join(board))
        e=wrong+1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print(" You are Winner!!!")
            print(" ".join(board))
            win=True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("ざんねん、失敗。正解は{}".format(word))


prob=input("wordを入力してください:")
for i in range(0,100):
    print("\n")
hangman(prob)

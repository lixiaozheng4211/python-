print("============欢迎来到牢大的密室逃脱============\n")
p=1
while(p!=0):
    #-----------入口-----------
    if(p==1):
        print('man!,你现在位于密室逃脱的入口处，要不要进去看看？1-yes 2-no')
        a=input()
        if(a=="1"):
            p=2
        else:
            p=0
            print('请离开！')
    if(p==2):
        print('man!你现在来到了密室大厅')
        print('现在你有四种选择')
        print('1-青龙殿 2-白虎殿 3-朱雀殿 4-返回入口回家睡觉')
        b=input()
        if(b=='1'):
            p=3
        elif(b=='2'):
            p=4
        elif(b=='3'):
            p=5
        elif(b=='4'):
            p=1
            print('赶快回家睡觉')
        else:
            p=0
    if(p==3):
        print('再进去之前你碰到了牢二，他给了你一把金色钥匙并告诉你后面会对你有帮助')
        print('你已进入青龙殿')
        print('在你面前有一个宝箱，但是上面有一把锁，你想起了牢二给你的钥匙，半信半疑的把钥匙插了上去')
        print('箱子开了!')
        print('恭喜你获得装备青龙之戒--提高精神念力')
        print('现在你有两种选择 1-返回大厅 2-就在这耗时间')
        c=input()
        if(c=='1'):
            p=2
        else:
            p=0
    if(p==4):
        print("你已进入白虎殿")
        print('\n伴随着一声巨响，一位魁梧的中年男子出现在你面前，“小伙子，你是来玩密室逃脱的吗”')
        print('\n你点点头，仔细打量着这位大叔')
        print('\n“看来我们很有缘呢，呐，我把这把白虎匕送给你吧！”')
        print('你连忙感谢他，接过了这把透露着锋芒的匕首')
        print('现在你有两种选择 1-返回大厅 2-就在这耗时间')
        d=input()
        if(d=='1'):
            p=2
        else:
            p=0
    if(p==5):
        print('你已进入朱雀殿')
        print('\n“嗯~  小兄弟，你是来参加密室逃脱的吗？”\n')
        print('映入眼帘的是一位身着紫红色旗袍的美妇，美眸里透露着冷艳之意')
        print('你咽了咽口水，慌乱的点点头')
        print('\n“好嘛，小兄弟不必紧张，我不是什么坏人，但是我希望你帮我一个忙”\n')
        print('什么忙，你说，只要我猪猪侠能够帮的就一定会帮你')
        print('\n“你能不能帮我解决掉玄武殿的那头千年王八，作为酬劳，我把我祖传朱雀炎甲送给你，你一定要活着出去！\n')
        print('你沉重的点点头，眼神坚定')
        print('现在你有两种选择 1-返回大厅 2-进入玄武殿，决战千年玄武怪！')
        e=input()
        if(e=='2'):
            p=6
        else:
            p=2
    if(p==6):
        print('你已进入玄武殿')
        print('\n轰隆隆-------------------------------\n')
        print('一头通体呈现紫金色的巨龟出现在你的面前')
        print('\n“此路是我开，此殿是我盖，要想过此路，除非击败我，吼~~~”\n')
        print('你深吸一口气，作为超级英雄牢大，怎会畏惧一只王八，你大步向前，像是下定了某种决心，来吧，出生！')
        print('经过你不懈的努力，最终在前面所获得的宝物的加持下，击败了千年玄武！')
        print('你长舒一口气，心里默念：我做到了！')
        print('现在你有两种选择 1-去出口 2-就在这耗时间')
        f=input()
        if(f=='1'):
            p=0
            print('恭喜你成功逃脱密室，欢迎下次光临！')
        else:
            print('man,what can i cay!，你就在这呆一辈子吧')

        

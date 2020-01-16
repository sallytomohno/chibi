import random
s = ['「おなかすいた」','「ねむたいよ」','「さんぽ行きたい」','「一緒に遊んで！」','「一緒に話そう！」' ]
u = random.choice(s)
print('ぽんた',u)
if u == '「おなかすいた」' :
        t = input('お菓子をあげる？(yes or no)')
        if(t == 'yes'):
            print("ぽんた「わーい、甘くて美味しい!」")
        else:
            print("ぽんた「ご飯の時間まで我慢するよ...」")
if u == '「ねむたいよ」' :
        t = input('布団をかけてあげる？(yes or no)')
        if(t == 'yes'):
            print("ぽんた「暖かいな！おやすみなさい」")
        else:
            print("ぽんた「さ.さむいな...」")
if u == '「さんぽ行きたい」' :
        t = input('お出かけする？(yes or no)')
        if(t == 'yes'):
            print("ぽんた「外の空気はおいしいね♪」")
        else:
            print("ぽんた「僕ダイエットしてるのに...」")
if u == '「一緒に遊んで！」' :
        t = input('遊んであげる？(yes or no)')
        if(t == 'yes'):
            print("ぽんた「手裏剣で遊ぼう♪」")
        else:
            print("ぽんた「じゃあいいもん。浮気するもん！」")
if u == '「一緒に話そう！」' :
        t = input('平野紫耀派?(yes）　岸優太派?(no)　(yes or no)')
        if(t == 'yes'):
            print("ぽんた「僕より天然だよね」")
        else:
            print("ぽんた「英語が話せて羨ましいな」")

if u == '「好きなプロ野球球団は？」' :
        t = input('阪神？　巨人？　　（hanshin or kyozin）')
        if(t == 'hanshin'):
            print("六甲おろーしに～♪")
        else:
            print("闘魂込めて～♪")
















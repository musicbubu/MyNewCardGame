import random

# --- 1. 初始化資料 ---
diamonds = 1000
my_collection = []  # 存放抽到的卡片 (List 結構)

# 定義牌組與稀有度 (Dictionary 結構)
card_pool = {
    "SSR": ["✨聖光龍", "🌑暗黑冥王"],
    "SR": ["🔥火戰士", "💧水精靈", "🌿木守衛"],
    "R": ["🏹哥布林", "🦇小蝙蝠", "🍄史萊姆"]
}

print("=== 歡迎來到 AI 抽卡模擬器 ===")
print(f"目前餘額：{diamonds} 鑽石")

while True:
    print("\n[1] 單抽 (100鑽) [2] 查看倉庫 [3] 離開")
    choice = input("請輸入指令：")

    if choice == "1":
        if diamonds >= 100:
            diamonds -= 100
            # 隨機判定稀有度 (SSR: 10%, SR: 30%, R: 60%)
            rarity = random.choices(["SSR", "SR", "R"], weights=[10, 30, 60])[0]
            card = random.choice(card_pool[rarity])
            
            print(f" >>> 獲得：{card} (稀有度: {rarity})")
            my_collection.append(card) # 資料結構：將資料加入 List
            print(f" 剩餘鑽石：{diamonds}")
        else:
            print("❌ 鑽石不足！")

    elif choice == "2":
        print(f"\n--- 我的倉庫 (目前共有 {len(my_collection)} 張卡) ---")
        if not my_collection:
            print("目前空空如也...")
        else:
            for c in my_collection:
                print(f"- {c}")

    elif choice == "3":
        print("遊戲結束，下次見！")
        break
    else:
        print("無效指令，請重新輸入。")
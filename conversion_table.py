from enum import Enum


class VoiceType(Enum):
    DORM = "Dorm"
    BATTLE = "Battle"
    COMMUNICATIONS = "Communications"
    SYSTEM = "System"
    OTHER = "Other"


table_languages = ['cn', 'en']


voice_conversion_table: dict[VoiceType, dict[str, tuple[str]]] = {
    VoiceType.DORM: {
        # dorm
        "008": ("早上问候", "Morning greeting"),
        "009": ("晚间问候", "Night greeting"),
        "010": ("深夜问候", "Late night greeting"),

        "005": ("收到邮件", "Mail received"),

        "013": ("元旦", "New Year"),
        "014": ("春节", "Spring Festival"),
        "015": ("圣诞节", "Christmas"),
        "016": ("情人节", "Valentine's Day"),
        "017": ("卡拉彼丘纪念日", "Strinova anniversary"),
        "065": ("七夕", "Qixi Festival"),

        "030": ("战斗胜利", "Winning"),
        "031": ("战斗胜利MVP", "MVP"),
        "032": ("战斗失败", "Losing"),
        "033": ("战斗失败SVP", "SVP"),

        "001": ("点击互动", "Touching"),
        "002": ("点击互动", "Touching"),
        "003": ("点击互动", "Touching"),
        "004": ("摸头", "Head pat"),
        "059": ("互动交谈", "Touching"),
        "060": ("互动交谈", "Touching"),
        "061": ("互动交谈", "Touching"),
        "062": ("互动交谈", "Touching"),
        "063": ("互动交谈", "Touching"),
        "025": ("好感度上升后触碰", "Touching (high favorability)"),
        "026": ("好感度上升后触碰", "Touching (high favorability)"),
        "027": ("好感度上升后触碰", "Touching (high favorability)"),
        "028": ("好感度上升后触碰", "Touching (high favorability)"),
        "029": ("好感度上升后触碰", "Touching (high favorability)"),
        "035": ("好感提升后交谈", "Chatting (friendship 1)"),
        "036": ("好感提升后交谈", "Chatting (friendship 3)"),
        "037": ("好感提升后交谈", "Chatting (friendship 7)"),
        "038": ("好感提升后交谈", "Chatting (friendship 10)"),
        "039": ("打招呼", "Greeting"),
        "040": ("打招呼", "Greeting"),
        "041": ("打招呼", "Greeting"),
        "042": ("打招呼", "Greeting"),
        "043": ("打招呼", "Greeting"),
        "023": ("打招呼", "Greeting (friendship 10)"),
        "044": ("待机", "Idle"),
        "045": ("待机", "Idle"),
        "046": ("待机", "Idle"),
        "047": ("待机", "Idle"),
        "048": ("待机", "Idle"),
        "049": ("打断角色状态", "Interrupting"),
        "050": ("打断角色状态", "Interrupting"),
        "051": ("打断角色状态", "Interrupting"),
        "052": ("打断角色状态", "Interrupting"),
        "053": ("打断角色状态", "Interrupting"),
        "054": ("近景交谈", "Close up chatting"),
        "055": ("近景交谈", "Close up chatting"),
        "058": ("近景交谈", "Close up easter egg"),
        "064": ("好感度10语音", "Friendship 10 easter egg"),
        "024": ("感谢礼物", "Thanking a gift"),
        "056": ("感谢礼物", "Thanking a gift (close up)"),
        "057": ("感谢专属礼物", "Thanking a special gift"),

        "152": ("?", "?"),
        "153": ("?", "?"),
        "154": ("?", "?"),
        "155": ("生气", "Angry"),
        "156": ("安慰玩家", "Comforting the player"),
        "157": ("?", "?"),
        "158": ("?", "?"),
        "159": ("?", "?"),
        "160": ("?", "?"),
        "161": ("?", "?"),
        "162": ("?", "?"),
        "163": ("?", "?"),
        "164": ("?", "?"),
        # no prefix
        "011": ("玩家生日", "Player birthday"),
        "034": ("玩家生日", "Player birthday"),
        "012": ("角色生日", "Character birthday"),
        "700": ("生日贺卡", "Birthday greeting card"),
        "701": ("生日蛋糕", "Birthday cake"),
        "702": ("生日回礼", "Reciprocating birthday gift"),
        "703": ("讨论生日礼物", "Discussing birthday gift"),
        "704": ("收到生日礼物", "Receiving birthday gift"),
        "705": ("收到礼物", "Receiving birthday gift"),
        "006": ("朋友生日", "Friend birthday"),
        "007": ("朋友生日", "Friend birthday"),
    },
    VoiceType.BATTLE: {
        "066": ("选择角色", "Character select"),
        "067": ("确认准备", "Confirm"),
        "068": ("开场台词", "Opening line"),
        "069": ("开场台词", "Opening line"),
        "070": ("开场台词", "Opening line"),
        "071": ("Q技能冷却完毕", "Active skill cooldown complete"),
        "072": ("主动技能", "Active skill"),
        "073": ("主动技能", "Active skill"),
        "074": ("主动技能", "Active skill"),
        "075": ("被动生效", "Passive activated"),
        "076": ("大招充能完毕", "Ultimate charged"),
        "077": ("释放大招", "Ultimate skill"),
        "078": ("释放大招", "Ultimate skill"),
        "079": ("释放大招", "Ultimate skill"),
        "080": ("大招无法使用", "Ultimate unavailable"),
        "108": ("受击", "Getting hit"),
        "109": ("击杀敌人", "Downing an enemy"),
        "110": ("击杀敌人", "Downing an enemy"),
        "111": ("击杀敌人", "Downing an enemy"),
        "112": ("击杀敌人", "Downing an enemy"),
        "113": ("击杀敌人", "Downing an enemy"),
        "114": ("击杀敌人", "Downing an enemy"),
        "115": ("双杀", "Double kill"),
        "116": ("三杀", "Triple kill"),
        "117": ("四杀", "Quadra kill"),
        "118": ("五杀", "Penta kill"),
        "119": ("超神", "God-like"),
        "120": ("复仇", "Revenge"),
        "123": ("被忍锋击倒", "Downed by Ninjato"),
        "124": ("危险区域死亡", "Dying outside the zone"),
        "125": ("摔死", "Falling to death"),
        "126": ("击倒敌人", "Downing an enemy"),
        "127": ("被击倒", "Being downed"),
        "122": ("倒地时间结束后死亡", "Dying after being downed"),
        "121": ("被击杀", "Dying"),
        "128": ("向队友求救", "Seeking a revive"),
        "129": ("救助队友", "Helping a teammate"),
        "130": ("被队友扶起", "Revived by teammate"),
        "131": ("安装炸弹", "Plant bomb"),
        "132": ("捡起炸弹", "Pick up bomb"),
        "133": ("开始拆除炸弹", "Defusing bomb"),
        "134": ("丢弃炸弹", "Abandoning the bomb"),
        "135": ("发现已被安装的炸弹", "Seeing a planted bomb"),
        "136": ("飞行", "Flying"),
        "137": ("失败", "Defeat"),
        "138": ("胜利", "Victory"),
        "139": ("失败SVP", "SVP"),
        "140": ("胜利MVP", "MVP"),
        "141": ("彩蛋", "Easter egg"),
        "142": ("彩蛋", "Easter egg"),
        "143": ("彩蛋", "Easter egg"),
        "144": ("彩蛋", "Easter egg"),
        "145": ("彩蛋", "Easter egg"),
        "146": ("彩蛋", "Easter egg"),
        "147": ("彩蛋", "Easter egg"),
        "148": ("彩蛋", "Easter egg"),
        "149": ("彩蛋", "Easter egg"),
        "150": ("彩蛋", "Easter egg"),
        "500": ("击倒敌人", "Downing an enemy"),
        "501": ("击倒敌人", "Downing an enemy"),
        "502": ("远处有敌人", "Enemy spotted far away"),
        "503": ("远处有敌人", "Enemy spotted far away"),
        "504": ("近处有敌人", "Enemy spotted close by"),
        "505": ("近处有敌人", "Enemy spotted close by"),
        "506": ("多名敌人", "Multiple enemies spotted"),
        "507": ("多名敌人", "Multiple enemies spotted"),
        "508": ("击中敌人", "Enemy hit"),
        "509": ("击中敌人", "Enemy hit"),
        "510": ("击中敌人", "Enemy hit"),
        "511": ("重创敌人", "Enemy heavily hit"),
        "512": ("重创敌人", "Enemy heavily hit"),
        "513": ("敌人重伤", "Enemy low on health"),
        "514": ("受到攻击", "Under attack"),
        "515": ("受到攻击", "Under attack"),
        "516": ("左侧有敌人", "Enemies on the left"),
        "517": ("左侧有敌人", "Enemies on the left"),
        "518": ("右侧有敌人", "Enemies on the right"),
        "519": ("右侧有敌人", "Enemies on the right"),
        "520": ("身后有敌人", "Enemies behind"),
        "521": ("身后有敌人", "Enemies behind"),
    },
    VoiceType.COMMUNICATIONS: {
        "081": ("进攻", "Attack"),
        "082": ("等待", "Wait"),
        "083": ("撤退", "Retreat"),
        "084": ("谢谢", "Thanks"),
        "085": ("称赞", "Praise"),
        "086": ("是", "Yes"),
        "087": ("否", "No"),
        "088": ("抱歉", "My bad"),
        "089": ("你好", "Hi"),
        "090": ("手榴弹", "Grenade"),
        "091": ("拦截者", "Interceptor"),
        "092": ("烟雾弹", "Smoke Bomb"),
        "093": ("闪光弹", "Flashbang"),
        "094": ("治疗雷", "Healing Greande"),
        "095": ("风场雷", "Windstorm Grenade"),
        "096": ("减速雷", "Slow Grenade"),
        "097": ("警报器", "Tattletale"),
        "098": ("危险信号", "Danger"),
        "099": ("我守这里", "Defend"),
        "100": ("需要支援", "Need backup"),
        "101": ("进攻这里", "Attack here"),
        "102": ("注意这里", "Attention here"),
        "103": ("这里可以安装炸弹", "Bomb can be planted here"),
        "104": ("这里有炸弹", "Bomb is here"),
        "105": ("这里有子弹", "Bullets here"),
        "106": ("这里有护甲", "Armor here"),
        "107": ("这里有战术道具", "Grenade here"),
        "151": ("警报器发现敌人", "Tattletale triggered")
    },
    VoiceType.SYSTEM: {

    },
    VoiceType.OTHER: {
        "022": ("标题", "Title"),
        "018": ("获得角色", "Character obtained"),
        "019": ("查看角色", "Character page"),
        "020": ("装备副武器", "Equip secondary weapon"),
        "021": ("装备战术道具", "Equip grenade"),
    }
}

voice_conversion_table_flat: dict[str, tuple[str]] = dict((k, v) for d in voice_conversion_table.values() for k, v in d.items())

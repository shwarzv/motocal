# -*- coding:utf-8 -*-
import os, csv, sys, math, time, re, json, codecs, types
from collections import OrderedDict
skillnamelist = OrderedDict()

# normal L and LL
skillnamelist["normalLL"] = {u"紅蓮の攻刃II": "fire", u"霧氷の攻刃II": "water", u"地裂の攻刃II": "earth", u"乱気の攻刃II": "wind", u"天光の攻刃II": "light", u"奈落の攻刃II": "dark"}
# 守護IIがない？
# skillnamelist["normalHPLL"] = {u"紅蓮の守護II": "fire", u"霧氷の守護II": "water", u"地裂の守護II": "earth", u"乱気の守護II": "wind", u"天光の守護II": "light", u"奈落の守護II": "dark"}
skillnamelist["normalL"] = {u"紅蓮の攻刃": "fire", u"霧氷の攻刃": "water", u"地裂の攻刃": "earth", u"乱気の攻刃": "wind", u"天光の攻刃": "light", u"奈落の攻刃": "dark"}
skillnamelist["normalHPL"] = {u"紅蓮の守護": "fire", u"霧氷の守護": "water", u"地裂の守護": "earth", u"乱気の守護": "wind", u"天光の守護": "light", u"奈落の守護": "dark"}
skillnamelist["normalCriticalL"] = {u"紅蓮の技巧": "fire", u"霧氷の技巧": "water", u"地裂の技巧": "earth", u"乱気の技巧": "wind", u"天光の技巧": "light", u"奈落の技巧": "dark"}
skillnamelist["normalHaisuiL"] = {u"紅蓮の背水": "fire", u"霧氷の背水": "water", u"地裂の背水": "earth", u"乱気の背水": "wind", u"天光の背水": "light", u"奈落の背水": "dark"}
skillnamelist["normalBoukunL"] = {u"紅蓮の暴君": "fire", u"霧氷の暴君": "water", u"地裂の暴君": "earth", u"乱気の暴君": "wind", u"天光の暴君": "light", u"奈落の暴君": "dark"}
skillnamelist["gurenJuin"] = {u"紅蓮の呪印・弐": "fire"}
skillnamelist["muhyoTuiga"] = {u"霧氷の追牙・肆": "water"}
skillnamelist["normalNiteL"] = {u"紅蓮の二手": "fire", u"霧氷の二手": "water", u"地裂の二手": "earth", u"乱気の二手": "wind", u"天光の二手": "light", u"奈落の二手": "dark"}
skillnamelist["normalSanteL"] = {u"紅蓮の三手": "fire", u"霧氷の三手": "water", u"地裂の三手": "earth", u"乱気の三手": "wind", u"天光の三手": "light", u"奈落の三手": "dark"}
skillnamelist["normalKonshinL"] = {u"紅蓮の渾身": "fire", u"霧氷の渾身": "water", u"地裂の渾身": "earth", u"乱気の渾身": "wind", u"天光の渾身": "light", u"奈落の渾身": "dark"}
# skillnamelist["normalKamui"] = {u"紅蓮の神威": "fire", u"霧氷の神威": "water", u"地裂の神威": "earth", u"乱気の神威": "wind", u"天光の神威": "light", u"奈落の神威": "dark"}
skillnamelist["normalKatsumokuS"] = {u"紅蓮の括目": "fire", u"霧氷の括目": "water", u"地裂の括目": "earth", u"乱気の括目": "wind", u"天光の括目": "light", u"奈落の括目": "dark"}

# normalM
skillnamelist["normalM"] = {u"業火の攻刃": "fire", u"渦潮の攻刃": "water", u"大地の攻刃": "earth", u"竜巻の攻刃": "wind", u"雷電の攻刃": "light", u"憎悪の攻刃": "dark"}
skillnamelist["normalHPM"] = {u"業火の守護": "fire", u"渦潮の守護": "water", u"大地の守護": "earth", u"竜巻の守護": "wind", u"雷電の守護": "light", u"憎悪の守護": "dark"}
skillnamelist["normalNiteM"] = {u"業火の二手": "fire", u"渦潮の二手": "water", u"大地の二手": "earth", u"竜巻の二手": "wind", u"雷電の二手": "light", u"憎悪の二手": "dark"}
skillnamelist["normalCriticalM"] = {u"業火の技巧": "fire", u"渦潮の技巧": "water", u"大地の技巧": "earth", u"竜巻の技巧": "wind", u"雷電の技巧": "light", u"憎悪の技巧": "dark"}
skillnamelist["normalHaisuiM"] = {u"業火の背水": "fire", u"渦潮の背水": "water", u"大地の背水": "earth", u"竜巻の背水": "wind", u"雷電の背水": "light", u"憎悪の背水": "dark"}
skillnamelist["normalSetsuna"] = {u"業火の刹那": "fire", u"渦潮の刹那": "water", u"大地の刹那": "earth", u"竜巻の刹那": "wind", u"雷電の刹那": "light", u"憎悪の刹那": "dark"}
skillnamelist["normalKatsumiM"] = {u"業火の克己": "fire", u"渦潮の克己": "water", u"大地の克己": "earth", u"竜巻の克己": "wind", u"雷電の克己": "light", u"憎悪の克己": "dark"}
skillnamelist["normalRasetsuM"] = {u"業火の羅刹": "fire", u"渦潮の羅刹": "water", u"大地の羅刹": "earth", u"竜巻の羅刹": "wind", u"雷電の羅刹": "light", u"憎悪の羅刹": "dark"}

# normalS
skillnamelist["normalS"] = {u"火の攻刃": "fire", u"水の攻刃": "water", u"土の攻刃": "earth", u"風の攻刃": "wind", u"光の攻刃": "light", u"闇の攻刃": "dark"}
skillnamelist["normalHPS"] = {u"火の守護": "fire", u"水の守護": "water", u"土の守護": "earth", u"風の守護": "wind", u"光の守護": "light", u"闇の守護": "dark"}
skillnamelist["normalCriticalS"] = {u"火の技巧": "fire", u"水の技巧": "water", u"土の技巧": "earth", u"風の技巧": "wind", u"光の技巧": "light", u"闇の技巧": "dark"}
skillnamelist["normalHaisuiS"] = {u"火の背水": "fire", u"水の背水": "water", u"土の背水": "earth", u"風の背水": "wind", u"光の背水": "light", u"闇の背水": "dark"}
skillnamelist["normalKamui"] = {u"火の神威": "fire", u"水の神威": "water", u"土の神威": "earth", u"風の神威": "wind", u"光の神威": "light", u"闇の神威": "dark"}
skillnamelist["normalNiteS"] = {u"火の二手": "fire", u"水の二手": "water", u"土の二手": "earth", u"風の二手": "wind", u"光の二手": "light", u"闇の二手": "dark"}

# magna II
skillnamelist["magnaL"] = {u"機炎方陣・攻刃II": "fire", u"海神方陣・攻刃II": "water", u"創樹方陣・攻刃II": "earth", u"嵐竜方陣・攻刃II": "wind", u"騎解方陣・攻刃II": "light", u"黒霧方陣・攻刃II": "dark"}
skillnamelist["magnaHPL"] = {u"機炎方陣・守護II": "fire", u"海神方陣・守護II": "water", u"創樹方陣・守護II": "earth", u"嵐竜方陣・守護II": "wind", u"騎解方陣・守護II": "light", u"黒霧方陣・守護II": "dark"}
skillnamelist["magnaHaisuiL"] = {u"機炎方陣・背水II": "fire", u"海神方陣・背水II": "water", u"創樹方陣・背水II": "earth", u"嵐竜方陣・背水II": "wind", u"騎解方陣・背水II": "light", u"黒霧方陣・背水II": "dark"}
skillnamelist["magnaCriticalL"] = {u"海神方陣・技巧II": "water"}

# magna I
skillnamelist["magnaM"] = {u"機炎方陣・攻刃": "fire", u"海神方陣・攻刃": "water", u"創樹方陣・攻刃": "earth", u"嵐竜方陣・攻刃": "wind", u"騎解方陣・攻刃": "light", u"黒霧方陣・攻刃": "dark"}
skillnamelist["magnaHPM"] = {u"機炎方陣・守護": "fire", u"海神方陣・守護": "water", u"創樹方陣・守護": "earth", u"嵐竜方陣・守護": "wind", u"騎解方陣・守護": "light", u"黒霧方陣・守護": "dark"}
skillnamelist["magnaKatsumiM"] = {u"機炎方陣・克己": "fire", u"海神方陣・克己": "water", u"創樹方陣・克己": "earth", u"嵐竜方陣・克己": "wind", u"騎解方陣・克己": "light", u"黒霧方陣・克己": "dark"}
skillnamelist["magnaKamui"] = {u"機炎方陣・神威": "fire", u"海神方陣・神威": "water", u"創樹方陣・神威": "earth", u"嵐竜方陣・神威": "wind", u"騎解方陣・神威": "light", u"黒霧方陣・神威": "dark"}
skillnamelist["magnaHaisuiS"] = {u"機炎方陣・背水": "fire", u"海神方陣・背水": "water", u"創樹方陣・背水": "earth", u"嵐竜方陣・背水": "wind", u"騎解方陣・背水": "light", u"黒霧方陣・背水": "dark"}
skillnamelist["magnaSetsuna"] = {u"機炎方陣・刹那": "fire", u"海神方陣・刹那": "water", u"創樹方陣・刹那": "earth", u"嵐竜方陣・刹那": "wind", u"騎解方陣・刹那": "light", u"黒霧方陣・刹那": "dark"}
# skillnamelist["magnaNiteM"] = {u"機炎方陣・二手": "fire", u"海神方陣・二手": "water", u"創樹方陣・二手": "earth", u"嵐竜方陣・二手": "wind", u"騎解方陣・二手": "light", u"黒霧方陣・二手": "dark"}
skillnamelist["magnaBoukun"] = {u"機炎方陣・暴君": "fire", u"海神方陣・暴君": "water", u"創樹方陣・暴君": "earth", u"嵐竜方陣・暴君": "wind", u"騎解方陣・暴君": "light", u"黒霧方陣・暴君": "dark"}
skillnamelist["magnaSanteL"] = {u"機炎方陣・三手": "fire", u"海神方陣・三手": "water", u"創樹方陣・三手": "earth", u"嵐竜方陣・三手": "wind", u"騎解方陣・三手": "light", u"黒霧方陣・三手": "dark"}
skillnamelist["magnaKatsumokuS"] = {u"機炎方陣・括目": "fire", u"海神方陣・括目": "water", u"創樹方陣・括目": "earth", u"嵐竜方陣・括目": "wind", u"騎解方陣・括目": "light", u"黒霧方陣・括目": "dark"}
skillnamelist["magnaRasetsuM"] = {u"機炎方陣・羅刹": "fire", u"海神方陣・羅刹": "water", u"創樹方陣・羅刹": "earth", u"嵐竜方陣・羅刹": "wind", u"騎解方陣・羅刹": "light", u"黒霧方陣・羅刹": "dark"}

# アンノウン
skillnamelist["unknownL"] = {u"アンノウン・ATK II": "unknown"}
skillnamelist["unknownM"] = {u"アンノウン・ATK": "unknown"}
skillnamelist["unknownHPL"] = {u"アンノウン・VIT II": "unknown"}
skillnamelist["unknownHPM"] = {u"アンノウン・VIT": "unknown"}
skillnamelist["strengthS"] = {u"スピードスペル": "light"}
skillnamelist["strengthM"] = {u"大自然の摂理": "light"}
skillnamelist["strengthL"] = {u"ストレングス": "unknown", u"セービングアタック": "water", u"Vスキル": "earth", u"その魂よ、安らかに": "light", u"烈光の至恩": "dark", u"自動辻斬装置": "water", u"半獣の咆哮": "fire", u"西風のラプソディ": "wind", u"我流の太刀筋": "wind", u"カースドテンタクル": "dark", u"ポイント・オブ・エイム": "earth", u"天の福音": "light", u"森林の祝福": "wind", u"お友達になってくれる？": "dark", u"蒼薔薇の棘": "water", u"翠薔薇の棘": "wind", u"橙薔薇の棘": "earth", u"紅薔薇の棘": "fire"}
skillnamelist["strengthLL"] = {u"灼滅の覇道": "fire", u"裁考の覇道": "earth"}
skillnamelist["strengthHaisuiM"] = {u"マジックチャージ": "light"}
skillnamelist["unknownOtherBoukunL"] = {u"ミフネ流剣法・極意": "fire", u"インテリジェンス": "dark"}
skillnamelist["unknownOtherNiteS"] = {u"ミフネ流剣法・双星": "fire", u"デクステリティ": "dark"}

# バハ
# フツルス拳系はスキル名が同じなので先に処理
skillnamelist["bahaFUHP-fist"] = {u"ヒュムアニムス・メンスII": "dark"}
skillnamelist["bahaFUHP-katana"] = {u"ドーラアニムス・メンスII": "dark"}
skillnamelist["bahaFUHP-bow"] = {u"エルンアニムス・メンスII": "dark"}
skillnamelist["bahaFUHP-music"] = {u"ハヴンアニムス・メンスII": "dark"}
skillnamelist["bahaAT-dagger"] = {u"ヒュムアニムス・ウィス": "dark"}
skillnamelist["bahaAT-axe"] = {u"ドーラアニムス・ウィス": "dark"}
skillnamelist["bahaAT-spear"] = {u"エルンアニムス・ウィス": "dark"}
skillnamelist["bahaAT-gun"] = {u"ハヴンアニムス・ウィス": "dark"}
skillnamelist["bahaATHP-sword"] = {u"コンキリオ・ルーベル": "dark"}
skillnamelist["bahaATHP-wand"] = {u"コンキリオ・ケルレウス": "dark"}
skillnamelist["bahaHP-fist"] = {u"ヒュムアニムス・メンス": "dark"}
skillnamelist["bahaHP-katana"] = {u"ドーラアニムス・メンス": "dark"}
skillnamelist["bahaHP-bow"] = {u"エルンアニムス・メンス": "dark"}
skillnamelist["bahaHP-music"] = {u"ハヴンアニムス・メンス": "dark"}
skillnamelist["bahaFUATHP-sword"] = {u"コンキリオ・イグニス": "dark"}
skillnamelist["bahaFUATHP-dagger"] = {u"コンキリオ・ウェントス": "dark"}
skillnamelist["bahaFUATHP-spear"] = {u"コンキリオ・コルヌ": "dark"}
skillnamelist["bahaFUATHP-axe"] = {u"コンキリオ・テラ": "dark"}
skillnamelist["bahaFUATHP-wand"] = {u"コンキリオ・インベル": "dark"}
skillnamelist["bahaFUATHP-gun"] = {u"コンキリオ・アルボス": "dark"}

# コスモス
skillnamelist["cosmosAT"] = {u"アタック・スタンス": "light"}
skillnamelist["cosmosBL"] = {u"バランス・スタンス": "light"}
skillnamelist["cosmosDF"] = {u"ディフェンド・スタンス": "light"}
skillnamelist["cosmosPC"] = {u"ペキューリア・スタンス": "light"}
skillnamelist["cosmos-sword"] = {u"ソード・オブ・コスモス": "light"}
skillnamelist["cosmos-dagger"] = {u"ダガー・オブ・コスモス": "light"}
skillnamelist["cosmos-spear"] = {u"ランス・オブ・コスモス": "light"}
skillnamelist["cosmos-axe"] = {u"サイス・オブ・コスモス": "light"}
skillnamelist["cosmos-wand"] = {u"ロッド・オブ・コスモス": "light"}
skillnamelist["cosmos-gun"] = {u"ガン・オブ・コスモス": "light"}
skillnamelist["cosmos-fist"] = {u"ガントレット・オブ・コスモス": "light"}
skillnamelist["cosmos-bow"] = {u"アロー・オブ・コスモス": "light"}
skillnamelist["cosmos-katana"] = {u"ブレイド": "light"}
skillnamelist["cosmos-music"] = {u"ハープ・オブ・コスモス": "light"}

# 天司の祝福系
skillnamelist["tenshiShukufukuII"] = {u"ミカエルの祝福II": "fire", u"ガブリエルの祝福II": "water", u"ウリエルの祝福II": "earth", u"ラファエルの祝福II": "wind"}
skillnamelist["tenshiShukufuku"] = {u"ミカエルの祝福": "fire", u"ガブリエルの祝福": "water", u"ウリエルの祝福": "earth", u"ラファエルの祝福": "wind"}

# キャラ固有武器
skillnamelist["tsuranukiKiba"] = {u"貫きの牙": "fire"}
skillnamelist["washiouKekkai"] = {u"鷲王の結界": "fire"}

armtypelist = OrderedDict()
armtypelist[u"剣"] = "sword"
armtypelist[u"銃"] = "gun"
armtypelist[u"短剣"] = "dagger"
armtypelist[u"槍"] = "spear"
armtypelist[u"斧"] = "axe"
armtypelist[u"杖"] = "wand"
armtypelist[u"格闘"] = "fist"
armtypelist[u"弓"] = "bow"
armtypelist[u"楽器"] = "music"
armtypelist[u"刀"] = "katana"

def skill_replace(skill):
    decoded_skill = skill.decode("utf-8")
    for inner_skillname, onelist in skillnamelist.items():
        for skillname, elem in onelist.items():
            m = re.match(skillname, decoded_skill)
            if m:
                res = inner_skillname
                element = elem
                return res, element

    return "non", "none"

def type_replace(armtype):
    decoded_armtype = armtype.decode("utf-8")
    for armtypename, inner_armtype in armtypelist.items():
        m = re.match(armtypename, decoded_armtype)
        if m:
            res = inner_armtype
            return res
    return "none"

if __name__ == '__main__':
    key_pattern = re.compile("\d+")
    skill_pattern = re.compile("\[\[([\W\w]+)\>")
    jougen_pattern = re.compile(u"○")
    baha_pattern = re.compile(u"bahaFU")
    mycsv = csv.reader(open("txt_source/armData-ssr.txt", 'r'), delimiter="|")
    json_data = OrderedDict()
    imageURL = []

    # ssr
    for row in mycsv:
        newdict = {}

        # print len(row)
        if len(row) <= 1:
            continue
        else:
            m = key_pattern.search(row[1])
            if m:
                key = row[1][m.start():m.end()]

            name = row[2].translate(None, "&br;")
            name = name.replace("[]", "")
            newdict["name"] = name

            # element
            if row[3].find("火") > 0:
                newdict["element"] = "fire"
            elif row[3].find("水") > 0:
                newdict["element"] = "water"
            elif row[3].find("土") > 0:
                newdict["element"] = "earth"
            elif row[3].find("風") > 0:
                newdict["element"] = "wind"
            elif row[3].find("光") > 0:
                newdict["element"] = "light"
            elif row[3].find("全属性") > 0:
                newdict["element"] = "all"
            else:
                newdict["element"] = "dark"

            # type
            newdict["type"] = type_replace(row[4])

            skill = "non"
            element1 = "none"
            m = skill_pattern.search(row[7])
            if m:
                skill, element1 = skill_replace(m.group(1))

            newdict["skill1"] = skill

            skill = "non"
            element2 = "none"
            m = skill_pattern.search(row[8])
            if m:
                skill, element2 = skill_replace(m.group(1))

            if element2 == "none" or element2 == "unknown":
                element2 = newdict["element"]

            newdict["skill2"] = skill
            newdict["element2"] = element2
            newdict["minhp"] = row[9]
            newdict["minattack"] = row[10]
            newdict["hp"] = row[11]
            newdict["attack"] = row[12]

            m = jougen_pattern.search(row[15].decode("utf-8"))
            if m:
                newdict["slvmax"] = 15
                newdict["maxlv"] = 150
                newdict["hplv100"] = row[16]
                newdict["attacklv100"] = row[17]
            else:
                m = baha_pattern.search(newdict["skill1"])

                if m:
                    newdict["slvmax"] = 15
                    newdict["maxlv"] = 150
                    newdict["hplv100"] = row[16]
                    newdict["attacklv100"] = row[17]
                else:
                    newdict["slvmax"] = 10
                    newdict["maxlv"] = 100

            newdict["imageURL"] = "./imgs/" + key + ".png"
            json_data[name] = newdict
            # imageURL.append("http://gbf-wiki.com/index.php?plugin=attach&refer=img&openfile=" + key + ".png\n")

    mycsv = csv.reader(open("txt_source/armData-sr.txt", 'r'), delimiter="|")
    # sr
    for row in mycsv:
        newdict = {}

        # print len(row)
        if len(row) <= 1:
            continue
        else:
            m = key_pattern.search(row[1])
            if m:
                key = row[1][m.start():m.end()]

            name = row[2].translate(None, "&br;")
            newdict["name"] = name

            # element
            if row[3].find("火") > 0:
                newdict["element"] = "fire"
            elif row[3].find("水") > 0:
                newdict["element"] = "water"
            elif row[3].find("土") > 0:
                newdict["element"] = "earth"
            elif row[3].find("風") > 0:
                newdict["element"] = "wind"
            elif row[3].find("光") > 0:
                newdict["element"] = "light"
            else:
                newdict["element"] = "dark"

            # type
            newdict["type"] = type_replace(row[4])

            skill = "non"
            element1 = "none"
            m = skill_pattern.search(row[7])
            if m:
                skill, element1 = skill_replace(m.group(1))

            newdict["skill1"] = skill

            skill = "non"
            element2 = "none"
            m = skill_pattern.search(row[8])
            if m:
                skill, element2 = skill_replace(m.group(1))

            if element2 == "none" or element2 == "unknown":
                element2 = newdict["element"]

            newdict["skill2"] = skill
            newdict["element2"] = element2
            newdict["minhp"] = row[9]
            newdict["minattack"] = row[10]
            newdict["hp"] = row[11]
            newdict["attack"] = row[12]
            newdict["slvmax"] = 10
            newdict["maxlv"] = 75

            newdict["imageURL"] = "./imgs/" + key + ".png"
            json_data[name] = newdict
            imageURL.append("http://gbf-wiki.com/index.php?plugin=attach&refer=img&openfile=" + key + ".png\n")

    f = open("./armData.json", "w")
    json.dump(json_data, f, ensure_ascii=False, indent=4)
    f.close()

    #f = open("./imageURLlist.txt", "w")
    #for x in imageURL:
    #    f.write(x)
    #f.close()

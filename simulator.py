#coding=utf-8
import io
import os
import sys
import json


#加载游戏数据
rider_file = io.open("riders.json","r",encoding='utf-8')
rider_dic = json.load(rider_file)
rider_file.close()
print(u'加载riders数据完成...');
print "riders file version " + rider_dic["version"] + "\n"

otomon_file = io.open("otomons.json","r",encoding='utf-8')
otomon_dic = json.load(otomon_file)
otomon_file.close()
print(u'加载otomons数据完成...');
print "otomons file version " + otomon_dic["version"] + "\n"

#加载quest文件
quest_file = io.open("quest.json","r",encoding='utf-8')
quest = json.load(quest_file)
quest_file.close()
print(u'加载任务文件完成...');
print "simulating quest:" + quest["quest_name"] + "\n"

#加载队伍文件
party_file = io.open("my_party.json","r",encoding='utf-8')
party = json.load(party_file)
party_file.close()
print(u'加载自定义队伍完成...');
print u"模拟队伍: " + party["team_name"] + "\n"

#TODO：队伍检查

#模拟过程

#初始化队伍

#初始化boss

#战斗模拟T1-N

#最优解输出

#统计数据输出


file_path = io.open("test_file.json", "w+", encoding='utf-8')

data = json.dumps(party, ensure_ascii=False, sort_keys=True, indent=4)
file_path.write(data)
file_path.close()
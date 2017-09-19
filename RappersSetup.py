import sys
import operator
import requests
import json
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights


pi_username = 'c2cf577d-be68-41f4-8368-ee029043c18a'
pi_password = '2dNCNvKaEjvG'

personality_insights = PersonalityInsights(username=pi_username, password=pi_password)



#Kanye

#CollegeDropout
kanyeCDString = ""
kanyeCDFile = open("rappers/kanye/CollegeDropout.txt", "r")
kanyeCDString = kanyeCDFile.read()

kanyeCDResult = personality_insights.profile(kanyeCDString);

with open("rappers/kanye/CollegeDropout_R.txt", "w") as saveFileCD:
    json.dump(kanyeCDResult, saveFileCD)



#Late Registration
kanyeLRString = ""
kanyeLRFile = open("rappers/kanye/LateRegistration.txt", "r")
kanyeLRString = kanyeLRFile.read()

kanyeLRResult = personality_insights.profile(kanyeLRString);

with open("rappers/kanye/LateRegistration_R.txt", "w") as saveFileLR:
    json.dump(kanyeLRResult, saveFileLR)

#Graduation
kanyeGraduationString = ""
kanyeGraduationFile = open("rappers/kanye/Graduation.txt", "r")
kanyeGraduationString = kanyeGraduationFile.read()

kanyeGraduationResult = personality_insights.profile(kanyeGraduationString);

with open("rappers/kanye/Graduation_R.txt", "w") as saveFileGraduation:
    json.dump(kanyeGraduationResult, saveFileGraduation)

#808s
kanye808String = ""
kanye808File = open("rappers/kanye/808s.txt", "r")
kanye808String = kanye808File.read()

kanye808Result = personality_insights.profile(kanye808String);
with open("rappers/kanye/808s_R.txt", "w") as saveFile808:
    json.dump(kanye808Result, saveFile808)

#MBDTF
kanyeMBDTFString = ""
kanyeMBDTFFile = open("rappers/kanye/MBDTF.txt", "r")
kanyeMBDTFString = kanyeMBDTFFile.read()

kanyeMBDTFResult = personality_insights.profile(kanyeMBDTFString);
with open("rappers/kanye/MBDTF_R.txt", "w") as saveFileMBDTF:
    json.dump(kanyeMBDTFResult, saveFileMBDTF)

#Watch the Throne
kanyeWTTString = ""
kanyeWTTFile = open("rappers/kanye/WatchTheThrone.txt", "r")
kanyeWTTString = kanyeWTTFile.read()

kanyeWTTResult = personality_insights.profile(kanyeWTTString);
with open("rappers/kanye/WTT_R.txt", "w") as saveFileWTT:
    json.dump(kanyeWTTResult, saveFileWTT)
#Yeezus
kanyeYeezusString = ""
kanyeYeezusFile = open("rappers/kanye/Yeezus.txt", "r")
kanyeYeezusString = kanyeYeezusFile.read()

kanyeYeezusResult = personality_insights.profile(kanyeYeezusString);
with open("rappers/kanye/Yeezus_R.txt", "w") as saveFileYeezus:
    json.dump(kanyeYeezusResult, saveFileYeezus)

#TLOP
kanyeTLOPString = ""
kanyeTLOPFile = open("rappers/kanye/TLOP.txt", "r")
kanyeTLOPString = kanyeTLOPFile.read()

kanyeTLOPResult = personality_insights.profile(kanyeTLOPString);
with open("rappers/kanye/TLOP_R.txt", "w") as saveFileTLOP:
    json.dump(kanyeTLOPResult, saveFileTLOP)
#Kanye Total
kanyeTotalString = kanyeCDString + kanyeLRString + kanyeGraduationString + kanye808String + kanyeMBDTFString + kanyeWTTString + kanyeYeezusString + kanyeTLOPString
kanyeTotalResult = personality_insights.profile(kanyeTotalString);
with open("rappers/kanye/results.txt", "w") as saveFileKanye:
    json.dump(kanyeTotalResult, saveFileKanye)


#Frank
#Channel Orange
frankOrangeString = ""
frankOrangeFile = open("rappers/frank/orange.txt", "r")
frankOrangeString = frankOrangeFile.read()

frankOrangeResult = personality_insights.profile(frankOrangeString);
with open("rappers/frank/orange_R.txt", "w") as saveFileOrange:
    json.dump(frankOrangeResult, saveFileOrange)
#Blonde
frankBlondeString = ""
frankBlondeFile = open("rappers/frank/blonde.txt", "r")
frankBlondeString = frankBlondeFile.read()

frankBlondeResult = personality_insights.profile(frankBlondeString);
with open("rappers/frank/blonde_R.txt", "w") as saveFileBlonde:
    json.dump(frankBlondeResult, saveFileBlonde)
#Total
frankTotalString = frankOrangeString + frankBlondeString
frankTotalResult = personality_insights.profile(frankTotalString);
with open("rappers/frank/results.txt", "w") as saveFileFrank:
    json.dump(frankTotalResult, saveFileFrank)

#kendrick

#chance
#10 Day
chance10DayString = ""
chance10DayFile = open("rappers/chance/10day.txt", "r")
chance10DayString = chance10DayFile.read()

chance10DayResult = personality_insights.profile(chance10DayString);
with open("rappers/chance/10Day_R.txt", "w") as saveFile10Day:
    json.dump(chance10DayResult, saveFile10Day)
#acid rap
chanceAcidString = ""
chanceAcidFile = open("rappers/chance/acidrap.txt", "r")
chanceAcidString = chanceAcidFile.read()

chanceAcidResult = personality_insights.profile(chanceAcidString);
with open("rappers/chance/acidrap_R.txt", "w") as saveFileAcid:
    json.dump(chanceAcidResult, saveFileAcid)
#coloringbook
chanceCBString = ""
chanceCBFile = open("rappers/chance/coloringbook.txt", "r")
chanceCBString = chanceCBFile.read()

chanceCBResult = personality_insights.profile(chanceCBString);
with open("rappers/chance/coloringbook_R.txt", "w") as saveFileCB:
    json.dump(chanceCBResult, saveFileCB)

#total
chanceTotalString = chance10DayString + chanceAcidString + chanceCBString
chanceTotalResult = personality_insights.profile(chanceTotalString);
with open("rappers/chance/results.txt", "w") as saveFileChance:
    json.dump(chanceTotalResult, saveFileChance)

#jcole

#drake

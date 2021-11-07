#Importing the CSV library
import csv

#Importing the user reviews csv document in to a dataframe
with open('userReviews.csv', encoding='utf-8-sig') as csv_file:
    df = csv.DictReader(csv_file, delimiter=';')
    df_list = list(df)

#Checking which authors have seen pirates of the caribbean the curse of the black pearl and reviewed it
X = list()
for row in df_list:
    if row['movieName'] == 'pirates-of-the-caribbean-the-curse-of-the-black-pearl':
        X.append(row['Author'])
#print(X)

#For the authors that have seen pirates of the caribbean the curse of the black pearl check the scores the gave to other movies
Y = list()
for row in df_list:
    if row['Author'] in X:
        Y.append(row['Metascore_w'])
#print(Y)

#For the authors that have seen pirates of the caribbean the curse of the black pearl check the other movies they have reviewed
I = list()
for row in df_list:
    if row['Author'] in X:
        I.append(row['movieName'])
#print(I)

#Create a list of unique movies reviewed by people which watched pirates of the caribbean the curse of the black pearl
U = list()
for row in I:
    if row not in U:
        U.append(row)
#print(U)

#Calculation the average review for pirates of the caribbean the curse of the black pearl which is 8.45
F = list()
for row in df_list:
    if row['movieName'] == 'pirates-of-the-caribbean-the-curse-of-the-black-pearl':
        if row['Author'] in X:
            F.append(row['Metascore_w'])
F_int = list(map(int, F))
F_sum = sum(F_int)
length = len(F)
F_final = F_sum / length
print(F_final)

#Caclulation 50 average reviews by fans of the pirates movie, because i could not figure out how to do it automatically i decided i will do 50 and see the results for that
F1 = list()
for row in df_list:
    if row['movieName'] == 'leap!':
        if row['Author'] in X:
            F1.append(row['Metascore_w'])
F1_int = list(map(int, F1))
F1_sum = sum(F1_int)
length = len(F1)
F1_final = F1_sum / length
F1_name = 'leap!'
print(F1_final)

F2 = list()
for row in df_list:
    if row['movieName'] == 'birth-of-the-dragon':
        if row['Author'] in X:
            F2.append(row['Metascore_w'])
F2_int = list(map(int, F2))
F2_sum = sum(F2_int)
length = len(F2)
F2_final = F2_sum / length
F2_name = 'birth-of-the-dragon'
print(F2_final)

F3 = list()
for row in df_list:
    if row['movieName'] == 'good-time':
        if row['Author'] in X:
            F3.append(row['Metascore_w'])
F3_int = list(map(int, F3))
F3_sum = sum(F3_int)
length = len(F3)
F3_final = F3_sum / length
F3_name = 'good-time'
print(F3_final)

F4 = list()
for row in df_list:
    if row['movieName'] == 'the-hitmans-bodyguard':
        if row['Author'] in X:
            F4.append(row['Metascore_w'])
F4_int = list(map(int, F4))
F4_sum = sum(F4_int)
length = len(F4)
F4_final = F4_sum / length
F4_name = 'the-hitmans-bodyguard'
print(F4_final)

F5 = list()
for row in df_list:
    if row['movieName'] == 'wish-upon':
        if row['Author'] in X:
            F5.append(row['Metascore_w'])
F5_int = list(map(int, F5))
F5_sum = sum(F5_int)
length = len(F5)
F5_final = F5_sum / length
F5_name = 'wish-upon'
print(F5_final)

F6 = list()
for row in df_list:
    if row['movieName'] == '47-meters-down':
        if row['Author'] in X:
            F6.append(row['Metascore_w'])
F6_int = list(map(int, F6))
F6_sum = sum(F6_int)
length = len(F6)
F6_final = F6_sum / length
F6_name = '47-meters-down'
print(F6_final)

F7 = list()
for row in df_list:
    if row['movieName'] == 'the-house':
        if row['Author'] in X:
            F7.append(row['Metascore_w'])
F7_int = list(map(int, F7))
F7_sum = sum(F7_int)
length = len(F7)
F7_final = F7_sum / length
F7_name = 'the-house'
print(F7_final)

F8 = list()
for row in df_list:
    if row['movieName'] == 'derailed':
        if row['Author'] in X:
            F8.append(row['Metascore_w'])
F8_int = list(map(int, F8))
F8_sum = sum(F8_int)
length = len(F8)
F8_final = F8_sum / length
F8_name = 'derailed'
print(F8_final)

F9 = list()
for row in df_list:
    if row['movieName'] == 'girls-trip':
        if row['Author'] in X:
            F9.append(row['Metascore_w'])
F9_int = list(map(int, F9))
F9_sum = sum(F9_int)
length = len(F9)
F9_final = F9_sum / length
F9_name = 'girls-trip'
print(F9_final)

F10 = list()
for row in df_list:
    if row['movieName'] == 'personal-shopper':
        if row['Author'] in X:
            F10.append(row['Metascore_w'])
F10_int = list(map(int, F10))
F10_sum = sum(F10_int)
length = len(F10)
F10_final = F10_sum / length
F10_name = 'personal-shopper'
print(F10_final)

F11 = list()
for row in df_list:
    if row['movieName'] == 'your-name':
        if row['Author'] in X:
            F11.append(row['Metascore_w'])
F11_int = list(map(int, F11))
F11_sum = sum(F11_int)
length = len(F11)
F11_final = F11_sum / length
F11_name = 'your-name'
print(F11_final)

F12 = list()
for row in df_list:
    if row['movieName'] == 'pirates-of-the-caribbean-dead-men-tell-no-tales':
        if row['Author'] in X:
            F12.append(row['Metascore_w'])
F12_int = list(map(int, F12))
F12_sum = sum(F12_int)
length = len(F12)
F12_final = F12_sum / length
F12_name = 'pirates-of-the-caribbean-dead-men-tell-no-tales'
print(F12_final)

F13 = list()
for row in df_list:
    if row['movieName'] == 'kidnap':
        if row['Author'] in X:
            F13.append(row['Metascore_w'])
F13_int = list(map(int, F13))
F13_sum = sum(F13_int)
length = len(F13)
F13_final = F13_sum / length
F13_name = 'kidnap'
print(F13_final)

F14 = list()
for row in df_list:
    if row['movieName'] == 'a-ghost-story':
        if row['Author'] in X:
            F14.append(row['Metascore_w'])
F14_int = list(map(int, F14))
F14_sum = sum(F14_int)
length = len(F14)
F14_final = F14_sum / length
F14_name = 'a-ghost-story'
print(F14_final)

F15 = list()
for row in df_list:
    if row['movieName'] == 'war-for-the-planet-of-the-apes':
        if row['Author'] in X:
            F15.append(row['Metascore_w'])
F15_int = list(map(int, F15))
F15_sum = sum(F15_int)
length = len(F15)
F15_final = F15_sum / length
F15_name = 'war-for-the-planet-of-the-apes'
print(F15_final)

F16 = list()
for row in df_list:
    if row['movieName'] == 'annabelle-creation':
        if row['Author'] in X:
            F16.append(row['Metascore_w'])
F16_int = list(map(int, F16))
F16_sum = sum(F16_int)
length = len(F16)
F16_final = F16_sum / length
F16_name = 'annabelle-creation'
print(F16_final)

F17 = list()
for row in df_list:
    if row['movieName'] == 'the-bad-batch':
        if row['Author'] in X:
            F17.append(row['Metascore_w'])
F17_int = list(map(int, F17))
F17_sum = sum(F17_int)
length = len(F17)
F17_final = F17_sum / length
F17_name = 'the-bad-batch'
print(F17_final)

F18 = list()
for row in df_list:
    if row['movieName'] == 'spider-man-homecoming':
        if row['Author'] in X:
            F18.append(row['Metascore_w'])
F18_int = list(map(int, F18))
F18_sum = sum(F18_int)
length = len(F18)
F18_final = F18_sum / length
F18_name = 'spider-man-homecoming'
print(F18_final)

F19 = list()
for row in df_list:
    if row['movieName'] == 'baby-driver':
        if row['Author'] in X:
            F19.append(row['Metascore_w'])
F19_int = list(map(int, F19))
F19_sum = sum(F19_int)
length = len(F19)
F19_final = F19_sum / length
F19_name = 'baby-driver'
print(F19_final)

F20 = list()
for row in df_list:
    if row['movieName'] == 'the-dark-tower':
        if row['Author'] in X:
            F20.append(row['Metascore_w'])
F20_int = list(map(int, F20))
F20_sum = sum(F20_int)
length = len(F20)
F20_final = F20_sum / length
F20_name = 'the-dark-tower'
print(F20_final)

F21 = list()
for row in df_list:
    if row['movieName'] == 'the-big-sick':
        if row['Author'] in X:
            F21.append(row['Metascore_w'])
F21_int = list(map(int, F21))
F21_sum = sum(F21_int)
length = len(F21)
F21_final = F21_sum / length
F21_name = 'the-big-sick'
print(F21_final)

F22 = list()
for row in df_list:
    if row['movieName'] == 'all-eyez-on-me':
        if row['Author'] in X:
            F22.append(row['Metascore_w'])
F22_int = list(map(int, F22))
F22_sum = sum(F22_int)
length = len(F22)
F22_final = F22_sum / length
F22_name = 'all-eyez-on-me'
print(F22_final)

F23 = list()
for row in df_list:
    if row['movieName'] == 'transformers-the-last-knight':
        if row['Author'] in X:
            F23.append(row['Metascore_w'])
F23_int = list(map(int, F23))
F23_sum = sum(F23_int)
length = len(F23)
F23_final = F23_sum / length
F23_name = 'transformers-the-last-knight'
print(F23_final)

F24 = list()
for row in df_list:
    if row['movieName'] == 'valerian-and-the-city-of-a-thousand-planets':
        if row['Author'] in X:
            F24.append(row['Metascore_w'])
F24_int = list(map(int, F24))
F24_sum = sum(F24_int)
length = len(F24)
F24_final = F24_sum / length
F24_name = 'valerian-and-the-city-of-a-thousand-planets'
print(F24_final)

F25 = list()
for row in df_list:
    if row['movieName'] == 'the-mummy-2017':
        if row['Author'] in X:
            F25.append(row['Metascore_w'])
F25_int = list(map(int, F25))
F25_sum = sum(F25_int)
length = len(F25)
F25_final = F25_sum / length
F25_name = 'the-mummy-2017'
print(F25_final)

F26 = list()
for row in df_list:
    if row['movieName'] == 'how-to-be-a-latin-lover':
        if row['Author'] in X:
            F26.append(row['Metascore_w'])
F26_int = list(map(int, F26))
F26_sum = sum(F26_int)
length = len(F26)
F26_final = F26_sum / length
F26_name = 'how-to-be-a-latin-lover'
print(F26_final)

F27 = list()
for row in df_list:
    if row['movieName'] == 'diary-of-a-wimpy-kid-the-long-haul':
        if row['Author'] in X:
            F27.append(row['Metascore_w'])
F27_int = list(map(int, F27))
F27_sum = sum(F27_int)
length = len(F27)
F27_final = F27_sum / length
F27_name = 'diary-of-a-wimpy-kid-the-long-haul'
print(F27_final)

F28 = list()
for row in df_list:
    if row['movieName'] == 'everything-everything':
        if row['Author'] in X:
            F28.append(row['Metascore_w'])
F28_int = list(map(int, F28))
F28_sum = sum(F28_int)
length = len(F28)
F28_final = F28_sum / length
F28_name = 'everything-everything'
print(F28_final)

F29 = list()
for row in df_list:
    if row['movieName'] == 'alien-covenant':
        if row['Author'] in X:
            F29.append(row['Metascore_w'])
F29_int = list(map(int, F29))
F29_sum = sum(F29_int)
length = len(F29)
F29_final = F29_sum / length
F29_name = 'alien-covenant'
print(F29_final)

F30 = list()
for row in df_list:
    if row['movieName'] == 'wonder-woman':
        if row['Author'] in X:
            F30.append(row['Metascore_w'])
F30_int = list(map(int, F30))
F30_sum = sum(F30_int)
length = len(F30)
F30_final = F30_sum / length
F30_name = 'wonder-woman'
print(F30_final)

F31 = list()
for row in df_list:
    if row['movieName'] == 'phoenix-forgotten':
        if row['Author'] in X:
            F31.append(row['Metascore_w'])
F31_int = list(map(int, F31))
F31_sum = sum(F31_int)
length = len(F31)
F31_final = F31_sum / length
F31_name = 'phoenix-forgotten'
print(F31_final)

F32 = list()
for row in df_list:
    if row['movieName'] == 'going-in-style':
        if row['Author'] in X:
            F32.append(row['Metascore_w'])
F32_int = list(map(int, F32))
F32_sum = sum(F32_int)
length = len(F32)
F32_final = F32_sum / length
F32_name = 'going-in-style'
print(F32_final)

F33 = list()
for row in df_list:
    if row['movieName'] == 'the-lovers-2017':
        if row['Author'] in X:
            F33.append(row['Metascore_w'])
F33_int = list(map(int, F33))
F33_sum = sum(F33_int)
length = len(F33)
F33_final = F33_sum / length
F33_name = 'the-lovers-2017'
print(F33_final)

F34 = list()
for row in df_list:
    if row['movieName'] == 'the-circle-2017':
        if row['Author'] in X:
            F34.append(row['Metascore_w'])
F34_int = list(map(int, F34))
F34_sum = sum(F34_int)
length = len(F34)
F34_final = F34_sum / length
F34_name = 'the-circle-2017'
print(F34_final)

F35 = list()
for row in df_list:
    if row['movieName'] == 'colossal':
        if row['Author'] in X:
            F35.append(row['Metascore_w'])
F35_int = list(map(int, F35))
F35_sum = sum(F35_int)
length = len(F35)
F35_final = F35_sum / length
F35_name = 'colossal'
print(F35_final)

F36 = list()
for row in df_list:
    if row['movieName'] == 'free-fire':
        if row['Author'] in X:
            F36.append(row['Metascore_w'])
F36_int = list(map(int, F36))
F36_sum = sum(F36_int)
length = len(F36)
F36_final = F36_sum / length
F36_name = 'free-fire'
print(F36_final)

F37 = list()
for row in df_list:
    if row['movieName'] == 'ghost-in-the-shell-2017':
        if row['Author'] in X:
            F37.append(row['Metascore_w'])
F37_int = list(map(int, F37))
F37_sum = sum(F37_int)
length = len(F37)
F37_final = F37_sum / length
F37_name = 'ghost-in-the-shell-2017'
print(F37_final)

F38 = list()
for row in df_list:
    if row['movieName'] == 'gifted':
        if row['Author'] in X:
            F38.append(row['Metascore_w'])
F38_int = list(map(int, F38))
F38_sum = sum(F38_int)
length = len(F38)
F38_final = F38_sum / length
F38_name = 'gifted'
print(F38_final)

F39 = list()
for row in df_list:
    if row['movieName'] == 'snatched':
        if row['Author'] in X:
            F39.append(row['Metascore_w'])
F39_int = list(map(int, F39))
F39_sum = sum(F39_int)
length = len(F39)
F39_final = F39_sum / length
F39_name = 'snatched'
print(F39_final)

F40 = list()
for row in df_list:
    if row['movieName'] == 'smurfs-the-lost-village':
        if row['Author'] in X:
            F40.append(row['Metascore_w'])
F40_int = list(map(int, F40))
F40_sum = sum(F40_int)
length = len(F40)
F40_final = F40_sum / length
F40_name = 'smurfs-the-lost-village'
print(F40_final)

F41 = list()
for row in df_list:
    if row['movieName'] == 'the-lost-city-of-z':
        if row['Author'] in X:
            F41.append(row['Metascore_w'])
F41_int = list(map(int, F41))
F41_sum = sum(F41_int)
length = len(F41)
F41_final = F41_sum / length
F41_name = 'the-lost-city-of-z'
print(F41_final)

F42 = list()
for row in df_list:
    if row['movieName'] == 'a-quiet-passion':
        if row['Author'] in X:
            F42.append(row['Metascore_w'])
F42_int = list(map(int, F42))
F42_sum = sum(F42_int)
length = len(F42)
F42_final = F42_sum / length
F42_name = 'a-quiet-passion'
print(F42_final)

F43 = list()
for row in df_list:
    if row['movieName'] == 'their-finest':
        if row['Author'] in X:
            F43.append(row['Metascore_w'])
F43_int = list(map(int, F43))
F43_sum = sum(F43_int)
length = len(F43)
F43_final = F43_sum / length
F43_name = 'their-finest'
print(F43_final)

F44 = list()
for row in df_list:
    if row['movieName'] == 'king-arthur-legend-of-the-sword':
        if row['Author'] in X:
            F44.append(row['Metascore_w'])
F44_int = list(map(int, F44))
F44_sum = sum(F44_int)
length = len(F44)
F44_final = F44_sum / length
F44_name = 'king-arthur-legend-of-the-sword'
print(F44_final)

F45 = list()
for row in df_list:
    if row['movieName'] == 'norman-the-moderate-rise-and-tragic-fall-of-a-new-york-fixer':
        if row['Author'] in X:
            F45.append(row['Metascore_w'])
F45_int = list(map(int, F45))
F45_sum = sum(F45_int)
length = len(F45)
F45_final = F45_sum / length
F45_name = 'norman-the-moderate-rise-and-tragic-fall-of-a-new-york-fixer'
print(F45_final)

F46 = list()
for row in df_list:
    if row['movieName'] == 'duma':
        if row['Author'] in X:
            F46.append(row['Metascore_w'])
F46_int = list(map(int, F46))
F46_sum = sum(F46_int)
length = len(F46)
F46_final = F46_sum / length
F46_name = 'duma'
print(F46_final)

F47 = list()
for row in df_list:
    if row['movieName'] == 'kong-skull-island':
        if row['Author'] in X:
            F47.append(row['Metascore_w'])
F47_int = list(map(int, F47))
F47_sum = sum(F47_int)
length = len(F47)
F47_final = F47_sum / length
F47_name = 'kong-skull-island'
print(F47_final)

F48 = list()
for row in df_list:
    if row['movieName'] == 't2-trainspotting':
        if row['Author'] in X:
            F48.append(row['Metascore_w'])
F48_int = list(map(int, F48))
F48_sum = sum(F48_int)
length = len(F48)
F48_final = F48_sum / length
F48_name = 't2-trainspotting'
print(F48_final)

F49 = list()
for row in df_list:
    if row['movieName'] == 'chips':
        if row['Author'] in X:
            F49.append(row['Metascore_w'])
F49_int = list(map(int, F49))
F49_sum = sum(F49_int)
length = len(F49)
F49_final = F49_sum / length
F49_name = 'chips'
print(F49_final)

F50 = list()
for row in df_list:
    if row['movieName'] == 'zoolander':
        if row['Author'] in X:
            F50.append(row['Metascore_w'])
F50_int = list(map(int, F50))
F50_sum = sum(F50_int)
length = len(F50)
F50_final = F50_sum / length
F50_name = 'zoolander'
print(F50_final)

#Comparing the average rating between a random movie and the pirates movie, if they have a higher score they are added to a list to be printed out as recommended movies
Q = list()
if F1_final >= F_final:
    Q.append(F1_name)
if F2_final >= F_final:
    Q.append(F2_name)
if F3_final >= F_final:
    Q.append(F3_name)
if F4_final >= F_final:
    Q.append(F4_name)
if F5_final >= F_final:
    Q.append(F5_name)
if F6_final >= F_final:
    Q.append(F6_name)
if F7_final >= F_final:
    Q.append(F7_name)
if F8_final >= F_final:
    Q.append(F8_name)
if F9_final >= F_final:
    Q.append(F9_name)
if F10_final >= F_final:
    Q.append(F10_name)
if F11_final >= F_final:
    Q.append(F11_name)
if F12_final >= F_final:
    Q.append(F12_name)
if F13_final >= F_final:
    Q.append(F13_name)
if F14_final >= F_final:
    Q.append(F14_name)
if F15_final >= F_final:
    Q.append(F15_name)
if F16_final >= F_final:
    Q.append(F16_name)
if F17_final >= F_final:
    Q.append(F17_name)
if F18_final >= F_final:
    Q.append(F18_name)
if F19_final >= F_final:
    Q.append(F19_name)
if F20_final >= F_final:
    Q.append(F20_name)
if F21_final >= F_final:
    Q.append(F21_name)
if F22_final >= F_final:
    Q.append(F22_name)
if F23_final >= F_final:
    Q.append(F23_name)
if F24_final >= F_final:
    Q.append(F24_name)
if F25_final >= F_final:
    Q.append(F25_name)
if F26_final >= F_final:
    Q.append(F26_name)
if F27_final >= F_final:
    Q.append(F27_name)
if F28_final >= F_final:
    Q.append(F28_name)
if F29_final >= F_final:
    Q.append(F29_name)
if F30_final >= F_final:
    Q.append(F30_name)
if F31_final >= F_final:
    Q.append(F31_name)
if F32_final >= F_final:
    Q.append(F32_name)
if F33_final >= F_final:
    Q.append(F33_name)
if F34_final >= F_final:
    Q.append(F34_name)
if F35_final >= F_final:
    Q.append(F35_name)
if F36_final >= F_final:
    Q.append(F36_name)
if F37_final >= F_final:
    Q.append(F37_name)
if F38_final >= F_final:
    Q.append(F38_name)
if F39_final >= F_final:
    Q.append(F39_name)
if F40_final >= F_final:
    Q.append(F40_name)
if F41_final >= F_final:
    Q.append(F41_name)
if F42_final >= F_final:
    Q.append(F42_name)
if F43_final >= F_final:
    Q.append(F43_name)
if F44_final >= F_final:
    Q.append(F44_name)
if F45_final >= F_final:
    Q.append(F45_name)
if F46_final >= F_final:
    Q.append(F46_name)
if F47_final >= F_final:
    Q.append(F47_name)
if F48_final >= F_final:
    Q.append(F48_name)
if F49_final >= F_final:
    Q.append(F49_name)
if F50_final >= F_final:
    Q.append(F50_name)

#print the results of which movies are higher rated then pirates by viewers which also rated the pirates movie
print(Q)
    
#printing the results to a csv file
with open('output.csv','w') as result_file:
    wr = csv.writer(result_file, dialect='excel')
    wr.writerow(Q)
import pytest


link = "https://iced-latte.uk/"
first_name = "Test"
last_name = "Testtest"
email = "ilsinyakovmo4@gmail.com"
password = "80000005a"
'''Positive values of Names: 2 symbols with UPPERCASE letter, 3 symbols lowercase letters, 13 symbols with hyphens and space
                                  127 symbols with hyphens and UPPERCASE letters in the middle,
                                  128 symbols with spase
'''
new_first_name_127sym = "vfmpevqkeukeukidxtyxWSqzhdpstrahexbgtmypsmmtqv-ebupnzrslccysaduwtgncthlraykruyqcaqchoelsfiktzvdaewbwymapkfmwxfgbrqqwrsdhoamiyto"
new_first_name_128sym = "vfmpevqkeukeukidxtyxwsqzhdpstrahexbgtmypsmmtqvfebupnzrslccys duwtgncthlraykruyqcaqchoelsfiktzvdaewbwymapkfmwxfgbrqqwrsdhoamiytob"
new_first_name_positive = ["Il","ily", "Ann-Mary Kate",
                           pytest.param(new_first_name_127sym, marks=pytest.mark.xfail(reason='BE bug (>55 symbols) is not fixed')),
                           pytest.param(new_first_name_128sym, marks=pytest.mark.xfail(reason='BE bug (>55 symbols) is not fixed'))
                           ]
new_last_name_127sym = "qwertvqkeukeukidxtyxWSqzhdpstrahexbgtmypsmmtqv-ebupnzrslccysaduwtgncthlraykruyqcaqchoelsfiktzvdaewbwymapkfmwxfgbrqqwrsdhoamiyto"
new_last_name_128sym = "qwertvqkeukeukidxtyxWSqzhdpstrahexbgtmypsmmtqvs ebupnzrslccysaduwtgncthlraykruyqcaqchoelsfiktzvdaewbwymapkfmwxfgbrqqwrsdhoamiyto"
new_last_name_positive = ["Si","sin", 
                          pytest.param("Sinyak-Yak Ov", marks=pytest.mark.xfail(reason='FE bug "-" & "space" is not fixed')),
                          pytest.param(new_last_name_127sym, marks=pytest.mark.xfail(reason='Bugs: BE (>55 symbols) & FE (- & space) is not fixed')),
                          pytest.param(new_last_name_128sym, marks=pytest.mark.xfail(reason='Bugs: BE (>55 symbols) & FE (- & space) is not fixed')),
                          ]
new_email = "new@gmail.com"

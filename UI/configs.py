link = "https://iced-latte.uk/"
first_name = "Test"
last_name = "Testtest"
email = "ilsinyakovmo4@gmail.com"
password = "80000005a"
'''Positive values of First Name: 2 symbols with UPPERCASE letter, 3 symbols lowercase letters, 13 symbols with hyphens and space
                                  127 symbols with hyphens and UPPERCASE letters in the middle, 
                                  128 symbols with spase
'''
new_first_name_positive = ["Il","ily", "Ann-Mary Kate",
                           pytest.param("vfmpevqkeukeukidxtyxWSqzhdpstrahexbgtmypsmmtqv-ebupnzrslccysaduwtgncthlraykruyqcaqchoelsfiktzvdaewbwymapkfmwxfgbrqqwrsdhoamiyto", marks=pytest.mark.xfail(reason='BE bug (>55 symbols) is not fixed')), 
                           pytest.param("vfmpevqkeukeukidxtyxwsqzhdpstrahexbgtmypsmmtqvfebupnzrslccys duwtgncthlraykruyqcaqchoelsfiktzvdaewbwymapkfmwxfgbrqqwrsdhoamiytob", marks=pytest.mark.xfail(reason='BE bug (>55 symbols) is not fixed'))]
new_last_name_positive = ["Si","sin", "Sinyak-Yak Ov",
                           "qwertvqkeukeukidxtyxWSqzhdpstrahexbgtmypsmmtqv-ebupnzrslccysaduwtgncthlraykruyqcaqchoelsfiktzvdaewbwymapkfmwxfgbrqqwrsdhoamiyto", 
                           "asdfgvqkeukeukidxtyxwsqzhdpstrahexbgtmypsmmtqvfebupnzrslccys duwtgncthlraykruyqcaqchoelsfiktzvdaewbwymapkfmwxfgbrqqwrsdhoamiytob"]
new_email = "new@gmail.com"

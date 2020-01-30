import webbrowser
#
# webbrowser.open("https://www.nba.com", new=2)
#
# help(webbrowser)


# for i in range(1,10):
#     print(1,2,3,4,5,6,7,8,9, sep="", end=' ')

chrome = webbrowser.get(using='chrome')
chrome.open_new("https://www.nba.com")

safari = webbrowser.get(using='safari')
safari.open_new("https://www.nfl.com")




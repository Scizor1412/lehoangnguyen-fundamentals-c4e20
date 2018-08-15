from youtube_dl import YoutubeDL
options = {
    'default_search' : 'ytsearch',
    'format': 'bestaudio',
    'max_downloads' : 1
}
dl=YoutubeDL(options)
# dl.download(['https://www.youtube.com/watch?v=WHK5p7JL7g4'])
# dl.download(['https://www.youtube.com/watch?v=wNVIn-QS4DE', 'https://www.youtube.com/watch?v=JZjRrg2rpic'])
# dl.download(['con điên tamka PKL'])
dl.download(['nhớ mưa sài gòn lam trường'])
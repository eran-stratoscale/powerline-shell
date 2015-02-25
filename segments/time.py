from datetime import datetime

def add_fuzzy_time():

    now = datetime.now()
    powerline.append( now.strftime(" %H:%M:%S ")  ,Color.TIME_FG, Color.TIME_BG)
    return

add_fuzzy_time()

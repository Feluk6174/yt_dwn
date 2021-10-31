import pafy, sys

def info(url):
    # instant created
    video = pafy.new(url)
    
    text = f"""__________{video.title}__________
    Author: {video.author}
    Rating: {video.rating}
    Views: {video.viewcount}
    Duration: {video.length}s
    Likes: {video.likes}
    Dislikes: {video.dislikes}
    """

    print(text)

def video(url, argv):
    url = argv[2]
    try:
        prefered_type = argv[3][1::]
        if not argv[3] == "-p":
            p = 1
        else:
            p = 2
    except IndexError:
        p = 0
    
    video = pafy.new(url)
  
    streams = video.streams
    for i in streams:
        print(i)
        
    # get best resolution regardless of format
    if not p == 1:
        best = video.getbest()
    else:
        best = video.getbest(preftype = prefered_type)
    
    print(best.resolution, best.extension)
    
    # Download the video
    if not p == 2:
        best.download()

def audio(url, argv):
    video = pafy.new(url)
    correct = []
 
    try:
        prefered_type = argv[3][1::]
        if not argv[3] == "-p":
            p = 1
        else:
            p = 2
    except IndexError:
        p = 0

    if not p == 0:
        audiostreams = video.audiostreams
        for i, a in enumerate(audiostreams):
            print(i, a.bitrate, a.extension, a.get_filesize())
            if p == 1:
                #print(a.extension, prefered_type)
                if a.extension == prefered_type:
                    correct.append(i)
        #print(correct)
        if p == 1:
            #print(correct[-1])
            audiostreams[correct[-1]].download()
    
    else:
        bestaudio = video.getbestaudio()
        bestaudio.download()

def help():
    text = """
-h >> Shows the this message
-s >> Opens Shell
-a >> Downloads audio of video, argumets url file_type(ex: -m4a, -webm...)
-v >> Downloads video, argumets url file_type(ex: -mp4, -3gp...)
-f >> Downloads everithing from a text file, arguments, -v or -a for video or audio, -d or -path, if you use -d it will use the deault text file(./music.txt), -path needs to be followed from the path of the text file you want to download, and at the end you can specify what filetype you want (es -m4a, -mp4...)
    """
    print(text)

if sys.argv[1] == "-h" or sys.argv[1] == "--help":
    help()

if sys.argv[1] == "-f":
    prefered_type = None
    if sys.argv[3] == "-d":
        file = "./music.txt"
        try:
            prefered_type = sys.argv[4]
        except IndexError:
            pass
    if sys.argv[3] == "-path":
        file = sys.argv[4]
        try:
            prefered_type = sys.argv[5]
        except IndexError:
            pass


    with open(file, "r") as f:
        text = f.readlines()

    if sys.argv[2] == "-a":
        for line in text:
            line = line[:-1:]
            print(line, line[-1])
            if prefered_type == None:
                audio(line, [None, "-a", line])
            else:
                audio(line, [None, "-a", line, prefered_type])
    elif sys.argv[2] == "-v":
        for line in text:
            line = line[:-1:]
            #print(line, line[-1])
            if prefered_type == None:
                audio(line, [None, "-v", line])
            else:
                audio(line, [None, "-v", line, prefered_type])

if sys.argv[1] == "-v":
    url = sys.argv[2]
    video(url, sys.argv)

if sys.argv[1] == "-a":
    url = sys.argv[2]
    audio(url, sys.argv)
    

if sys.argv[1] == "-i":
    url = sys.argv[2]
    info(url)
    

if sys.argv[1] == "-s":
    while True:
        command = input("   >> ")
        if command == "exit" or command == "e":
            break
        elif command == "help" or command == "h":
            help()
        else:
            args = command.split(" ")
            if args[0] == "info" or args[0] == "i":
                info(args[1])
            elif args[0] == "audio" or args[0] == "a":
                try:
                    audio(line, [None, "-a", args[1], "-"+args[2]])
                except IndexError:
                    audio(line, [None, "-a", args[1]])
            elif args[0] == "video" or args[0] == "v":
                try:
                    video(line, [None, "-v", args[1], "-"+args[2]])
                except IndexError:
                    video(line, [None, "-v", args[1]])
                
            
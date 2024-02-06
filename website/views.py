from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
data = {}


def index(request):
    global data

    # Change your name and description here
    data["yourname"] = "Keval Vavaliya"
    data["whatareyou"] = ["Designer", "Programmer", "Reader"]

    # about
    data[
        "aboutpara1"
    ] = "I’m Keval, a Software Developer from Surat, India.I am Currently pursuing Bachelor of Engineering in Information Technology at LDCE, I consider myself as a maker of things, who solves user-problems using technology. My interests and skills extend to  Mobile apps development,Backend systems and Machine Learning, allowing me to explore the realms of intelligent systems and architecting efficient solutions."
    data[
        "aboutpara2"
    ] = "I like to work with new tools and technologies,I’m always down for hearing about new projects, so feel free to drop me a line."
    data["aboutimage"] = "image/kevalvavaliya.jpeg"

    # my journey (can have max 4 only)
    data["journey1"] = {
        "startyear": "2018",
        "endyear": "",
        "desc": "Completed Secondary school at Gajera International School,Surat",
    }
    data["journey2"] = {
        "startyear": "2018-",
        "endyear": "2021",
        "desc": "Joined Diploma in Information Technology,at SSGCET , Surat",
    }
    data["journey3"] = {
        "startyear": "2021",
        "endyear": "2023",
        "desc": "Bachelor in I.T, at LDCE,Hackathons, built projects like Yog4life and Plastidive",
    }
    data["journey4"] = {
        "startyear": "2023-",
        "endyear": "Present",
        "desc": "Gained experience by working at startups like Discoze,Opensort and Kwiktech",
    }

    # my skills
    data["skills"] = [
        {"name": "Android", "icon": "icons/kevalvavaliya-android.svg"},
        {"name": "Java", "icon": "icons/kevalvavaliya-java.svg"},
        {"name": "Flutter", "icon": "icons/kevalvavaliya-flutter.svg"},
        {"name": "Dart", "icon": "icons/kevalvavaliya-dart.svg"},
        {"name": "Python", "icon": "icons/kevalvavaliya-python.svg"},
        {"name": "Django", "icon": "icons/kevalvavaliya-django.svg"},
        {"name": "JavaScript", "icon": "icons/kevalvavaliya-js.svg"},
        {"name": "HTML", "icon": "icons/kevalvavaliya-html.svg"},
        {"name": "CSS", "icon": "icons/kevalvavaliya-css.svg"},
        {"name": "PHP", "icon": "icons/kevalvavaliya-php.svg"},
        {"name": "JQuery", "icon": "icons/kevalvavaliya-jquery.svg"},
        {"name": "Github", "icon": "icons/kevalvavaliya-github.svg"},
        {"name": "Firebase", "icon": "icons/kevalvavaliya-firebase.svg"},
        {"name": "Docker", "icon": "icons/kevalvavaliya-docker.svg"},
        # {"name": "Wordpress", "icon": "icons/kevalvavaliya-wordpress.svg"},
        {"name": "MySQL", "icon": "icons/kevalvavaliya-mysql.svg"},
        {"name": "Flask", "icon": "icons/kevalvavaliya-flask.svg"},
        {"name": "Tensorflow", "icon": "icons/kevalvavaliya-tensorflow.svg"},
        {"name": "Google Cloud", "icon": "icons/kevalvavaliya-googlecloud.svg"},
        {"name": "PostgreSQL", "icon": "icons/kevalvavaliya-postgresql.svg"},
        {"name": "CockroachDB", "icon": "icons/cockroachdb.svg"},
        
        
    ]

    # social-links
    data["social_links"] = [
        {"name": "Github", "socialURL": "https://github.com/kevalvavaliya"},
        {"name": "Twitter", "socialURL": "https://twitter.com/keval_vavaliya"},
        {"name": "Linkedin", "socialURL": "https://www.linkedin.com/in/kevalvavaliya/"},
        {"name": "Instagram", "socialURL": "https://www.instagram.com/kevalvavliya/"},
    ]

    # projects
    data["projects"] = [
        {
            "id": "01",
            "name": "Vedvaani",
            "live":"https://play.google.com/store/apps/details?id=com.vedvaani.app&pcampaignid=web_share",
            "projectimg": "image/project/kevalvavaliya-vedvaani.png",
            "tech": "#FLUTTER #MATERIALUI #FIREBASE",
            "desc": "VedVaani is a platform that allows users to engage in conversations with AI characters. Users can interact with AI Astrologers, Movie Characters, Career and Love Coaches, and Influencers, and even participate in an Adventure Game.This app has been Designed, Developed and engineered by me at Discoze.",
        },
        {
            "id": "02",
            "name": "Plastidive",
            "github": "https://github.com/kevalvavaliya/PlastiDive",
            "devpost":"https://devpost.com/software/plastdive",
            "projectimg": "image/project/kevalvavaliya-plastidive.png",
            "tech": "#FLUTTER #FLASK #YOLOV5 #FIREBASE #ML",
            "winner":"DeepDive Hacks",
            "desc": "A game app that helps to eliminate plastic,Click some polluted photos of the beach, the app will upload them to the server. YOLO model will determine the level of plastic and show it up on the map for help from society. Virtuous will help clean the place and upload the photo. YOLO model will check if the beach is clean or not and will reward virtuous with virtual currency.",
        },
        {
            "id": "03",
            "name": "Yog4Life Social App",
            "github": "https://github.com/kevalvavaliya/Yog4Life",
            "devfolio":"https://devfolio.co/projects/yoglife-b20d",
            "projectimg": "image/project/kevalvavaliya-yog.png",
            "tech": "#FLUTTER #HEDERA #NODE.JS #IPFS(FILECOIN)",
            "winner":"HackOdisha",
            "desc": "An app for helping people their healthy life. Yog4Life Has a feed feature which is help to get information from the folks, Yog4Life has an anonymous chat room to get connected with the world.",
        },
        {
            "id": "02",
            "name": "OpenSort's site",
            "github": "https://github.com/rajmahadev8/OpenSort",
            "live": "https://www.opensort.io/",
            "projectimg": "image/project/kevalvavaliya-opensort.png",
            "tech": "#HTML #CSS #JS #JQUERY",
            "desc": "Designed and developed the website for a dynamic startup committed to family empowerment.",
        },
        {
            "id": "03",
            "name": "Bauddhik-Geeks Portfolio",
            "github": "https://github.com/Bauddhik-Geeks/Bauddhik-Geeks.github.io",
            "live": "https://bauddhikgeeks.co/",
            "projectimg": "image/project/kevalvavaliya-bauddhik.png",
            "tech": "#HTML #CSS #JS #JQUERY",
            "desc": "Awesome Community Portfolio website for Bauddhik-Geeks community",
        },
        {
            "id": "06",
            "name": "Connect",
            "github": "https://github.com/abhigoyani/connect1",
            "projectimg": "image/project/kevalvavaliya-connect.png",
            "tech": "#REACT #FLASK #JQUERY #MYSQL",
            "desc": "Connect connects audiences to all of your content with just one click.It is an open source alternative to linkrtree implemented in javscript and flask",
        },
        {
            "id": "07",
            "name": "Goverdhan Institute site",
            "github": "https://github.com/kevalvavaliya/Goverdhan-infotech",
            "projectimg": "image/project/kevalvavaliya-goverdhan.png",
            "tech": "#DJANGO #HTML #CSS #JS #MYSQL",
            "desc": "Education site for goverdhan institute that manages the courses and events online which makes student easy to reach them.",
        },
        {
            "id": "08",
            "name": "We-Donate",
            "github": "https://github.com/kevalvavaliya/We-Donate",
            "projectimg": "image/project/kevalvavaliya-wedonate.png",
            "tech": "#ANDROID #FLASK #XML #COCKROACHDB #JAVA",
            "desc": "We-Donate aims in bringing digitization in donation.we donate delivers your donation to the right hands and provides home pickup services.",
        },
        {
            "id": "09",
            "name": "Localens",
            "github": "https://github.com/kevalvavaliya/Localens",
            "projectimg": "image/project/kevalvavaliya-localens.png",
            "tech": "#ANDROID #FLASK #XML #COCKROACHDB #JAVA",
            "desc": "Localens is an android app for finding local beauty spots in your localities and get them capture in the app and take it to the world",
        },
        {
            "id": "10",
            "name": "Vishvas Fabrics Ecommerce site",
            "github": "https://github.com/kevalvavaliya/E-commerce-site",
            "projectimg": "image/project/kevalvavaliya-vishvas.png",
            "tech": "#PHP #HTML #CSS #JS #MYSQL",
            "desc": "A basic ecommerce site for vishvas fabrics",
        },
        
    ]
    data[
        "resumelink"
    ]= "https://drive.google.com/file/d/1Nc_Wl2OmqLR_BIquDEC3s8E-VCwbO-z8/view?usp=sharing"

    return render(request, "index.html", data)

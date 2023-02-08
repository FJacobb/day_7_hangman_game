from tkinter import *
from tkinter import messagebox
import random
import time
word_list = [
  "hello",
  "world",
  "python",
  "code",
  "programming",
  "language",
  "computer",
  "science",
  "data",
  "artificial",
  "intelligence",
  "machine",
  "learning",
  "deep",
  "neural",
  "network",
  "algorithm",
  "math",
  "statistics",
  "research",
  "academia",
  "development",
  "software",
  "engineering",
  "development",
  "web",
  "mobile",
  "desktop",
  "game",
  "graphics",
  "design",
  "user",
  "experience",
  "interface",
  "frontend",
  "backend",
  "fullstack",
  "devops",
  "cloud",
  "security",
  "database",
  "network",
  "administration",
  "systems",
  "administrator",
  "operator",
  "security",
  "penetration",
  "testing",
  "ethical",
  "hacking",
  "cybersecurity",
  "cryptography",
  "encryption",
  "decryption",
  "digital",
  "signature",
  "certificate",
  "authentication",
  "authorization",
  "access",
  "control",
  "management",
  "compliance",
  "regulation",
  "policy",
  "law",
  "litigation",
  "contract",
  "agreement",
  "negotiation",
  "arbitration",
  "mediation",
  "dispute",
  "resolution",
  "conflict",
  "peace",
  "justice",
  "equality",
  "freedom",
  "liberty",
  "human",
  "rights",
  "dignity",
  "autonomy",
  "sovereignty",
  "citizenship",
  "nation",
  "state",
  "government",
  "politics",
  "policy",
  "diplomacy",
  "military",
  "defense",
  "security",
  "intelligence",
  "espionage",
  "covert",
  "overt",
  "operations",
  "tactics",
  "strategy",
  "war",
  "peacekeeping",
  "peacemaking",
  "humanitarian",
  "assistance",
  "relief",
  "development",
  "sustainability",
  "environment",
  "conservation",
  "preservation",
  "ecology",
  "biodiversity",
  "climate",
  "change",
  "global",
  "warming",
  "pollution",
  "waste",
  "management",
  "recycling",
  "sustainability",
  "renewable",
  "energy",
  "resources",
  "mining",
  "extraction",
  "production",
  "manufacturing",
  "industry",
  "econom"]
blank = []
ck = []
def word2():
    global wd, blankword,blank, ck
    blank = []
    wd = random.choice(word_list)
    ck.append(wd)
    print(ck)
    word_list.remove(wd)
    for x in wd:
        blank.append("-")
    blankword = "".join(blank)
    return wd, blankword
###########################################################################################################################
def check(user_input, word, life):
    global name, blankword,num
    if life >1 :
        if user_input in word:
            for x in range(0,len(word)):
                if user_input == word[x]:
                    blank[x] = user_input

        else:
            life = life - 1
    else:
        life = life - 1
        canvers.itemconfig(hangtree, image=tree2)
        canvers.delete(manpic, womanpic)
    blankword = "".join(blank)
    print(blankword)

    return blankword, life
#########################################################################################################################
def play_game():
    def bt():
        global life,blankword,num
        blankword, life = check(input_lt.get(), name, life)
        input_lt.delete(0, "end")
        canvers.itemconfig(bk, text=f"{blankword}", font=("Arial Rounded MT Bold", 30, "bold"), fill="white")
        canvers.itemconfig(health, image=lv[life])
        if name == "".join(blank):
            messagebox.showinfo("Game results", f"you win level {num}")
            num += 1
            play_game()


    def enter1(e):
        canvers.itemconfig(butten_exit, image=exit_b2)
        time.sleep(2)
        canver.delete("all")
        home.destroy()
    global hangtree, canvers,manpic,womanpic
    canvers = Canvas(width=826, height=620)
    mainpage = canvers.create_image(413, 310, image=background)
    hangtree = canvers.create_image(650, 270, image=tree)
    level2 = canvers.create_image(400, 110, image=level)
    stage = canvers.create_text(400, 133, text=f"{num}",font=("Arial Rounded MT Bold", 30, "bold"), fill="white")
    bd = canvers.create_image(400, 500, image=bread)
    manpic = canvers.create_image(100, 390, image=man)
    womanpic = canvers.create_image(200, 400, image=woman)
    butten_exit = canvers.create_image(100, 120, image=exit_b)
    health = canvers.create_image(720, 70, image=l6)
    input_lt = Entry(canvers, width=4,justify=CENTER, font=("Arial Rounded MT Bold", 25, "bold"), fg="white", border=1, bg="#ed2424")
    input_lt.place(x=350, y=539)
    name, blankwd = word2()
    canvers.tag_bind(butten_exit, "<Button>", enter1)
    print(name)
    bf = Button(canvers, text="check", command=bt, fg="white", border=1, bg="#ed2424")
    bf.place(x=460,y=545)
    bk = canvers.create_text(395,500, text=f"{blankwd}",font=("Arial Rounded MT Bold", 30, "bold"), fill="white")
    bh = canvers.create_text(400, 400, text=f"Guess a letter", font=("Arial Rounded MT Bold", 15, "bold"), fill="white")
    canvers.place(x=-1, y=0)
#####################################################################################################################################################
def start_game(e):
    canver.itemconfig(butten_play, image=play_on)
    time.sleep(2)
    canver.delete("all")
    play_game()
def end_game(e):
    canver.itemconfig(butten_exit, image=exit_b2)
    time.sleep(2)
    canver.delete("all")
    home.destroy()
num =1
life=6
home = Tk()
home.title("HANG MAN")
home.geometry("826x620")
background = PhotoImage(file="image/seamless-colorful-trees-forest-against-backdrop-mountains_284645-1314.png")
play = PhotoImage(file="image/play.png")
start_tree = PhotoImage(file="image/Layer 1.png")
play_on = PhotoImage(file="image/play 2.png")
exit_b = PhotoImage(file="image/exit.png")
exit_b2 = PhotoImage(file="image/exit 2.png")
level = PhotoImage(file="image/level.png")
bread = PhotoImage(file="image/word borad.png")
man = PhotoImage(file="image/man.png")
woman = PhotoImage(file="image/woman.png")
tree = PhotoImage(file="image/tree.png")
tree2 = PhotoImage(file="image/Layer 2.png")
l0 = PhotoImage(file="image/0 life.png")
l1 = PhotoImage(file="image/1 life.png")
l2 = PhotoImage(file="image/2 life.png")
l3 = PhotoImage(file="image/3 life.png")
l4 = PhotoImage(file="image/4 life.png")
l5 = PhotoImage(file="image/5 life.png")
l6 = PhotoImage(file="image/6 life.png")
lv =[l0,l1,l2,l3,l4,l5,l6]
def enter1(e):
    canver.itemconfig(butten_exit, image=exit_b2)
def leave1(e):
    canver.itemconfig(butten_exit, image=exit_b)
def enter(e):
    canver.itemconfig(butten_play, image=play_on)
def leave(e):
    canver.itemconfig(butten_play, image=play)
def text():
    print("festus")
canver = Canvas(width=826,height=620)
canver.configure(highlightthickness=0)
mainpage = canver.create_image(413,310, image=background)
butten_play = canver.create_image(250,250, image=play)
butten_exit = canver.create_image(250, 350, image=exit_b)
tree_black = canver.create_image(650, 270, image=tree)

welcome = canver.create_text(590,30, text="WELCOME TO HANGMAN", font=("Arial Rounded MT Bold", 25, "bold"), fill="white")
canver.tag_bind(butten_play, "<Button>", start_game)
canver.tag_bind(butten_exit, "<Button>", end_game)
canver.place(x=-1, y=0)

home.mainloop()


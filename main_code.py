menu = "enter your key \n 'a' add movie \n 'l' to see your movie \n 'f' to find the movie \n 'q' to quit"
movie = []


def add_movie():
    title = input("enter the movie title ")
    director = input("enter the director name ")
    year = input("enter the year released ")
    movie.append({
        "title": title,
        "director": director,
        "year": year
    })



def show_movie():
    for i in movie:
        print_movie(i)


def print_movie(i):
    print(f"Title : {i['title']}")
    print(f"Director : {i['director']}")
    print(f"Year : {i['year']}")


def find_movie():
    search = input("enter require title: ")

    for i in movie:
        if (i["title"] == search):
            print_movie(i)


user_option={
    "a":add_movie,
    "l":show_movie,
    "f":find_movie
}

def MENU():
    entry = input(menu)
    while (entry != 'q'):
        if entry in user_option:
            select=user_option[entry]
            select()
        else:
            print("Invalid input ")

        entry=input(menu)



MENU()

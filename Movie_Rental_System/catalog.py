m_list = []

def addMovie(title,genre,r_price,):
    m_details = (title,genre,r_price)
    m_list.append(m_details)
    print(f"movie :{title} added successfully...")


def availableMovies():
    if m_list:
        print("available movies are : ")
        for mov in m_list:
            print(f"title : {mov[0]} , genre : {mov[1]} , r_price : {mov[2]}")      
    else:
        print("no available movies .....")
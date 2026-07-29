import pandas as pd
import tkinter as tk
def load_book():
    books = pd.read_csv("book_recommend/book_dataset.csv")                
    return books


def find_book(books,book_name):
        result = books[books['Title']==book_name]             
        if result.empty:                  
            print("Book not found!")
            return None
        else:
            selected_genre = result.iloc[0]['Genre']            
            selected_author = result.iloc[0]['Author']         
            selected_language = result.iloc[0]['Language']
            return selected_language, selected_genre, selected_author
        



def recommended_books(books,book_name,selected_language,selected_genre,selected_author):
        recommendations = []             

        for index,row in books.iterrows():    
            if row['Title'] == book_name:
                pass
            else:
                score = 0
                if row['Language'] == selected_language:
                    score = score + 1
                if row['Genre'] == selected_genre:               
                    score = score + 2
                if row['Author'] == selected_author:
                    score = score + 3
            
                if score > 0:
                    recommendations.append((row,score))                  
        return recommendations


def display_recommendations(recommendations,num):
        if len(recommendations)==0:
            print("Sorry! No similar books found.")
        else:
            recommendations = sorted(recommendations,key=lambda x: x[1],reverse=True)          
            print("=> Top ",num," recommended books are:-- \n")
            for item in recommendations[0:num]:
                book = item[0]
                score = item[1]

                print("Title : ",book['Title'])
                print("Author : ",book['Author'])
                print("Genre : ",book['Genre'])
                print("Language : ",book['Language'])
                print("Year : ",book['Year'])
                print("=" * 30)



def recommend():
    result_box.delete(1.0,tk.END)
    books = load_book()
    book_name = book_entry.get()

    if book_name == "":
        result_box.insert(tk.END, "⚠ Please enter a book name.")
        return

    try:
        num = int(num_entry.get())
    except:
        result_box.insert(tk.END, "⚠ Enter a valid number.")
        return

    data = find_book(books, book_name)

    if data is None:
        result_box.insert(tk.END, "❌ Book not found.")
        return

    selected_language, selected_genre, selected_author = data

    recommendations = recommended_books(books,book_name,selected_language,selected_genre,selected_author)

    recommendations = sorted(recommendations,key=lambda x: x[1],reverse=True)

    result_box.insert(tk.END,f"📚 Top {num} Recommendations\n")
    result_box.insert(tk.END,"="*55 + "\n\n")

    for item in recommendations[:num]:

        book = item[0]

        result_box.insert(
            tk.END,
            f"📖 {book['Title']}\n"
            f"👤 Author : {book['Author']}\n"
            f"🏷 Genre : {book['Genre']}\n"
            f"🌍 Language : {book['Language']}\n"
            f"📅 Year : {book['Year']}\n"+ "-"*55 + "\n\n"
        )


#------------CREATE MAIN WINDOW------------
root = tk.Tk()
root.title("Book recommendation system")
root.geometry("850x650")
root.config(bg="#EAF4FC")


#----------HEADING---------------
heading = tk.Label(root,text="📚 BOOK RECOMMENDATION SYSTEM",font=('Segoe UI',22,'bold'),bg='#4A90E2',fg='white')
heading.pack(padx=20,pady=10)




#---------BOOK NAME---------
label1 = tk.Label(root,text="Enter book name:",font=('Arial',14),width=40)
label1.pack()

book_entry = tk.Entry(root,font=('Segoe UI',14),width=40)
book_entry.pack(pady=10)



#----------NO. OF RECOMMENDATIONS---------
label2 = tk.Label(root,text='Number of Recommendations:',font=('Arial',14),bg="#E8F6F3")
label2.pack()

num_entry = tk.Entry(root,font=('Arial',14),width=10)
num_entry.pack(pady=10)


#-------RESULT BOX---------
result_box = tk.Text(root,width=80,height=20,font=('Consolas',11),bg='#FDFEFE')
result_box.pack(pady=20)

result_box.insert(tk.END,"📚 Welcome to the Book Recommendation System!\n\n""📖 Enter a book name.\n""🔍 Choose the number of recommendations.\n""✅ Click the 'Recommend' button.\n\n"+ "="*60 + "\n\n")



#-----BUTTONS------
recommend_btn = tk.Button(root,text="🔍Recommend",font=('Segoe UI',14,'bold'),bg='#2ECC71',fg='white',command=recommend)
recommend_btn.pack(pady=10)


#--------CLEAR BUTTON-------
def clear():
    book_entry.delete(0,tk.END)
    num_entry.delete(0,tk.END)
    result_box.delete(1.0,tk.END)

clear_btn = tk.Button(root,text="🗑Clear",command=clear,bg='#E67E22',fg='white',font=('Segoe UI',12))
clear_btn.pack()


root.mainloop()

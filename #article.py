#article

import os

# define the article class
class Article:
    def __init__(self, title, content):
        self.title = title
        self.content = content
    
    def __str__(self):
        return f"{self.title}\n\n{self.content}\n"

# define the article database class
class ArticleDB:
    def __init__(self):
        self.articles = []
        self.load_articles()
    
    def load_articles(self):
        if not os.path.exists('articles.txt'):
            return
        
        with open('articles.txt', 'r') as file:
            title = ''
            content = ''
            
            for line in file:
                if line.strip() == '':
                    if title != '' and content != '':
                        self.articles.append(Article(title, content))
                        title = ''
                        content = ''
                elif title == '':
                    title = line.strip()
                elif content == '':
                    content = line.strip()
    
    def save_articles(self):
        with open('articles.txt', 'w') as file:
            for article in self.articles:
                file.write(str(article))
    
    def add_article(self):
        title = input("Enter the article title: ")
        content = input("Enter the article content: ")
        
        self.articles.append(Article(title, content))
        self.save_articles()
        
        print("Article added successfully!")
    
    def delete_article(self):
        if not self.articles:
            print("There are no articles to delete.")
            return
        
        print("Select an article to delete:")
        for i, article in enumerate(self.articles):
            print(f"{i + 1}. {article.title}")
        
        selection = int(input("> ")) - 1
        
        del self.articles[selection]
        self.save_articles()
        
        print("Article deleted successfully!")
    
    def view_articles(self):
        if not self.articles:
            print("There are no articles to view.")
            return
        
        for article in self.articles:
            print(article)
    
    def menu(self):
        while True:
            print("Select an option:")
            print("1. Add article")
            print("2. Delete article")
            print("3. View articles")
            print("4. Quit")
            
            selection = int(input("> "))
            
            if selection == 1:
                self.add_article()
            elif selection == 2:
                self.delete_article()
            elif selection == 3:
                self.view_articles()
            elif selection == 4:
                break
            else:
                print("Invalid selection. Please try again.")
        
        print("Goodbye!")

# start the application
db = ArticleDB()
db.menu()

#GUI Articles

import tkinter as tk

class ArticleDB:
    def __init__(self):
        self.articles = []
    
    def create_article(self, title, content):
        self.articles.append({'title': title, 'content': content})
        print('Article created.')
    
    def view_article(self, index):
        try:
            article = self.articles[index]
            print(f"Title: {article['title']}\nContent: {article['content']}\n")
        except IndexError:
            print('Invalid article index.')
    
    def delete_article(self, index):
        try:
            del self.articles[index]
            print('Article deleted.')
        except IndexError:
            print('Invalid article index.')

class ArticleApplication:
    def __init__(self):
        self.db = ArticleDB()
        self.root = tk.Tk()
        self.root.title('Article Storage')
        
        title_label = tk.Label(self.root, text='Title:')
        title_label.grid(row=0, column=0)
        self.title_entry = tk.Entry(self.root)
        self.title_entry.grid(row=0, column=1)
        
        content_label = tk.Label(self.root, text='Content:')
        content_label.grid(row=1, column=0)
        self.content_entry = tk.Entry(self.root)
        self.content_entry.grid(row=1, column=1)
        
        create_button = tk.Button(self.root, text='Create Article', command=self.create_article)
        create_button.grid(row=2, column=0)
        
        view_button = tk.Button(self.root, text='View Articles', command=self.view_articles)
        view_button.grid(row=2, column=1)
        
        delete_button = tk.Button(self.root, text='Delete Article', command=self.delete_article)
        delete_button.grid(row=2, column=2)
        
        self.root.mainloop()
    
    def create_article(self):
        title = self.title_entry.get()
        content = self.content_entry.get()
        self.db.create_article(title, content)
        self.title_entry.delete(0, tk.END)
        self.content_entry.delete(0, tk.END)
    
    def view_articles(self):
        for i, article in enumerate(self.db.articles):
            print(f"{i+1}. {article['title']}")
    
    def delete_article(self):
        index = int(input('Enter article number to delete: ')) - 1
        self.db.delete_article(index)

if __name__ == '__main__':
    app = ArticleApplication()

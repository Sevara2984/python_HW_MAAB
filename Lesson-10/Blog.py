class Post:
    def __init__(self,title,content, author):
        self.title = title
        self.content = content
        self.author = author


def __str__(self):
        return f'Title {self.title}\nContent {self.content}\nAuthor {self.author}'
    



class Blog:
    post_list = []
    def __init__(self,blog_name):
        self.blog_name = blog_name


    def add_post(self,title):
        if len(self.post_list) < 1:
            content = input('Enter content: ')
            author = input('Enter author: ')
            post_object = Post(title, content, author)
            self.post_list.append(post_object)

        else: 
            for i in self.post_list:
                if i.title != title:
                    content = input('Enter content: ')
                    author = input('Enter author: ')
                    post_object = Post(title,content, author)
                    self.post_list.append(post_object)
                    print(f'Title {post_object.title} was added successfully!')
                    break
                else:
                    print(f'Title {i.title} is already exists')

    def list_all_posts(self):
        for i in self.post_list:
            print (f'{i.title} - {i.author}')

    def display_posts(self, author):
        for i in self.post_list:
            print (f'{i.title} - {i.author}')
            


    
def print_menu():
    print("\nBlog System Management Menu:")
    print("1. Add a post")
    print("2. List all posts")
    print("3. Display posts by a specific author")
    print("4. Delete a post")
    print("5. Edit a post")
    print("6. Exit")
    

    
def main():
    My_blog = Blog('MB')
    while True:
        choice = input('please select numbers: ')
        if choice == '1':
            title = input('Enter Post Title: ')
            
            My_blog.add_post(title)
        elif choice == '2':
            My_blog.list_all_posts()
        elif choice == '3':
            title = input('Enter Post Title ')
            My_blog.display_posts(title)
       
            
            
            
        else:
            break
            
a = print_menu()
b = main()
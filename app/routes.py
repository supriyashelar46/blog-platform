from flask import render_template,request,redirect,url_for,flash
from . import db  # Importing db for models if needed later
from .models import Post 


# Define the routes here
def init_routes(app):
    #Route to display all posts
    @app.route('/')
    def index():
        posts=Post.query.all() #fetch all posts from the database
        return render_template('index.html',posts=posts)

    # Add more routes as needed

    # Route to create a new post (Create operation)
    @app.route('/create', methods=['GET', 'POST'])
    def create_post():
        if request.method == 'POST':
            title = request.form.get('title')
            content = request.form.get('content')

            #Check if both fields are provided
            if not title or not content:
                flash('Title and content are required!','error')
                return redirect(url_for('create_post'))
            
            #Save the new post to the database
            new_post = Post(title=title,content=content)
            db.session.add(new_post)
            db.session.commit()

            flash('Post created successfully!','success')
            return redirect(url_for('index'))

        return render_template('create_post.html')  # A new template for creating posts
    
    #Route to update a post (update opertaion)
    @app.route('/update/<int:post_id>', methods=['GET', 'POST'])
    def update_post(post_id):
        posts = Post.query.get_or_404(post_id)  # Fetch the post by ID
        if request.method == 'POST':
            posts.title = request.form.get('title')
            posts.content = request.form.get('content')

            #Save changes to the database
            db.session.commit()
            flash('Post updated successfully!','success')
            return redirect(url_for('index'))
        
        return render_template('update_post.html',posts=posts)
    

    #Route to delete a post(Delete operation)
    @app.route('/delete/<int:post_id>',methods=['POST'])
    def delete_post(post_id):
        posts=Post.query.get_or_404(post_id)
        db.session.delete(posts)
        db.session.commit()
        flash('Post deleted successfully!','success')
        return redirect(url_for('index'))


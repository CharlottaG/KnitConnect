# The Knit Connect
![image](https://github.com/CharlottaG/KnitConnect/assets/138576943/d3f1d092-19e0-4550-a2c7-6432326e40a0)

[The Knit Connect](https://theknitconnect-456a7f14d941.herokuapp.com/)

## Purpose and Idea:
The Knit Connect is an app designed to create a vibrant and inclusive community for passionate knitters. Its main objectives are:
1.	Centralized Platform: The app provides a centralized platform where knitters of all skill levels can come together. It serves as a hub for sharing patterns, ideas, and experiences related to knitting.
2.	Creativity and Collaboration: “The Knit Connect” fosters creativity by allowing users to showcase their designs, explore new patterns, and collaborate with fellow enthusiasts. Whether you’re a seasoned knitter or a beginner, the app encourages creativity and learning.
3.	User-Friendly Interface: The app prioritizes ease of use. Its intuitive design ensures that even beginners can navigate and participate in the knitting community effortlessly.
4.	Meaningful Connections: By connecting knitters worldwide, “The Knit Connect” aims to build camaraderie and meaningful relationships. Users can learn from each other, seek inspiration, and share their passion for knitting.

## User Demographic:
The Knit Connect caters to a diverse group of users:
1.	Knitting Enthusiasts: Passionate knitters of all ages and backgrounds who want to connect with like-minded individuals, share their work, and learn from others.
2.	Beginners: Novice knitters seeking inspiration, guidance, and tutorials. The app provides a supportive environment for learning and improving knitting skills.
3.	Experienced Knitters: Seasoned knitters who want to showcase their designs, collaborate with others, and stay updated on the latest trends.
4.	Community Builders: Individuals interested in fostering a positive and encouraging knitting community. They contribute by sharing knowledge, organizing events, and supporting fellow users.

## Technologies Used
- HTML
- CSS
- Boostrap Framework CSS
- JavaScript
- Django Framework

## Tools
- Github – code repository
- Gitpod – cloud-based development environment
- Cloudinary – cloud storage for images
- ElefantSQL – postgres database

## Installation
To run the project locally, follow these steps:
1. Clone this repository to your local machine.
- git clone https://gitpod.com/charlottag/theknitconnect.git
2. Install Django and other dependencies.
- pip install django
3. Run migrations to create the database.
- python manage.py makemigrations
- python manage.py migrate
4. Create a superuser to manage the website.
- python manage.py createsuperuser
5. Start the server.
- python manage.py runserver

Go to https://theknitconnect-456a7f14d941.herokuapp.com/ in your browser to see The Knit Connect in action.

## User Stories
**Must have:**
- As a user, I want to sign up for an account on the app so that I can access its features and connect with other users.
- As a user, I want to log in to my account securely to access my saved patterns, project lists, and other personalized content.
- As a user, I want to be able to create and upload my own knitting patterns to share with the community.
- As a user, I want to view detailed information about each knitting pattern, including materials needed, gauge, and instructions.
- As a user, I want to be able to add knitting patterns to my project list for future reference and organization.
- As a user, I want to be able to leave comments on knitting patterns to share my experiences and feedback with other users.
- As a user, I want to be able to mark patterns as favorites for easy access and reference.

**Out of scope – for future development:**
- As a user, I want to be able to follow other users and see updates on their latest projects and patterns.
- As a user, I want to be able to search for knitting patterns based on categories such as type (e.g., sweaters, socks), difficulty level, and yarn weight.
- As a user, I want to be able to categorize yarns based on attributes such as fiber content, color, and brand.
- As a user, I want to be able to receive notifications for new patterns, comments on my patterns, and updates from users I follow.
- As a user, I want to be able to search for yarns based on categories and add them to my stash for tracking purposes.


## Relationship diagram
![image](https://github.com/CharlottaG/KnitConnect/assets/138576943/0b155a12-93de-4021-a3d7-a4e4d6be4156)

- Each "User" can create multiple "Patterns"
- Each "Pattern" can have multiple "Comments"
- "Comment" is associated with a "Pattern" through a foreign key relationship
- Each "User" can have multiple "Patterns" in their "ProjectList", and each "Pattern" can belong to multiple "ProjectLists"

## Pages
### The Knit Connect/Home
This is the home page, with a short introduction to the application.

### My page
This is the user’s own page, with lists of liked patterns, their own created patterns and patterns they want to knit. This page will evolve with more features in the future, things like yarn stash and needle range.
![image](https://github.com/CharlottaG/KnitConnect/assets/138576943/1449f1ba-b883-498b-8fce-53edb53df660)

### Patterns
This page contains all patterns added by the users with an image and the key facts that a user would look for, like level of difficulty, needle size and knitting gauge and a link to the actual pattern instructions.

### Pattern details
This is where the pattern instructions come, and where you can like the pattern, add it to you projects and also leave comments.

## Features & functionalities
### Account Management
Users can register for an account, sign-in or logout. All content except the home page is only available for logged-in users.

### Admin management
As a superuser you have access to the admin panel accessing the app from backend. The superuser can add and delete users, patterns and comments, as well as publish and unpublish patterns.

### Navigation Bar
From the navigation bar you can access patterns and the user’s own page.

### Patterns
Patterns is an app within the project. Logged in users can view other users’ patterns as well as add their own patterns. They can like patterns and view them as a list in their profile page. They can also add patterns to their list of projects, things they’d like to knit.

### Comments
Logged in users can comment on patterns and share their thoughts or ask questions to the pattern creator.

### Likes
Logged in users can like patterns and those will automatically be added to a list of liked patterns on the user’s own page.

### Add to projects
Logged in users can add patterns to a list of patterns they would like to knit in the future, which is featured on the user’s own page.

### Messages
The app use message functionality to let the user know what happens in the background, such as successfully adding a pattern or comment, liking/unlinking a pattern and adding a pattern to their project list.


## Deployment Process to Heroku
- Create Heroku App
- Set up of necessary environment variables or configuration settings for the application.
- Deployment the application to Heroku using Git. This involves pushing the code to the Heroku remote repository. 
- Heroku will then build the application using the specified buildpack and dependencies. 
- Once the build process is complete, URL can be used to access and interact with the deployed application.
  
## Testing
### Manual testing:
#### Links:	
- The Knit Connect – Home/Index page
- Register – that this takes the user to a registration page, and that it works to register
- Login - that this takes the user to a login page, and it works to login
- Logout - that this logs the user out, and that the user get a question if they want to do so. And that this link only shows when users are logged in.
- My page - That this link only shows when users are logged in and takes the user to a page with lists populated by the logged in user’s activity.
- Pattern – that this takes you to a page with patterns, and that the view details links take you to a detailed view of the pattern with instructions.

#### Functionality:
- Liking/Unliking a pattern – that it adds to the likes count shown at the side of the thumbs up icon, that it gets populated at the user’s page, and the liked patterns list. That the logged in user can’t like their own patterns.
- Add to project – that it gets added to the list of projects to knit at the user’s page.
- Commenting – that the logged in user can leave a comment on a pattern, and also edit or delete it.
- Messages – that all the actions the user takes to send information to the database is being visualized as notifications at the top of the page.
- Add pattern – that the form works, that the user can upload images and add texts in all fields to add a pattern, with validation to ensure unique values for pattern names.

## Future development:
I decided to create two apps in my project, one for patterns and one for users. The reason is that I want to develop the user app with more content related to the user such as creating a more complex user profile with more features, and potentially add different types of users with different levels of access to the content and functionality within The Knit Connect application. Other features that I’m thinking of include is a calculator for different knitting parameters, useful for knitters in their project plannings.

## Credits
I have referenced the CodeInstitute course content for I Think Therefor I Blog. I have also used google to find how to do different functions. Some are:
- https://stackoverflow.com/questions/63960326/django-no-file-chosen-in-fileinput
- https://docs.djangoproject.com/en/5.0/
- https://getbootstrap.com/docs/5.0/ 
- https://www.w3schools.com/django/

## Acknowledgment
I want to express my gratitude to Luke Buchanan for guiding me during this project and offering support and advice to help me overcome challenges and make progress.


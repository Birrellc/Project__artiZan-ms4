# ArtiZan

---

## Description

![PICTURE](/media/artizan-readme.png)

_this is a fictitious website created for my milestone project 4 with the code institute_.

An Ecommerce website created with django where there main purpose is for the user to view/purchase art and also have a sense of community with a blog that website visitors can comment on.

This is my final project in the Code Institute Full Stack Development course of which the main goal is to use Django to create an Ecommerce website with full payment system (stripe) with static and media files hosted on AWS.

Due to time constraints from when I started this project till my submission I was unable to implement some of the features I would have liked but plan to update this project after i have recieved my final grade. (Please see Future Features section to see planned improvements).

---

## Table of Contents

---

## UX

### Wireframes

The initial wireframes for this project [Wireframes](https://github.com/Birrellc/artiZan-ms4/tree/master/docs/wireframes)

_soon after starting this project I could make huge improvements to the initial design plan and immediately decided to change up the process._

---

### Database

Initial DB: [SQLite3](https://www.sqlite.org/index.html)
Final DB: [Heroku Postgres](https://www.heroku.com/postgres)


##### Category Model (Products Model)

| Field         | Field Type | Field Options                         |
| --------------| ---------- | ------------------------------------- |
| name          | CharField  | max_length=254                        |
| friendly_name | CharField  | max_length=254, null=True, blank=True |

##### Art Model (Products Model)

| Field         | Field Type   | Field Options                                                      |
| --------------| ----------   | ------------------------------------------------------------------ |
| name          | CharField    | max_length=254                                                     |
| sku           | CharField    | max_length=254                                                     |
| artist        | CharField    | max_length=254                                                     |
| price         | DecimalField | max_digits=10, decimal_places=2                                    |
| category      | ForeignKey   | 'Category', null=True, blank=True, on_delete=models.SET_NULL       |
| height        | DecimalField | max_digits=10, decimal_places=2                                    |
| width         | DecimalField | max_digits=10, decimal_places=2                                    |
| image_path    | URLField     | max_length=254, null=True, blank=True                              |
| image         | ImageField   | null=True, blank=True                                              |
| sold          | BooleanField | default=False                                                      |

##### Contact Details Model (Contact Model)

| Field         | Field Type | Field Options                         |
| --------------| ---------- | ------------------------------------- |
| label         | CharField  | max_length=254                        |
| email         | CharField  | max_length=254, blank=True            |
| tel           | CharField  | max_length=254, null=True, blank=True |

##### Order Model (Checkout Model)

| Field                | Field Type    | Field Options                                                                                  |
| ---------------------| ----------    | -----------------------------------------------------------------------------------------------|
| order_number         | CharField     | max_length=32, null=False, editable=False                                                      |
| user_profile         | ForeignKey    | UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders            |
| full_name            | CharField     | max_length=50, null=False, blank=False                                                         |
| email                | EmailField    | max_length=254, null=False, blank=False                                                        |
| phone_number         | CharField     | max_length=20, null=False, blank=False                                                         |
| country              | CountryField  | blank_label='Country \*', null=False, blank=False                                              |
| postcode             | CharField     | max_length=20, null=True, blank=True                                                           |
| town_or_city         | CharField     | max_length=40, null=False, blank=Falsee                                                        |
| street_address1      | Charfield     | max_length=80, null=False, blank=False                                                         |
| street_address2      | Charfield     | max_length=80, null=True, blank=True                                                           |
| county               | Charfield     | max_length=80, null=True, blank=True                                                           |
| date                 | DateTimeField | auto_now_add=True                                                                              |
| delivery_cost        | DecimalField  | max_digits=6, decimal_places=2, null=False, default=0                                          |
| order_total          | DecimalField  | max_digits=10, decimal_places=2, null=False, default=0                                         |
| grand_total          | DecimalField  | max_digits=10, decimal_places=2, null=False, default=0                                         |
| original_basket      | TextField     | null=False, blank=False, default=''                                                            |
| stripe_pid           | Charfield     | max_length=254, null=False, blank=False, default=''                                            |

##### OrderLineItem (Checkout Model)

| Field                | Field Type    | Field Options                                                                                  |
| ---------------------| ----------    | -----------------------------------------------------------------------------------------------|
| order                | ForeignKey    | Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems'             |
| product              | ForeignKey    | Art, null=False, blank=False, on_delete=models.CASCADE                                         |
| quantity             | IntegerField  | null=False, blank=False, default=0                                                             |
| lineitem_total       | DecimalField  | max_digits=6, decimal_places=2, null=False, blank=False, editable=False                        |

##### UserProfile (Profiles Model)

| Field                    | Field Type    | Field Options                                  |
| -------------------------| ----------    | -----------------------------------------------|
| user                     | OnetoOneField | User, on_delete=models.CASCADE                 |
| default_phone_number     | CharField     | max_length=20, null=True, blank=True           |
| default_street_address1  | CharField     | max_length=80, null=True, blank=True           |
| default_street_address2  | CharField     | max_length=80, null=True, blank=True           |
| default_town_or_city     | CharField     | max_length=40, null=True, blank=True           |
| default_county           | CharField     | max_length=80, null=True, blank=True           |
| default_postcode         | CharField     | max_length=20, null=True, blank=True           |
| default_country          | CountryField  | blank_label='Country', null=True, blank=True   |

##### Post (Blog Model)

| Field                    | Field Type    | Field Options                                              |
| -------------------------| ----------    | -----------------------------------------------------------|
| title                    | CharField     | max_length=200, unique=True                                |
| slug                     | SlugField     | max_length=200, unique=True                                |
| author                   | ForeignKey    | User, on_delete=models.CASCADE, related_name='blog_posts'  |
| updated_on               | DateTimeField | auto_now=True                                              |
| content                  | TextField     |                                                            |
| created_on               | DateTimeField | auto_now_add=True                                          |
| status                   | IntegerField  | choices=STATUS, default=0                                  |


##### Comment (Blog Model)

| Field                    | Field Type    | Field Options                                           |
| -------------------------| ----------    | --------------------------------------------------------|
| post                     | ForeignKey    | Post, on_delete=models.CASCADE, related_name='comments' |
| name                     | CharField     | max_length=80                                           |
| email                    | EmailField    | max_length=80, null=True, blank=True                    |
| body                     | TextField     | max_length=80, null=True, blank=True                    |
| created_on               | DateTimeField | auto_now_add=True                                       |
| active                   | BooleanField  | default=False                                           |


---

### User Stories

#### All Users:

- As a user i would like to access the site on my mobile, tablet, and desktop without issues.

- As a user i would like to easily navigate through the website to achieve my goal with ease.

- As a user i would like to be able to contact the owner/business with ease.

- As a user i would like to find the information of the artworks displayed with the products (eg. dimensions / artist name etc)

- As a user i would like to be able to add items to a shopping basket which i can then view and remove items before purchase if needed.

- As a user i would like to see the complete breakdown of the purchase i'm making.

- As a user i would like to be able to securely purchase artwork.

- As a user i would like to receive an email confirmation once I complete the payment.

- As a user i would like to be able to make an account to make purchases.

#### Returning Users:

- As a user i would like to be able to login to my existing account for making purchases.

- As a user i would like to be able to view past orders

- As a user i would like to be able to see and update my personal information.

- As a user i would like to be able to make purchases quicker by having previously stored my information.

#### Owner:

- As the owner i would like to be able to edit and delete products to the website.

- As the owner i would like to provide a way for the user to contact us for example with a contact form.

- As the owner i would like to have social media icons present on the website for proofing.


#### Goals Derived From User Stories:

- Create a responsive website design.

- Make sure social media is visable for proofing.

- Provide CRUD functionality (adding updating viewing and deleting products).

- Secure login system.

- Payment gateway (for users to make purchases).

---

### Landing Page

As an Art themed website once I got started I knew I had to make sure the landing page was aesthetically please so i chose to go with quite a basic color set in order to avoid chaos and keep it very art themed and minimalistic for the user.

The landing page consists of:

Navbar
Banner
Search Bar(on Desktop view)
Carousel of a few prints from the website
About us section
Hero image
Social Footer

---

### Store

For my store page I browsed various online retailers in multiple sectors and also using the code institute course material i decided to go with a simple product placement in rows of 4 and limited detail below each product so users wouldn't be distracted and also so they could browse products easily. The products are displayed in a card format with a color and border to help them stand out from the white background.

The Store page consists of:

Navbar
Banner
Products (in card form)
Sort filter
Categories filter
Small button to return to the top of the page
Update & Delete products buttons for admin
Ability to mark products as sold (this is for a later date when I manage to implement a stocking system)
Social Footer

---

### Blog

The Blog page like the rest of the website is of simple format to be quick and easy for the user to view and understand the premis. The plog posts are created in django admin where they can be marked and draft while waiting for review by the owner or immediately published. In the future I would like to add a form for specific users to create the Blog posts on page without having to go into the admin panel. Users can also click on the view button below the blog post to be view the full post and on that page they can also leave comments which have to be approved by the admin on the admin panel in the comments section to prevent unwanted posts. In future I would like to link this feature to user accounts

The Blog page consists of:

Navbar
Banner
Blog Posts (in card form)
Comments section (when posts have been expanded)
Social Footer

---

### Contact

The Contact page is very basic as all it contains is an image and a table containing some contact numbers and email addresses as I wanted to experiment with using a model to just display information added from the admin panel (This practice here made it possible for me to understand the concepts needed to setup my blog app with the help of the tutorials i used for that app also)

The Contact page consists of:

Navbar
Banner
Contact Details (displayed in card)
Image
Social Footer

### Profile

The User Profile page consists of 2 elements, we have a form which users can fill in their delivery information and update to make checkouts easier and faster and also the users order history is displayed in order for the user to interact with.

The Profile page consists of:

Navbar
Banner
Delivery Information Form
Order History
Social Footer

### Basket/Checkout

The Basket & Checkout pages are both quite similar showing the product information that the user is purchasing plus the calculated total cost and delivery for the products.
The checkout page also has a form for delivery information and payment but still displays the users order.

Navbar
Banner
Delivery Information Form & payment (checkout)
Order
Social Footer

### Product Management (Add Product / Edit Product)

The Product Management page takes the admin to the add product page but also this page shares the same design as the edit product page which is simply just a form where the admin can add products or edit them.

Navbar
Banner
Product Form
Social Footer

---

### Strategy Plane

Strategy Plane
The purpose of the website created is to create an easy to use Ecommerce store with an Art prints theme where users can come to the platform and easily find products and make purchases.

Also I find that Art is a hobbiest community so I decided that the website should have a blog feature which visitors can interact with to build a community around the project which I see as a key point for customer retention.

- Design an easy to use Ecommerce Store.
- Focused on Art Prints & Blog
- Mobile Responsive
- Login System

---

### Scope

#### Goals

- The website will provide a clean UX / UI for users to use effectively.
- The website will have full login functionality for users to create accounts to make purchases but also be able to without an account.
- The website will provide users the ability to interact with the store to make purchases.
- the website will provide users the ability to interact with the blog to build community.
- The website will be an easy to use website focused on simplicity rather than more complicated design.
- All forms that require the input of user data must be validated for efficiency and professionalism.
- Allow Admin to Create, Read, Update and Delete submitted content (CRUD).

#### Features

- Responsive website
- Login system
- Easy to use navigation
- About section for basic company info
- Profile page
- Shopping basket
- Checkout page
- Payment system
- Product search (desktop view)
- Product page
- Product details
- Blog
- Blog comments section
- Contact page
- Social footer
- Product Management

#### Future Features

- Stock and quantity system
- User accounts linked to blog comments
- Allow users to upload their own art.
- Subscription model
- Review system
- User specific blogs
- Social Login

---

### Structure

- The Website is laid out in a simple and easy to use manner to provide ease of use to any site visitors.
- Toast messages are displayed sidewide on interaction to help guide and confirm for users.

- Please see sections above for specific page struction

---

### Skeleton

Minimal Theme Navigation.
Pages - There will be a Home, Store page, Product detail page, Basket page, Checkout page, Login/Signup page, Profile page, Blog page, Post detail page (blog posts) and a Contact Page.
Admin - Admins will be able to access the admin panel to do CRUD based tasks on nearly everything on the website (ie. products, blog posts, contact links)
Users - Will have a specific profile page where they can see their previous orders, also update their delivery details on top of that users can purchase products, comment on blog posts(no login required).
Visitors(non logged in users) - Will still be able to make purchases and interact with the comment section on blog posts and have full site navigation other than profile page.

---

### Surface

#### Color Scheme



#### Font



#### Images


---

## Features

### Website Features




### Features to be Implemented in the Future



---

## Security

### Project Security



---

## Technologies

### Languages

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [Javascript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))


### Frameworks

- [jQuery](https://jquery.com/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)


### Workspace

- [VSCode](https://code.visualstudio.com/)
- [Gitpod](https://www.gitpod.io/)
- [Git](https://git-scm.com/)
- [GitHub](https://github.com/)

### External Resources

- [Google Fonts](https://fonts.google.com/) - Used to import fonts for the website.
- [W3C HTML Validator](https://validator.w3.org/) - Used to test/validate HTML code on the website.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - Used to test/validate the CSS code on the website.
- [Pexels](https://https://www.pexels.com/) - Stock image resource.
- [Tinypng](http://https://tinypng.com/) - Website used to compress my images to allow for faster loading times.
- [Font Awesome](https://fontawesome.com/) - Used to provide small icons for the website. eg. Testimonial quotes section.
- [Stack Overflow](https://stackoverflow.com/) - Resource for solving problems.
- [Responsivley App](https://responsively.app/) - Used to test responsive web apps.
- [Real Favicon Generator](https://realfavicongenerator.net/) - Used to create my favicon image and also test to see if it was working.
- [Spell Checker for Chrome](https://chrome.google.com/webstore/detail/spell-checker-for-chrome/jfpdnkkdgghlpdgldicfgnnnkhdfhocg?hl=en) - Used to spell check my **README.md** & **testing.md**.
- [W3 Schools](https://www.w3schools.com/) - Used as a general resource to help with coding.
- [Am I Responsive](http://ami.responsivedesign.is/) - Used to create mockup of responsive website for **README.md**.
- [Youtube](https://www.w3schools.com/) - Used as a general resource for help with code.
- [Balsamiq](https://balsamiq.com/wireframes/) - Used to create wireframes.
- [Markdown Cheat Sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) - Used to create my **README.md** & **Testing.md** files.
- [Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/) - Used throughout the website for help with all Flask Framework issues.
- [WTForms](https://wtforms.readthedocs.io/en/2.3.x/) - Used to help setup my forms for the website.
- [Code Institute](https://codeinstitute.net/) - Main source of coding knowledge and project was heavily based of their course material.
- Code institute Slack Community - Used for inspiration for my website.

### Dependencies



---

## Testing

Testing has is logged in its own document [HERE]() - testing placeholder

---

## Project Barriers



### Known Bugs



---

## Deployment



### Prerequisites



### Cloning from GitHub

- Head over to the repository location here(insert link later)
- Click the 'code' button and download the zip file from the repository or alternatively you can clone the repository by using the following url in your terminal with the commands:

``` git clone "project link" ```

### IDE

- Open the application in your IDE.
- In your IDE terminal with the Application folder open type
``` python -m pip -r requirements.txt ```
- This will install the required modules for the application




### Heroku

- First ensure a "Procfile" is created and your requirements.txt is up to date, do this by using the following commands:
``` pip3 freeze --local > requirements.txt ```
``` echo web: python app.py > Procfile ```
- Next login to your Heroku account and create a new app.
- Make sure you have a GitHub Repository for this project.
- You can then add Heroku to your GitHub Repository by heading to your settings then pasting the URL in your terminal for example:

``` git remote add heroku https://git.heroku.com/your-heroku-git-url-here ```

- You can then push to heroku with the following command in your terminal:

``` git push heroku master ```

- Once you are ready to prepare the application for deployment and launch use the command:


---

## Credits

-

### Media

- The only image for this project were taken from [Pexels](https://https://www.pexels.com/)

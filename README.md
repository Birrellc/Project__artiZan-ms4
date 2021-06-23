# ArtiZan

---

## Description

![PICTURE](https://github.com/Birrellc/artiZan-ms4/tree/master/media/artizan-readme.jpg)

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

*soon after starting this project I could make huge improvements to the initial design plan and immediately decided to change up the process.*

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



---



---



---



---



---

### Strategy Plane



---

### Scope



---

### Structure



---

### Skeleton



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

# Testing

This project has been tested throughout with the use of preview, DevTools, manual testing which allowed me to test every feature as I implemented them, at the end of the process i completed all the tests on my live deployment on Heroku App.

---

## Table of Contents

- [Validation Testing](#Validation-Testing)
- [Responsive Testing](#Responsive-Testing)
- [Lighthouse](#lighthouse)
- [Manual Testing](#Manual-Testing)

---

## Validation Testing

Validation testing for HTML, CSS, JS & Python:

### HTML

- For HTML testing I ran my code through [W3C HTML Validator](https://validator.w3.org) by URI validation using my [Deployed Live Site](https://artizan-prints.herokuapp.com/).
- On first try I received multiple formatting errors for my nav pages but nothing else in which i have placed list elements without and unordered list.
- I rectified the errors and now when I paste the Website URL in the formatter I receive no errors as displayed below.

![HTML VALIDATION TEST](/media/readme-images/html-validation.png)

---

### CSS

- For CSS testing I first put my **base.css** code through [Auto Prefixer CSS](https://autoprefixer.github.io) to make sure my CSS has all the correct vendor prefixes.
- The commit showing these changes being implemented can be found [Here](https://github.com/Birrellc/artiZan-ms4/commit/4236c4dde0ddee1c57d516f0a3dadc12c40869fc)
- I then proceeded to run my code through [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) and received no errors as shown in the image below.
- I also then applied a red border to all my elements to check for any overflow issues & there are none.

![CSS VALIDATION TEST](/media/readme-images/css-validation.png)

---

### JavaScript

- Alot of the JavaScript for this project came from either [Stripe](https://jshint.com/) or the [Codeinstitute Final Project](https://codeinstitute.net)
- For JavaScript validation I ran my code through [JsHint](https://jshint.com/) and received no errors as show in the image below.

![JS VALIDATION TEST](/media/readme-images/js-validation.png)

---

### Python

- For Python testing I ran my code through [Pep8 Online](http://pep8online.com/).
- I ran all my python files through this validator and came up with no serious code breaking errors only the occasional line length and no new line issues
- I have chosen not to display images for this test due to the number of files tested.

---

## Responsive Testing

Full list of tested resolutions with [DevTools](https://developer.chrome.com/docs/devtools/) & [Responsivley App](https://responsively.app/):

1. iPhone 5/5se 320px
2. iPhone X 375px
3. Pixel 2 411px
4. iPhone 6/7/8 Plus 414px
5. Ipad 768px
6. Nexus 10 800px
7. Generic Laptop 1280px
8. MacBook Air 1440px
9. Desktop 1920px

---

## Lighthouse

I ran a desktop and mobile test with google chromes build in lighthouse tool and received the following results:

### Desktop

![Desktop Lighthouse](/media/readme-images/lighthouse-desktop.png)

### Mobile

![Desktop Lighthouse](/media/readme-images/lighthouse-mobile.png)

---

## Manual Testing

### Home

| Functionality               | Expected Outcome                    | Pass/Fail |
| ----------------------------|-------------------------------------|-----------|
| Clicking `view store` button| Expect to be taken to the store page| Pass      |
| Carousel                    | Expect images to auto play          | Pass      |


### Navigation

#### Main Nav Menu

| Functionality                                  | Expected Outcome                                                  | Pass/Fail |
| -----------------------------------------------|-------------------------------------------------------------------|-----------|
| Clicking on `home` link                        | Redirects to the "Index" page                                     | Pass      |
| Clicking on `store` link                       | Redirects to the Store Page                                       | Pass      |
| Clicking on `blog` link                        | Redirects to the Blog page                                        | Pass      |
| Clicking on `contact` link                     | Redirects to the Contact page                                     | Pass      |
| Clicking on `profile` link                     | Redirects to the Profile page                                     | Pass      |
| Clicking on `log Out` link                     | Logs out user                                                     | Pass      |
| Clicking on `register` link                    | Redirects to the Register page                                    | Pass      |
| Clicking on `login` link                       | Redirects to the Register page                                    | Pass      |  
| Clicking on `dashboard` link as Admin          | Redirects to the dashboard page when logged in as admin           | Pass      |
| Clicking on `product management` link as Admin | Redirects to the product management page when logged in as admin  | Pass      |

#### Sub Nav Menu

| Functionality                                  | Expected Outcome                                                  | Pass/Fail |
| -----------------------------------------------|-------------------------------------------------------------------|-----------|
| Clicking on `home` link                        | Redirects to the "Index" page                                     | Pass      |
| Clicking on `store` link                       | Redirects to the Store Page                                       | Pass      |
| Clicking on `blog` link                        | Redirects to the Blog page                                        | Pass      |
| Clicking on `contact` link                     | Redirects to the Contact page                                     | Pass      |

#### Footer

| Functionality                                  | Expected Outcome                                                  | Pass/Fail |
| -----------------------------------------------|-------------------------------------------------------------------|-----------|
| Clicking on `Twitter` icon                     | Opens Twitter website in new tab                                  | Pass      |
| Clicking on `Instagram` icon                   | Opens Instagram website in new tab                                | Pass      |
| Clicking on `Pinterest` icon                   | Opens Pinterest website in new tab                                | Pass      |
| Clicking on `GitHub` icon                      | Opens my Github in a new tab                                      | Pass      |
| Clicking on `LinkedIn` icon                    | Opens my LinkedIn in a new tab                                    | Pass      |
| Clicking on `Paper Airplane` icon              | Opens my Portfolio in a new tab                                   | Pass      |

### Store

| Functionality                                                         | Expected Outcome                                                  | Pass/Fail |
| ----------------------------------------------------------------------|-------------------------------------------------------------------|-----------|
| Clicking `Sort` shows all sort options                                | Shows options to sort by                                          | Pass      |      
| Clicking `Sort` options work correctly                                | Each sort filter sorts the products the correct way               | Pass      |
| Clicking `Category` shows all category options                        | Show list of categories to view                                   | Pass      |
| Clicking `Category` options working correctly                         | Being able to filter by each category by clicking on them         | Pass      |
| Clicking `Product image` to open product specific page                | Displaying the correct product on a new detailed page             | Pass      |
| Clicking `view` button to open product specific page                  | Displaying the correct product on a new detailed page             | Pass      |
| Clicking green `edit` icon to edit product (logged in as admin)       | Redirects to the edit product page for that specific product      | Pass      |
| Clicking red `delete` icon to delete the product (logged in as admin) | Displaying the correct product on a new detailed page             | Pass      |

### Product Detail Page (specific product page)

| Functionality                                                         | Expected Outcome                                                  | Pass/Fail |
| ----------------------------------------------------------------------|-------------------------------------------------------------------|-----------|
| Clicking on `keep shopping` button                                    | Takes the user back to the overall store page                     | Pass      |
| Clicking on `add to basket` button                                    | Adds the product to the users basket                              | Pass      |
| Clicking green `edit` icon to edit product (logged in as admin)       | Redirects to the edit product page for that specific product      | Pass      |
| Clicking red `delete` icon to delete the product (logged in as admin) | Displaying the correct product on a new detailed page             | Pass      |

## Blog

| Functionality                                                         | Expected Outcome                                                  | Pass/Fail |
| ----------------------------------------------------------------------|-------------------------------------------------------------------|-----------|
| Clicking on `Read more` button                                        | Opens a new page with the full blog post and comment section      | Pass      |

## Post Detail (Blog post page)

| Functionality                                                         | Expected Outcome                                                  | Pass/Fail |
| ----------------------------------------------------------------------|-------------------------------------------------------------------|-----------|
| Clicking on `back` button                                             | Redirects to the main blog page                                   | Pass      |
| Filling out `comments` form                                           | creates a comment on the specific blog(admin has to approve post) | Pass      |

## Contact

**NO NEED TO TEST CONTACT PAGE NO USER INTERACTIVITY APART FROM ADMIN WHICH HAS BEEN TESTED BY CREATING THE CONTENT IN THE ADMIN DASHBOARD THAT IS DISPLAYED ON THE PAGE**

## Product Management (ADMIN TOOL)

### Add product

| Functionality                                                         | Expected Outcome                                                  | Pass/Fail |
| ----------------------------------------------------------------------|-------------------------------------------------------------------|-----------|
| Fill out the correct fields to add a new product                      | New product to appear in store                                    | Pass      |
| Clicking on `cancel` button                                           | Redirects to the main blog page                                   | Pass      |

## Account

### Registration

| Functionality               | Expected Outcome                                                                                                               | Pass/Fail |
| ----------------------------|--------------------------------------------------------------------------------------------------------------------------------|-----------|
| Filling form out and signup | Registers the user and redirects to verify email address. If registration form is incomplete, shows Please fill out this field | Pass      |
| Clicking on `back` button   | Redirects to the main blog page                                                                                                | Pass      |

### Login in

| Functionality                                              | Expected Outcome                                             | Pass/Fail |
| -----------------------------------------------------------|--------------------------------------------------------------|-----------|
| Clicking on `Sign In` with correct username and password   | Directs user to the home page                                | Pass      |
| Clicking on `Sign In` with Incorrect username and password | flash message to user showing incorrect username or password | Pass      |
| Clicking on `Forgot password`                              | Opens "Forgot password" page                                 | Pass      |

### Profile

| Functionality                                              | Expected Outcome                                             | Pass/Fail |
| -----------------------------------------------------------|--------------------------------------------------------------|-----------|
| Filling out form and clicking `update information`         | Updates the users delivery information                       | Pass      |
| Clicking on an order number in order history section       | Loads up the order details for that specific order           | Pass      |


## Basket

| Functionality                                                 | Expected Outcome                                                             | Pass/Fail |
| --------------------------------------------------------------|------------------------------------------------------------------------------|-----------|
| If no items in basket display `your basket is empty`          | When there are no items in the basket message is displayed                   | Pass      |
| Clicking `keep shopping` button returns to store              | When clicked returns user to the store as expected                           | Pass      |
| Error messages                                                | Incorrect payment details shows an error message                             | Pass      |
| Clicking `adjust basket` button                               | Returns user to basket as expected                                           | Pass      |
| Clicking `Complete Order` button                              | Completes payment successfully if correct payment details                    | Pass      |

## Checkout

| Functionality                                                 | Expected Outcome                                                             | Pass/Fail |
| --------------------------------------------------------------|------------------------------------------------------------------------------|-----------|
| Correct order info displayed                                  | The order from the basket to be the same                                     | Pass      |
| Users Delivery info be displayed if they updated in my profile| Previously entered data was there prefilled                                  | Pass      |
| Clicking `secure checkout` button takes user to checkout page | When clicked takes user to checkout page as expected with correct order info | Pass      |
| Clicking `delete` icon                                        | Correctly removes the product from the users basket                          | Pass      |
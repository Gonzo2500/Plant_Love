h1 align="center">Plant Parent</h1>
<h1 align="center"><img src="./readme_files/read_me_hero.PNG" /></h1>

 <a href="https://plant-love.herokuapp.com/"><img src="./media/logo.png" width="25px" /></a> :point_left: Live website

<a href="https://github.com/Gonzo2500/Plant_Love"><img src="./readme_files/github.png" width="25px" /></a> :point_left: GitHub Repository

<a href="https://github.com/Gonzo2500/Plant_Love/blob/master/README.md"> :scroll: </a>  :point_left:  README.md file
 


# Table of Contents

1. [Functionality](#functionality)

1. [Validators](#validators)
    - [HTML5](#html5)
    - [CSS](#css)
    - [JavaScript](#javascript)
    - [Python](#python)

1. [Compatibility](#compatibility)

1. [Performance](#performance)

1. [User Stories](#user-stories)

1. [Bugs](#bugs)
    - [Identified Bugs](#identified-bugs)
    - [Existing Bugs](#existing-bugs)

1. [Future Testing](#future-testing)


# Functionality
- #### Navigation bar
    - The navigation bar is positioned at the top of the screen and stays visible on the top of the screen when the site is being scrolled.
    - When hovered over and/or active, the main nav links have a pink, offset background. The icons, when hovered over have filled in the background.
    - Home page and Membership links bring the user to the relevant pages.
    - Shop link when clicked, drops down a menu with item categories that bring the user to the shop page with the selected category displayed and items filtered.
    - Search button activates a dropdown with the search bar. This is fully active from all pages and returns items containing the searched word in the title or description.
    - Cart icon brings the user to the cart page.
    - When the user icon is clicked on, it opens up a dropdown menu displaying different options depending on whether the user is logged in or not. For logged-in users, 'Order History', 'My Membership', 'My Details', and 'Log Out' are displayed. Non authorized users to see 'Register'and 'Log In'.
    - When each link in the user dropdown is clicked, the user is navigated to the appropriate page.
    - On mobile and tablet views, the navbar collapses and a hamburger menu button is displayed instead.
    - When clicked, the hamburger menu reveals main menu items and the search bar that are all functional, when 'x' is clicked, the menu links are collapsed back in the navbar.
    - Hamburger menu icon is animated and works as expected.
    - The logo is a clickable link, when clicked on it brings the user to the home page.

- #### Footer
    - Footer is visible on all pages apart from membership checkout which is purposeful to prevent users from clicking out of the checkout.
    - Footer is always positioned at the bottom of the site, even when there isn't a full page of content, the footer stays at the bottom of the page.
    - When social links are clicked in the footer, a new tab opens and the relevant social page is displayed.
    - When hovered over, social buttons have filled in the background to help the user identify which link will be clicked on.

- #### Search bar
    - Search bar is collapsed/hidden by default to take up less space on the page.
    - When the search icon is clicked on desktop sizes, the search bar is revealed with seamless, smooth animation.
    - In mobile sizes, the search bar is incorporated in the collapsable menu and is shown when the hamburger menu button is clicked and the menu itself is revealed.
    - When the input is focused on, the form has a pink, sharp box-shadow to indicate that the user has clicked/tapped on it.
    - When an empty form is submitted, an error message is displayed to let the user know that a value is needed.
    - When a value is entered and 'Search' is clicked, the user is navigated to the 'Products' page (aka Shop) with matched results displayed.
    - If no results are found that match the search, a message is displayed on the screen to let the user know.

- #### Registration
    - When a user clicks on the 'Register' button from the main navbar or 'Sign Up' button in various alluth pages (such as 'Sign In'), the user is directed to the 'Memberships' page.
    - User can also navigate to the 'Memberships' page from the main navbar.
    - On the 'Memberships' page, the user has to select one of the membership types, one of them being free, after which the user is directed to the allauth 'Sign Up' form.
    - In the form, all fields are required, if any are left out, the allauth displays a validation message.
    - Allauth will also display a validation error if e-mails do not match, the username is shorter than 4 characters, passwords don't match, or if the password is not up to standards (too short, too similar to the username or e-mail, too easy/common).
    - When 'Sign Up' is clicked with a valid form, a message is displayed to let the user know that they have to validate their e-mail address.
    - User receives an e-mail from Plant Parent with a link that brings the user to the 'Confirm E-mail Address'. When 'confirm" is clicked on this page, the user is re-directed to the 'Sign In' page.
    - After a successful sign-in, the user is re-directed to the 'Membership Checkout' page where they have to confirm their selected membership or change it to a different one. If the user has chosen a paid membership plan, they will be navigated to a payment form.
    - When the user registers, their profile is created automatically.
    - From the 'Register' page, the user can access the 'Login' page using the link at the bottom which is functional.

- #### Sign Out / Log in
    - Sign in form allows users to sign in using their existing Plant Parent account or Google account.
    - For Plant Parent sign-in, the validation form will display a validation message if either password or username/e-mail are left blank.
    - Form will display a validation error if  username/e-mail and/or password were incorrect so malicious users don't know specifically which field was incorrect.
    - When the 'Forgot Password' link is clicked, the user is navigated to a page where they are prompted to enter their e-mail address. They will then receive an e-mail with a link to reset the password. When the link is clicked, the user is navigated to the page and prompted to enter the new password twice. If this is successful, the user is navigated to a success page.
    - When the 'Sign Up' link is clicked on the 'Login' page, the user is brought to the Register page.
    - When valid credentials are entered on the Log In page, the user is logged in and redirected to either the 'Membership Checkout' page if they just signed up, or their profile page if they didn't select a membership beforehand.
    - Log Out page has one button, which when clicked, removes the user's session and logs the user out. The user is then re-directed to the Home page.

- #### Home Page
    - Home page scrolls nicely and is responsive on all screen sizes.
    - All buttons are working and bring the user to the relevant page. Join and Memberships buttons bring the user to the 'Memberships' page where they can select the membership and register for the site.
    - Shop button brings the user to the shop so they can buy products.
    - Instagram account handle brings the user to the Instagram website (it's one of the future features to have an Instagram account and all pictures connected to it).

- #### Shop Page
    - When the Shop link in the navbar is clicked, a dropdown offers the user to select a category or view all items in the shop. Either option brings the user to the same Products page with items filtered to the selected category.
    - There are 4 category buttons on the top of the page that have a hover effect and also are styled differently when the category has been chosen.
    These work just like dropdown buttons in the navbar, however, the user doesn't have to go through the navbar.
    - When a category button is clicked, items are filtered to the selected category.
    - There is a filter/sort button just above the products, when this is clicked, it expands to reveal sorting buttons that sort selected items by added date, price, or alphabetically/reverse. If the filter button is clicked again, the sorting buttons disappear.
    - All of the sorting buttons have a hover effect to let the user easily identify which button will be clicked.
    - All products are laid out in a grid and a responsive design, resizing to have 4 items per row on extra-large screens, 3 on medium, 2 on small, and 1 on mobile view.
    - Each product have their Image, title, rating, price and 'Buy Now' button visible.
    - When the 'Buy Now' button is clicked, the item is automatically added to the cart.
    - When Item's image is clicked, the user is navigated to the individual item's page.

- #### Product Detail Page
    - Back button at the top of the page brings the user back to the previous page they were on.
    - Product Detail Page displays product image, title, description, quantity selector, price, 'put in the cart' button, and Reviews section at the bottom of the page.
    - When the user clicks +/- buttons for quantity, the quantity increases or decreases, and the price updates to reflect that.
    - the - button and + button are disabled (function and style) if the user has entered 1 or 10 to indicate that they cannot add more/less.
    - Typing has been disabled to prevent as much as possible for the user to 'accidentally' select more or less than the allowed quantity.
    - Arrow buttons are still available but allow the user to only enter 1-10 by using form validation.
    - If the user overrides the front-end validation (deleting HTML max and min attributes in Google Develop Tools for example) and enters a value that's >10 or <0, an error message is displayed and quantity not added.
    - When the user has selected a valid quantity and the 'Add to cart' button is clicked, an item is added to the cart and a cart notification is displayed with all items in the cart and the page is refreshed.
    - Reviews section shows all reviews (if any), the overall average product rating, and a Review button.
    - Review button is only displayed to logged-in users. This was tested by looking at pages while logged in and also when not.
    - When the Review button is clicked, a modal is opened as an overlay on the page with a review form. All fields are required and the form will not submit otherwise.
    - When 'x' or 'cancel' are clicked, the module is closed without saving.
    - When the form is filled out and the user clicks 'Add', the review is saved to the database, modal is closed and a success notification tells the user that the review was successfully added.
    - Overall rating is updated to include the new rating, and the review is displayed automatically.
    - User can only add 1 review per item
    - User can see 'edit' and 'delete' buttons under their reviews.
    - When the 'Edit' button is clicked, the modal opens with review's details prefilled. When 'x' and 'cancel' are clicked, the modal closes, and the review is not updated. If 'Edit' is clicked, the review is updated, modal closed, and a message is displayed to let the user know.
    - If the 'delete' button is clicked, a modal appears asking the user to confirm if they want to delete the review. If 'x' or cancel are clicked, the modal is closed and the review is not deleted. If 'delete' is clicked, the review is deleted and a message is displayed confirming it to the user.


- #### Memberships Page
    - This page should be displayed slightly differently depending on if the user is logged in or not.
    - For a non-authorized user it displays all three memberships with benefits, images, titles, price, and 'Prick Me' buttons.
    - Authorized user sees the same, however, the membership that they have subscribed to has a border around it and the 'Prick Me' button says 'Subscribed' and is disabled. Other buttons now say 'Change'.
    - If a user is authorized but they skipped the subscription or it's their first time signing in (just after registration), they will be re-directed to this page after each sign-in and a message will display that the user does not have a membership plan yet and they will be allowed to select a membership using 'Prick Me' buttons.
    - When a user without a membership subscription selects a membership using the 'Prick Me' button, they are re-directed to the Membership Checkout page.
    - User will see their selected membership with benefits and can change the membership by selecting a different one under the 'Change' dropdown and clicking 'Update. When the user clicks 'Update' the page will refresh and selected members will be updated.
    - Under 'Payment' user sees the total and a message stating that the amount will be taken out monthly.
    - When 'Confirm' is clicked, the user is navigated to a checkout form hosted by Stripe with payment details to be added.
    - Each field in this form is mandatory and validation is handled by Stripe.
    - If a valid form is entered, by using a webhook user's details are added to the Stripe system, added in the database as StripeCustomer, and new membership is added to the user's profile.
    - User is then re-directed to their profile page which displays the membership summary and amount.
    - If the webhook fails and the user's details are not added to the systems, the user will be re-directed to the membership page next time they sign in.
    - When a user with existing membership clicks on the 'Change' button, they are redirected to the Membership Change page which uses the same template as Memebrership Checkout, however, they see their current as well as selected membership details displayed for comparison. Additionally, they cannot update their selected membership and they can cancel the change if they changed their mind.
    - When Cancel is clicked on, the user is re-directed to the products page.
    - When Confirm is clicked, the user's membership is updated and they are re-directed to their profile where they can see their new membership summary, and a message is displayed to confirm the change.
    - Membership checkout and membership change pages do not display header and footer to prevent the user from clicking out without completing the subscription and not having a membership attached to their profile. This is handled in the back end but will be more of annoyance as the next time when user logs in they will be re-directed to the Memberships page. Users changing their membership can cancel it as they already have a membership associated with their account.

- #### Shopping Cart Page and toast
    - When the user clicks 'Buy Now' or 'Add to the cart' from the products detail view, the item is added to the cart and cart toast is displayed and a little badge with item count is added to the cart icon in the navbar.
    - In cart toast, the user sees item image, price, quantity, and total.
    - If the user changes the quantity in the cart toast, the page refreshes, and the cart, as well as cart toast, are updated.
    - When 'Don't want this' is clicked, the page is refreshed and the item is removed from the cart and new cart toast is shown. If this was the last item, a message is displayed letting the user know that the cart is empty.
    - From cart toast, if the user clicks on 'View Cart', they are navigated to the Shopping Cart page.
    - From the cart toast, when 'Checkout' is clicked, the user is navigated to the checkout page.
    - When 'x' is clicked in the cart toast, the toast is closed, otherwise, it stays open for 90000 ms but not forever.
    - User can navigate to the cart page from the navbar, cart toast, or checkout page.
    - On the page, the user sees a summary of their order, with items, their price, image, quantity, and total displayed. They also see the subtotal and a note that this amount excludes the delivery charges. The user does see a discount, if any, that is applied.
    - When 'More Shopping' is clicked, the user is navigated to the shop page.
    - When 'Checkout' is clicked, the user is navigated to the checkout page to proceed with the payment.
    - when +/- buttons are clicked, quantity is updated and the page refreshed, this logic is the same as on the product detail page however loops through all the items and each is functioning as expected.
    - When 'I don't want this' is clicked, the item is removed from the cart.
    - If the last item is removed, the user will see an 'empty cart' text and a button redirecting them to the shop page.

- #### Checkout Page
    - On the checkout page, the user sees Delivery, Shipping, and Payment Info forms and order summary.
    - Only the Delivery form is active, making the user select the payment method.
    - When the delivery method is selected and 'Apply' is clicked, Delivery Info becomes disabled displaying selected value, the delivery charge is updated and the rest of the form becomes available.
    - Apply button now says 'Change', when clicked, the form is cleared and the user can change the delivery type.
    - If a user tries to 'Apply' delivery type without selecting a value, the form validation will return a validation message.
    - Discount and delivery are calculated based on the membership, if any, and whether this is the user's first order ever.
    - All fields are required apart from the 'Region/State', if they are not filled out, validation will prompt the user to fill it in.
    - If a user submits the form with an invalid phone number, and an error message will let them know that the form and phone number are invalid.
    - If the user enters invalid card details, Stripe will return an error with an error message displayed.
    - When a valid form has been filled out, and the user clicks on 'Make Payment' they see a loading page and then are re-directed to the Checkout Success page where they can see their order details, with a customer, and shipment details added.
    - When the user clicks on the 'Back to the Shop' button, they are re-directed to the shop page.
    - If the user decides to add more products before the payment button is clicked but after the delivery type is selected, the delivery type will remain selected for when the user returns to the checkout page and they only have to enter their delivery and payment information.
    - If the user is logged in, they are offered an option to save their shipping details to their profile.
    - If the user is not logged in, they can log in or sign up using the links under the Delivery Form

- #### Profile Page
    - When user signs in, they are re-directed to the Profile page, user can also access it via the 'My details' link in the user dropdown in the navbar.
    - User sees the Membership summary at the top with the name and the monthly price. 
    - When a user clicks on 'More' under membership summary, they are navigated to the user membership page where they can see more details.
    - In the profile user also sees their profile details that user can edit/add and click save to amend them in the database.
    - If the user adds an item to the cart and goes to checkout now, they will see their saved details prefilled in the form after selecting the delivery type.

- #### User Memebrship Page
    - Logged in user only can navigate to this page from the navbar by clicking on the 'My Membership' link or their profile page.
    - User sees their selected membership details and benefits and the 'Change' button at the bottom.
    - When the change button is clicked, the user is redirected to the Membership page which displays all memberships for a user with a membership already active. This page was tested and described under the 'Membership Page' section.

- #### Order History
    - Logged in user only can navigate to this site by clicking on the 'Order History' link in the navbar.
    - User will see all of their orders in a collapsed accordion with the latest order on top revealed.
    - In a collapsed view, the user can see order number, total, and order date.
    - When a user clicks on an order, it expands to reveal items ordered and an 'Order Details' button.
    - Each item has its image, name, total, and quantity displayed, and 'Review' and 'Buy again' buttons are displayed under the item.
    - When the 'Review' button is clicked, the user is navigated to the item's detail page, review section where they can add an order.
    - When the 'Buy Again' button is clicked, the user is redirected to the item's detail page, top section, where they can purchase the item again.
    - When a user clicks on another order, the previous one collapses and the next one expands.
    - Expanded order summary top details will change background and text color to signify to the user which order is expanded.
    - When the 'Order Details' button is clicked, the user is navigated to the Order Details page where they can see the detailed view of the order which uses the same template as the checkout success page.
    - User sees the Order date on top, as well as delivery and dispatch dates. If the order has not been dispatched or delivered yet, they will see estimated dispatch or/and estimated delivery dates.
    - There is a back button at the top of the page under the header, this button takes the user back to the Order History page.



# Validators

## [HTML5](https://validator.w3.org/)
- :white_check_mark: Home - [Pass](https://validator.w3.org/nu/?doc=https%3A%2F%2Fplant-love.herokuapp.com%2F)
- :white_check_mark: Shop - [Pass](https://validator.w3.org/nu/?doc=https%3A%2F%2Fplant-love.herokuapp.com%2Fproducts%2F)
    - 1 warning advising for me to remove type attribute from script tag. This is a script tag inserted by AWS and cannot be removed.
- :white_check_mark: Memberships - [Pass](https://validator.w3.org/nu/?doc=https%3A%2F%2Fplant-love.herokuapp.com%2Fmemberships%2F)
- :white_check_mark: Membership Checkout - [Pass](https://validator.w3.org/nu/?doc=https%3A%2F%2Fplant-love.herokuapp.com%2Fmemberships%2Fmembership_checkout%2F)
- :white_check_mark: Memebrship Change - [Pass](https://validator.w3.org/nu/?doc=https%3A%2F%2Fplant-love.herokuapp.com%2Fmemberships%2Fmembership_change%2F)
- :white_check_mark: Cart - [Pass](https://validator.w3.org/nu/?doc=https%3A%2F%2Fplant-love.herokuapp.com%2Fcart%2F)
- :white_check_mark: Delivery - [Pass](https://validator.w3.org/nu/?doc=https%3A%2F%2Fplant-love.herokuapp.com%2Fcheckout%2Fdelivery%2F)
- :white_check_mark: Checkout - [Pass](https://validator.w3.org/nu/?doc=https%3A%2F%2Fplant-love.herokuapp.com%2Fcheckout%2F)
- :white_check_mark: Checkout Success - [Pass](https://validator.w3.org/nu/?doc=https%3A%2F%2Fplant-love.herokuapp.com%2Fcheckout%2F1E48B745-4C21-4E78-A939-E4CDA071196A%2Fcheckout_success%2F)
- :white_check_mark: Profile - [Pass](https://validator.w3.org/nu/?doc=https%3A%2F%2Fplant-love.herokuapp.com%2Fprofile%2F)
- :white_check_mark: User Membership Detail - [Pass](https://validator.w3.org/nu/?doc=https%3A%2F%2Fplant-love.herokuapp.com%2Fmemberships%2Fuser_membership%2F)
- :white_check_mark: Order History - [Pass](https://validator.w3.org/nu/?doc=https%3A%2F%2Fplant-love.herokuapp.com%2Fprofile%2Forders%2F)
- :white_check_mark: Order Details - [Pass](https://validator.w3.org/nu/?doc=https%3A%2F%2Fplant-love.herokuapp.com%2Fprofile%2Forders%2F4)
- :white_check_mark: Log In - [Pass](https://validator.w3.org/nu/?doc=https%3A%2F%2Fplant-love.herokuapp.com%2Faccounts%2Flogin%2F)
- :white_check_mark: Register - [Pass](https://validator.w3.org/nu/?doc=https%3A%2F%2Fplant-love.herokuapp.com%2Faccounts%2Fsignup%2F)



## [CSS3](https://jigsaw.w3.org/css-validator/)
- :white_check_mark:base.css - Pass
- :white_check_mark:home.css - Pass
- :white_check_mark:checkout.css - Pass
- :white_check_mark:membership_checkout.css - Pass
- :white_check_mark:shop.css - Pass
- :white_check_mark:orders.css - Pass
- **Note** - When validating [base.css](https://github.com/Gonzo2500/Plant_Love/blob/master/static/css/base.css) and [home.css](https://github.com/Gonzo2500/Plant_Love/blob/master/home/static/home/css/home.css), validator returned errors associated with not recognizing variables in linear gradient. If variables were overwritten by regular color names, the validator passes. This has also been echoed in this [Stack Overflow Post](https://stackoverflow.com/questions/57661659/w3c-css-validation-parse-error-on-variables) Additionally validator displays warnings as it does not recognizes imports adn prefixes. 

    <img src="./readme_files/css-valid.png" height="200px" />

## [JSHint](https://jshint.com/)
- :white_check_mark:base.js - Pass
- :white_check_mark:stripe.js - Pass
- :white_check_mark:stripe_sub.js - Pass
- :white_check_mark:product_item.js - Pass
- :white_check_mark:shop.js - Pass
- :white_check_mark:cart.js - Pass
- **Note** - All files passed, only feedback was regarding ES6 (let, const, =>, string literals etc), and use of built in variables such as `Stripe` and `$`.
Examples of these are shown in the images below.

## [PEP8](http://pep8online.com/)
- :white_check_mark:all - Pass
- I used [flake8](https://flake8.pycqa.org/en/latest/) installed on my VSCode IDE as a validator throughout the project.
- Additionally, I also added all python files written by me in the [PEP8](http://pep8online.com/) validator online to ensure all files fit the standard.
- **Note** - Few files that came built-in Django did not meet PEP8 requirements (such as [settings.py](https://github.com/Gonzo2500/Plant_Love/blob/master/plant_parent/settings.py)). However, these were not written by myself and the formatting was left as is.


# Usability
- To test the ease of navigation, this website was shared with friends and family of different ages and different levels of computer/smart device knowledge. There were no issues identified regarding the simplicity of navigating the website.
- The testers also verified that all functionality aspects are working as explained above and as expected.
- Testers expressed that the design is easy to understand and navigate.
- To further expand on user testing,  multiple 'dummy' accounts were created to test the registration, log-in, membership subscription, CRUD functionality with reviews and purchasing items. These accounts were created with different memberships to verify that discounts and delivery charges work as well.

# Compatibility
- Browser Compatibility

    | Screen size\Browser | Safari           | Opera            | Microsoft Edge   | Chrome           | Firefox          | Internet Explorer |
    | --------------------|:----------------:|:----------------:|:----------------:|:----------------:|:----------------:|:-----------------:|
    | Mobile              |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:| Not Tested        |
    | Tablet              |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:| Not Tested        |
    | Laptop              |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:| Not Tested        |
    | Desktop             |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:| Not Tested        |


- The devices used in this testing include windows desktop with a 27" screen, Macbook Pro, lenovo laptop, iPad Pro, iPhone 9,  HTC U Ultra, iPhone 8, and other android mobile phones.

- The website was exhaustively tested for responsiveness on Chrome DevTools and Responsive Web Design Checker all screen sizes provided. Different viewport sizes were simulated ranging from as small as Galaxy Fold (280px) to large desktop sizes (1200px and above).

# Performance Testing



# User Stories
- #### Common user stories
    1. I want to easily navigate the site so that I can find what I'm looking for quickly.
        - Navbar is always located at the top of the page so that the user can easily navigate to the pages they are looking for.
        - Most popular call-to-action buttons are displayed on the home page so that users can find the membership and shop pages quickly.
    1. I want to be able to contact the company if I'm experiencing an issue.
        - Social links are located in the footer allowing the user to contact the company in three different ways
    1. I want the website to be readable on all screen sizes.
        - The website is responsive and tested on all screen sizes allowing the user to have an equally good experience on mobile as well as desktop devices.
        - Navbar collapses on screen sizes medium and down, this prevents overcrowding of links on smaller screen sizes.
        - rem instead of px was used as much as possible to aid with responsiveness.

    
- #### As a first-time visitor I want to
    1. Easily understand the purpose of the site so that I can decide whether I want to invest my time into it.
        - When the user opens the site, the first thing they see is an image of cactus and a call to action to join the membership.
        - In the navbar, links are named 'Shop' and 'Memberships' thus indicating to the user that this is an e-commerce site with a membership system.
    1. Understand the benefits of becoming a member/registering for the site so that I can decide if I want to.
        - On the landing page, it is clearly stated that discounts will be applied as soon as the user subscribes to a membership.
        - It is stated that memberships start from free which shows the user that there is no disadvantage to sign up and get the discount.
    1. View and compare all memberships so that I can decide what membership if any, I want to subscribe to.
        - Memberships page shows the memberships and the benefits side by side thus allowing the user to compare them
        - If a registered user wishes to compare and potentially change their membership, they can do so on the Memberships page and have theirs marked.
    1. Easily find where I can register for the site so that I don't waste my time looking for it and I'm not discouraged not to sign up.
        - Landing Page has a call-to-action button 'Join' which will navigate the user to the register page
        - Navbar had Register button accessible from all pages
        - Membership page lets the user pick their membership and redirects them to the Register page
        - If the user ends up on the sign-in page, they can access the registration page by clicking on the 'Sign Up' link.
    1. Be able to quickly register and start using the site so that I can have my account and receive the benefits.
        - Register page only need the user's e-mail, username, and password
        - E-mail verification arrives instantaneously.
        - Once the user has received the e-mail they can confirm it and log in straight away and view their profile.

- #### As a casual shopper I want to
    1. Navigate to the shop page easily so that I can find what I need quickly.
        - Shop button is always located in the navbar on top and visible/accessible from all pages
        - Home page has a Shop button displayed under the 'New Items this week' section
        - If the user ends up on a 404 page or empty cart page, they will see shop buttons allowing the user to navigate to the shop page.
    1. Filter all products by category so that I can quickly have oversight of the products that I'm interested in.
        - Shop button dropdown in the navbar shows categories that the user can select and will be navigated to the shop page with the selected category filter applied.
        - Shop page has separate category buttons so that users can easily change the category that they are looking for without the need to click on Shop link in the navbar.
    1. Sort all items by date added, name or price so that I can identify new products, products that fit my budget, and find easier what I'm looking for.
        - Shop page has a filter button that expands into multiple sort buttons. 
        - User can sort items (both ascending and descending) by date added, price and name.
    1. Search for an item from anywhere on the site so that I can easily find what I'm looking for.
        - Search icon in the desktop navbar reveals the search component which is accessible from all pages. After submitting the search query, the user will be redirected to the shop page with relevant search items showing.
        - In the mobile view, the search component is located with the main navigation links and is revealed when the hamburger menu icon is clicked.
    1. Be able to see the price of the item without clicking into it so that I can easily decide if I can afford the item.
        - Prices are displayed under each item
        - User can additionally sort items by price to identify the cheapest/most expensive items to help with decision making
    1. Be able to quickly add the item without having to click on the product so that I can save time if I know that I want to purchase the item.
        - Each item has a 'Buy Now' button that adds an item to the cart
        - When a user adds an item to the cart, they can edit the quantity of the item in the cart toast without having to navigate to another page.
    1. Be able to see more details about the product so that I can make an educated decision of whether to purchase the item.
        - Each Item has an Item details page with more information, such as description and reviews on it.
    1. Select the quantity of the product so that I can choose how many products I'm purchasing and not have to add the same item multiple times.
        - User can select the quantity/remove of the product from the Item details page.
        - User can change the quantity/remove from the cart toast.
        - User can change the quantity/remove it from the cart page itself.
    1. Be able to see the rating and reviews to allow me to judge if the item is worth the price based on other feedback.
        - Rating is displayed on the shop page for each item so that the user has a quick oversight of the ratings
        - Rating is displayed on the item detail page and under the reviews section as well
    1. Leave a review so that I can provide my feedback and experience to the company and other shoppers.
        - Logged-in users can add a review from the item details page by clicking on the 'Review' button
        - Users can access the Review button of their purchased items also from their order history page
    1. Edit my review so that I can change it in case I've changed my mind or made a mistake while adding the review.
        - Under all reviews written by a user, there is an edit button displayed which allows the user to edit their review.
    1. Delete my review so that I can remove it in case my review is no longer relevant or I don't want to keep it up.
        - Under all reviews written by a user, there is a delete button displayed which allows the user to delete their review.
    1. See my shopping cart as items are added to know how the total without having to go to another page.
        - When an item is added, the shopping cart toast will display the new total and all items added to it so far.
    1. Edit the quantity of added items so that I don't have to remove and add items again.
        - User can select the quantity/remove of the product from the Item details page.
        - User can change the quantity/remove from the cart toast.
        - User can change the quantity/remove it from the cart page itself.
    1. Remove added items easily so that I can purchase only the items that I want.
        - Each item on the cart and cart toast pages has an 'I don't want this' button that removes the item from the cart.
    1. See my shopping cart before checkout so that I can make changes before purchase.
        - User will have an opportunity to visit the shopping cart page before the checkout
        - If a user navigates to the checkout before the shopping cart, they can easily navigate back as checkout has a button to bring the user to the shopping cart.
    1. See all charges included before making a payment so that I can decide if I want to proceed with the purchase.
        - After the user selects their delivery type in the checkout, all charges discounts, and the updated total is shown with the order summary.
    1. View my order as I'm checking out to be able to confirm what I'm purchasing.
        - Checkout page has an order summary on the right-hand side so the user can have oversight of the items before making a payment.
        - On the mobile screen, the order summary is collapsed but easily expandable, the total is always visible.
    1. easily add my details without too many steps so that I don't get discouraged by the lengthy checkout process.
        - There is only one checkout form after the user has selected the delivery type.
        - Delivery info form can be pre-filled if the user has an account. Another great reason to sign up.
    1. Securely add my payment information so that I feel safe giving my card details.
        - Payments are handled by Stripe, securely, they are encrypted and card details are not shared with anyone.
    1. See Order confirmation and receive confirmation e-mail so that I have proof of purchase and order number.
        - E-mail confirmation is sent to the user after their order has been successfully processed.
        - Order confirmation is displayed on the screen as well.
        - For members, orders can be viewed on the order history page.


- #### As a member I want to
    1. Log in and sign out quickly and easily so that I can access or close my account.
        - Sign In button is located in the navbar and is accessible to the user from all pages.
        - Sign In link is displayed on the Register page so that User can easily navigate to it
        - Checkout page further displays the Sign In link if the user isn't signed in.
    1. See my personal account information so that I can manage my details.
        - After signing in, if the user has a membership, they are navigated to the profile page.
        - User can access the profile page from the navbar too.
    1. See my membership site so that I can verify my benefits and the price of the membership.
        - Users can view their membership on the 'My membership' site where user can see their benefits and cost.
        - Users can see the summary of their membership on the profile page.
        - Users can see their membership plan highlighted on the Memberships page.
    1. Change the membership easily so that I can control what benefits and expenses I'm having.
        - User can navigate to the Membership change page from the 'Memberships' page when membership is selected.
        - Membership is easily changed just by clicking confirm
    1. Cancel paid membership so that I don't have to pay for it.
        - User can always change their membership to the Basic plan which is for free and will cancel the paid membership
    1. See my order history so that I can have the confirmation and details for all of them in one place and manage them easily.
        - Logged in user can access their Order history page from the navbar
        - User can see all the details associated with the order once they click 'Details' under any given order summary
    1. Can see the estimated date of delivery so that I can arrange to receive the package.
        - User can see their estimated delivery date on the Delivery DEtails page
    1. Recieve benefits as a member so that I get my money's worth.
        - All memberships receive some benefits
        - All paid memberships receive a first and overall discount on prices
        - All memberships receive a quarterly gift

- #### As an admin I want to
    1. Be able to add an item so that I can update the products on the site.
        - Admin can access admin site from which they can add items, membership plans, delivery types.
    1. Be able to edit and remove items so that I can customize items on the site and offer new deals to customers depending on the demand and new trends.
        - ADmin can edit the item from the admin page.
    1. Add and edit new memberships so that I can customize the price and benefits depending on the popularity of the membership.
        - This can be achieved from the admin page
    1. Add and edit new delivery types to accommodate shipping to more countries.
        - This can be achieved from the admin page
    1. Have oversight of the user data so that if anyone is experiencing an issue I can investigate and resolve the issue.
        - This can be achieved from the admin page


# Bugs
 :beetle:
1. ## Identified bugs
- Stripe payment button not being re-enabled after making a payment that requires authorization.
    - The idea is that while after the user clicks to make a payment, the submit button is disabled so that the user cannot submit multiple payments of the same order.
        Once the payment is completed the submit button is re-enabled for future payments or to fix the form. The reason why re-enablement wasn't working is that JS code was setting `disable=False` to re-enable the button which didn't work. Instead, I amended the code to remove the `disable` attribute altogether and add it if need disabling.
- Integration Error please Call Stripe with public key
    - stripe public key was called after user selected dilvery type and so it threw a console error fixed with that statement {% if 'delivery' not in request.get_full_path %}

2. ## Existing Bugs
- Back button on the Item Details page only brings the user back one page
    - This functionality uses code to send user back exactly one step by using `onclick="history.back(-1)"`. This works fine if the user only wants to go back to the previous page, however on the product details page, the user will most likely want to add a product or a review which will cause the page to be refreshed and the previous link to be the same as current. I implemented an improvement by checking in JS if the current URL is the same as the previous, if yes, then bring the user back 2 pages. Which will cover a large proportion of user cases. However if a user adds an item and then decides to add another item, this will again bring them back to the same page. This will be fixed in future versions.

- Google Authorization not creating a profile
    - I had Google authorization set up and it lets the user select their account after which an error occurs `RelatedObjectDoesNotExist Exception Value: User has no profile.`. I didn't get a chance to implement the fix but I found an [article on stock overflow](https://stackoverflow.com/questions/49784358/django-2-0-django-allauth-relatedobjectdoesnotexist-at-account-edit-user-h) that discussed a potential fix by adding a post save signal and creating a profile through that. This will be implemented in future versions.

- Website not loading on iamresponsive and sites similar to it.
    - The reason why I used a mockup image and not an image from iamresponsive is that I got an x-frame error and the site would not load.



# Future Testing
- Future testing will include automated tests such as Jasmine for JS and built-in Django automated testing for Python and implement Travis CI.
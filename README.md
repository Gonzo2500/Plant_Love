
<h1 align="center">Plant Parent</h1>
<h1 align="center"><img src="./readme_files/read_me_hero.PNG" /></h1>

 <a href="https://plant-love.herokuapp.com/"><img src="./media/logo.png" width="25px" /></a> :point_left: Live website

  <a href="https://github.com/Gonzo2500/Plant_Love"><img src="./readme_files/github.png" width="25px" /></a> :point_left: GitHub Repository
 
 # About

An e-commerce store where you can buy new everything your plant family needs

# Table of Contents

1. [User Experience (UX)](#user-experience)
    1. [Strategy Plane](#strategy-plane)
        1. [Business Goals](#business-goals)
        1. [User Stories](#user-stories)
    1. [Scope Plane](#scope-plane)
    1. [Structure Plane](#structure-plane)
    1. [Skeleton Plane](#skeleton-plane)
        - [Wireframes](#wireframes)

    1. [Surface Plane](#surface-plane)
        - [Color sheme](#color-scheme)
        - [Typography](#typography)
        - [Imagery](#imagery)
        - [Animations](#aniamations)
        - [Transitions](#transitions)

1. [Features](#features)
    1. [Existing Features](#existing-features)
        - [Common Features Accross Pages](#common-features-accross-pages)
        - [Features Specific to Pages](#features-specific-to-pages)
    1. [Future Features](#future-features)

1. [Information Architecture](#information-architecture)
    1. [Database](#database)
    1. [Structure](#structure)
    1. [Relationship](#relationship)

1. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    1. [Frameworks, Libraries and Programs](#frameworks,-libraries-and-programs)

1. [Testing](#testing)

1. [Deployment](#deployment)
    1. [Local](#local)
        - [Pre-requisites](#pre-requisites)
        - [Recommended](#recommended)
        - [Steps](#steps)
    1. [Remote](#remote)
        - [Pre-requisites](#pre-requisites)
        - [Steps](#steps)

1. [Credits](#credits)

## Strategy Plane
The main target audience for Plant Parent
- Users interested in plants.
- Users interested in decorating their rooms with plants and nice pots for plants.

The user can purchase individual items on the site which makes the site available to anyone visiting. However, when choosing a subscription each month users have the opportunity, based on their subscription value, to choosing new products that are delivered to them. This creates a fun aspect, inviting users to return and possibly purchase more products.

Research
- This is a B2C model, hence the website makes use of larger images/graphics and less text
- People purchasing items online are mostly impulse shopping and not many users like to register for new pages. This is why a subscription model is used to increase the number of returning users.

Features worth doing
- A Roadmap was used to identify which objectives are worth achieving. All objectives/high-level features were listed and scored on a 1-5 scale (5 being the most important) if they are Important or Viable. The importance score was summed together while the Viability scored was averaged and multiplied by the number of features. Since these numbers did not equal, they were plotted on the Importance/Viability graph to identify the most important ones and the ones that, for now, will be left out.

    <img src="./readme_files/feature_table.png"/>


    <img src="./readme_files/feasibility_chart.png"/>

### Business Goals
- Earn profit by allowing anyone to purchase products
- Connect the business to users to access a larger audience by having social media links accessible 
- Outperform competitors by providing excellent products, services, and customer support

### User Stories

- #### Common user stories
    1. I want to easily navigate the site so that I can find what I'm looking for quickly.
    1. I want to be able to contact the company if I'm experiencing an issue.
    1. I want the website to be readable on all screen sizes.

- #### As a first-time visitor I want to
    1. Easily understand the purpose of the site so that I can decide whether I want to invest my time into it.
    1. Understand the benefits of becoming a member/registering for the site so that I can decide if I want to.
    1. View and compare all memberships so that I can decide what membership if any, I want to subscribe to.
    1. Easily find where I can register for the site so that I don't waste my time looking for it and I'm not discouraged not to sign up.
    1. Be able to quickly register and start using the site so that I can have my account and receive the benefits.

- #### As a casual shopper I want to
    1. Navigate to the shop page easily so that I can find what I need quickly.
    1. Filter all products by category so that I can quickly have oversight of the products that I'm interested in.
    1. Sort all items by date added, name or price so that I can identify new products, products that fit my budget, and find easier what I'm looking for.
    1. Search for an item from anywhere on the site so that I can easily find what I'm looking for.
    1. Be able to see the price of the item without clicking into it so that I can easily decide if I can afford the item.
    1. Be able to quickly add the item without having to click on the product so that I can save time if I know that I want to purchase the item.
    1. Be able to see more details about the product so that I can make an educated decision of whether to purchase the item.
    1. Select the quantity of the product so that I can choose how many products I'm purchasing and not have to add the same item multiple times.
    1. Be able to see the rating and reviews to allow me to judge if the item is worth the price based on other feedback.
    1. Leave a review so that I can provide my feedback and experience to the company and other shoppers.
    1. Edit my review so that I can change it in case I've changed my mind or made a mistake while adding the review.
    1. Delete my review so that I can remove it in case my review is no longer relevant or I don't want to keep it up.
    1. See my shopping cart as items are added to know how the total without having to go to another page.
    1. Edit the quantity of added items so that I don't have to remove and add items again.
    1. Remove added items easily so that I can purchase only the items that I want.
    1. See my shopping cart before checkout so that I can make changes before purchase.
    1. See all charges included before making a payment so that I can decide if I want to proceed with the purchase.
    1. View my order as I'm checking out to be able to confirm what I'm purchasing.
    1. easily add my details without too many steps so that I don't get discouraged by the lengthy checkout process.
    1. Securely add my payment information so that I feel safe giving my card details.
    1. See Order confirmation and receive confirmation e-mail so that I have proof of purchase and order number.

- #### As a member I want to
    1. Log in and sign out quickly and easily so that I can access or close my account.
    1. See my personal account information so that I can manage my details.
    1. See my membership site so that I can verify my benefits and the price of the membership.
    1. Change the membership easily so that I can control what benefits and expenses I'm having.
    1. Cancel paid membership so that I don't have to pay for it.
    1. See my order history so that I can have the confirmation and details for all of them in one place and manage them easily.
    1. Can see the estimated date of delivery so that I can arrange to receive the package.
    1. Recieve benefits as a member so that I get my money's worth.

- #### As an admin I want to
    1. Be able to add an item so that I can update the products on the site.
    1. Be able to edit and remove items so that I can customize items on the site and offer new deals to customers depending on the demand and new trends.
    1. Add and edit new memberships so that I can customize the price and benefits depending on the popularity of the membership.
    1. Add and edit new delivery types to accommodate shipping to more countries.
    1. Have oversight of the user data so that if anyone is experiencing an issue I can investigate and resolve the issue.


## Scope Plane
- Minimal Viable Product for this project is an e-commerce site with at least following features:
    - Authorization
    - Payment system
    - Product page
    - Reviews
    - Profile page

## Surface Plane

- #### Color scheme
    - The color scheme chosen for this project is muted pastels to go well with the colorful images. It is my view that if I had chosen a more bold color palette, it would be too hectic and too busy looking. Creating a messy look and feel for the website. The main three colors used are Cadet Blue Crayola (#B3BCC9), Gainsboro(#E4DADC), and Opal (#A9C6C4). Secondary colors were Shadow Blue (#75859B) and Lavender Gray(#CEC5CC) and darker variations of those for text contrast.

        <img src="./readme_files/color_palette.png" height="100px" />

- #### Typography
    - This project uses 3 different fonts.
        - Primary font is Sans Serif type of a font called Quicksand. I chose this font to help with readability and to add to the simplistic color scheme. I wanted the site to feel clean and modern and not too overcrowded. This font was used for most of the text and links.

        
        - The secondary font is a Serif type of font Bodoni Moda. This font goes well together with a sans serif font like Quicksand to provide a contrast in style and with that capture reader's attention and make the site a bit more interesting and dynamic. This font was used for most of the headings.

        - The last font used is Caveat. This font is just used as a decoration as I was looking for something that would resemble handwriting. Even though I want the design of the site to feel sophisticated, I also wanted to give it a fun personality which I think can be partially achieved by imitating handwritten headings or signs.


        - Additionally, [fontawesome](https://fontawesome.com/) icons were used to emphasize the point, use for buttons, or just to add to the design.

- #### Imagery
    - Images
        - The primary reason for using images is for informative purposes. Images are displayed in item cards to allow users to visually engage with items added by other users and decide if they are interested in the item.
        The secondary purpose of the images is aesthetic. The images displayed on cards are kept quite large and the same size while not being distorted. This attributes to the clean, organized look of the website. An image is also used as a hero image that takes the full screen to separate the page and not distract the user from the message on the landing page.
        All images have been taken from [unspalsh](https://unsplash.com/) and graphics from [flaticon](https://www.flaticon.com/).

- #### Other 
    - All headings and navbar links were given half of a background color that looks like is offset from the top. Three primary colors were used interchangeably on all pages but the design remained the same. I believe this adds to my vision of a clean but modern-looking site.

    - All buttons have the same design of having a border in one of the primary colors and have a hover effect with background fill. 

    - [Bootstrap 5.0]() was used as the front end framework to help with layout and easy pre-built components such as accordeons

    - [Notyf](https://github.com/caroso1222/notyf) and built-in Bootstrap toast were used for notifications and cart toast

    - For hamburger menu animations, jonsuh.com(https://jonsuh.com/hamburgers/) was used

# Features

## Existing Features

### Common Features Across Pages
- [x] **Header** - facilitates an effortless navigation across all pages
    - The header is positioned to always be visible at the top of the screen (mobile, tablet, and desktop) which allows visitors to find it quickly.
    - The brand logo is positioned at the top of the page in the header and redirects the user back to the home page. This allows the user to easily find the homepage.
    - The page navigation is located in the header at the top of the page on desktop and laptop sizes and collapsable top navigation for mobiles and tablets. This adheres to the navigation conventions allowing the user to intuitively navigate the page.
    - Navigation links have a custom background color that seems to be offset downwards when hovered over on larger screen sizes, letting the user know that these are clickable links.
    - The navigation link, matching the page that the user is visiting, stay 'active'(which matches the hover effect from the previous point) to let the user quickly establish which page she/he is visiting.
    - Navigation links collapse in a personalized hamburger menu when viewed in mobile sizes.
    - Cart and user icons are always visible in the navbar on all screen sizes so that users can easily identify the number of items they have in the cart and so that they can visit user sites quickly and easily.
    - User icon is a dropdown menu displaying 'Register' and 'Log In' for the unauthorized user and 'My Details', 'My Membership', and 'Order History' for an authorized user.
- [x] **Heading**
    - All headings are styled in the same manner to let the user understand the page structure quickly.
- [x] **Links/buttons**
    - All links have a hover effect and are noticeably different than the rest of the text around them, indicating that they are clickable.
    - All external links open in a new tab to allow the user to easily navigate back to the page.
    - Buttons are outlined, with transparent background. On hover the background is filled in to match the border of the button, indicating that the button is clickable.
- [x] **Footer**
    - Footer is always displayed at the bottom of the page, regardless of the content size.
    - Socials are displayed and grouped. They are displayed in the footer to adhere to the convention and let the user locate them quickly.
- [x] **Messages and Cart Toast**
    - A feedback is provided to the user throughout the whole page. The messages shown are colored to match the tone of the message - whether it's a success message or an error message.
    - Cart Toast, similarly to Messages is displayed as a pop-up and across the whole page indicated to the user what the total is and what items have been added to the cart.
    - User can easily change the number of items from this cart and remove them altogether.
    - User can dismiss the toast with an 'x' close button. 

### Features Specific to Pages
- [x] **Home** Page
    - Hero image with a short description and a call-to-action to let users join a membership plan.
    - A section describing high-level how the site works
    - A section with this month's featured items and a button to redirect the user to the shop.
    - Instagram picture gallery with an Instagram handle so that users can easily find it and navigate to it.

- [x] **Shop** Page
    - Items displayed in a responsive grid layout to accommodate all screen sizes
    - Only the most important information is displayed on the card such as title, rating, price, and 'Buy Now' button.
    - Item image can be clicked to bring the user to the details page.
    - Page has category buttons at the top so that user can easily filter all items by categories or all
    - Filter icon button that can be toggled to collapse or reveal sort icons
    - Sort icons that can sort items by date added, price and name
    - Buy Now button that automatically adds an item to the cart

- [x] **Product Detail** Page
    - Back button that brings the user back to the previous page.
    - Average rating displayed.
    - Description of the product which allows users to gain more information on the product.
    - Quantity adder that allows user to select 1-10 items and display price as the item quantity os changed.
    - Add to the cart button that adds an item to the cart.
    - Reviews section that displays reviews added by all users.
    - Reviews are implemented as modals that appear as a top layer over all other content.
    - If the user has added a review, they will see the edit and delete buttons that allow the user to edit or delete the review

- [x] **Memberships** Page
    - All memberships are displayed side by side to allow the user to compare them all and make an educated decision.
    - Buttons lets the user select a membership they want and redirects them to the Register page.

- [x] **Memberships Checkout and Change** Page
    - Displays chosen membership it's benefits.
    - In the Membership Checkout view, the user can change the membership before payment.
    - user can press confirm and will be redirected to the Stripe Checkout page.
    - In membership change, user can see their current membership and selected one.

- [x] **Cart** Page
    - Displays summary of items with the subtotal excluding the delivery.
    - Allow users to change the quantity or remove the item.
    - User can navigate back to the shop page or the checkout page

- [x] **Delivery/Checkout** Page
    - Order Summary is displayed on the right or small screens as a collapsed excellent at the top of the page.
    - User can select their shipping type which will update their delivery cost.
    - Delivery Details are provided as a form using crispy forms.
    - User can save their delivery details to their profile if they have one, otherwise, they are offered sign in and sign up buttons
    - User is provided with a secure wat to enter their bank details in.

- [x] **Checkout Success** Page
    - Order Details are provided to the user as a confirmation on top of the e-mail that has been sent to them.

- [x] **Profile** Page
    - User's membership summary is shown with the name and the price of it.
    - 'More' button brings the user to the 'My Membership' site.
    - A crispy forms form that displays to the user any details that the user has saved. They can be edited or added to this page.

- [x] **My Membership** Page
    - User's membership in detail is displayed
    - User can click on the 'Change' button that brings the user to the Membership view where they can select which membership they want to change to

- [x] **Order History** Page
    - an accordion of all order, with only the lastest order not collapsed.
    - Items are displayed within the collapsed element and users can view them by clicking on it.
    - Each item has Buy Again and Review buttons to allow the user to easily interact with purchased items.
    - Details button brings the user to the Order details view

- [x] **Order Details** Page
    - User can view the particular order's details
    - Dispatch, delivery, and order dates are displayed unless they are not entered yet then estimated dates are shown based on the delivery speed.

## Future Features
- [ ] Implement multi-colored items, database is already set up for it.
- [ ] Add Apple pay to payments and Google sign-in

# Information Architecture

## Database
- The databse used for this project was **[PostgresSQL](https://www.postgresql.org/)** for deployed project and **[SQLite]()https://www.sqlite.org/index.html** on the local machine in development

## Structure
- The data consists of 10 models accross 7 apps
    - **Home app** - Displays the home page of the website.
    - **Checkout app** - Handles the checkout pages and the checkout view for product purchase, including payments.

        - DeliveryType Model - holds different delivery type information such as rate of cost for delivery, dispatch time, delivery_speed, constant deliver charge, limit at which delivery charge changes from constant to a rate

                name = models.CharField('Delivery Type', max_length=20)
                dispatch_speed = models.IntegerField('days to dispatch order')
                delivery_speed = models.IntegerField('days to deliver order')
                limit = models.DecimalField('order amount limit for set delivery cost', max_digits=5, decimal_places=2, default=0)
                const = models.DecimalField('set delivey cost', max_digits=5, decimal_places=2, default=0)
                rate = models.DecimalField('delivery rate', max_digits=5, decimal_places=2, default=0)

        - Order Model - Holds information on each order. This is populated when user completes the checkout. The details entered in the checkout will populate this model as well as custom calculations for total amount and discount and delivery charge

                order_number = models.CharField(max_length=36, default=uuid.uuid4, editable=False)
                user_profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='user_orders')
                first_name = models.CharField(max_length=30)
                last_name = models.CharField(max_length=30)
                full_name = models.CharField(max_length=70, editable=False, default='')
                phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="Enter phone number in a format: '+111111111' and no longer that 15 digits.")
                phone_number = models.CharField(validators=[phone_regex], max_length=16, default=0)
                email = models.EmailField(max_length=254)
                address_line_1 = models.CharField(max_length=100,)
                address_line_2 = models.CharField(max_length=100, null=True, blank=True)
                city = models.CharField('city or town', max_length=85)
                region = models.CharField('region or county', max_length=85, null=True, blank=True)
                country = CountryField(blank_label='Country *')
                postcode = models.CharField('post/zip code', max_length=10)
                order_date = models.DateTimeField(auto_now_add=True)
                dispatch_date = models.DateTimeField('order dispatched on', null=True, blank=True)
                est_dispatch_dte = models.DateTimeField('estimated order dispatch date', ditable=False, null=True, blank=True)
                delivery_date = models.DateTimeField('order delivered on', null=True, blank=True)
                est_deliery_dte = models.DateTimeField('estimated order delivery date', editable=False, null=True, blank=True)
                delivery_type = models.ForeignKey(DeliveryType, on_delete=models.CASCADE)
                delivery_cost = models.DecimalField(max_digits=7, decimal_places=2, default=0)
                subtotal = models.DecimalField(max_digits=7, decimal_places=2, default=0)
                total = models.DecimalField(max_digits=7, decimal_places=2, default=0)
                original_cart = models.TextField(default='')
                stripe_pid = models.CharField(max_length=254, default='')

        - OrderLine Model that captures each item added to the cart and are used for calucations in the Order Model

                order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_line')
                product = models.ForeignKey(Product, on_delete=models.CASCADE)
                color = models.CharField(max_length=20, null=True, blank=True)
                quantity = models.IntegerField(default=0)
                line_total = models.DecimalField(max_digits=7, decimal_places=2, default=0, editable=False)

    - Memberships app - Displays different kinds of memebrship plans, handles user subscription to membership plans

        - Membership Model - contains memebrship plans

                name = models.CharField(max_length=50)
                pic = models.ImageField('Membership Picture', null=True, blank=True)
                free_delivery = models.CharField(max_length=1, hoices=FREE_DELIVERY, default='N')
                first_order_disc = models.IntegerField('First Order Discount', default=0)
                overall_discount = models.IntegerField(default=0)
                priority = models.CharField(max_length=10, choices=PRIORITY, help_text=('Priority of announcements'))
                q_gift = models.CharField('Quarterly Gift', max_length=50, null=True, blank=True)
                price = models.DecimalField(max_digits=4, decimal_places=2)

        - StripCustomer Model - stores information used to identify a user in Stripe payment system for subscriptions

                user = models.OneToOneField(to=User, on_delete=models.CASCADE)
                stripeCustomerId = models.CharField(max_length=255)
                stripeSubscriptionId = models.CharField(max_length=255)

    - Products app - Handles Product Display and Individual Item Detil view
        - Category Model - Stores Item categories

                name = models.CharField(max_length=20)
        
        - Product Model - stores Individual Item information

                product_code = models.CharField(max_length=36, default=uuid.uuid4, editable=False)
                category = models.ForeignKey(Category, on_delete=models.CASCADE)
                name = models.CharField(max_length=50)
                description = models.TextField()
                avg_rating = models.DecimalField('average product rating', max_digits=2, decimal_places=1, default=0, null=True, blank=True)
                price = models.DecimalField(max_digits=5, decimal_places=2)
                many_colors = models.CharField(max_length=1, choices=MANY_COLORS, help_text=('Will the product come in multiple colors?'))
                main_pic = models.ImageField('thumbnail picture', null=True, blank=True)
                pic2 = models.ImageField('additional picture 2', null=True, blank=True)
                pic3 = models.ImageField('additional picture 3', null=True, blank=True)
                pic4 = models.ImageField('additional picture 4', null=True, blank=True)
                added_date = models.DateTimeField(auto_now_add=True)
                release_date = models.DateTimeField('product release date', help_text=('Select today/now as the input if the product is being published now.'))

        - Color Model - handles they colors of an item if the item hsa mutliple colors

                name = models.CharField(max_length=20)
                color_hex = ColorField(default='#FFFFFF')
                product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)

    - Profiles app - Handles Profile view and creating a profile whenever a user registers. It also handles Order History view.
        - Profile Model - holds data on each user, this can be used in checkout to prefill the checkout form.

                user = models.OneToOneField(User, on_delete=models.CASCADE)
                membership = models.ForeignKey(Membership, on_delete=models.CASCADE, null=True, blank=True)
                user_phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Enter phone number in a format: '+111111111' and no longer that 15 digits.")
                user_phone_number = models.CharField(validators=[user_phone_regex], max_length=16, null=True, blank=True)
                user_address_line_1 = models.CharField(max_length=100, null=True, blank=True)
                user_address_line_2 = models.CharField(max_length=100, null=True,  blank=True)
                user_city = models.CharField('city or town', max_length=85, null=True, blank=True)
                user_region = models.CharField('region or county', max_length=85, null=True, blank=True)
                user_country = CountryField(blank_label='Country',  null=True, blank=True)
                user_postcode = models.CharField('post/zip code', max_length=10, null=True, blank=True)


    - Reviews app  - Handles CRUD operations for Reviews
        - Review Model

                user = models.ForeignKey(Profile, on_delete=models.CASCADE)
                product = models.ForeignKey(Product, on_delete=models.CASCADE)
                title = models.CharField(max_length=50)
                description = models.TextField()
                rating = models.IntegerField(choices=RATE)
                upvotes = models.IntegerField(default=0)
                downvotes = models.IntegerField(default=0)
                date_posted = models.DateTimeField(auto_now_add=True)

    - Shpping Cart app - Handles CRUD operations with order items in cart
        - No models

## Relationship
- The relation of the models are displayed in the image below

    <img src="./readme_files/data_schema.png" height="500px" />

# Technologies Used

### Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://www.javascript.com/)
- [Python 3.9.5](https://www.python.org/)

### Frameworks, Libraries and Programs Used
- Front-End
    - [Bootstrap 5.0](https://getbootstrap.com/) - Used for the responsive layout as well as the navigation, header, footer, forms, dropdowns, item cards, modals.
    - [Font Awesome](https://fontawesome.com/) - Font Awesome was used to add social media icons at the bottom of the page and icons throughout the pages.
    - [Google Fonts](https://fonts.google.com/) - Google Fonts was used to import 'Montserrat' font in the style.css file.
    - [Notyf](https://github.com/caroso1222/notyf) - Used to display messages
    - [jQuery 3.5.1](https://jquery.com/) - Used in stripe javascript logic
    - Back-End
- [Django](https://www.djangoproject.com/) - used as the main framework to build the project.
- [Stripe](https://stripe.com) - used to facilitate single payments and subscription plans
[Psycopg2](https://pypi.org/project/psycopg2/)  - used to allow postgresSQL to be used with python
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - used to display forms
- [Gunicorn](https://pypi.org/project/gunicorn/)  - deployment tool
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)  - aid the deployment of AWS S3
- [Pillow](https://pillow.readthedocs.io/en/stable/) - image proccessing tool in python
- [pip3](https://pip.pypa.io/en/stable//)  - used to install all packages in python
- [SQlite3](https://www.sqlite.org/index.html) - used as a database in development
- [PostgreSQL](https://www.postgresql.org/) - used as a database in deployment
- [AWS S3](https://aws.amazon.com/)  - used to store images and static files displayed in the deployed site
- General
    - [Git](https://git-scm.com/) - Git was used to allowing for tracking of any changes in the code and version control.
    - [Github](https://github.com/) - GitHub is used to host the project files.
    - [Gitpod](https://www.gitpod.io/) - IDE used to compile the code as well as facilitate a virtual environment.
    - [Heroku](https://dashboard.heroku.com/apps) - A cloud platform used to deploy the web application.
    - [Addtext](https://addtext.com/) - add text on product images

# Deployment

## Local
Instructions to run the project on your local device using an IDE

### Pre-requisites
- [Python 3](https://www.python.org/downloads/) - used to write the code and to run the project
- [PIP](https://pypi.org/project/pip/) - used to install packages
- [Git](https://git-scm.com/downloads) - used for version control
- [Gitpod](https://www.gitpod.io/) or any IDE of your choice - used to compile the code.
- [Stripe](https://stripe.com/en-ie) Account

### Recommended
- A virtual environment of your choice - used to contain all installations and packages and prevents clashing projects that might use the same package but different versions.
    - Python 3 has a built-in virtual environment [venv](https://docs.python.org/3/tutorial/venv.html). The commands might differ depending on your Operating System, it is advised to read the docs to ensure accuracy. To initialize on MacOS:

            python3 -m venv .venv
        where `.venv` is the name/path you are giving to the virtual environment

### Steps
1. Go to the project [repository](https://github.com/Gonzo2500/Plant_Love)
1. Get the files used by using one of the methods below:
    - Download the files used by clicking the 'Code' button located in the top section of the repository. Then select 'Download ZIP' and unzip the files in the directory of your choice.

        <img src="./readme_docs/zip.png" height="200px" /> 
    
    - Clone the repository by running the following command from your IDE

            gh repo clone Gonzo2500/Plant_Love
    
1. In your IDE, navigate to the project directory where you located downloaded files/cloned the repo

        cd path/to/your/folder
1. Activate your virtual environment. If using Python's venv:

        source .venv/bin/activate
    on MacOS and Unix where .venv is the name you gave previously

        .venv\Scripts\activate.bat
    on Windows where .venv is the name you gave previously

1. Install all reqauirements from [requirements.txt](requrements.txt) file
    
        pip3 install -r requirements.txt

1. Create a file `env.py` to store environment variables
1. Add environment variable in the format as shown below

        os.environ.setdefault('SECRET_KEY', '<your-variable-goes-here>')
        os.environ.setdefault('DEVELOPMENT', '1')
        os.environ.setdefault('ALLOWED_HOSTS', '<your-variable-goes-here>')
        os.environ.setdefault('STRIPE_PUBLIC_KEY', '<your-variable-goes-here>')
        os.environ.setdefault('STRIPE_SECRET_KEY', '<your-variable-goes-here>')
        os.environ.setdefault('STRIPE_WH_SECRET_CH', '<your-variable-goes-here>')
        os.environ.setdefault('STRIPE_WH_SECRET_SUB', '<your-variable-goes-here>')
    where 
    -  `SECRET_KEY` value is a key of your choice, to ensure appropriate seccurity measures, this can be generated using [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/)
    -  `DEVELOPMENT` is set to `1` and is used in settings.py logic to ensure file is dynamic between local and remote setups
    - `STRIPE_PUBLIC_KEY` and `STRIPE_SECRET_KEY` values are obatined from the [Stripe](https://stripe.com/en-ie) website
                <details>
                        <summary>How to get Stripe API values</summary>
                        <ul>
                            <li>Once logged in, you will be redirected to the **Overview** page, if not, navigate there by clicking **Overview** on the left hand side
                            </li>
                                <img src="./readme_files/stripe_setup.png" height="200px">
                            <li>Get the API values by clicking on **Get your test API keys** as shown in the image above</li>
                            <li>Add Publishable key as `STRIPE_PUBLIC_KEY` and Secret key as `STRIPE_SECRET_KEY` environmental variable values</li>
                        </ul>
                </details>
    - `STRIPE_WH_SECRET` value is obtained from the [Stripe](https://stripe.com/en-ie) website 
                    <details>
                        <summary>Getting Webhooks API value</summary>
                        <ul>
                            <li>Go to your [stripe dashboard](dashboard.stripe.com) and naviagte to **Developers** > **Webhooks**
                            </li>
                            <li>Click **Add endpoint** and enter your ngrok link followed by `/checkout/wh/` as shown in the image below</li>
                                <img src="./readme_files/webhook.PNG" height="400px">
                            <li>Click on **recieve all events** and then Add endpoint to finish the setup</li>
                            <li>To get the `STRIPE_WH_SECRET` value, click on the added link under Endpoints and copy the Signing secret key in your variable</li>
                        </ul>
                </details>
    - `ALLOWED_HOSTS` this should be set to your gitpod or ngrok if you using visual studio code as an example url
1. Run the application

        python3 manage.py runserver

1. Website should be available on a link similar to `http://127.0.0.1:8000`. (check your IDE terminal)
1. Note: `python3` and `pip3` commands can vary depending on version/machine/IDE you're using. Always check docs if unsure.

## Remote
### Pre-requisites
- Set up [Heroku](https://dashboard.heroku.com/apps) Account and app
        <details>
            <summary>Heroku Basic Set Up</summary>
            <ul>
                <li>Register to the Heroku website by clicking on this [sign up link(https://signup.heroku.com/login)]</li>
                <li>Create a new app on the Heroku website, enter a unique name and choose a region closest to you.
                </li>
            </ul>
        </details>
- Create AWS account and upload static files used in the project
        <details>
            <summary>AWS S3 static file storage setup</summary>
            <ul>
                <li>Go to [aws.amazon.com](https://aws.amazon.com/) website and Register, you might have to enter your credit card details, however, while using free tier there should be no charges. That being said, you should monitor your own usage.</li>
                <li>After registration, go back to the [AWS](https://aws.amazon.com/) site and click the orange 'sign in to the Console' button.</li>
                <li>Sign in as 'Root User' with your e-mail address and password used in registration.</li>
                <li>At the top of the site, search for S3 and click on it to open.</li>
                <li>Click on the **Create bucket** button located on the top right.
                </li>
                <li>Name should match the Heroku app name, Region is set to the closest tot you, untick the 'Block all public access' and tick the acknowledgement next to the warning symbol.</li>
                <li>Go to the end and click **Create Bucket**</li>
                <li>To Enable static website hosting
                    <ul>
                        <li>Select the bucket by clicking on it and go to **Properties** located at the top.</li>
                        <li>Scroll down to the very bottom and click on 'Edit' under **Static website hosting**.</li>
                        <li>Select 'Enable' and enter the default values for Index document and Error document as these won't be used.
                        </li>
                        <li>Click **Save changes**</li>
                    </ul>
                </li>
                <li>Make changes in Permissions
                    <ul>
                        <li>Go to **Permissions** located at the top</li>
                        <li>Scroll down and click 'Edit' under **Cross-origin resource sharing (CORS)** which will provide access between Heroku and the bucket</li>
                        <li>Scroll down to the very bottom and click on 'Edit' under **Static website hosting**.</li>
                        <li>Add the following JSON code (indent it properly) and save changes.
                            <pre>
                                [
                                    {
                                        "AllowedHeaders": [
                                            "Authorization"
                                        ],
                                        "AllowedMethods": [
                                            "GET"
                                        ],
                                        "AllowedOrigins": [
                                            "*"
                                        ],
                                        "ExposeHeaders": []
                                    }
                                ]
                            </pre>
                        </li>
                        <li>Click 'Edit' under **bucket policy** and click on 'Policy Generator' which will open in a new tab.</li>
                        <li>'Select Type or Policy' set to 'S3 Bucket Policy', 'Principal' set to '*', under 'Actions' add 'GetObject, GetObjectAcl, PutObject, PutObjectAcl, DeleteObject'</li>
                        <li>Go back to the previous tab and copy the **Bucket ARN** and paste it under **Amazon Resource Name (ARN)**
                        </li>
                        <li>Click 'Add Statement' and then click 'Generate Policy'.</li>
                        <li>Copy the code, paste it in the **bucket policy** field (previous tab) and add `/*` after the ARN to allow all resources in the bucket</li>
                        <li>Click 'Save Changes'.</li>
                        <li>Still in permissions click 'Edit' under **Access control list (ACL)**</li>
                        <li>Under 'Everyone', tick 'List'</li>
                        <li>Tick 'I understand the effects....' and Save changes.</li>
                    </ul>
                </li>
                <li>At the top search for **IAM** and click on it.</li>
                <li> Create a Group
                    <ul>
                        <li>On the left hand side, under 'Access management' click on **Groups**
                        </li>
                        <li>On the top right click 'Create New Group' and name it something that makes sense to you.</li>
                        <li>Click 'Next Step' and then 'Create Group' (skips the policy for now, we will create it in one of the following steps).</li>
                    </ul>
                </li>
                <li> Create a Policy
                    <ul>
                        <li>On the left hand side, under 'Access management' click on **Policies**.</li>
                        <li>On the top right click 'Create policy' select JSON and click on 'Import Managed Policy'.
                        </li>
                        <li>Search for 'S3', select **AmazonS3FullAccess** and click 'Import'.</li>
                        <li>Since we only want full access to our Bucket, go back to copy your ARN from before and add it under 'Resource' twice, the second time with `/*` after the ARN.
                        </li>
                        <li>Click on 'Review policy', add name and description and 'Create policy'.</li>
                    </ul>
                </li>
                <li> Attach the Policy to the Group created
                    <ul>
                        <li>Go to **Groups** on the left hand side.</li>
                        <li>Click on the relevant group and click on 'Attach Policy'.</li>
                        <li>Search for the policy just created, select it and click 'Attach Policy'.</li>
                    </ul>
                </li>
                <li> Create Users to put in the Group
                    <ul>
                        <li>Click on **Users** on the left hand side adn click 'Add user'.</li>
                        <li>Add name and tick to give 'Programmatic access', then click 'Next: Permissions'.</li>
                        <li>Select the group to put the user in and keep clicking 'Next; until the very end and click 'Create user'.</li>
                        <li>Click on 'Download .csv' file, this is important as you won't have access to it again!</li>
                        <li>Use the values from this file to later set your     `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` variables. </li>
                    </ul>
                </li>
        </details>


### Steps
1. In Heroku, go to **Resources** and search for **Heroku Postgres**, we will use this as our development database
    - Select 'Hobby Dev - Free' and click to Submit Order Form

1. Comment out the 'SQLite and Postgres databases' section in the `settings.py` file and uncomment 'Postgres Database' section. Add your `DATABASE_URL` link obtained from Heroku Config Vars

        DATABASES = {
            'default': dj_database_url.parse('your-url-goes-here')
        }
1. Migrate your models to Postgres SQL database

        python3 manage.py migrate

1. If you have a JSON file with products displayed on the site, import them now in this order

        python3 manage.py loaddata categories
        python3 manage.py loaddata products

1. Create a superuser that will be used to access the admin page as well as to manage the database. Enter username, password, and e-mail as required

        python3 manage.py createsuperuser

1. In `settings.py` delete the 'Postgres SQL Database' section (make sure you don't commit your DATABASE_URL link!) and un-comment 'SQLite and Postgres SQL Databases' section - this will allow for use of  either of the databases interchangeably

1. Freeze dependencies in a  requirements.txt file (if it hasn't been created/updated before)

        pip3 freeze --local > requirements.txt

1. Create a Procfile that tells Heroku to create a web dyno and add the following line in it, where `the-name-of-your-app` is the name of your django project

        web: gunicorn the-name-of-your-app.wsgi:application

1. `Add`, `commit` and `push` your changes up to GitHub

1. Go to Heroku and add all of the following environmental variables (Settings > Reveal Config Vars)

    | Key | Value |
    --- | ---
    AWS_ACCESS_KEY_ID | `<your_aws_access__key>`
    AWS_SECRET_ACCESS_KEY | `<your_aws_secret_access_key>`
    DATABASE_URL | `generated automatically`
    EMAIL_HOST_PASS | `<your_email_key>`
    EMAIL_HOST_USER | `<your_email>`
    SECRET_KEY | `<your_secret_key>`
    STRIPE_PUBLIC_KEY | `<your_stripe_public_key>`
    STRIPE_SECRET_KEY | `<your_stripe_secret_key>`
    STRIPE_WH_SECRET_CH | `<your_stripe_webhook_key>`
    STRIPE_WH_SECRET_SUB | `<your_stripe_webhook_key>`
    USE_AWS | `True`
    ALLOWED_HOSTS | `<your-heroku-app-url>`
    
1. In Heroku go to **Deploy** that's located at the top of the site


1. Click on the **GitHub** option and connect your GitHub account as well as your repo from GitHub (search for the repo name)


1. Click on **Enable Automatic Deploys** and then **Deploy Branch**, you should see a successful build here


1. Open your app


1. You should see `static/` folder with your static files in it in you S3 bucket.

1. In your S3 bucket, add `media/` folder.

1. If you didn't use JSON filer for product import, now is a good time to navigate to `your-ulr/admin/` page and add the Products and Categories in.

1. Your app should be deployed and you should be able to see your added products.

### Code :floppy_disk:
- Collapsible sections in README.md seen on [GitHub Gist](https://gist.github.com/pierrejoubert73/902cc94d79424356a8d20be2b382e1ab) post done by pierrejoubert73
- CSS Prefixed by [Autoprefixer CSS online](https://autoprefixer.github.io/)
- [django-colorfield](https://pypi.org/project/django-colorfield/) - Used for color picker in Products.Color model
- [Notyf](https://github.com/caroso1222/notyf) for toasts
- Hamburger animation taken from [jonsuh.com](https://jonsuh.com/hamburgers/)
- stripe subscription model was modified to fit this project but originally taken from these sources:
    - [testdriven](https://testdriven.io/blog/django-stripe-subscriptions/)
    - [stripe](https://stripe.com/docs/billing/subscriptions/checkout)

### Media :clapper:
-[GIF](https://icons8.com/preloaders/) for loader page
- all images taken from [unspalsh](https://unsplash.com/) 
- all plant icons taken from [flaticon](https://www.flaticon.com/)




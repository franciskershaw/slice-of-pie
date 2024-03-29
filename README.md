# Slice of Pie!

![Wireframe temp hero image](media/nonproducts/amiresponsive.png)

## Code Institute's Milestone Project 4 - Full Stack Frameworks

Slice of Pie is the brainchild of Zoe Thexton, who produces custom triangular tables that fit seamlessly into any section of a person's living or bedroom. Designed using CAD software, the tables can be assembled by hand in a variety of sizes, types of wood, and number of shelving levels. The inspiration for this product came from the need to get creative with the limited space available in her own living room (and generally missing somewhere to put a cup of tea down as a result of this!), while the product's name comes from the triangular shape of the finished design. The only thing missing was a means to sell this innovative product to consumers, so I offered to develop and build a prototype ecommerce store capable of displaying the product range and accepting secure payments for orders. My aim for this project was to create a site that allows potential customers to browse all available designs or build their ideal table using a product builder, while allowing administrators to manage the products by adding, editing, or deleting SKUs when required.

This project is the fourth and final of four 'milestone' projects which are required to complete the Code Institute's diploma in full stack web development. Assessment criteria for this milestone project focuses on the ability to produce a full-stack ecommerce store with secure Stripe payments built using the Django Python framework alongside HTML, CSS and JavaScript to control a centrally-owned dataset.

You can view the live site [here](https://slice-of-pie.herokuapp.com/), and a link to the GitHub repository can be found [here](https://github.com/franciskershaw/slice-of-pie).

If you would like to run through the checkout process without spending any of your own money, use *4242 4242 4242 4242* as the long card number, *04/24* as the expiry date, *242* as the security code, and *424242* as the billing postcode.

## Table of Contents
* [UX](#ux)
    * [User Stories](#user-stories)
* [Planning and Design](#planning-and-design)
    * [Strategy Plane](#strategy-plane)
    * [Scope Plane](#scope-plane)
    * [Structure Plane](#structure-plane)
    * [Skeleton Plane](#skeleton-plane)
    * [Surface Plane](#surface-plane)
        * [Colour Scheme](#colour-scheme)
        * [Typography](#typography)
        * [Animations](#animations)
    * [Data Model](#data-model)
* [Apps and Features](#apps-and-features)
* [Existing Features](#existing-features)
* [Defensive design features](#defensive-design-features)
* [Features left to implement](#features-left-to-implement)
* [Technologies used](#technologies-used)
    * [Languages and frameworks](#languages-and-frameworks)
    * [Additional tools](#additional-tools)
* [Git commit messages](#git-commit-messages)
* [Testing](#testing)
* [Deployment](#deployment)
* [Setting up AWS](#setting-up-amazon-web-services-aws)
* [Setting up Emails](#setting-up-email-confirmations)
* [Cloning](#cloning)
* [Credits](#credits)
    * [Media](#media)
    * [Acknowledgements](#acknowledgements)  

  
## UX

My main goals for the creation of this website were as follows:

* To create an ecommerce store where my client can sell a novel concept to the public.
* Design the site in a way that makes the user’s journey from visit to checkout as pleasant and quick as possible.
* Demonstrate my new found skills applying Django as an MVC framework in order to pass this final part of the course and obtain my Diploma.

### User Stories

#### Developer

As the software developer building the store:

1. I want to create a full-stack online shop on which users can browse and securely make purchases, and site admins have control to add, edit or delete items from the site so that I can pass this part of the course.
2. I want this project to adequately display the huge progress I've made in the past year by combining all previously learnt languages and frameworks in unison on a fully-functioning and bug free site.

#### Site owner/administrator

As the owner of the site, or as an administrator:

1. I want to have admin access allowing me to add, edit, delete, and amend the availability of products on my online store so that I can keep my product range up to date.
2. I would like users to be unable to purchase unavailable products so that I don’t have to go through a refund process.
3. I want users to have a product builder which allows them to feel like they are custom building their product as per their preferences so that my store stands out aesthetically compared to competitors.
4. I want the site to be as aesthetically pleasing and intuitive as possible so that users are left with a positive emotional response to their visit and are more likely to make a purchase.

#### Users

As a user/prospective customer:

1. I want to be able to browse available products so that I can see if there’s anything I want to buy.
2. I would like to be able to easily filter and sort products by a range of parameters so that I can quickly find what I am looking for.
3. I want to see clearly if certain products are not available so that I don’t waste my time putting them in my basket.
4. I want to be able to add a product to my basket and then keep on browsing or proceed to checkout.
5. I want to be able to remove or amend the quantity of products in my basket easily so that I have the power to change my mind during my journey.
6. I would like to receive visual feedback at every stage of my journey when I perform actions, so that I am sure what I intended to do has in fact taken place.
7. I want to be able to complete an order without creating an account so that I don’t need to have my details saved.
8. I would like to register for an account so that I can save my delivery details, and see my order history so that my journey on the site is made easier.
9. As an account holder, I would like to be able to save products in my favourites so that I can decide later whether to proceed with my purchase.
10. As an account holder, I would like to be able to save my delivery details so that checkout is faster during my next purchase.
11. As an account holder who has saved their details, I would like to make amends to my saved delivery address so that I can ensure this information is updated accurately.
12. At checkout, I would like the payment process to be simple and intuitive so that I don’t waste any time during my journey.
13. At checkout, I would like to be sure that my details are secure during the payment process so that I don’t feel like I’m taking any risks with my money.
14. After checkout, I would like to receive an order confirmation both on my screen and in my emails so that I can review the purchase and make sure that everything occurred as it was supposed to.

## Planning and Design

### Strategy Plane

The **user stories** as detailed above were the first stage of strategising for the project and were at the forefront during every stage of development. Features that are not in service of the user stories were not considered during the creation of this project.

The **focus** of the project is:
* To create a fully functioning online store that allows the site owner to sell small bespoke tables, on which new products can be added and old products can be removed.

The **business goals** of the stakeholder are:

* To sell as many products as possible.
* Encourage users to return for future browsing and purchases.
* Have a store that can have products added to it and removed so that the product selection remains fresh.

*Therefore, a bespoke website using a full stack framework is required to meet the focus and business goals as it is the only way within my current skill set to produce an ecommerce store that is both aesthetically pleasing and contains the necessary features to allow users to browse and checkout securely, with administrators also able to manipulate the backend when needed.*

At this early stage of planning, it was time to begin researching potential competitors online to get ideas about what features and style choices are prerequisites for an ecommerce store to be successful. As I believe the product being sold is quite novel, I searched mainly for 'quirky' furniture stores that might lead me in the right direction when making decisions later on.

The following sites stood out to me and provided inspiration for certain stylistic choices and features that could be implemented:

* [Rockett St George](https://www.rockettstgeorge.co.uk/furniture/collections.html)
* [Not on the Highstreet](https://www.notonthehighstreet.com/home/furniture)  
* [Audenza](https://www.audenza.com/furniture)

Using the below importance vs viability metric, I listed out all of the opportunities on offer when building this site to help me decide what was achievable, relevant and appropriate with regard to my user stories.

| Opportunity                                 | Importance | Viability
| --------------------------                  | ---------- |-----------
| 10% offer for signing up                    | 2          | 3
| Sign-up to email updates                    | 3          | 3
| Free shipping for ordering a certain amount | 2          | 4
| Animation when you hover over a product     | 3          | 5
| ‘New’ label for new products                | 2          | 5
| Product builder                             | 4          | 3
| Blog                                        | 1          | 3
| Register/sign in option                     | 4          | 4
| Heart icon to save for later                | 3          | 4
| Search bar                                  | 2          | 4
| Filtering of products                       | 5          | 3
| **Total**                                   | **31**     | **41**

At this stage, I felt confident that the features I had in mind for the creation of this site would be mostly viable when compared to their relevant importance to the project. However, it was clear very early on that there were a couple of common ecommerce features that were surplus to requirements for this particular store and would not need to be included:

* Search bar - the site is essentially selling one type of product with different customisations available to it, so there is not an awful lot the user will likely want to search by. Filtering and sorting is a far more logical method for the user to navigate the site.
*  Blog - this is unnecessary for the requirements of version 1 of the project, but could be an interesting feature to include on a future iteration of the site so that the site user can maintain engagement with customers.
* 10% offer for signing up to a mailing list - this is slightly beyond the scope of this project, but again could well be something to pursue on a later version of the site.

### Scope Plane

Based on research and planning achieved during the strategy plane, and considering any limitations of my current coding abilities, the features I decided were critical for the completion of my user stories were as follows:

#### Required functional specifications

* Registration and login capability, so that details and preferences can be saved.
* Admin ability to manage content via the frontend.
* Product builder, which will basically be an advanced filter directing users to a more detailed page about the product of their choice.
* Product details for individual products.
* Ability to simply browse all available products and apply filters or sorting.
* Add, remove or amending the shopping cart.
* Add, remove or amending a wishlist or favourites.
* Profile page for favourites and order history (if logged in).
* Secure checkout and payment.
* Free delivery for reaching a certain threshold.

#### Content requirements

* Ability to request a new password if the user has forgotten.
* Admin control should allow for CRUD capability on listed products.
* The product builder needs to be aesthetically pleasing and seamless to the user journey.
* Checkout must offer the ability to save details for later (if logged in) or guest checkout for those that do not wish to create an account.

#### Nice to haves

I felt at this stage that the above features would contribute to a well rounded and functioning final product, but listed out some features that would be great to include if there was time:

* Create an account using social media.
* FAQ or about section to both give the seller a profile and explain what the product is and who the site owner is.
* Sign up option for a mailing list.

### Structure Plane

With the functional specifications and content requirements nicely ironed out, I concluded that I would need the following pages or Django apps in order to allow users the most seamless journey across the site as possible:

1. **Homepage, containing:**

* Hero image which captures the tone of the site and introduces the user to what is being sold.
* The name of the site and calls to action directing the user to the ‘build your table’ and ‘create account’ sections of the site.
* Featured products just beneath the fold, split into two sides of the screen. Each box has an image of the product and a ‘view’ button. First one could be the basic or flagship product (which is the cheapest available table), and the second one could be the most premium offering.
* (Bonus) A brief 'about' section to provide slightly more context for any organic visitors.

2. **Registration/login/password reset forms, containing:**
* Login or registration form.
* Feedback if fields are incorrectly populated.
* Option to switch from register to login, or vice versa.
* Forgot password option on login form.
* Confirm email address after logging in.
* (Bonus) Ability to sign in using social media.

3. **Product builder page, containing:**
* Animations that present the options available to build a table step by step, appearing and disappearing as per the users input.
* The selection of the final parameter directs the user to the individual product detail page.

4. **All products page, containing:**
* Conventional square boxes structure as per most ecommerce stores, containing product images, descriptions, prices, 'view' buttons', and a heart which would add the product to the user's wishlist.
* Option to sort by price and amount of shelves.
* Option to filter by certain size of table, amount of shelves, or material.

5. **Product (detail) page, containing:**
* Larger version of the product image.
* Title and price per unit of the product.
* Quantity buttons, the default being 1 with the option to increase or decrease quantity accordingly.
* Add to basket or wish list buttons.
* Dimmed and disabled buttons if the product is unavailable.
* Description, and information if the materials of the table are sustainably sourced or not.

6. **Bag and wishlist sidebars across each page, containing:**
* Basket items which can be increased or decreased in quantity, or removed entirely.
* Items in the wish list can be added directly to the basket, or removed.
* Checkout option directly from the basket, or a message saying 'Your bag is empty' if there is nothing in there.

7. **Checkout page, containing:**
* A summary of what is about to be ordered.
* Form with personal details and delivery details, which can be saved by the user if they want to and are logged in.

8. **Product management page for administrators only, containing:**
* A form to add products onto the site, update them, or delete them if required.
* 'Unavailable' option so that products are disabled to users when not available for purchase.

#### Interaction Design

* The site needs a nonlinear structure through the use of a fixed navigation bar which allows users to choose what section of the site they can jump to.
* A consistent footer across all pages can display the logo, copyright information and social links.
* User feedback is required at various stages of their journey, such as:
    * When hovering over links.
    * Feedback message when any user actions pertaining to the bag or wish list through use of toasts.
* The same colour scheme and design choices are needed across all pages to maintain consistency.
* Where applicable, content should be viewable just beyond the fold so users know they can continue to scroll.

#### Information Architecture

* Tree structure should be implemented with the use of burger icon on mobile devices.
* Priority of links from left to right.
* Priority as follows: logo on far left, then in the middle is ‘build table’ and ‘browse all’, far right is ‘Sign in/sign out’, ‘wish list’, ‘basket’.
* Most important CTAs should be visible on the landing page: ‘build product’ or ‘create account’.
* Where possible attempts should be made to reduce the amount of clicks taken for a user to reach the end of their journey.

### Skeleton Plane

At this point in development, it felt safe to start work on wireframes. These were created using [InVision](https://www.invisionapp.com/) as with all my previous projects, and were really useful in ironing out any potential design flaws before any line of code had been written.

![All wireframes](media/nonproducts/all-wireframes.png)

![Homepage](media/nonproducts/landing-page.png)

![Login](media/nonproducts/login.png)

![Profile](media/nonproducts/profile.png)

![Product builder](media/nonproducts/product-builder.png)

![Product detail](media/nonproducts/product-details.png)

![All products](media/nonproducts/all-products.png)

![Checkout](media/nonproducts/checkout.png)

![Product manager](media/nonproducts/product-manager.png)

### Surface Plane

Once wireframing was complete, it was time to start thinking seriously about how the Front End of the website should be approached in terms of 'look and feel'. I asked Zoe for some key words that she'd like to have associated with a website that she owns, and we settled on the following:

* Modern
* Nature
* Innovative
* Homemade

These words would help inform some of the trickier aesthetic choices to be made with the site from this stage of development.

#### Colour Scheme

After combining the key associative words with the colour palette generator found on Coolors, I settled on the following colour scheme for the website:

* #e7e0da (off white)
* #ab793f (copper)
* #7d1224 (burgundy)
* #14223d (dark blue)
* #111a2c (rich black)

The attempt here was to replicate some of the colours associated with the materials used when creating the products.

![Coolors](media/nonproducts/ms4-coolors.png)

#### Typography

As the general feel of the site needed to feel professional and modern, plenty of existing fonts could be easily ruled out of contention straight away. In the end I settled on the Varela Round font from Google Fonts, as it was noted that as well as looking professional, the rounded edge of the lettering mirrors the tables that are on sale nicely.

![Varela Round](media/nonproducts/varela-round.png)

#### Animations

I set out at the beginning of development with the intention of implementing all of the following animations to aid the user experience:

* Change of image, or a zoom effect whenever a product is hovered over - be it on the homepage, product builder, or all products page.
* The product builder feature will rely heavily on entry and exit animations for the various stages of the product building process.
* Custom loading animations for when a page might take a while to load.

### Data Model

#### Conceptual Design Phase

Before implementing any database, I started by drawing up a very basic map of how I could get my various entities to interact with each other on a conceptual level:

![Conceptual design](media/nonproducts/conceptual-design.png)

#### Logical Design Phase

The finalised way my collections work would together on the backend is best illustrated by the below entity relationship diagram:

![Logical design](media/nonproducts/eb-diagram.png)

*Products*
* SKU: a product ID of sorts to help identify it
* Name: product name
* Size: foreign key from the angle model
* Levels: foreign key from the levels model
* Material: foreign key from the material model
* Price: product price
* Image 1: default image for the product
* Image 2: the second product that will appear on the site
* Unavailable: boolean value to declare whether the product is available for purchase or not

*Size/angle model*
* Name: name of angle (how large it is)
* Friendly name: available as an option when rendering to HTML templates

*Levels model*
* Name: name of levels (how many there are)
* Friendly name: available as an option when rendering to HTML templates

*Material model*
* Name: name of material (type of wood)
* Friendly name: available as an option when rendering to HTML templates
* Is sustainable: boolean value to determine whether the material is sustainably sourced.

#### Physical Design Phase

I started by writing all of the product information into a Google spreadsheet, making sure not to forget anything from the previous design steps. Once the information was converted into JSON, I loaded the data onto my workspace, converting it into a SqLite3 database in the process. PostgreSQL is the database provisioned by Heroku on the deployed site, the process of which can be found further down in the deployment section of the document.

## Apps and Features

### Existing Features

#### Consistent across all pages

* A fixed navigation bar appears on every page with the logo and brand on the far left, the main site features in the middle, and interactive icons on the far left for the user's profile, wishlist, and shopping basket. The options present within the profile icon changes depending on whether a user is signed in, or whether a user is an admin user. If a user has items in their wishlist or basket, a small icon with the total quantity appears by the relevant icon.

![desktop navigation](media/nonproducts/readme-nav-desktop.png)

* In mobile, the main navigation items collapse into a conventional burger icon, while the name of the site disappears in order to save space on the smaller screen size. An animation turns the hamburger bars into an X when the navigation links are open for interaction.

![mobile navigation](media/nonproducts/readme-nav-mob.png)

* The footer also remains consistent across all pages, containing the logo, site name, and links to external social media sites.

![footer](media/nonproducts/readme-footer.png)

* All interactable content (like buttons and links) contain hover properties that indicate the user can click on them, while feedback from certain actions (such as adding or removing items from your basket or wishlist) is presented to the user via Bootstrap's toast components.

![toats](media/nonproducts/readme-toast.png)

#### Homepage

* The homepage contains a hero image of a living room table with a plant and a teapot on it, which was chosen for its relaxed tone. The brand name, tagline and two main calls to action appear in the hero section. The calls to action will differ depending on whether a user is signed in, display 'Sign Up' if the user is not logged in instead of 'All Tables'.

![home hero](media/nonproducts/readme-home-hero.png)

* The content of the page appears through a staggered entry animation, which should mask the loading time on the main hero image for most devices.

* Just beneath the fold, the user should be able to see the featured tables section which directs the users to the 'Most Popular' offering (in actual fact, the cheapest table the site has to offer) and 'Recommended' (which happens to be the most expensive product on offer).

![home featured](media/nonproducts/readme-home-featured.png)

* A brief 'about' section explaining the point of the site for those who have continued scrolling follows the featured section, containing one final call to action to direct users to the Table Builder page.

![home about](media/nonproducts/readme-home-about.png)

#### Login and registration

* Using Django's allauth plugin, the users can securely create new accounts and sign back in with either their email address or username.
* Feedback is provided should any user inputs be invalid.

![login](media/nonproducts/readme-login.png)

#### Profile

* The profile page provides signed in users with the option to update their delivery details and peruse former orders.

* All previous order information is housed in accordion components to save space on the browser screen.

* If the user has not yet placed an order, there is a call to action directing them to the product builder so that they may begin their customer journey.

![profile](media/nonproducts/readme-profile.png)


#### All products page

*Note: as the real life product is still currently in development, the product images had to be computer generated to provide as close a depiction to the final products as possible. This is mentioned in the product descriptions, however the intention is very much that on a future iteration of the site there will be professional grade photos taken to improve the overall aesthetics of the site and provide more useful references for the customers.*

* The all products page is styled much like any conventional ecommerce store, with an option to filter or sort the products by preference.
*Note: I encountered a few bugs do do with combining filtering and sorting at the same time, which I go into further detail in the **Known Bugs** section of the testing document.* 

![products desktop](media/nonproducts/readme-products-desktop.png)

* Hovering over the product images triggers a slide animation, displaying an alternative image for the user to look at.

* On smaller screen sizes the filter option becomes an offscreen element that slides down from the top if the user presses the button. Using JavaScript, I ensured that if the user resizes their device this won't break the page.

Mobile view | Filter collapsed
:-----------|:----------------
![products mobile](media/nonproducts/readme-products-mob.png) | ![filter](media/nonproducts/readme-products-filter.png)


* For users that have scrolled down, there is an option to return the user back to the top using a smooth transition.

![scroll](media/nonproducts/readme-scrollup.png)

#### Product builder

* The main feature I wanted to push with this site was the interactive product builder, which essentially functions as an advanced filter for all the products in the database. The user is led on a journey whereby they think they are putting together a table based on their own preferences, whereas information is actually being gathered through JavaScript to determine the product that they wish to browse.

* The choices come into and out of frame through animations to improve the emotional response to this feature.

![product builder](media/nonproducts/readme-productbuilder.png)

#### Product detail page

* The product detail page, which is the end point from both the product builder and browsing the all products page, contains a larger version of the products images box, alongside options to choose the quantity of the product or save a product in the wishlist for later, and a description of the product being viewed.

* A randomly generated set of products appears beneath in order to provide more content and other options for the user to browse.

![product detail](media/nonproducts/readme-product-detail.png)

* Depending on which material model is being used, there may be a supplementary description highlighting that the material has been sustainably sourced.

![sustainable message](media/nonproducts/readme-sustainable.png)

#### Basket and wishlist

* I decided early on that I wanted the basket and wishlist features to be sidebars so that users could access them wherever they were on the site. On mobile, these sidebars take up the entire viewport of the device, but anything above tablet size would only cover up a small portion of the screen.

![basket](media/nonproducts/readme-basket.png)

* Users are able to conveniently move items from their wishlist directly into their basket during their session.

![wishlist](media/nonproducts/readme-wishlist.png)

#### Checkout

* The checkout app uses Stripe payments to securely take payment from prospective customers, conveniently placing everything within one page to reduce the amount of clicks needed to complete a purchase.

* The view provides one section for delivery and payment details, and one section which summarises the order so that users can double check what they are purchasing.

* There is also an option to save delivery details to the profile for those users who have created an account and are signed in.

* A confirmation email is sent out to the users once the payment is complete so that they have a record, and the order is then added to their profile page.

* Stripe webhooks are also fully functioning in order to properly capture any orders that might go wrong during the checkout process from a user perspective.

![checkout](media/nonproducts/readme-checkout.png)

#### Adding and editing products (admin only)

* Admin users can add new products into the database and onto the store via the front end by following the link present in the profile dropdown of the navigation bar.

![add product](media/nonproducts/readme-add-product.png)

* Edit and delete buttons are present on the product detail page.

![edit/delete](media/nonproducts/readme-edit-delete.png)

* The admin user can select 'Unavailable' in the form, which will change the appearance of the product on the front end to inform users that this product is not currently available for purchase.

![unavailable](media/nonproducts/readme-product-unavailable.png)

### Defensive design features

Several defensive design features were required for this project, as much for enhancing the general user experience as for protecting the site against any user with potentially hostile intentions.

#### On the frontend

* Should a user attempt to add a product into their basket that is already there, the product will update to the new quantity with a toast message explaining the product quantity has been updated rather than added for the first time.

* If a user tries to add a product into their wishlist which is already there, an alert toast message appears informing the user that they have already added that product to their favourites.

* Custom 404 pages were created to display at any point a user ended up on the wrong link with a redirect CTA back to safety. I elected to use 404 pages for all errors as I believe this code is slightly more user friendly and recognisable to general audiences on websites.

* Any required form field will not allow a form to be submitted without filling in these fields correctly, through the use of the required attribute.

* Unavailable products are greyed out, with their price being replaced with a very noticeable 'Unavailable', while the button to add to basket is disabled.

* If an unavailable product is in the wishlist, the buttons to add that item directly into the basket are removed, and a 'Coming back soon' message replaces the product name.

![coming soon](media/nonproducts/readme-coming-soon.png)

#### On the backend

* The @login_required decorator was employed on several backend functions relating to admin permissions to restrict non superusers from certain actions on the site. That way, anyone who tries to force their way into certain sections or with a url to remove or edit products will be stopped and provided with a toast message explaining why they cannot continue.

* Checks are made to ensure that unavailable products are not added into the basket, thus ensuring the user does not accidentally purchase something that is not available for purchase.

* Several of the forms have required=True coded into the backend in order to build on top of the required attribute from the front end.

### Features left to implement

The scope of this project was a huge step up from my previous work, and unfortunately due to time constraints there were several features that I was not able to implement fully or at all by the time the submission deadline rolled around. However, I view this iteration of the site as version 1 and I would very much like to return to rethink some aspects of the design and features.

* I initially wanted an animation to greet the user when landing on the homepage, possibly of the tables assembling themselves in an aesthetically pleasing motion - I had neither the required skill set or time to learn how to make this a reality on this occasion.

* I would like users with accounts to be able to leave reviews or testimonials for the site and aggregate an average rating.

* Currently, the wishlist only remains as long as the user keeps their session alive. This is fine for many users who would not log out every time they leave a site, however in the future I would like favourited items to become a part of the profile itself - that way preferences are saved for each session.

* As this product is personal to the site owner, it would be a nice added touch to include a blog feature where users can be updated about upcoming releases.

## Technologies used

### Languages and frameworks

* **HTML5:** Language used for structure and content across all pages.
* **CSS3:** Language used to style elements from the HTML pages.
* **Bootstrap:** CSS and JavaScript framework which allowed for the quick implementation of various components and the grid system.
* **JavaScript::** Programming language used to add interactivity across the site.
* **jQuery::** JavaScript framework which helped me select and manipulate elements with greater ease than purely through JavaScript.
* **Python/Django:** Backend language and high-level framework used to control the logic on the site.
* **SQLite:** The database used as a default in my local development environment.
* **PostgreSQL:** The database used for the live site through Heroku

### Additional tools

* [Amiresponsive:](http://ami.responsivedesign.is/) Used to produce the hero image in README.md and check general responsiveness of the pages.
* [AWS:](https://aws.amazon.com/) Used for hosting static files and media on the cloud in conjunction with Heroku.
* [CSS Gradient:](https://cssgradient.io/) Used to create the subtle gradient in the background of all pages and in the about section of the homepage.
* [Favicon Generator:](https://realfavicongenerator.net/) Used to create the favicon on the browser tab.
* [FontAwesome:](https://fontawesome.com/) Large database of icons which I used all over the site to add to the visual language.
* [Free Formatter:](https://www.freeformatter.com/html-formatter.html) Used to help ensure code was consistently formatted across all files.
* [Github:](https://github.com/) Version control and storage of my code.
* [Gitpod:](https://gitpod.io/) Development environment where all the code was written.
* [Google Docs:](https://docs.google.com/) Used for note taking and was where much of my readme was initially written.
* Google Developer Tools: Used for debugging and testing of responsiveness across several screen sizes. Also vital to the testing of JavaScript functions as and when they were created.
* [Heroku:](https://www.heroku.com/) Hosts the live site.
* [Google Fonts:](https://fonts.google.com/) Provided my site with the 'Varela' font.
* [InVision:](https://www.invisionapp.com/) Used to create all of my wireframes at the beginning of the development process.
* [JSHint:](https://jshint.com/) Checked my javascript code was valid and error free.
* [PEP8Online:](http://pep8online.com/) Confirmed that my Python code complied with PEP8 standards.
* [TinyJPG:](https://tinyjpg.com/) Service used to compress background images and help with site performance
* [Trello:](https://trello.com/) Used to split all tasks into several sprints, to help bring the development process in line with agile principles.
* [W3C CSS Validation Service:](https://jigsaw.w3.org/css-validator/) Confirmed that my CSS is legal.
* [W3C Markup Validation Service:](https://validator.w3.org/) Confirmed that my HTML code is legal.
* [WAVE:](https://wave.webaim.org/) Allowed me to evaluate and test the accessibility of the site.

## Git commit messages

For the commits on this project, I continued to follow the basic rules I had set during my three previous milestone projects. That is to say:

* Always use the imperative tense so that readers would read as *the purpose of this commit is to* - etc.
* Commit often, and keep messages as short as possible.
* Start comments where possible with a prefix that summarises what the commit is for, such as fix (for bugs), add, remove, amend, style, or docs (for anything added to README.md).
* Include the file name or function in question where possible.
* Use the prefix 'test:' for any commits that were being pushed specifically to test bug fixes onto the live site.

At the time of writing, these are among my recent commit messages and illustrate the format I applied for this project:

![Commit Messages](media/nonproducts/commit-messages.png)

## Testing

Please see a full report of the testing applied to this project [here.](testing.md)

## Deployment

This project was deployed very early on during development to Heroku and linked to GitHub through automatic deployments so that changes made to the development environment would update on the live site as soon as they were pushed from Gitpod.

The steps taken to deploy this project were as follows:

1. Open the project in Gitpod, and run the command ` pip3 freeze > requirements.txt ` to create a txt file that Heroku uses to check which dependencies are in use on the site.
2. Create a Procfile by following these steps:
    * Run ` pip3 install gunicorn `
    * Create a Procfile in your root directory
    * At the top of the Procfile, add ` web: gunicorn slice_of_pie.wsgi:application `
3. Commit these new changes to ensure your repository is up to date. 
4. Create a new app in Heroku by signing into the dashboard, clicking 'Create new app' and choosing a relevant name (ensuring that there are dashes where spaces might be).
5. Add a Postgres database to your Heroku app by navigating to the 'Resources' tab and searching for the Heroku Postgres free plan.
6. Set up your Heroku config variables in the 'Settings' tab as follows:
| Key               | Value
| -----------       | ---------- 
| DATABASE_URL      | *The postgres link goes here*
| STRIPE_PUBLIC_KEY | *The secret key on the Stripe dashboard*
| STRIPE_SECRET_KEY	| *The secret key on the Stripe dashboard*
| USE_AWS           | True
| SECRET_KEY        | *my_secret_key*
7. Add a new database in your *settings.py* file as follows:
    * Run ` pip3 install dj_database_url ` and ` pip3 install pyscopg2 ` in your terminal, making sure not to forget to freeze these latest requirements to *requirments.txt*
    * At the top of *settings.py*, add in the line ` import dj_database_url ` alongside your other imports.
    * Comment out *DATABASES* in your *settings.py* file (this will only be temporarily).
    * Add this line in, which includes your Postgres URL so **do not push any changes to GitHub for the moment**:
```
    DATABASES = {
        'default': dj_database_url.parse("*your Postrgres database URL*")
    }
```
8. Make migrations of your models to the Postgres database with the ` python3 manage.py makemigrations ` and ` python3 manage.py migrate ` commands in your terminal.
9. Load the data fixtures from the json data files with these commands (make sure products is definitely last, otherwise proceed in whatever order): 
    * ` python3 manage.py loaddata angles `
    * ` python3 manage.py loaddata levels `
    * ` python3 manage.py loaddata materials `
    * ` python3 manage.py loaddata products `
10. Create a superuser which will have admin rights on the live site by running ` python3 manage.py createsuperuser`  in your terminal and following the steps when prompted.
11. Uncomment the previously commented out *DATABASES* section and remove the sensitive postgres data. The final version of this section should be an if statement which checks which environment is being used before assigning the correct database:
```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
```
12. Add your live hostname to the *ALLOWED_HOSTS* section of *settings.py*, using a comma to separate from the 'localhost'
13. Add your code changes to the staging area, commit, and push to GitHub.
14. Finally, enable automatic deployment to Heroku:
    * Navigate to the 'Deploy' section. 
    * Scroll to the Deployment method section.
    * Click connect to GitHub.
    * Search for your repository and select it.
    * Scroll down to 'Automatic Deployment, and click 'Enable Automatic Deploys'.

## Setting up Amazon Web Services (AWS)

You will likely need to host static files and images with AWS for a site like this, and can do so with the following steps:
### *S3*
1. Create a free AWS account and head to the AWS management console.
2. Search for **S3** or find it in the services section, then create a new bucket.
3. Enter a bucket name (choosing the name of your project would be logical here) and select the nearest available region, uncheck *Block public access* box, then click *Create bucket*.
4. Click on the newly created bucket, navigate to *Properties* tab, turn on static website hosting, and fill in index and error document fields with *index.html* and *error.html* respectively.
5. In the Permissions section, paste in the following configuration:
```
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
```
6. Navigate to the Bucket Policy tab within permissions and click on policy generator.
7. Choose S3 Bucket Policy, allow all principals by entering a star (*) in the Principal field, and select 'GetObject from the Actions dropdown.
8. Return to the previous tab (without closing down the policy generator) and copy the arn number, paste it into the ARN field in the policy generator.
9. Click 'Add Statement', click 'Generate Policy', copy the json code that displays, and paste it into the Bucket Policy tab from before.
10. Add ` /*  ` to the end of the 'Resource' line, and click save.
11. Navigate to the *Access Control List* tab within permissions and set the List objects for everyone under the Public Access section.
### IAM
12. Return to the services section of AWS and open **IAM**
13. Navigate to *Groups*, create a group, and name it something that makes sense for the project (with dashes instead of spaces).
14. Click 'Next Step' until you reach the 'Create Group' button, and click that one too.
15. Click on 'Policies, then 'Create Policy'. Go to the JSON tab, then click 'import managed policy', then search and import the 'S3' policy.
16. Retrieve the bucket ARN from S3, and paste it in the 'Resource' line of the JSON document, duplicating it with a ` /* ` at the end of the second line.
17. Click 'Review Policy', give it a name and description, and click 'Create Policy'.
18. Attach the policy to the previously created group by going to *Groups*, clicking on the correct group, clicking 'Attach Policy', search for and select the recently created policy, and then click 'Attach Policy'.
19. Create a user to put in the group by navigating to *Users*, clicking 'Add user', filling in a username, selecting 'Programmatic access', and then selecting 'Next'.
20. Tick the correct user, and then click through the 'Next' buttons until the end before clicking 'Create User'.
21. **Download and save the CSV file, this is important for connecting to Django.**
### *Connecting to Django*
22. Back in your workspace, run two installation commands: ` pip3 install boto3 ` and ` pip3 install django-storages `, making sure to freeze them in to the *requirements.txt* file.
23. Add storages to installed apps in *settings.py*.
24. Add the following line of code into *settings.py*:
    ```
    if 'USE_AWS' in os.environ:
        // Cache control
        AWS_S3_OBJECT_PARAMETERS = {
            'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT', // handles cache control
            'CacheControl': 'max-age-94608000',
        }

        // Bucket configuration
        AWS_STORAGE_BUCKET_NAME = <bucket_name>
        AWS_S3_REGION_NAME = <selected_region>
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID)
        AWS_SECRET_ACCESS_KEY_ID = os.environ.get('AWS_SECRET_ACCESS_KEY_ID)
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

        // For static and media files
        STATICFILES_STORAGE = 'custom_storages.StaticStorage'
        STATICFILES_LOCATION = 'static'
        DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
        MEDIAFILES_LOCATION = 'media'

    ```
24. Add all AWS variables to Heroku configuration settings (these can be found in the previously downloaded CSV file).
25. Add in the USE_AWS variable into the Heroku configuration settings, with a value of *True*.
26. Create a file called *custom_storages.py* in the root level directory of your workspace, import settings and S3Boto3Storage from storages.backends.s3boto3 at the top of the file.
27. Create classes for static storage and media storage, inheriting S3Boto3Storage, and setting the location of the static and media files.
28. Add, commit and push all changes to trigger automatic deployment to Heroku - you should be able to check everything is working so far from the build logs and in S3.
29. Create a media folder in S3, and upload all the images required on the site, ensuring to grant public read access to the images.

## Setting up email confirmations

If you want to set up automated emails with Django and Gmail, follow these steps:

1. Create a Gmail account (or sign in if you have one already), navigate to 'Account Settings', 'Other Google Account Settings', 'Security.
2. Turn on 2-step verification if it hasn't already.
3. Go to 'App passwords' within 'Security', select 'Mail' from the dropdown choices, and copy the long character password.
4. Add this password into the Heroku configuration variables as EMAIL_HOST_PASS.
5. Copy your Gmail address and add it as the EMAIL_HOST_USER to the Heroku configuration variables.

## Cloning

You're more than welcome to clone this repository is you like, just follow these steps:

1. Within this repository, navigate to the Code button and copy the URL
2. In your workspace, run a ` git clone ` command with the repository url.
3. Install the requirements by running ` pip3 install -r requirements.txt `.
4. Set environment variables as per all previous steps when setting up AWS and deploying to Heroku.
5. Migrate the models by running the following commands
    ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```
5. Load data from the fixtures files into the local database by running the following commands:
    ```
    python3 manage.py loaddata levels
    python3 manage.py loaddata angles
    python3 manage.py loaddata materials
    python3 manage.py loaddata products
    ```
6. Create a superuser so that you can access the Django admin panel by running ` python3 manage.py createsuperuser `
7. Finally, to run the server and access the site preview run ` python3 manage.py runserver `

## Credits

### Media

* The hero image found on the homepage is a free to licence photo from Unsplash, and can be found [here](https://unsplash.com/photos/iLFOK7ntmgs).

* The image of various materials in the about section of the homepage was also from Unsplash, and can be found [here](https://unsplash.com/photos/wSBL_x4R-Io).

* All product images were computer generated while the product remains in the prototype stage, and were produced by Zoe Thexton.


### Acknowledgements

**The code for this project was inspired by the Code Institute's walk through project, *Boutique Ado*. There will be similarities in how much of the backend was structured, though with significant customisation to apply it properly to this project.**

Code snippets and inspiration are detailed below, and are also included via comments in the code itself.

* My navigation bar was inspired by and amended to spec after reading [this helpful blog post](https://www.aleksandrhovhannisyan.com/blog/responsive-navbar-without-bootstrap/) by Aleksandr Hovhannisyan.

* Help generating a random product for the product detail page's recommended products section using python and django syntax was found on [this helpful article](https://books.agiliq.com/projects/django-orm-cookbook/en/latest/random.html) and tweaked to work correctly.

* Help implementing a smooth scrolling effect to the top of a page smoothly using JS was found on [this article](https://stackoverflow.com/questions/15935318/smooth-scroll-to-top).

* The wipe-up hover effect that can be seen on all 'View' or add to wishlist buttons was borrowed from [this article](https://codemyui.com/minimalistic-hover-effect-button-animations/)

A huge thank you to all the people who took part in user testing, the Code Institute's Slack community, and my mentor Aaron Sinnott for advice at various stages during development of the site.
# Slice of Pie!

## Code Institute's Milestone Project 4 - Full Stack Frameworks

Slice of Pie is the brainchild of Zoe Thexton, who produces custom triangular tables that fit seamlessly into any section of a person's living or bedroom. Designed using CAD software, the tables can be assembled by hand in a variety of sizes, types of wood, and number of shelving levels. The inspiration for this product came from the need to get creative with the limited space available in her own living room (and generally missing somewhere to put a cup of tea down as a result of this!), while the product's name comes from the triangular shape of the finished design. The only thing missing now is a means to sell this innovative product to consumers, so I offered to develop and build an e-commerce store capable of displaying the product range and accepting secure payments for orders. My aim for this project is to create a site that allows potential customers to browse all available designs or build their ideal table using a product builder, while allowing administrators to manage the products by adding, editting, or deleting SKUs when required.

This project is the fourth and final of four 'milestone' projects which are required to complete the Code Institute's diploma in full stack web development. Assessment criteria for this milestone project focuses on the ability to produce a full-stack e-commerce store with secure Stripe payments built using the Django Python framework alongside HTML, CSS and JavaScript to control a centrally-owned datatset.

You can view the live site [here](#) (site not live yet), and a link to the GitHub repository can be found [here](https://github.com/franciskershaw/slice-of-pie).

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
* [Features and Django Apps](#features-and-django-apps)
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
* Design the site in a way that makes the user’s journey from visit to checkout as pleasant as possible.
* Demonstrate my new found skills applying Django as an MVC framework in order to pass this final part of the course and obtain my Diploma.

### User Stories

#### Developer

As the software developer building the store:

1. I want to create a full-stack online shop on which users can browse and securely make purchases, and site admins have control to add, edit or delete items from the site so that I can pass this part of the course.
2. I want this project to look as aesthetically pleasing as possible so that my final project of the course is the most impressive and displays my progress.

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
3. I want to see clearly if certain products are not available so that I don’t waste my time putting them in my basket
4. I want to be able to add a product to my basket and then keep on browsing or proceed to checkout.
5. I want to be able to remove or amend the quantity of products in my basket easily so that I have the power to change my mind during my journey.
6. I would like to receive visual feedback at every stage of my journey when I perform actions, so that I am sure what I intended to do has in fact taken place.
7. I want to be able to pay securely without creating an account so that I don’t need to have my details saved.
8. I would like to register for an account so that I can save my payment details, and see my order history so that my journey on the site is made easier.
9. As an account holder, I would like to be able to save products in my favourites so that I can decide later whether to proceed with my purchase.
10. As an account holder, I would like to be able to save my delivery details so that checkout is faster during my next purchase.
11. As an account holder who has saved their details, I would like to make amends to my saved delivery address so that I can ensure this information is updated accurately.
12. At checkout, I would like the payment process to be simple and intuitive so that I don’t waste any time during my journey
13. At checkout, I would like to be sure that my details are secure during the payment process so that I don’t feel like I’m taking any risks with my money.
14. After checkout, I would like to receive an order confirmation both on my screen and in my emails so that I can review the purchase and make sure that everything occurred as it was supposed to.

## Planning and Design

### Strategy Plane

The **user stories** as detailed above were the first stage of strategising for the project and are at the forefront during every stage of development. Features that are not in service of the user stories were not considered during the creation of this project.

The **focus** of the project is:
* To create a fully functioning online store that allows the site owner to sell small bespoke tables, on which new products can be added and old products can be removed.

The **business goals** of the stakeholder are:

* To sell as many products as possible.
* Encourage users to return for future browsing and purchases.
* Have a store that can have products added to it and removed so that the product selection remains fresh.

*Therefore, a bespoke website using a full stack framework is required to meet the focus and business goals as it is the only way within my current skillset to produce an e-commerce store that is both aesthetically pleasing and contains the necessary features to allow users to browse and checkout securely, with administrators also able to manipulate the backend when needed.*

At this early stage of planning, it was time to begin researching potential competitors online to get ideas about what features and style choices are prerequisites for an e-commerce store to be successful. As I believe the product being sold is quite novel, I searched mainly for 'quirky' furniture stores that might lead me in the right direction when making decisions later on.

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
| Animation when you hover over a product     | 3          | 5
| ‘New’ label for new products                | 2          | 5
| Product builder                             | 4          | 3
| Blog                                        | 1          | 3
| Register/sign in option                     | 4          | 4
| Heart icon to save for later                | 3          | 4
| Search bar                                  | 2          | 4
| Filtering of products                       | 5          | 3
| **Total**                                   | **34**     | **46**

At this stage, I felt confident that the features I had in mind for the creation of this site would be mostly viable when compared to their relevant importance to the project. However, it was clear very early on that there were a couple of common e-commerce features that were surplus to requirements for this particular store and would not need to be included:

* Search bar - the site is essentially selling one type of product with different customisations available to it, so there is not an awful lot the user will likely want to search by. Advanced filtering and sorting is a far more logical method for the user to navigate the site.
*  Blog - this is unnecessary for the requirements of version 1 of the project, but could be an interesting feature to include on a future iteration of the site.
* 10% offer for signing up - this is slightly beyond the scope of this project, but again could well be something to pursue on a later version of the site.

### Scope Plane

Based on research and planning achieved during the strategy plane, and considering any limitations of my current coding abilities, the features I decided were critical for the completion of my user stories were as follows:

#### Required functional specifications

* 

#### Content requirements

* 

#### Nice to haves

(intro to nice to haves)

* 

### Structure Plane

(intro to structure plane)

1. **Homepage, containing:**


#### Interaction Design

* 

#### Information Architecture

* 

### Skeleton Plane

(intro to skeleton)

#### Changes from skeleton plane to final result

* 

### Surface Plane

(Intro to surface and buzzwords)

* Professional

#### Colour Scheme

(Intro to colours)

* 

(screenshot)

#### Typography

(intro to typography and reasoning behind choices)

(screenshot of fonts)

![Nunito screenshot](static/images/nunito.png)

#### Animations

### Data Model

#### Conceptual Design Phase

A basic map of how I could get my various entities to interact with each other on a conceptual level was created as the below flowchart:

(screenshot)

#### Logical Design Phase

The finalised way my collections work would together on the backend is best illustrated by the below entity relationship diagram:

(screenshot)

#### Physical Design Phase

(Explanation of the database choice and how it is used)

#### Data models

(Bullet points of the models)

## Features and Django Apps

### Existing Features

#### Consistent across all pages

* 

#### Homepage

* 

#### Login and registration

* 

#### Products/product builder

* 

#### Profile

* 

#### Bag and wishlist

* 

#### Checkout

* 

#### Profile page

* 

### Defensive design features

(Intro to section)

#### On the frontend

#### On the backend

*Custom 404 and 500 pages were created as well*

### Features left to implement

## Technologies used

### Languages and frameworks

* **HTML5:** Language used for structure and content across all pages.
* **CSS3:** Language used to style elements from the HTML pages.
* **Bootstrap:** CSS and JavaScript framework which allowed for the quick implementation of the homepage modals and the grid system which greatly improved the responsiveness of each page.
* **JavaScript:** Programming language used to add interactivity to the homepage and implement the logic required to make the game work.
* **jQuery:** JavaScript framework which helped me select and manipulate elements with greater ease than purely through JavaScript.
* **Python:** Backend language used to control the logic on the site.
* **Flask:** Python framework used to simmplify the routing and HTML templating on the site.
* **MongoDB**: Non-relational database used to store and update the information provided by users of the site.

### Additional tools

* [Amiresponsive:](http://ami.responsivedesign.is/) Used to produce the hero image in README.md and check general responsiveness of the pages.
* [dbdiagram:](https://dbdiagram.io/home) Used to create my entity relationship diagram.
* [Favicon Generator:](https://realfavicongenerator.net/) Used to create the favicon on the browser tab.
* [FontAwesome:](https://fontawesome.com/) Large database of icons which I used all over the site to add to the visual language.
* [Free Formatter:](https://www.freeformatter.com/html-formatter.html) Used to help ensure code was consistently formatted across all files.
* [Github:](https://github.com/) Version control and storage of my code.
* [Gitpod:](https://gitpod.io/) Development environment where all the code was written.
* [Google Docs:](https://docs.google.com/) Used for note taking and was where much of my readme was initially written.
* Google Developer Tools: Used for debugging and testing of responsiveness across several screen sizes. Also vital to the testing of JavaScript functions as and when they were created.
* [Google Fonts:](https://fonts.google.com/) Provided my site with the 'Nunito' font.
* [InVision:](https://www.invisionapp.com/) Used to create all of my wireframes at the beginning of the development process.
* [JSHint:](https://jshint.com/) Checked my javascript code was valid and error free.
* [PEP8Online:](http://pep8online.com/) Confirmed that my Python code complied to PEP8 standards.
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
* Use the prefix 'logic:' in any commits aimed at amending or adding in something that was specifically related to backend logic.
* Use the prefix 'test:' for any commits that were being pushed specifically to test bug fixes onto the live site.

At the time of writing, these are among my recent commit messages and illustrate the format I applied for this project:

## Testing

Please see a full report of the testing applied to this project [here.](testing.md)

## Deployment

## Setting up Amazon Web Services (AWS)

## Setting up email confirmations

## Cloning

## Credits

### Media

* 

### Acknowledgements

A huge thank you to all the people who took part in user testing, the Code Institute's Slack community, and my mentor Aaron Sinnott for advice at various stages during development of the site.
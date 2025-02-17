# Really Love Running

![Really Love Running screenshot](./documentation/images/Responsivity.PNG)

(Developers: [Charles Tack](https://github.com/CharlesTack), [Charlie Flockhart](https://github.com/charlieflockhart), [Jack Groves](https://github.com/jackgroves2024), [Ashrafur Ahmed](https://github.com/Ashrafur93))

[Link to deployed site](https://really-love-running-92dc01beda45.herokuapp.com/)

Really Love Running is a full stack website which is a practical implementation of a static website project which we 4 Developers built individually as a project earlier on in our Web Development journey as part of our training at [Code Institute](https://codeinstitute.net/).<br>
Really Love Running is designed to create a supportive community for runners of all levels. The platform allows users to share their running experiences, track their progress, and access valuable resources to improve their fitness journey. By fostering a sense of camaraderie and motivation, the website aims to encourage more people to take up running as a regular physical activity.

# Table Of Content

- [User Stories](#user-stories)
- [Design](#design)
    - [Wireframes](#wireframes)
    - [Database Schema](#database-schema)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Deployment](#deployment)
- [AI Implementation and Orchestration](#ai-implementation-and-orchestration)
- [Testing](#testing)
  - [Lighthouse](#lighthouse)
  - [HTML validation](html-validation)
  - [CSS validation](#css-validation)
  - [Contrast checker](#contrast-checker)
  - [JS analysis tool](#js-analysis-tool)
  - [Python linter](#python-linter)
- [Future Enhancements](#future-enhancements)
- [Conclusion](#conclusion)
- [Credits](#credits)


## User Stories

[(Really Love Running Project Board)](https://github.com/users/Ashrafur93/projects/8/views/1)

1. As a developer I want to use wireframes so that I can have a clear idea of the site's structure and theme. [#11](https://github.com/users/Ashrafur93/projects/8/views/1?pane=issue&itemId=97627549&issue=Ashrafur93%7Creally-love-running%7C11)
2. As a user I want to read comments, I want to read comments on location pages so that I can see what others have shared about their experiences. [#4](https://github.com/users/Ashrafur93/projects/8/views/1?pane=issue&itemId=97615324&issue=Ashrafur93%7Creally-love-running%7C4)
3. As a user I want to post comments, so that I can share my ideas and opinions with the community. [#3](https://github.com/users/Ashrafur93/projects/8/views/1?pane=issue&itemId=97609574&issue=Ashrafur93%7Creally-love-running%7C3)
4. As a user, I want to sign up and log in securely so that I can access my jogging social profile. [#1](https://github.com/users/Ashrafur93/projects/8/views/1?pane=issue&itemId=97598397&issue=Ashrafur93%7Creally-love-running%7C1)
5. As a user I want to join jogging events, so that I can participate in group runs and meet other joggers. [#2](https://github.com/users/Ashrafur93/projects/8/views/1?pane=issue&itemId=97607610&issue=Ashrafur93%7Creally-love-running%7C2)
6. As a user, I want to follow/unfollow other users, so that I can stay connected with my jogging community. [#7](https://github.com/users/Ashrafur93/projects/8/views/1?pane=issue&itemId=97619434&issue=Ashrafur93%7Creally-love-running%7C7)
7. As a user, I want to log my jogs (date, duration, distance), so that I can track my progress. [#6](https://github.com/users/Ashrafur93/projects/8/views/1?pane=issue&itemId=97619034&issue=Ashrafur93%7Creally-love-running%7C6)
8. As a returning user, I want to edit my profile, so that I can update my information. [#5](https://github.com/users/Ashrafur93/projects/8/views/1?pane=issue&itemId=97617295&issue=Ashrafur93%7Creally-love-running%7C5)
9. As a user, I want to see a leaderboard of top runners so that I can compare my performance with others. [#8](https://github.com/users/Ashrafur93/projects/8/views/1?pane=issue&itemId=97622159&issue=Ashrafur93%7Creally-love-running%7C8)
10. As a user, I want to see my ranking, so that I know where I stand. [#9](https://github.com/users/Ashrafur93/projects/8/views/1?pane=issue&itemId=97622352&issue=Ashrafur93%7Creally-love-running%7C9)

## Design

### Wireframes

#### Mobile

<details><summary>Home</summary>
<img src="./documentation/images/Home - Mobile.PNG">
</details>
<details><summary>Meetup</summary>
<img src="./documentation/images/Meetup - Mobile.PNG">
</details>
<details><summary>Profile</summary>
<img src="./documentation/images/Profile - Mobile.PNG">
</details>
<details><summary>Gallery</summary>
<img src="./documentation/images/Gallery - Mobile.PNG">
</details>
<details><summary>Signup</summary>
<img src="./documentation/images/Signup - Mobile.PNG">
</details>
<details><summary>Login</summary>
<img src="./documentation/images/Login - Mobile.PNG">
</details>
<details><summary>Logout</summary>
<img src="./documentation/images/Logout - Mobile.PNG">
</details>

#### Tablet

<details><summary>Home</summary>
<img src="./documentation/images/Home - Tablet.PNG">
</details>
<details><summary>Meetup</summary>
<img src="./documentation/images/Meetup - Tablet.PNG">
</details>
<details><summary>Profile</summary>
<img src="./documentation/images/Profile - Tablet.PNG">
</details>
<details><summary>Gallery</summary>
<img src="./documentation/images/Gallery - Tablet.PNG">
</details>
<details><summary>Signup</summary>
<img src="./documentation/images/Signup - Tablet.PNG">
</details>
<details><summary>Login</summary>
<img src="./documentation/images/Login - Tablet.PNG">
</details>
<details><summary>Logout</summary>
<img src="./documentation/images/Logout - Tablet.PNG">
</details>

#### Desktop

<details><summary>Home</summary>
<img src="./documentation/images/Home - Mobile.PNG">
</details>
<details><summary>Meetup</summary>
<img src="./documentation/images/Meetup - Desktop.PNG">
</details>
<details><summary>Profile</summary>
<img src="./documentation/images/Profile - Desktop.PNG">
</details>
<details><summary>Gallery</summary>
<img src="./documentation/images/Gallery - Desktop.PNG">
</details>
<details><summary>Signup</summary>
<img src="./documentation/images/Signup - Desktop.PNG">
</details>
<details><summary>Login</summary>
<img src="./documentation/images/Login - Desktop.PNG">
</details>
<details><summary>Logout</summary>
<img src="./documentation/images/Logout - Desktop.PNG">
</details>

### Database Schema

The entity relationship diagram was built using [DBDiagram](https://dbdiagram.io/home):

<details><summary>Database Schema screenshot</summary>
<img src="./documentation/images/ERD.PNG">
</details>

## Features

- **User Profiles**: Each user can create a profile to track their running stats, set goals, and share their achievements with the community.
- **Community chat**: A space for users to discuss various topics related to running, including training tips and run preparation.
- **Event Calendar**: Users can find and participate in local running events, runs and meetups.

## Technology Stack

- **Frontend**: HTML, CSS, JavaScript, and Bootstrap for responsive design.
- **Backend**: Django framework with Python for robust and scalable web application development.
- **Database**: PostgreSQL for reliable data storage and management.
- **Media**: Cloudinary for image hosting.

## Deployment

- **Platform:** [Heroku](https://www.heroku.com/)
- **High-Level Deployment Steps:** 
  1. Clone the repository
  2. Set up the Heroku environment with a PostgreSQL database.
  3. Configure environment variables for sensitive data (e.g., secret keys).
  4. Deploy using Heroku GitHub integration.
- **Verification and Validation:**
  - Tested the deployed application against the development environment for consistent functionality and design.
  - Verified accessibility using tools such as Lighthouse and manual testing.
- **Security Measures:**
  - Sensitive data is stored in environment variables.
  - DEBUG mode is disabled in the production environment to enhance security.

## Testing

### Lighthouse
  <details><summary>Home</summary>
  <img src="./documentation/images/Lighthouse - Home.PNG">
  </details>

  <details><summary>Meetup</summary>
  <img src="./documentation/images/Lighthouse - Meetup.PNG">
  </details>

  <details><summary>Gallery</summary>
  <img src="./documentation/images/Lighthouse - Gallery.PNG">
  </details>

  <details><summary>Profile</summary>
  <img src="">
  </details>

   <details><summary>Signup</summary>
  <img src="">
  </details>

### HTML validation
  <details><summary>Index</summary>
  <img src="/documentation/images/HTML_Validation/Home_Page_HTML_Validation.png">
  </details>

  <details><summary>Gallery</summary>
  <img src="/documentation/images/HTML_Validation/Gallery_HTML_Validation.png">
  </details>

  <details><summary>Profiles</summary>
  <img src="/documentation/images/HTML_Validation/Profiles_HTML_Validation.png">
  </details>

  <details><summary>Sign In</summary>
  <img src="/documentation/images/HTML_Validation/Sign_In_HTML_Validation.png">
  </details>

  <details><summary>Sign Out</summary>
  <img src="/documentation/images/HTML_Validation/Sign_Out_HTML_Validation.png">
  </details>

  <details><summary>Sign Up</summary>
  <img src="/documentation/images/HTML_Validation/Sign_Up_HTML_Validation.png">
  </details>

### CSS validation
  <details><summary>CSS</summary>
  <img src="/documentation/images/CSS_Validation/CSS_Validated.png">
  </details>

### Python linter
#### Home
  <details><summary>Apps</summary>
  <img src="/documentation/images/Python_Validation/Home/Home_Apps_py.png">
  </details>

  <details><summary>Urls</summary>
  <img src="/documentation/images/Python_Validation/Home/Home_urls_py.png">
  </details>

  <details><summary>Views</summary>
  <img src="/documentation/images/Python_Validation/Home/Home_views_py.png">
  </details>

#### Jogging Post
  <details><summary>Admin</summary>
  <img src="/documentation/images/Python_Validation/Jogging_post/Jogging_post_admin_py.png">
  </details>

  <details><summary>Apps</summary>
  <img src="/documentation/images/Python_Validation/Jogging_post/Jogging_post_apps_py.png">
  </details>

  <details><summary>Models</summary>
  <img src="/documentation/images/Python_Validation/Jogging_post/Jogging_post_models_py.png">
  </details>

  <details><summary>Urls</summary>
  <img src="/documentation/images/Python_Validation/Jogging_post/Jogging_post_urls_py.png">
  </details>

  <details><summary>Views</summary>
  <img src="/documentation/images/Python_Validation/Jogging_post/Jogging_post_views_py.png">
  </details>

#### Profiles
  <details><summary>Admin</summary>
  <img src="/documentation/images/Python_Validation/Profiles/Profiles_admin_py.png">
  </details>

  <details><summary>Apps</summary>
  <img src="/documentation/images/Python_Validation/Profiles/Profiles_apps_py.png">
  </details>

  <details><summary>Forms</summary>
  <img src="/documentation/images/Python_Validation/Profiles/Profiles_forms_py.png">
  </details>

  <details><summary>Models</summary>
  <img src="/documentation/images/Python_Validation/Profiles/Profiles_models_py.png">
  </details>

  <details><summary>Urls</summary>
  <img src="/documentation/images/Python_Validation/Profiles/Profiles_urls_py.png">
  </details>

  <details><summary>Views</summary>
  <img src="/documentation/images/Python_Validation/Profiles/Profiles_views_py.png">
  </details>

#### Really Love Running 
  <details><summary>Urls</summary>
  <img src="/documentation/images/Python_Validation/Really_Love_Running/Really_love_running_urls_py.png">
  </details>

  <details><summary>Asgi</summary>
  <img src="/documentation/images/Python_Validation/Really_Love_Running/Really_love_running_asgi_py.png">
  </details>

  <details><summary>Wsgi</summary>
  <img src="/documentation/images/Python_Validation/Really_Love_Running/Really_love_running_wsgi_py.png">
  </details>

### Manual testing

| Location | Feature            | Expected Outcome                                             | Pass/Fail | Notes               |
| -------- | ------------------ | ------------------------------------------------------------ | --------- | ------------------- |
| Home     | Navbar             | Clicking on home takes the user to home                      | Pass      |                     |
| Home     | Navbar             | Clicking on logo takes the user to home                      | Pass      |                     |
| Home     | Navbar             | Clicking on Gallery takes the user to the gallery page       | Pass      |                     |
| Home     | Navbar             | Clicking on Profile takes the user to the profile page       | Pass      |                     |
| Home     | Navbar             | Clicking on logout takes the user to the sign out page       | Pass      |                     |
| Home     | Navbar             | Register link only appears when user logged out              | Pass      |                     |
| Home     | Navbar             | Login link only appears when user logged out                 | Pass      |                     |
| Home     | Navbar             | Clicking on Regsiter takes the user to register page         | Pass      |                     |
| Home     | Navbar             | Logout link only appears when user logged in                 | Pass      |                     |
| Home     | Navbar             | Clicking on Login takes the user to Log In page              | Pass      |                     |
| Home     | Navbar             | Admin link only appears to superusers                        | Pass      |                     |
| Home     | Navbar             | Clicking on admin link takes the superuser to the admin page | Pass      |                     |
| Home     | Navbar             | Links have hover effect (underline)                          | Pass      |                     |
| Home     | Navbar             | Clicking on link consistently gives active indicator         | Pass      |                     |
| Home     | Navbar             | Stays at top when scrolling                                  | Pass      |                     |
| Home     | Navbar             | Login status appears top right                               |       |  |
| Home     | Meet Up Cards      | Cards dim when hovered over                                  | Pass      |                     |
| Home     | Meet Up Cards      | Cards take you to the right page when clicked                | Pass      |                     |
| Home     | Footer             | Github links work correctly                                  | Pass      |                     |
| Logout   | Logout             | User is logged out when clicked on Sign Out button           | Pass      |                     |
| Gallery  | Responsive images  | Images scale appropriately on different device sizes         | Pass      |                     |
| Register | Form validation    | Form validation matches rules on the screen                  | Pass      |                     |
| Register | Accepts new users  | New users are accepted on valid form submission              | Pass      |                     |
| Login    | Form validation    | Access only allowed to registered users                      | Pass      |                     |
| Register | Login              | User logged in on valid username and password                | Pass      |                     |
| Home     | Responsiveness     | Screen correct at 320px (Mobile S)                           | Pass      |                     |
| Home     | Responsiveness     | Screen correct at 375px (Mobile M)                           | Pass      |                     |
| Home     | Responsiveness     | Screen correct at 425px (Mobile L)                           | Pass      |                     |
| Home     | Responsiveness     | Screen correct at 768px (Tablet)                             | Pass      |                     |
| Home     | Responsiveness     | Screen correct at 1024px (Laptop)                            | Pass      |                     |
| Home     | Responsiveness     | Screen correct at 1440px (Laptop L)                          | Pass      |                     |
| Home     | Responsiveness     | Screen correct at 2560px (4K)                                | Pass      |                     |
| Meet up  | Comment Logged out | Logged out user cannot post a comment                        | Pass      |                     |
| Meet up  | Comment Logged in  | Logged in user can post a comment                            | Pass      |                     |
| Meet up  | Comment Logged in  | Logged in user can edit their own comment                    | Pass      |                     |
| Meet up  | Comment            | Nobody can edit or delete anyone else's comments             | Pass      |                     |
| Meet up  | Comment Logged in  | Logged in user can delete their own comment                  | Pass      |                     |
| Gallery  | Responsiveness     | Screen correct at 320px (Mobile S)                           | Pass      |                     |
| Gallery  | Responsiveness     | Screen correct at 375px (Mobile M)                           | Pass      |                     |
| Gallery  | Responsiveness     | Screen correct at 425px (Mobile L)                           | Pass      |                     |
| Gallery  | Responsiveness     | Screen correct at 768px (Tablet)                             | Pass      |                     |
| Gallery  | Responsiveness     | Screen correct at 1024px (Laptop)                            | Pass      |                     |
| Gallery  | Responsiveness     | Screen correct at 1440px (Laptop L)                          | Pass      |                     |
| Gallery  | Responsiveness     | Screen correct at 2560px (4K)                                | Pass      |                     |
| Profile  | Profile Info       | User can add and edit profile data including images          | Pass      |                     |
| Profile  | Profile Delete     | User can delete their profile and user records               | Pass      |                     |
| Profile  | Responsiveness     | Screen correct at 320px (Mobile S)                           | Pass      |                     |
| Profile  | Responsiveness     | Screen correct at 375px (Mobile M)                           | Pass      |                     |
| Profile  | Responsiveness     | Screen correct at 425px (Mobile L)                           | Pass      |                     |
| Profile  | Responsiveness     | Screen correct at 768px (Tablet)                             | Pass      |                     |
| Profile  | Responsiveness     | Screen correct at 1024px (Laptop)                            | Pass      |                     |
| Profile  | Responsiveness     | Screen correct at 1440px (Laptop L)                          | Pass      |                     |
| Profile  | Responsiveness     | Screen correct at 2560px (4K)                                | Pass      |                     |
| Logout   | Responsiveness     | Screen correct at 320px (Mobile S)                           | Pass      |                     |
| Logout   | Responsiveness     | Screen correct at 375px (Mobile M)                           | Pass      |                     |
| Logout   | Responsiveness     | Screen correct at 425px (Mobile L)                           | Pass      |                     |
| Logout   | Responsiveness     | Screen correct at 768px (Tablet)                             | Pass      |                     |
| Logout   | Responsiveness     | Screen correct at 1024px (Laptop)                            | Pass      |                     |
| Logout   | Responsiveness     | Screen correct at 1440px (Laptop L)                          | Pass      |                     |
| Logout   | Responsiveness     | Screen correct at 2560px (4K)                                | Pass      |                     |
| Register | Responsiveness     | Screen correct at 320px (Mobile S)                           | Pass      |                     |
| Register | Responsiveness     | Screen correct at 375px (Mobile M)                           | Pass      |                     |
| Register | Responsiveness     | Screen correct at 425px (Mobile L)                           | Pass      |                     |
| Register | Responsiveness     | Screen correct at 768px (Tablet)                             | Pass      |                     |
| Register | Responsiveness     | Screen correct at 1024px (Laptop)                            | Pass      |                     |
| Register | Responsiveness     | Screen correct at 1440px (Laptop L)                          | Pass      |                     |
| Register | Responsiveness     | Screen correct at 2560px (4K)                                | Pass      |                     |
| Login    | Responsiveness     | Screen correct at 320px (Mobile S)                           | Pass      |                     |
| Login    | Responsiveness     | Screen correct at 375px (Mobile M)                           | Pass      |                     |
| Login    | Responsiveness     | Screen correct at 425px (Mobile L)                           | Pass      |                     |
| Login    | Responsiveness     | Screen correct at 768px (Tablet)                             | Pass      |                     |
| Login    | Responsiveness     | Screen correct at 1024px (Laptop)                            | Pass      |                     |
| Login    | Responsiveness     | Screen correct at 1440px (Laptop L)                          | Pass      |                     |
| Login    | Responsiveness     | Screen correct at 2560px (4K)                                | Pass      |                     |

## Future Enhancements

- **Mobile App**: Development of a mobile application to provide users with on-the-go access to the platform.
Future developments can include:
- **User Posts**: The ability for users to post custom meetup cards which other users can interact with.
- **Running Partners/Groups**: A buddy system where users can be matched up with each other depending on their running goals and preferences. An advanced version of this would pair a user with an experienced runner.
- **Maps Integration**: A Google API map showing popular running routes and nearby facilities such as water stations and restrooms.
- **Moderator Powers**: Enhanced moderation tools to ensure a safe and supportive community by reviewing posts before publication.
- **Advanced Analytics**: Integration of advanced analytics to provide users with deeper insights into their running performance.
- **Social Media Integration**: Allow users to share their progress and achievements on social media platforms to inspire others.
- **Ranking System**: Allow users to compete with each other to rise in the on-site ranking leaderboards.

## Conclusion

Really Love Running is more than just a website; it's a community dedicated to promoting a healthy and active lifestyle through running. By providing a platform for runners to connect, share, and learn, we aim to make running an enjoyable and accessible activity for everyone.

## Credits

- [Microsoft Copilot](https://copilot.microsoft.com/) was used for AI tech support.
- [Remaker](https://remaker.ai/face-swap-free/) and [Fotor](https://www.fotor.com/apps/swapper/) were used to create face-swapped images.
- README documentation ideas and content were from [Code Institute's template](https://github.com/Code-Institute-Org/html-css-project/blob/main/full-stack-capstone-readme.md) and DarrachBarneveld's project, [CoolCoders-PP4](https://github.com/DarrachBarneveld/CoolCoders-PP4).

- Testing and validation was done using the following:
  - [Google Lighthouse](https://developer.chrome.com/docs/lighthouse/overview)
  - [Python linter](https://pep8ci.herokuapp.com/)
  - [HTML validation](https://validator.w3.org/)
  - [CSS validation](https://jigsaw.w3.org/css-validator/)
  - [JS analysis tool](https://jshint.com/)
 
- Images were taken from the following websites:
  - https://www.parkregisbirmingham.co.uk/blog/best-enjoy-birminghams-canals/
  - https://www.birmingham2022.com/venues/alexander-stadium
  - https://www.parkrun.org.uk/cannonhill/
  - https://www.birminghammail.co.uk/news/midlands-news/famous-birmingham-spot-everybody-knows-29936838
  - https://visitbirmingham.com/listing/run-of-a-kind/140870101/
  - https://commons.wikimedia.org/wiki/File:Profile_avatar_placeholder_large.png
  - https://visitbirmingham.com/listing/run-of-a-kind/140870101/
  - [Homepage, Gallery and Signup images were originally from Code Institute's Love Running project](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LRFX101+6/courseware/e805068059af42af87681032aa64053f/92a91cf7fcee4361a2af651b7827a341/)
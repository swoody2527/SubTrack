# SubTrack: Lightweight Subscription Tracker with GUI

**Video Demo:** [Watch SubTrack in Action](https://youtu.be/IQ3UfdIb_cM)

## Description

SubTrack was created with the goal of providing users with a local, lightweight GUI application to manage their running subscription plans. Built on an SQLite3 database, SubTrack allows users to track subscription details, including the name, price, start date, renewal period, and the next billing date. The application seamlessly transitions from a terminal-based interface to an intuitive graphical user interface (GUI) developed with Tkinter.

### Features and Implementation

- **Subscription Class (Sub()):** Utilizes Object-Oriented Programming (OOP) principles to represent subscriptions, ensuring uniform data storage and validation for name, price, start date, and renewal period.

- **Terminal-Based Functionality:** Initially designed to function in the terminal window, SubTrack accepts user input to navigate functions, using PrettyTables library for visually enhanced display of subscription information.

- **GUI Transition:** Seamlessly integrates a user-friendly GUI using Tkinter, allowing users to interact with buttons for viewing subscriptions, adding new ones, and deleting existing subscriptions.

- **Database Operations:** Employs SQLite3 database operations to add, delete, and view subscriptions. Implements error handling and input validation to maintain data integrity.

- **Next Billing Date Calculation:** Utilizes datetime module to calculate the next billing date based on the start date and renewal period, ensuring accurate tracking of subscription charges.

- **Visual Appeal:** Strives for a balance between functionality and visual appeal, with potential for further enhancements in future updates.

### User Interface (GUI)

- **View Subscriptions:** Presents subscription details in a tabular format with labels and input boxes, enhancing readability and user experience. Dates are reformatted for a user-friendly display.

- **Add Subscription:** Collects user input via input boxes, creating a new subscription instance and inserting it into the database upon submission. Implements lambda command for efficient button functionality.

- **Delete Subscription:** Utilizes a confirmation window, displaying subscription details and prompting users to confirm deletion. Ensures user verification before removing a subscription from the database.

## Future Enhancements

SubTrack is an ongoing project with the potential for further improvements:

- **Visual Refinement:** Explore enhanced visual elements, transitions, and themes to elevate the overall user interface.

- **Framework Exploration:** Investigate alternative GUI frameworks for improved design flexibility and aesthetics.

- **Feature Expansion:** Consider adding features such as notifications for upcoming billing dates, data backup options, and export functionalities.

## Acknowledgements

SubTrack represents a significant learning journey, integrating terminal functionality into a GUI application and applying OOP principles for robust data management. Continued updates and enhancements are planned to provide users with an even more streamlined and visually appealing subscription tracking experience.


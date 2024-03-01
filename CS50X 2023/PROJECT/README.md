# AniTime
### Video Demo: https://youtu.be/fYnV1A8Kbcc

AniTime is a browser extension that aims to enhance your anime-watching experience by presenting the day's anime schedule in a convenient popup.

Gone are the days when you would keep multiple tabs open to check for schedules. AniTime saves precious time and space by providing a seamless way to view the day's schedule with just a click of a button.

## Project

For my final project in CS50, I figured I should try making something that I would definitely use during my daily life. I chose to make a **Browser Extension**.

It was actually a friend of mine who suggested making an anime schedule extension. We both are avid anime watchers and watch seasonal anime. A person might decide to watch multiple animes per season and, with that, need to keep track of airing schedules so that they don't miss out on any episodes.

Some days, the anime they plan to watch might not air that day, so it would be a waste of time to visit their streaming website only to find out an episode has not aired yet or has been delayed until next week.

My extension aims to cut all that out by allowing the user to check the schedule beforehand to see if their anime has aired that day yet.

### Languages used:
- Javascript
- CSS
- HTML

## Process:

### Researching about API : —
The first thing I did was research how I could get data and display it because I certainly can't research the schedules for each and every anime. I have found plenty of anime schedule websites and wondered how I could borrow their data and display it on my extension.

The solution I came up with was API.

API stands for  **Application Programming Interface** and is a set of rules and protocols that allow two software programs to communicate with each other and **exchange data**.

This involves a request and response cycle, where the party **requesting** is called the **Client** and the party **responding** to the request is called the **Server**. The Client needs to make a request to a Server's **endpoint** in order to get the data they need. An endpoint is the digital location where an API receives the request about a resource on its server. It's usually in the form of a URL.

So from then on, I had to start looking for anime schedule websites or databases that offer API endpoints for my project.

### Making the layout and UI with HTML : —
After researching how I would get the data, I went ahead and started designing the layout of my extension with HTML. Most anime streaming websites have a schedule table that displays the anime schedules, so I drew inspiration from their designs for my first pass. The table would be the main point of the layout because that is where the data will be displayed.

The layout consists of two parts:
1. The **main table**, where the anime schedule is displayed.

2. The **date section**, which displays the current date and has two buttons for the user to navigate the previous and next schedules.

The table in my first pass looked similar to the table in [**subsplease.org**](https://subsplease.org). After playing around with CSS styling, I was able to bend the designs to my will and eventually came up with my own design, which is how it looks now.

Then I created the date section, which displayed the date with buttons allowing users to switch to the previous date or next date to check the schedule for that day.


### Requesting API : —
After having the table ready, I now needed to tackle the main obstacle: the data.

#### API Source:
- **AniList** [ https://anilist.gitbook.io/anilist-apiv2-docs/ ]

    After a lot of searching, I finally settled on utilizing the API offered by [**AniList**](https://anilist.co/). AniList is a platform with an extensive anime database that allows users to create and personalize anime and manga lists to keep track of. AniList also has a scheduling website called [**AniChart**](https://anichart.net/) which displays each season's airing schedule.

    AniList uses GraphQL API, which is a query language that prioritizes providing the client with exactly the data they request and no more. You're basically able to filter what you need.

    I was also happy to see that AniList has provided extensive, detailed documentation on their API references and how we can use GraphQL. It was very beginner-friendly and easy to work with.

The process of requesting data first requires me to structure a query to filter out what I need. My extension presents the anime that airs on the current day, so I created variables that hold the current date. The variables that the query uses are the timestamps for the start of the day (current day 00:00:00) and the end of the day (current day 23:59:59).

I had to create a function — `timestamps()` — that would convert the date into the UNIX time format, which is the number of seconds since January 1st, 1970 00:00:00 UTC, since that is the querying format that the reference uses. The function takes the current date and extracts the day, month, and year individually. Then it converts them into the timestamp format and adds the times of the start or end of the day, respectively.

The function that fetches the data — `fetchAnimeSchedule(startOfDayTimestamp, endOfDayTimestamp)` — then accepts the variables and queries for the data within those parameters. The function returns the anime titles, the episodes that air that day, and the time they air — all of the things I need to display on my extension.


### Handling the data : —

The array of data is inputted into the `handleData(data)` function, which proceeds to populate the popup.

The popup looks like a table that is separated by hours and ordered by time. Inside the table are cells with the titles of the animes, the episode numbers beneath them, and the time of release on top of the cells.

The data is first sorted into tables by hours. Then the tables are created via javascript; the headers are first created to display the hours; and then, with a loop, the body is created. The relevant data is extracted from the data pack received, including the title, episode number, and time. Then the table rows are created to be populated by the data.

The time row is first created to display the time the anime airs, then right below it, the anime row is created to display the anime title and episode. The row with the anime information is divided with the `<div></div>` tag, so they both display properly in the row.

There is also a circle bullet inside the cells that indicates the airing titles. The circles are initially blank, with only the outline of the circle. There is a function — `airing()` — that finds the airing episodes and fills the bullet. The function finds all the hour tables, iterates through the time cells, and compares them to the current day. If it finds any cells that are equal to or less than the current day, then the bullets are filled, letting users know that the episode has been released and is available for watching.

### Extras and buttons : —

The popup has a section on top that displays the user's local day and date. On the sides of this section, there are buttons that lead the user to the previous or next day's schedule, allowing the user to check the schedules for those days. This is achieved by creating a variable that holds the date.

Initially, the variable will hold the current day (today), and when a button is clicked, the variable holding the current day will instead be holding the `current day - 1` or `current day + 1`, essentially setting the current day as that day. The button will then run the functions that display the date and the function that fetches the data to fetch the data for the "current day".

## Future Implementations

1. **Manga Schedule**
    - Option to view release schedules for manga

2. **Themes**
    - Dark mode (currently default)
    - Light mode

3. **Bookmark Feature**
    - Alerts the user about airing episodes
    - Additional feature to selectively display bookmarked animes

4. **Search bar**
    - Allows users to quickly search for an anime to promptly bookmark or access the airing schedule

5. **Timezone Customization**
    - Allows users to choose their preferred timezone
    -  *Currently utilizes users' local timezone by default*

6. **Time Format Customization**
    - 12-hour format (currently default)
    - 24-hour format

7. **Language Preferences for Anime Titles**
    - Option to display titles in:
        - Romaji
        - English

8. **Priority for Currently Airing Episodes**
    - A feature to prioritize and display all currently airing episodes at the top

## Personal Comments

This project was very fun and exciting, and I was surprised by how much I can do with only this level of CS knowledge. However, I will admit that my designs are not the best. The colors are hardcoded, and the way the data is handled may not be the most efficient. But I am happy with how it turned out regardless. It works after all.

This extension is only supposed to display the anime schedule, but so many ideas are now filling my head with ways I could improve the UI and functions. I will definitely keep working on this project to improve it. Even though it gave me a hard time, the time spent on this made me grow attached to it. I have a feeling it will become something bigger in the future, at least for me.

I don't plan on publishing this publicly yet because I don't think it's on an acceptable level yet, but maybe I'll consider publishing it privately for my friends and myself. Once I improve it to a satisfactory level, I will definitely publish this for all my fellow anime watchers to use.

CS50 has allowed me to dip into the computer science world and has allowed me to take matters into my own hands, creating whatever I need by myself. I plan to continue to explore this path and find my place within this amazing place of freedom. Thank you for this chance; this was CS50!


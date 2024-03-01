document.addEventListener('DOMContentLoaded', () => {
  let dateHeader = document.getElementById('date_header');
  let dayHeader = document.getElementById('day_header');
  let previous = document.getElementById('previous'); // button
  let next = document.getElementById('next'); // button
  let currentDate = new Date();
  let use24HourFormat = false; // Variable that will switch to 24 hour or 12 hour format (TO BE IMPLEMENTED)
  let titleEnglish = false; // Variable that allows user to switch to english title or romaji title (TO BE IMPLEMENTED)
  let airingCurrent = true; // (TO BE IMPLEMENTED)

  dateAndDay();
  setInterval(dateAndDay, 60000);

  fetchDataFromBackground()
  .then(data => {
    handleData(data);

    setTimeout(scrollDown, 1000);
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });


  // Function that formats date into '1 Jan 2023'
  function formatDateString(date) {
    // Define format
    let format = { day: 'numeric', month: 'short', year: 'numeric' };
    // Get date in format
    let formattedDate = new Date(date).toLocaleDateString(undefined, format);

    // Split date into day, month, year
    let day = new Date(date).getDate();
    let month = formattedDate.split(' ')[0];
    let year = formattedDate.split(' ')[2];

    return { day, month, year };
  }

  // Function that updates the date and day display
  function dateAndDay() {
    // Check if found
    if (!dateHeader || !dayHeader) {
      return; // Exit this function if not
    }

    // Get formatted date
    let formattedDate = formatDateString(currentDate);
    // Get day
    let today = new Date(currentDate).toLocaleDateString(undefined, { weekday: 'long' });

    dateHeader.innerHTML = `${formattedDate.day} ${formattedDate.month} ${formattedDate.year}`;
    dayHeader.innerHTML = today;
  }

  // -------------------------------------------------------------------------------------------------------
  // Function that formats date into UNIX timestamp (the format used to filter the search for the schedule)
  function timestamps() {
    // Extract year, month, and day from current date
    let year = currentDate.getFullYear();
    let month = currentDate.getMonth() + 1;
    let day = currentDate.getDate();

    let monthNumeric = month < 10 ? `0${month}` : `${month}`;
    let dayNumeric = day < 10 ? `0${day}` : `${day}`;

    // Convert to UNIX
    startOfDayTimestamp = new Date(`${year}-${monthNumeric}-${dayNumeric}T00:00:00Z`).getTime() / 1000;
    endOfDayTimestamp = new Date(`${year}-${monthNumeric}-${dayNumeric}T23:59:59Z`).getTime() / 1000;

    return {startOfDayTimestamp, endOfDayTimestamp};
  }

  function fetchDataFromBackground() {
    const { startOfDayTimestamp, endOfDayTimestamp } = timestamps();

    return new Promise((resolve, reject) => {
      const port = chrome.runtime.connect({ name: 'popup' });

      port.postMessage({
          action: 'fetchData',
          startOfDayTimestamp,
          endOfDayTimestamp
      });

      port.onMessage.addListener((response) => {
          if (response.success) {
              resolve(response.data);
          } else {
              reject(new Error(response.error));
          }
          port.disconnect();
      });
  });
  }


  function handleData(data) {
    console.log('Received data:', data);
    let airingSchedules = data.data.Page.airingSchedules;

    console.log(airingSchedules);

    // Divide data into groups by hours
    let groups = {};
    for (let i = 0; i < airingSchedules.length; i++){
      let schedule = airingSchedules[i];
      let airingTime = new Date(schedule.airingAt * 1000);
      let hour = airingTime.getHours();

      if (!groups[hour]){
        groups[hour] = [];
      }

      groups[hour].push(schedule);
    }

    // Get div that will display schedule
    let upcomingTable = document.getElementById('upcoming-table');

    if (!upcomingTable){
      return; // If id not found, exit from this function
    }

    upcomingTable.innerHTML = ''; // Clear contents

    // Create tables for each hour
    for (let hour in groups){

      let hourTable = document.createElement('table');
      hourTable.id = 'upcoming-episodes';
      hourTable.className = 'anime-table';

      // Create thead and tr for the hour header
      let thead = document.createElement('thead');
      let theadTr = document.createElement('tr');
      let theadTd = document.createElement('td');
      theadTd.colSpan = 3;
      theadTd.className = 'upcoming-time';

      // Displaying hour in header
      let displayHour = use24HourFormat ? hour : (hour % 12) || 12;
      let amORpm = use24HourFormat ? '' : (hour < 12 ? 'AM' : 'PM');
      let timeTagDiv = document.createElement('div');
      timeTagDiv.className = 'time-tag';
      timeTagDiv.textContent = `${displayHour}:00 ${amORpm}`;

      theadTd.appendChild(timeTagDiv);
      theadTr.appendChild(theadTd);
      thead.appendChild(theadTr);
      hourTable.appendChild(thead);

      // Create tbody
      let tbody = document.createElement('tbody');
      hourTable.appendChild(tbody);

      // Loop to create and populate tables
      let schedulesForHour = groups[hour];
      for (let i = 0; i < schedulesForHour.length; i++) {
        // Define variables
        let schedule = schedulesForHour[i];
        let animeTitleEng = schedule.media.title.english; // Title in English
        let animeTitleRomaji = schedule.media.title.romaji; // Title in Romagi
        let episode = schedule.episode; // Episode
        let airingTime = new Date(schedule.airingAt * 1000); // Time

        let anime = document.createElement('tr');
        anime.className = 'anime-container';

        // Create time row
        let timeRow = document.createElement('tr');
        let timeCell = document.createElement('td');
        timeCell.colSpan = 3;
        timeCell.className = 'time-cell';

        // Populate time row
        let hour = airingTime.getHours();
        let minute = airingTime.getMinutes();
        let displayHour = use24HourFormat ? hour : ((hour + 11) % 12) + 1;  // Convert to 12-hour format
        let amOrPm = hour < 12 ? 'AM' : 'PM';
        let formattedTime = use24HourFormat ? `${hour.toString().padStart(2, '0')}:${minute.toString().padStart(2, '0')}` : `${displayHour}:${minute.toString().padStart(2, '0')} ${amOrPm}`;

        timeCell.textContent = formattedTime;
        timeRow.appendChild(timeCell);
        anime.appendChild(timeRow);
        tbody.appendChild(anime);

        // Create anime row
        // Bullets
        let animeRow = document.createElement('tr');
        let bulletCell = document.createElement('td');
        bulletCell.className = 'bullet-cell';
        let bulletDiv = document.createElement('div');
        bulletDiv.innerHTML = '<span class="material-icons-outlined">circle</span>';

        bulletCell.appendChild(bulletDiv);
        animeRow.appendChild(bulletCell);

        // Create anime info cell
        let animeInfoCell = document.createElement('td');
        animeInfoCell.className = 'anime-info-cell';
        let animeTitleDiv = document.createElement('div');

        // Display title in English or Romaji
        let title = titleEnglish && animeTitleEng ? animeTitleEng : animeTitleRomaji;
        title = title || animeTitleRomaji;

        animeTitleDiv.className = 'anime-title';
        animeTitleDiv.textContent = title;

        let animeEpDiv = document.createElement('div');
        animeEpDiv.className = 'anime-ep';
        animeEpDiv.textContent = `Ep ${episode}`;

        animeInfoCell.appendChild(animeTitleDiv);
        animeInfoCell.appendChild(animeEpDiv);
        animeRow.appendChild(animeInfoCell);
        anime.appendChild(animeRow);
        tbody.appendChild(anime);
      }

      upcomingTable.appendChild(hourTable);

    }

    // Call function to fill in airing episodes
    if (airingCurrent === true){
      airing();
      setInterval(airing, 60000); // make it automatic
    }

  }


// ---------------------------------------------------------------------------------------------

  function airing(){
    // Convert the real current date to UNIX time seconds
    today = new Date / 1000;
    let tables = document.querySelectorAll('.anime-table'); // Get all tables

    if (!tables) {
      console.log('No tables found');
      return;
    }

    tables.forEach((table) => { // For each table
      table.querySelectorAll('.anime-container').forEach((animeContainer) => { // For each container
        let timeCell = animeContainer.querySelector('.time-cell'); // Get time
        let bulletCell = animeContainer.querySelector('.bullet-cell'); // Get bullet

        if (!timeCell) {
          console.log('No time cell found for this anime container:', animeContainer);
          return;
        }

        // Get airingTime in UNIX
        let airingTime = animeTime(timeCell);

        if (airingTime <= today) { // All animes airing less than or equal to the current date is considered airing
          let bulletIcon = bulletCell.querySelector('span');
          if (bulletIcon) {
            bulletIcon.innerHTML = '<span class="material-icons">circle</span>'; // Change circle outline to filled
          }
        }
      });
    });
  }

  // Calculates UNIX time for timeCell (Logic: "currentDate" is the day and date when the anime was released, combine with time from timcell)
  function animeTime(timeCell){
    // Getting current day to convert to UNIX
    let day = currentDate.getDate();
    let month = currentDate.getMonth();
    let year = currentDate.getFullYear();

    // Convert date to UNIX
    let date = new Date(year, month, day).getTime() / 1000;

    let timeString = timeCell.textContent.trim(); // Extract time from timeCell
    let airingTime; // Variable

    // If airingTime format is 12 hour
    if (use24HourFormat === false) {
      let [time, amOrPm] = timeString.split(' ');

      // Split hours and minutes
      let [hour, minute] = time.split(':');

      // Convert to 24-hour format
      if (amOrPm === 'PM' && hour !== '12') {
        hour = String(parseInt(hour) + 12);
      }

      // Convert time to UNIX then add to date
      let tempTime = parseInt(hour) * 3600 + parseInt(minute) * 60;
      airingTime = tempTime + date;

    } else if (use24HourFormat === true) { // If airingTime is in 24 hour platform
      let [hour, minute] = timeString.split(':'); // Split time to hour and minute

      // Convert time to UNIX then add to date
      tempTime = parseInt(hour) * 3600 + parseInt(minute) * 60;
      airingTime = tempTime + date;
    }

    // return values
    return airingTime;
  }

  // Function that scrolls down to show cmost recent airing episode
  function scrollDown(){
    let airings = document.querySelectorAll('.bullet-cell .material-icons'); // Get list of airing episodes

    if (airings.length > 0){
      let recentAiring = airings[airings.length - 1]; // Get last one

      if (recentAiring){
        const viewportHeight = window.innerHeight;
        const elementTop = recentAiring.getBoundingClientRect().top;
        const offset = elementTop - (viewportHeight / 2);

        // Find location and then half it from the viewport to make it appear in the middle

        window.scrollBy({ top: offset, behavior: 'smooth' }); // scroll
      }
    }
  }

  // Listeners for the previous and next buttons
  // Changes date and day along with the schedule shown for that day
  if (previous) {
    previous.addEventListener('click', () => {
      currentDate.setDate(currentDate.getDate() - 1);
      dateAndDay();
      fetchDataFromBackground()
        .then(data => {
          handleData(data);
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
    });
  }

  if (next) {
    next.addEventListener('click', () => {
      currentDate.setDate(currentDate.getDate() + 1);
      dateAndDay();
      fetchDataFromBackground()
        .then(data => {
          handleData(data);
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
    });
  }

});

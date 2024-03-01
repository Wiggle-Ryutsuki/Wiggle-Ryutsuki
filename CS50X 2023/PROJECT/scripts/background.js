async function fetchAnimeSchedule(startOfDayTimestamp, endOfDayTimestamp) {
  // Query: get airing time, episode, and title
  const query = `
    query AnimeSchedule($startOfDay: Int, $endOfDay: Int) {
      Page(perPage: 25) {
        pageInfo {
          total
          currentPage
          lastPage
          hasNextPage
          perPage
        }
        airingSchedules(airingAt_greater: $startOfDay, airingAt_lesser: $endOfDay) {
          id
          airingAt
          episode
          media {
            id
            title {
              english
              romaji
            }
          }
        }
      }
    }
  `;

  // Get data ranging from start time to finish time
  const variables = {
    startOfDay: startOfDayTimestamp,
    endOfDay: endOfDayTimestamp
  };

  const url = 'https://graphql.anilist.co';

  const options = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
    },
    body: JSON.stringify({
      query: query,
      variables: variables
    })
  };

  // fetch
  try {
    const response = await fetch(url, options);

    if (!response.ok) {
      throw new Error(`Network response was not ok: ${response.statusText}`);
    }

    return await response.json();
  } catch (error) {
    throw new Error(`Error fetching anime schedule: ${error.message}`);
  }
}

// Receive message from popup.js and send back data
chrome.runtime.onConnect.addListener((port) => {
  port.onMessage.addListener(async (message) => {
    if (message.action === 'fetchData') {
      const { startOfDayTimestamp, endOfDayTimestamp } = message;
      try {
        const data = await fetchAnimeSchedule(startOfDayTimestamp, endOfDayTimestamp);
        port.postMessage({ success: true, data });
      } catch (error) {
        port.postMessage({ success: false, error: error.message });
      }
    }
  });
});


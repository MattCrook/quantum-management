import { useAttractions, useWaitTimes } from "../hooks.js";
import { getAttractionWaitTimes, getAttractions } from "../services.js";


const attractionWaitTimeDataTable = document.getElementById("wait_times");


const populateWaitTimeDataTable = async (parkId) => {
  const [waitTimes, setWaitTimes] = useWaitTimes();
  const [attractions, setAttractions] = useAttractions();
  const getAllWaitTimes = await getAttractionWaitTimes(parkId);
  const allAttractions = await getAttractions(parkId);
  setWaitTimes(getAllWaitTimes);
  setAttractions(allAttractions);

  const waitTimesFromHook = waitTimes();
  const attractionsFromHook = attractions();
  const attractionIds = attractionsFromHook.map((attraction) => attraction.id);
  const matchingWaitTimes = waitTimesFromHook.filter((waitTime) => attractionIds.includes(waitTime.attraction.id));
  const mostRecentWaitTimes = useLatestTimestamp(matchingWaitTimes);
  const waitTimeTableRows = formatDataTable(mostRecentWaitTimes);
  const topTenWaitTimes = [...waitTimeTableRows].splice(0, 10);

  attractionWaitTimeDataTable.innerHTML = "";
  topTenWaitTimes.forEach((row) => {
    attractionWaitTimeDataTable.innerHTML += row;
  });
};



function buildDataTable(name, time) {
    const readableTime = time.split(".")[0];
  return `
      <tr id="wait_time_row">
          <td id="wait_time_name" scope="col">${name}</td>
          <td id="wait_time_time" scope="col">${readableTime}</td>
      </tr>
        `;
};

function formatDataTable(waitTimeArray) {
  let tableRowArray = new Set();
  for (let waittime of waitTimeArray) {
    const name = waittime.attraction.name;
    const time = waittime.current_wait_time;
    const dataTable = buildDataTable(name, time);
    tableRowArray.add(dataTable);
  }
  return tableRowArray;
};


// Function to filter and format the timestamps to their corresponding ride. In an array of an objects which will be pushed into another array of objects.
function filterMultipleTimestampsPerAttraction(waitTimeArray, attractionId) {
  const findDuplicates = waitTimeArray.filter((wait_time) => wait_time.attraction_id === attractionId);
  return findDuplicates;
};


function filterToLatestTimestamp(timestamps) {
  const waitTimeWithLatestTimeStamp = timestamps.map((timestamp) => {
    if (timestamp.length > 1) {
      const sortedTimes = timestamp.sort((a, b) => {
        const timeA = new Date(a.timestamp);
        const timeB = new Date(b.timestamp);
        return timeA - timeB;
      });
      const timesFromRecentToOld = sortedTimes.reverse();
      return timesFromRecentToOld[0];
    } else {
      return timestamp[0];
    }
  });
  return waitTimeWithLatestTimeStamp;
};


function useLatestTimestamp(waitTimeArray) {
  let timestamps = [];
  waitTimeArray.forEach((waittime) => {
    const attractionId = waittime.attraction_id;
    const timestampsForAttraction = filterMultipleTimestampsPerAttraction(waitTimeArray, attractionId);
    timestamps.push(timestampsForAttraction);
  });
  const latestTimeStamps = filterToLatestTimestamp(timestamps);
  return latestTimeStamps;
}


export { populateWaitTimeDataTable };



//   const waitTimeAttractionIds = waitTimesFromHook.map((waitTime) => waitTime.attraction_id);
//   const matchingAttraction = attractionsFromHook.filter((attraction) => waitTimeAttractionIds.includes(attraction.id));

// const filterMultipleTimestampsPerAttraction = (attractionId) => {
//   const removedDuplicateIds = new Set();
//   waitTimeArray.forEach((waittime) => {
//     const attractionId = waittime.attractionId;
//     removedDuplicateIds.add(attractionId);
//   });
//     return removedDuplicateIds;
// };

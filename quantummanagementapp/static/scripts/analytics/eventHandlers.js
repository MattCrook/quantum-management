import { useAttractions, useWaitTimes } from "../hooks.js";
import { getAttractionWaitTimes, getAttractions } from "../services.js";

const attractionWaitTimeTableName = document.getElementById("wait_time_name");
const attractionWaitTimeTableTime = document.getElementById("wait_time_time");
const attractionWaitTimeDataTable = document.getElementById("wait_times");

const buildDataTable = (name, time) => {
  return `
    <tr>
        <td id="wait_time_name">${name}</td>
        <td id="wait_time_time">${time}</td>
    </tr>
      `;
};

const formatDataTable = (waitTimeArray) => {
  let tableRowArray = new Set()
  for (let waittime of waitTimeArray) {
    const name = waittime.attraction.name;
    const time = waittime.current_wait_time;
    const dataTable = buildDataTable(name, time);
    tableRowArray.add(dataTable);
  }
    console.log({tableRowArray})
  return tableRowArray;
};

// Need to check if an attraction is in the array multiple times. (has multiple timestamps)
// Take the most recent timestamp


// Function to filter and format the timestamps to their corresponding ride. In an array of an objects which will be pushed into another array of objects.
const filterMultipleTimestampsPerAttraction = (waitTimeArray, attractionId) => {
    const findDuplicates = waitTimeArray.filter((wait_time) => wait_time.attraction_id === attractionId);
    console.log('findDuplicates', findDuplicates)
  return findDuplicates;
};

const filterToLatestTimestamp = (timestamps) => {
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
  console.log("waitTimeWithLatestTimeStamp", waitTimeWithLatestTimeStamp);
  return waitTimeWithLatestTimeStamp;
};

const useLatestTimestamp = (waitTimeArray) => {
  let timestamps = [];
  waitTimeArray.forEach((waittime) => {
    const timestamp = waittime.timestamp;
    const attractionId = waittime.attraction_id;
    const timestampsForAttraction = filterMultipleTimestampsPerAttraction(waitTimeArray, attractionId);
    timestamps.push(timestampsForAttraction);
  });
  console.log("timestamps", timestamps);
    const latestTimeStamps = filterToLatestTimestamp(timestamps);
    console.log('latestTimeStamps', latestTimeStamps)
    return latestTimeStamps;
};

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
    console.log('attractionIds', attractionIds);

  const matchingWaitTimes = waitTimesFromHook.filter((waitTime) => attractionIds.includes(waitTime.attraction.id));
    console.log('matchingWaitTimes', matchingWaitTimes);
  const mostRecentWaitTimes = useLatestTimestamp(matchingWaitTimes);

  const waitTimeTableRows = formatDataTable(mostRecentWaitTimes);
  attractionWaitTimeDataTable.innerHTML = "";
  waitTimeTableRows.forEach((row) => {
    attractionWaitTimeDataTable.innerHTML += row;
  });
};

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

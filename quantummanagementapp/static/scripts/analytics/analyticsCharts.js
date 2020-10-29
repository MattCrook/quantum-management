import {
  retrieveAttraction,
  getAttractions,
  getParkAttractions,
  getVisitorsList,
  getAttractionWaitTimes,
  getAttractionVisitors,
} from "../services.js";

import { useVisitors, useAttractions, useAttractionVisitorsData } from "../hooks.js";



const buildAttractionVisitorsData = async (parkId) => {
  const [attractions, setAttractions] = useAttractions();
  const [visitors, setVisitors] = useVisitors();
  let attractionAdjacencyList = [];

  const allAttractionsInPark = await getAttractions(parkId);
  setAttractions(allAttractionsInPark);

  const attractionsInPark = attractions();
  const attractionIds = extractAttractionIds(attractionsInPark);

  let visitorsPromises = [];
  attractionIds.forEach((id) => {
    visitorsPromises.push(getAttractionVisitors(id));
  });

  const visitorData = await Promise.all(visitorsPromises);
  setVisitors(visitorData);
  const allVisitors = visitors();

  allVisitors.forEach((arrayOfVisitors) => {
    const whichAttraction = arrayOfVisitors[0].attraction_id;
    const park = findMatchingPark(attractionsInPark, "id", whichAttraction);

    const attractionObject = {
      attractionId: park.id,
      attractionName: park.name,
      visitors: arrayOfVisitors,
      count: arrayOfVisitors.length,
      capacity: park.capacity,
      operatingCapacity: park.current_operating_capacity,
      type: park.type,
      parkId: park.park.id,
      parkName: park.park.name,
    };

    attractionAdjacencyList.push(attractionObject);
  });
  return attractionAdjacencyList;
};

const formatAttractionVisitorsChart = async (parkId) => {
  const [attractionVisitorsData, setAttractionVisitorsData] = useAttractionVisitorsData();

  const initFormattedVisitorData = await buildAttractionVisitorsData(parkId);
  setAttractionVisitorsData([initFormattedVisitorData]);

  const allVisitorData = attractionVisitorsData();
  const visitorsToAttractionCount = extractCountToSort(allVisitorData);
  // const sortedByCountOfVisitors = sortByCount(visitorsToAttractionCount);

  const topTenAttractions = visitorsToAttractionCount.slice(0, 10);

  // Start building the Data Structure to format the data into the format google charts takes.
  const attractionsHeader = topTenAttractions.map((attraction) => attraction.attractionName.toString());
  let matrixHeader = ["Month", ...attractionsHeader, "Monthly Average"];

  // Array of  array of visitors for each attraction
  const visitorsArray = topTenAttractions.map((attraction) => {
    const vis = attraction.visitors;
    return vis;
  });

  // Array of array of months the visitors visited each attraction. In Same order as top 10.
  const topAttrWithMonthsOfVisitors = visitorsArray.map((visitorArr) => {
    let monthsOfTimeStamps = [];
    visitorArr.forEach((visitor) => {
      const timestamp = visitor.visit_timestamp.split("T")[0];
      const month = new Date(timestamp);
      monthsOfTimeStamps.push(month.getMonth());
    });
    return monthsOfTimeStamps;
  });

  const months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];

  const buildMatrixBodyData = buildVisitorsPerMonthArray(topTenAttractions, months);

  const january = buildMatrixRows("January", buildMatrixBodyData[0], totalMonthlyAverage);
  const february = buildMatrixRows("February", buildMatrixBodyData[1], totalMonthlyAverage);
  const march = buildMatrixRows("March", buildMatrixBodyData[2], totalMonthlyAverage);
  const april = buildMatrixRows("April", buildMatrixBodyData[3], totalMonthlyAverage);
  const may = buildMatrixRows("May", buildMatrixBodyData[4], totalMonthlyAverage);
  const june = buildMatrixRows("June", buildMatrixBodyData[5], totalMonthlyAverage);
  const july = buildMatrixRows("July", buildMatrixBodyData[6], totalMonthlyAverage);
  const august = buildMatrixRows("August", buildMatrixBodyData[7], totalMonthlyAverage);
  const september = buildMatrixRows("September", buildMatrixBodyData[8], totalMonthlyAverage);
  const october = buildMatrixRows("October", buildMatrixBodyData[9], totalMonthlyAverage);
  const november = buildMatrixRows("November", buildMatrixBodyData[10], totalMonthlyAverage);
  const december = buildMatrixRows("December", buildMatrixBodyData[11], totalMonthlyAverage);

  const Matrix = [
    [matrixHeader,
      january,
      february,
      march,
      april,
      may,
      june,
      july,
      august,
      september,
      october,
      november,
      december]
  ];
  return Matrix;
};

const drawAttractionVisitorsChart = async (parkId) => {
  const formattedAttractionVisData = await formatAttractionVisitorsChart(parkId);
  const chartData = google.visualization.arrayToDataTable(formattedAttractionVisData[0]);

  const options = {
    title: "Monthly Attraction Popularity",
    vAxis: { title: "Attendance" },
    hAxis: { title: "Month" },
    seriesType: "bars",
    series: {10: { type: "line" } },
  };

  const AttractionAttendanceChart = new google.visualization.ComboChart(document.getElementById("attraction_visitors_chart_div"));
  AttractionAttendanceChart.draw(chartData, options);
};



function buildVisitorsPerMonthArray(attractionArray, months) {
  const attrVisitorsPerMonth = [];
  months.forEach((month) => {
    const matchVisitorsToMonth = mapAttractionVisitorsToMonths(attractionArray, month);
    attrVisitorsPerMonth.push(matchVisitorsToMonth);
  });
  return attrVisitorsPerMonth;
}

function mapAttractionVisitorsToMonths(attractionsArray, month) {
  const intOfVisitorsToAttractionPerMonth = [];
  attractionsArray.forEach((attraction) => {
    const visitorsPerMonth = findVisitersPerMonthForAttraction(attraction, month);
    intOfVisitorsToAttractionPerMonth.push(parseInt(visitorsPerMonth));
  });
  return intOfVisitorsToAttractionPerMonth;
}

function findVisitersPerMonthForAttraction(attraction, month) {
  const visitors = attraction.visitors;
  const attendees = visitors.filter((visitor) => new Date(visitor.visit_timestamp.split("T")[0]).getMonth() === month);
  return attendees.length;
}

function buildMatrixRows(month, matrixBodyData, totalMonthlyAverage) {
  const average = totalMonthlyAverage(1);
  return [month, ...matrixBodyData, average];
}

function totalMonthlyAverage(row) {
  const analyticsMonthlyAverage = row;
  return analyticsMonthlyAverage;
}



function sortByCount(count) {
  const sortedCount = count.sort((a, b) => a - b);
  sortedCount.reverse();
  return sortedCount;
}

function extractCountToSort(arr) {
  const arrayFromHook = arr[0];
  const sortCount = [...arrayFromHook].sort((a, b) => {
    const attractionA = a.count;
    const attractionB = b.count;
    return attractionA - attractionB;
  });
  return sortCount;
}

function extractAttractionIds(attractionArray) {
  const Ids = attractionArray.map((attractionObject) => {
    const attractionId = attractionObject.id;
    return attractionId;
  });
  return Ids;
}

function findMatchingPark(array, keyToFind, valueToFind) {
  for (let item in array) {
    let index = item;
    let value = array[index];
    let parkId = value.id;
    const keys = Object.keys(value);
    const values = Object.values(value);
    if (keys.includes(keyToFind)) {
      if (values.includes(valueToFind) && valueToFind === parkId) {
        return value;
      }
    } else {
      return false;
    }
  }
}

const drawAllCharts = (parkId) => {
  drawAttractionVisitorsChart(parkId);
};

const initAnalytics = (parkId) => {
  google.charts.setOnLoadCallback(drawAllCharts(parkId));
}

export { initAnalytics };

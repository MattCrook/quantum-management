import {
  getAttractions,
  getAttractionVisitors,
} from "../services.js";

import { useVisitors, useAttractions, useAttractionVisitorsData } from "../hooks.js";

const buildAttractionVisitorsData = async (parkId) => {
  const [attractions, setAttractions] = useAttractions();
  const [visitors, setVisitors] = useVisitors();
  let attractionsWithVisitorsObject = [];

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

    attractionsWithVisitorsObject.push(attractionObject);
  });
  return attractionsWithVisitorsObject;
};

const formatAttractionVisitorsChart = async (parkId) => {
  const [attractionVisitorsData, setAttractionVisitorsData] = useAttractionVisitorsData();

  const initFormattedVisitorData = await buildAttractionVisitorsData(parkId);
  setAttractionVisitorsData([initFormattedVisitorData]);

  const allVisitorData = attractionVisitorsData();
  const visitorsToAttractionCount = extractCountToSort(allVisitorData);
  visitorsToAttractionCount.reverse();
  const topTenAttractions = visitorsToAttractionCount.slice(0, 10);

  // Start building the Data Structure to format the data into the format google charts takes.
  const attractionsHeader = topTenAttractions.map((attraction) => attraction.attractionName.toString());
  let matrixHeader = ["Month", ...attractionsHeader, "Total Monthly Average"];
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
    title: "Monthly Attraction Popularity (Top Ten Attractions)",
    vAxis: {
      title: "Attendance",
      textStyle: {
        color: "rgb(0, 0, 0)",
        fontSize: 14
      },
      baselineColor: "rgb(0, 0, 0)",
      titleTextStyle: {
        color: "rgb(0, 0, 0)",
        fontName: "helvetica neue",
        fontSize: 15,
        bold: true,
        italic: true,
      },
    },
    hAxis: {
      title: "Month",
      textStyle: {
        color: "rgb(0, 0, 0)",
        fontSize: 12,
      },
      titleTextStyle: {
        color: "rgb(0, 0, 0)",
        fontName: "helvetica neue",
        fontSize: 15,
        bold: true,
        italic: true,
      },
    },
    seriesType: "bars",
    tooltip: { textStyle: { color: "rgb(17, 19, 24)" }, showColorCode: true },
    series: {
      // 0: {
      //   color: "rgb(226, 8, 8)",
      // },
      // 1: {
      //   color: "#07aed8",
      // },
      // 2: {
      //   color: "rgb(34, 50, 121)",
      // },
      // 3: {
      //   color: "rgb(13, 117, 60)",
      // },
      // 4: {
      //   color: "rgb(224, 94, 18)",
      // },
      // 5: {
      //   color: "rgb(26, 27, 70)",
      // },
      // 6: {
      //   color: "rgb(109, 21, 28)",
      // },
      // 7: {
      //   color: "rgb(106, 5, 201)",
      // },
      // 8: {
      //   color: "rgb(25, 128, 122)",
      // },
      // 9: {
      //   color: "rgb(10, 21, 175)",
      // },
      10: {
        type: "line",
        color: 'rgb(90, 87, 99)',
      },
    },
    backgroundColor: "rgb(255, 254, 254)",
    titleTextStyle: {
      color: "rgb(0, 0, 0)",
      fontName: "helvetica neue",
      fontSize: 17,
      bold: true,
      italic: false,
    },
    legend: {
      textStyle: {
        color: "rgb(0, 0, 0)",
        fontName: "helvetica neue",
        fontSize: 14,
        italic: true,
      },
    },
  };

  const AttractionAttendanceChart = new google.visualization.ComboChart(document.getElementById("attraction_visitors_chart_div"));
  AttractionAttendanceChart.draw(chartData, options);
};

// Takes in array of top 10 attractions in park, and array of all months,
// Iterates the months, and passes the current [i] of months along with
// the array of attractions to [mapAttractionVisitorsToMonths],
// To then iterate the attractions, and match visitors to current [i] of month.
function buildVisitorsPerMonthArray(attractionArray, months) {
  const attrVisitorsPerMonth = [];
  months.forEach((month) => {
    const matchVisitorsToMonth = mapAttractionVisitorsToMonths(attractionArray, month);
    attrVisitorsPerMonth.push(matchVisitorsToMonth);
  });
  return attrVisitorsPerMonth;
}

// Takes in array of top 10 attractions, which is passed from previous function (buildVisitorsPerMonthArray),
// and current iteration of month,
// And iterates the attractions, calling [findVisitersPerMonthForAttraction] with the current [i] of the month,
// and now current [i] of attraction, passing both to match visitors to each attraction per month.
function mapAttractionVisitorsToMonths(attractionsArray, month) {
  const intOfVisitorsToAttractionPerMonth = [];
  attractionsArray.forEach((attraction) => {
    const visitorsPerMonth = findVisitersPerMonthForAttraction(attraction, month);
    intOfVisitorsToAttractionPerMonth.push(parseInt(visitorsPerMonth));
  });
  return intOfVisitorsToAttractionPerMonth;
}

// Takes in the attraction object from previous iteration,
// Looks at array of all visitors to that attraction, looks at timestamps,
// Matches the timestamp to the month which is passed in,
// From previous iteration of looping over months.
// So, this function is taking in two separate [i] from 2 separate loops.
function findVisitersPerMonthForAttraction(attraction, month) {
  const visitors = attraction.visitors;
  const attendees = visitors.filter((visitor) => new Date(visitor.visit_timestamp.split("T")[0]).getMonth() === month);
  return attendees.length;
}

// Matrix Data should be array of 10 items. (Top ten Rides). Should be 12 arrays of 10 items.
// Representing 12 months of top 10 ride attendance.
function buildMatrixRows(month, matrixBodyData, totalMonthlyAverage) {
  const average = totalMonthlyAverage(matrixBodyData);
  return [month, ...matrixBodyData, average];
}

// Average attendance of tall the rides, for the month.
function totalMonthlyAverage(row) {
  const sum = row.reduce((a, b) => a + b);
  const average = sum / 10;
  return average;
}

function extractCountToSort(arr) {
  const arrayFromHook = arr[0];
  const sortCount = arrayFromHook.sort((a, b) => {
    const attractionA = a.count;
    const attractionB = b.count;
    return attractionA - attractionB;
  });
  return sortCount;
};

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

// function sortByCount(count) {
//   const sortedCount = count.sort((a, b) => a - b);
//   sortedCount.reverse();
//   return sortedCount;
// }




const drawAllCharts = (parkId) => {
  drawAttractionVisitorsChart(parkId);
};

const initAnalytics = (parkId) => {
  google.charts.setOnLoadCallback(drawAllCharts(parkId));
};

export { initAnalytics };

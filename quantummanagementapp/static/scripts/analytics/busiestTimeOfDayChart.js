import { getVisitorsList, getVisitorCheckoutList } from "../services.js";

const buildBusiestTimeChart = async (parkId) => {
  const visitors = await getVisitorsList(parkId);
  const visitorCheckout = await getVisitorCheckoutList(parkId);
  const visitorCheckInMonths = visitors.map((visitor) => {
    const timeString = new Date(visitor.check_in);
    const month = timeString.getMonth();
    return month;
  });
  const tableHeader = ["Month", "Visitors"];
  const months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
    let monthsWithVisitors = [];

  months.forEach((m) => {
    const matchingMonths = mapVisitorCheckInToMonth(visitorCheckInMonths, m);
    monthsWithVisitors.push(matchingMonths);
  });

  const row = buildDataRow(monthsWithVisitors);

  const january = buildTableRow("January", row[0]);
  const february = buildTableRow("February", row[1]);
  const march = buildTableRow("March", row[2]);
  const april = buildTableRow("April", row[3]);
  const may = buildTableRow("May", row[4]);
  const june = buildTableRow("June", row[5]);
  const july = buildTableRow("July", row[6]);
  const august = buildTableRow("August", row[7]);
  const september = buildTableRow("September", row[8]);
  const october = buildTableRow("October", row[9]);
  const november = buildTableRow("November", row[10]);
  const december = buildTableRow("December", row[11]);

  const Table = [
      [tableHeader,
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
          december],
  ];
  return Table;
};

const drawBusiestTimeChart = async (parkId) => {
    const visitorMonthsData = await buildBusiestTimeChart(parkId);
    const chartData = google.visualization.arrayToDataTable(visitorMonthsData[0])

    const options = {
      title: 'Monthly Average Park Attendance',
        // curveType: 'function',
        legend: { position: 'bottom' },
        chartArea: { width: '85%', height: '65%' },
        lineWidth: 2,
        series: {
            0: {
                color: "#16426e",
            },
        },
        hAxis: {
            textStyle: {
                color: "rgb(161, 160, 160)",
                fontSize: 11,
                fontName: "helvetica neue",
            },
      },
      vAxis: {
        textStyle: {
            color: "rgb(161, 160, 160)",
            fontSize: 11,
            fontName: "helvetica neue",
        },
    },
        titleTextStyle: {
            color: "rgb(0, 0, 0)",
            fontName: "helvetica neue",
            fontSize: 15,
            bold: true,
            italic: false,
        },
    };
    const monthlyParkVisitorsChart = new google.visualization.LineChart(document.getElementById("curve_chart"));
    monthlyParkVisitorsChart.draw(chartData, options);
};


const initBusiestTimeChart = (parkId) => {
  drawBusiestTimeChart(parkId);
};




function mapVisitorCheckInToMonth(monthsArray, month) {
  const matchingMonth = monthsArray.filter((m) => m === month);
  return matchingMonth;
}

function buildDataRow(monthsWithVisitorsArray) {
  let rows = [];
  monthsWithVisitorsArray.forEach((month) => {
    const numberOfVisitors = month.length;
    rows.push(numberOfVisitors);
  });
  return rows;
}

function buildTableRow(month, dataRow) {
  return [month, dataRow];
}

export { initBusiestTimeChart };

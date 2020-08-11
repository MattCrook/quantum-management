import {
  getParkList,
  getEmployeeList,
  retrieveAttraction,
  getParkAttractions,
  getAttractionType,
  getVisitorsList,
} from "./services.js";

// get all the data I need
// drawResource Function
// Master init function, in HTML that calls the other init functions to kick off everything at once.

const getEmployeeData = async (parkId) => {
  const fetchEmployees = await getEmployeeList();
  const filterEmployees = fetchEmployees.filter((employee) => employee.park_id === parkId);

  let employees = [];
  filterEmployees.forEach((employee) => {
    const employeeRoleObj = {
      name: employee.first_name + " " + employee.last_name,
      role: employee.role,
    };
    employees.push(employeeRoleObj);
  });
  const roles = new Set();
  employees.forEach((employee) => {
    roles.add(employee.role);
  });

  const adjacencyList = new Map();
  roles.forEach((role) => {
    adjacencyList.set(role, []);
  });

  employees.forEach((employee) => {
    let title = employee.role;
    let name = employee.name;
    adjacencyList.get(title).push(name);
  });
  return adjacencyList;
};

const drawEmployeesChart = async (parkId) => {
  const initData = await getEmployeeData(parkId);
  const rows = [];
  initData.forEach(function (key, value) {
    const row = [value, key.length];
    rows.push(row);
  });

  const data = new google.visualization.DataTable();
  data.addColumn("string", "Position/Role");
  data.addColumn("number", "Employees");
  data.addRows(rows);

  // Set chart options
  const options = {
    title: "Employees By Role",
    width: 600,
    height: 600,
  };

  // Instantiate and draw our chart, passing in some options.
  const employeeChart = new google.visualization.PieChart(document.getElementById("employee_chart_div"));
  employeeChart.draw(data, options);
};

// Get all the attractions in a park, display the % make up of attractions by attraction type.
const buildAttractionTypeData = async (parkId) => {
  const fetchAttractions = await getParkAttractions(parkId);
  const buildAttractionObject = fetchAttractions.map((attraction) => {
    const attractionObject = {
      attractionId: attraction.attraction.id,
      parkAttractionId: attraction.id,
      name: attraction.attraction.name,
      type: attraction.attraction.type.name,
      typeId: attraction.attraction.type.id,
    };
    return attractionObject;
  });
  return buildAttractionObject;
};

const formatAttractionTypes = async (parkId) => {
  const filteredData = await buildAttractionTypeData(parkId);
  const types = new Set();
  filteredData.forEach((attraction) => {
    const type = attraction.type;
    types.add(type);
  });
  const typeAdjacencyList = new Map();
  types.forEach((type) => {
    typeAdjacencyList.set(type, []);
  });
  filteredData.forEach((attractionObj) => {
    const typeName = attractionObj.type;
    const attractionName = attractionObj.name;
    typeAdjacencyList.get(typeName).push(attractionName);
  });
  return typeAdjacencyList;
};

const drawAttractionTypeChart = async (parkId) => {
  const initTypeData = await formatAttractionTypes(parkId);
  const rows = [];
  initTypeData.forEach(function (key, value) {
    const row = [value, key.length];
    rows.push(row);
  });

  const typeData = new google.visualization.DataTable();
  typeData.addColumn("string", "Position/Role");
  typeData.addColumn("number", "Employees");
  typeData.addRows(rows);

  // Set chart options
  const options = {
    title: "Attractions by Attraction Type",
    width: 600,
    height: 600,
  };

  const attractionTypeChart = new google.visualization.PieChart(document.getElementById("attraction_type_chart_div"));
  attractionTypeChart.draw(typeData, options);
};

// Get Attendance by month of parks for Bar chart.
// Get all parks, then their daily visitors and separate by month for visualization.
// Get average of all attendance for average line.
const formatAttendanceChart = async () => {
  const parks = await getParkList();
  let visitorsPromises = [];
  parks.forEach((park) => {
    const park_id = park.id;
    visitorsPromises.push(getVisitorsList(park_id));
  });
  const attendanceAdjacencyList = new Map();
  parks.forEach((park) => {
    attendanceAdjacencyList.set(park.name, []);
  });
  const visitorData = await Promise.all(visitorsPromises);
  // visitor data is an array of arrays of objects of visitor objects in each specific park.
  visitorData.forEach((arrayOfVisitors) => {
    // Don't have to loop thru again, only have to check first object in the array for the park_id, bc they are all separated out by park_id already.
    const visitor = arrayOfVisitors[0];
    // check if visitor is not undefined. Bc if it is it throws an error for my Map.
    if (visitor) {
      const visitorParkName = visitor.park.name;
      attendanceAdjacencyList.get(visitorParkName).push(arrayOfVisitors);
    }
  });
  return attendanceAdjacencyList;
};


const buildAttendanceChart = async () => {
  const initAttractionData = await formatAttendanceChart();

  let columnLabels = [];
  // data from each individual park, in its own array, of visitors to that park.
  let parkVisitorsData = [];
  initAttractionData.forEach(function (key, value) {
    const columnLabel = [value];
    const visitorObj = [key];
    columnLabels.push(columnLabel);
    parkVisitorsData.push(visitorObj[0]);
  });
  let extractedParksForHeader = columnLabels.map((label) => label[0].toString());
  let matrixHeader = ["Month", ...extractedParksForHeader, "Monthly Average"];

  let year2019 = [];
  let year2020 = [];
  parkVisitorsData.forEach((parkVisitorArray) => {
    const visitors = parkVisitorArray[0];
    if (visitors) {
      const filter2019 = visitors.filter((attendee) => attendee.check_in.split("T")[0].includes("2019-"));
      year2019.push(filter2019);
      const filter2020 = visitors.filter((attendee) => attendee.check_in.split("T")[0].includes("2020-"));
      year2020.push(filter2020);
    }
  });

  if (parkVisitorsData) {
    const cedarPoint2019 = year2019[0];
    const kingsIsland2019 = year2019[1];
    const canadasWonderland2019 = year2019[2];
    const kingsDomonion2019 = year2019[3];
    const carowinds2019 = year2019[4];
    const knottsBerryFarm2019 = year2019[5];
    const valleyfair2019 = year2019[6];
    const californiasGreatAmerica2019 = year2019[7];

    const cedarPoint2020 = year2020[0];
    const kingsIsland2020 = year2020[1];
    const canadasWonderland2020 = year2020[2];
    const kingsDomonion2020 = year2020[3];
    const carowinds2020 = year2020[4];
    const knottsBerryFarm2020 = year2020[5];
    const valleyfair2020 = year2020[6];
    const californiasGreatAmerica2020 = year2020[7];

    const cpAugust2019 = buildMiddleMatrixRow(cedarPoint2019, "2019-08");
    const cpSeptember2019 = buildMiddleMatrixRow(cedarPoint2019, "2019-09");
    const cpOctober2019 = buildMiddleMatrixRow(cedarPoint2019, "2019-10");
    const cpNovember2019 = buildMiddleMatrixRow(cedarPoint2019, "2019-11");
    const cpDecember2019 = buildMiddleMatrixRow(cedarPoint2019, "2019-12");

    const kiAugust2019 = buildMiddleMatrixRow(kingsIsland2019, "2019-08");
    const kiSeptember2019 = buildMiddleMatrixRow(kingsIsland2019, "2019-09");
    const kiOctober2019 = buildMiddleMatrixRow(kingsIsland2019, "2019-10");
    const kiNovember2019 = buildMiddleMatrixRow(kingsIsland2019, "2019-11");
    const kiDecember2019 = buildMiddleMatrixRow(kingsIsland2019, "2019-12");

    const cwAugust2019 = buildMiddleMatrixRow(canadasWonderland2019, "2019-08");
    const cwSeptember2019 = buildMiddleMatrixRow(canadasWonderland2019, "2019-09");
    const cwOctober2019 = buildMiddleMatrixRow(canadasWonderland2019, "2019-10");
    const cwNovember2019 = buildMiddleMatrixRow(canadasWonderland2019, "2019-11");
    const cwDecember2019 = buildMiddleMatrixRow(canadasWonderland2019, "2019-12");

    const kdAugust2019 = buildMiddleMatrixRow(kingsDomonion2019, "2019-08");
    const kdSeptember2019 = buildMiddleMatrixRow(kingsDomonion2019, "2019-09");
    const kdOctober2019 = buildMiddleMatrixRow(kingsDomonion2019, "2019-10");
    const kdNovember2019 = buildMiddleMatrixRow(kingsDomonion2019, "2019-11");
    const kdDecember2019 = buildMiddleMatrixRow(kingsDomonion2019, "2019-12");

    const caAugust2019 = buildMiddleMatrixRow(carowinds2019, "2019-08");
    const caSeptember2019 = buildMiddleMatrixRow(carowinds2019, "2019-09");
    const caOctober2019 = buildMiddleMatrixRow(carowinds2019, "2019-10");
    const caNovember2019 = buildMiddleMatrixRow(carowinds2019, "2019-11");
    const caDecember2019 = buildMiddleMatrixRow(carowinds2019, "2019-12");

    const kbfAugust2019 = buildMiddleMatrixRow(knottsBerryFarm2019, "2019-08");
    const kbfSeptember2019 = buildMiddleMatrixRow(knottsBerryFarm2019, "2019-09");
    const kbfOctober2019 = buildMiddleMatrixRow(knottsBerryFarm2019, "2019-10");
    const kbfNovember2019 = buildMiddleMatrixRow(knottsBerryFarm2019, "2019-11");
    const kbfDecember2019 = buildMiddleMatrixRow(knottsBerryFarm2019, "2019-12");

    const vfAugust2019 = buildMiddleMatrixRow(valleyfair2019, "2019-08");
    const vfSeptember2019 = buildMiddleMatrixRow(valleyfair2019, "2019-09");
    const vfOctober2019 = buildMiddleMatrixRow(valleyfair2019, "2019-10");
    const vfNovember2019 = buildMiddleMatrixRow(valleyfair2019, "2019-11");
    const vfDecember2019 = buildMiddleMatrixRow(valleyfair2019, "2019-12");

    const cgaAugust2019 = buildMiddleMatrixRow(californiasGreatAmerica2019, "2019-08");
    const cgaSeptember2019 = buildMiddleMatrixRow(californiasGreatAmerica2019, "2019-09");
    const cgaOctober2019 = buildMiddleMatrixRow(californiasGreatAmerica2019, "2019-10");
    const cgaNovember2019 = buildMiddleMatrixRow(californiasGreatAmerica2019, "2019-11");
    const cgaDecember2019 = buildMiddleMatrixRow(californiasGreatAmerica2019, "2019-12");


    const cpJanuary2020 = buildMiddleMatrixRow(cedarPoint2020, "2020-01");
    const cpFebruary2020 = buildMiddleMatrixRow(cedarPoint2020, "2020-02");
    const cpMarch2020 = buildMiddleMatrixRow(cedarPoint2020, "2020-03");
    const cpApril2020 = buildMiddleMatrixRow(cedarPoint2020, "2020-04");
    const cpMay2020 = buildMiddleMatrixRow(cedarPoint2020, "2020-05");
    const cpJune2020 = buildMiddleMatrixRow(cedarPoint2020, "2020-06");
    const cpJuly2020 = buildMiddleMatrixRow(cedarPoint2020, "2020-07");
    const cpAugust2020 = buildMiddleMatrixRow(cedarPoint2020, "2020-08");

    const kiJanuary2020 = buildMiddleMatrixRow(kingsIsland2020, "2020-01");
    const kiFebruary2020 = buildMiddleMatrixRow(kingsIsland2020, "2020-02");
    const kiMarch2020 = buildMiddleMatrixRow(kingsIsland2020, "2020-03");
    const kiApril2020 = buildMiddleMatrixRow(kingsIsland2020, "2020-04");
    const kiMay2020 = buildMiddleMatrixRow(kingsIsland2020, "2020-05");
    const kiJune2020 = buildMiddleMatrixRow(kingsIsland2020, "2020-06");
    const kiJuly2020 = buildMiddleMatrixRow(kingsIsland2020, "2020-07");
    const kiAugust2020 = buildMiddleMatrixRow(kingsIsland2020, "2020-08");

    const cwJanuary2020 = buildMiddleMatrixRow(canadasWonderland2020, "2020-01");
    const cwFebruary2020 = buildMiddleMatrixRow(canadasWonderland2020, "2020-02");
    const cwMarch2020 = buildMiddleMatrixRow(canadasWonderland2020, "2020-03");
    const cwApril2020 = buildMiddleMatrixRow(canadasWonderland2020, "2020-04");
    const cwMay2020 = buildMiddleMatrixRow(canadasWonderland2020, "2020-05");
    const cwJune2020 = buildMiddleMatrixRow(canadasWonderland2020, "2020-06");
    const cwJuly2020 = buildMiddleMatrixRow(canadasWonderland2020, "2020-07");
    const cwAugust2020 = buildMiddleMatrixRow(canadasWonderland2020, "2020-08");

    const kdJanuary2020 = buildMiddleMatrixRow(kingsDomonion2020, "2020-01");
    const kdFebruary2020 = buildMiddleMatrixRow(kingsDomonion2020, "2020-02");
    const kdMarch2020 = buildMiddleMatrixRow(kingsDomonion2020, "2020-03");
    const kdApril2020 = buildMiddleMatrixRow(kingsDomonion2020, "2020-04");
    const kdMay2020 = buildMiddleMatrixRow(kingsDomonion2020, "2020-05");
    const kdJune2020 = buildMiddleMatrixRow(kingsDomonion2020, "2020-06");
    const kdJuly2020 = buildMiddleMatrixRow(kingsDomonion2020, "2020-07");
    const kdAugust2020 = buildMiddleMatrixRow(kingsDomonion2020, "2020-08");

    const caJanuary2020 = buildMiddleMatrixRow(carowinds2020, "2020-01");
    const caFebruary2020 = buildMiddleMatrixRow(carowinds2020, "2020-02");
    const caMarch2020 = buildMiddleMatrixRow(carowinds2020, "2020-03");
    const caApril2020 = buildMiddleMatrixRow(carowinds2020, "2020-04");
    const caMay2020 = buildMiddleMatrixRow(carowinds2020, "2020-05");
    const caJune2020 = buildMiddleMatrixRow(carowinds2020, "2020-06");
    const caJuly2020 = buildMiddleMatrixRow(carowinds2020, "2020-07");
    const caAugust2020 = buildMiddleMatrixRow(carowinds2020, "2020-08");

    const kbfJanuary2020 = buildMiddleMatrixRow(knottsBerryFarm2020, "2020-01");
    const kbfFebruary2020 = buildMiddleMatrixRow(knottsBerryFarm2020, "2020-02");
    const kbfMarch2020 = buildMiddleMatrixRow(knottsBerryFarm2020, "2020-03");
    const kbfApril2020 = buildMiddleMatrixRow(knottsBerryFarm2020, "2020-04");
    const kbfMay2020 = buildMiddleMatrixRow(knottsBerryFarm2020, "2020-05");
    const kbfJune2020 = buildMiddleMatrixRow(knottsBerryFarm2020, "2020-06");
    const kbfJuly2020 = buildMiddleMatrixRow(knottsBerryFarm2020, "2020-07");
    const kbfAugust2020 = buildMiddleMatrixRow(knottsBerryFarm2020, "2020-08");

    const vfJanuary2020 = buildMiddleMatrixRow(valleyfair2020, "2020-01");
    const vfFebruary2020 = buildMiddleMatrixRow(valleyfair2020, "2020-02");
    const vfMarch2020 = buildMiddleMatrixRow(valleyfair2020, "2020-03");
    const vfApril2020 = buildMiddleMatrixRow(valleyfair2020, "2020-04");
    const vfMay2020 = buildMiddleMatrixRow(valleyfair2020, "2020-05");
    const vfJune2020 = buildMiddleMatrixRow(valleyfair2020, "2020-06");
    const vfJuly2020 = buildMiddleMatrixRow(valleyfair2020, "2020-07");
    const vfAugust2020 = buildMiddleMatrixRow(valleyfair2020, "2020-08");

    const cgaJanuary2020 = buildMiddleMatrixRow(californiasGreatAmerica2020, "2020-01");
    const cgaFebruary2020 = buildMiddleMatrixRow(californiasGreatAmerica2020, "2020-02");
    const cgaMarch2020 = buildMiddleMatrixRow(californiasGreatAmerica2020, "2020-03");
    const cgaApril2020 = buildMiddleMatrixRow(californiasGreatAmerica2020, "2020-04");
    const cgaMay2020 = buildMiddleMatrixRow(californiasGreatAmerica2020, "2020-05");
    const cgaJune2020 = buildMiddleMatrixRow(californiasGreatAmerica2020, "2020-06");
    const cgaJuly2020 = buildMiddleMatrixRow(californiasGreatAmerica2020, "2020-07");
    const cgaAugust2020 = buildMiddleMatrixRow(californiasGreatAmerica2020, "2020-08");


    const rowAug2019 = buildMatrixRow("August", cpAugust2019, kiAugust2019, cwAugust2019, kdAugust2019, caAugust2019, kbfAugust2019, vfAugust2019, cgaAugust2019, totalAverage);
    const rowSept2019 = buildMatrixRow("September", cpSeptember2019, kiSeptember2019, cwSeptember2019, kdSeptember2019, caSeptember2019, kbfSeptember2019, vfSeptember2019, cgaSeptember2019, totalAverage)
    const rowOct2019 = buildMatrixRow("October", cpOctober2019, kiOctober2019, cwOctober2019, kdOctober2019, caOctober2019, kbfOctober2019, vfOctober2019, cgaOctober2019, totalAverage)
    const rowNov2019 = buildMatrixRow("November", cpNovember2019, kiNovember2019, cwNovember2019, kdNovember2019, caNovember2019, kbfNovember2019, vfNovember2019, cgaNovember2019, totalAverage)
    const rowDec2019 = buildMatrixRow("December", cpDecember2019, kiDecember2019, cwDecember2019, kdDecember2019, caDecember2019, kbfDecember2019, vfDecember2019, cgaDecember2019, totalAverage)

    const rowJan2020 = buildMatrixRow("January", cpJanuary2020, kiJanuary2020, cwJanuary2020, kdJanuary2020, caJanuary2020, kbfJanuary2020, vfJanuary2020, cgaJanuary2020, totalAverage)
    const rowFeb2020 = buildMatrixRow("February", cpFebruary2020, kiFebruary2020, cwFebruary2020, kdFebruary2020, caFebruary2020, kbfFebruary2020, vfFebruary2020, cgaFebruary2020, totalAverage)
    const rowMarch2020 = buildMatrixRow("March", cpMarch2020, kiMarch2020, cwMarch2020, kdMarch2020, caMarch2020, kbfMarch2020, vfMarch2020, cgaMarch2020, totalAverage)
    const rowApril2020 = buildMatrixRow("April", cpApril2020, kiApril2020, cwApril2020, kdApril2020, caApril2020, kbfApril2020, vfApril2020, cgaApril2020, totalAverage)
    const rowMay2020 = buildMatrixRow("May", cpMay2020, kiMay2020, cwMay2020, kdMay2020, caMay2020, kbfMay2020, vfMay2020, cgaMay2020, totalAverage)
    const rowJune2020 = buildMatrixRow("June", cpJune2020, kiJune2020, cwJune2020, kdJune2020, caJune2020, kbfJune2020, vfJune2020, cgaJune2020, totalAverage)
    const rowJuly2020 = buildMatrixRow("Juy", cpJuly2020, kiJuly2020, cwJuly2020, kdJuly2020, caJuly2020, kbfJuly2020, vfJuly2020, cgaJuly2020, totalAverage)
    const rowAug2020 = buildMatrixRow("August", cpAugust2020, kiAugust2020, cwAugust2020, kdAugust2020, caAugust2020, kbfAugust2020, vfAugust2020, cgaAugust2020, totalAverage)

    const Matrix = [
      [matrixHeader,
      rowAug2019,
      rowSept2019,
      rowOct2019,
      rowNov2019,
        rowDec2019],
      [matrixHeader,
      rowJan2020,
      rowFeb2020,
      rowMarch2020,
      rowApril2020,
      rowMay2020,
      rowJune2020,
      rowJuly2020,
      rowAug2020]
    ]
    return Matrix;
  }
};


function buildMiddleMatrixRow(park, monthYear) {
  const attendees = park.filter((visitor) => visitor.check_in.split("T")[0].includes(monthYear));
  return attendees.length;
}

function buildMatrixRow(month, cp, ki, cw, kd, ca, kbf, vf, cga, totalAverage) {
  const average = totalAverage(cp, ki, cw, kd, ca, kbf, vf, cga)
  return [month, cp, ki, cw, kd, ca, kbf, vf, cga, average];
}


function totalAverage(cp, ki, cw, kd, ca, kbf, vf, cga) {
  const sum = cp + ki + cw + kd + ca + kbf + vf + cga;
  const average = sum / 8;
  return average;
}

const drawAttendanceCharts = async () => {
  const attendanceData = await buildAttendanceChart();
  const Matrix2019 = attendanceData[0];
  const Matrix2020 = attendanceData[1];
  const data2019 = google.visualization.arrayToDataTable(Matrix2019);
  const data2020 = google.visualization.arrayToDataTable(Matrix2020);


  const options2019 = {
    title: "Monthly Attendance 2019",
    vAxis: { title: "Attendance" },
    hAxis: { title: "Month" },
    seriesType: "bars",
    series: { 8: { type: "line" } },
  };

  const options2020 = {
    title: "Monthly Attendance 2020",
    vAxis: { title: "Attendance" },
    hAxis: { title: "Month" },
    seriesType: "bars",
    series: { 8: { type: "line" } },
  };

  const attendanceChart2019 = new google.visualization.ComboChart(document.getElementById("2019_attendance_comboChart"));
  attendanceChart2019.draw(data2019, options2019);

  const attendanceChart2020 = new google.visualization.ComboChart(document.getElementById("2020_attendance_comboChart"));
  attendanceChart2020.draw(data2020, options2020)
};





const drawAllCharts = (parkId) => {
  drawEmployeesChart(parkId);
  drawAttractionTypeChart(parkId);
  drawAttendanceCharts();
};

const init = (parkId) => {
  google.charts.setOnLoadCallback(drawAllCharts(parkId));
};

export { init };

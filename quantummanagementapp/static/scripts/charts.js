import { getParkList, getEmployeeList, retrieveAttraction, getParkAttractions } from "./services.js";

// get all the data I need
// drawResource Function
// Master init function, in HTML that calls the other init functions to kick off everything at once.

const drawPark = () => {};

export const getEmployeeData = async (parkId) => {
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

export const drawEmployeesChart = async (parkId) => {
  const initData = await getEmployeeData(parkId);
  const rows = [];
  initData.forEach(function (key, value) {
    const row = [value, key.length];
    rows.push(row)
  });

  const data = new google.visualization.DataTable();
  data.addColumn("string", "Position/Role");
  data.addColumn("number", "Employees");
  console.log(rows)
  data.addRows(rows);

  // Set chart options
  const options = {
    title: "Employees By Role",
    width: 600,
    height: 500,
  };

  // Instantiate and draw our chart, passing in some options.
  const employeeChart = new google.visualization.PieChart(document.getElementById("employee_chart_div"));
  employeeChart.draw(data, options);
};



// get all the attractions in a park, display the % make up of attractions by attraction type.
const getAttractionTypeData = async (parkId) => {
  const fetchAttractions = await getParkAttractions();
  const filterByPark = fetchAttractions.filter((attraction) => attraction.park_id === parkId);
  const attractionIds = filterByPark.map((attraction) => attraction.attraction_id);
  const retrieveAttractionById = attractionIds.map(async (id) => {
    const getAttraction = await retrieveAttraction(id);
    console.log(getAttraction);
  });
  return retrieveAttractionById;
};

const drawAllCharts = (parkId) => {
  drawEmployeesChart(parkId)
};


const init = (parkId) => {
  google.charts.setOnLoadCallback(drawAllCharts(parkId));
};



export { init }

import { getParkList, getEmployeeList, retrieveAttraction, getParkAttractions, getAttractionType } from "./services.js";

// get all the data I need
// drawResource Function
// Master init function, in HTML that calls the other init functions to kick off everything at once.

const drawPark = () => {};

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
    height: 500,
  };

  // Instantiate and draw our chart, passing in some options.
  const employeeChart = new google.visualization.PieChart(document.getElementById("employee_chart_div"));
  employeeChart.draw(data, options);
};

// get all the attractions in a park, display the % make up of attractions by attraction type.

// const setAttractions = (attractionsArray) => attractions = attractionsArray;
// function useAttractions() {
//   let attractions = [];
//   return [() => attractions, (newState) => (attractions = newState)];
// }

// const [attractions, setAttractions] = useAttractions();

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
  const typeAdjList = new Map();
  types.forEach((type) => {
    typeAdjList.set(type, []);
  });
  filteredData.forEach((attractionObj) => {
    const typeName = attractionObj.type;
    const attractionName = attractionObj.name;
    typeAdjList.get(typeName).push(attractionName);
  });
  return typeAdjList;
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
    height: 500,
  };

  // Instantiate and draw our chart, passing in some options.
  const attractionTypeChart = new google.visualization.PieChart(document.getElementById("attraction_type_chart_div"));
  attractionTypeChart.draw(typeData, options);
};

const drawAllCharts = (parkId) => {
  drawEmployeesChart(parkId);
  drawAttractionTypeChart(parkId)
};

const init = (parkId) => {
  google.charts.setOnLoadCallback(drawAllCharts(parkId));
};

export { init };

  
  
  
  
  
  
  
  
  
  
  
  
  
// const setAttractions = (attractionsArray) => attractions = attractionsArray;
// function useAttractions() {
//   let attractions = [];
//   return [() => attractions, (newState) => (attractions = newState)];
// }

// const [attractions, setAttractions] = useAttractions();

// get all the attractions in a park, display the % make up of attractions by attraction type.

// const setAttractions = (attractionsArray) => attractions = attractionsArray;
// function useAttractions() {
//   let attractions = [];
//   return [() => attractions, (newState) => (attractions = newState)];
// }

// const [attractions, setAttractions] = useAttractions();

// let attractionsArr = [];
// let attractionTypes = [];

// const attractionTypeData = async (parkId) => {
//   const fetchAttractions = await getParkAttractions(parkId);
//   const buildAttractionObject = fetchAttractions.map(attraction => {
//     const attractionObject = {
//       id: attraction.attraction.id,
//       parkAttractionId: attraction.id,
//       name: attraction.attraction.name,
//       type: attraction.attraction.type.name,
//       typeId: attraction.attraction.type.id
//     };
//     return attractionObject;
//   });
//   return buildAttractionObject;
//   }

//   const attractionIds = fetchAttractions.map((attraction) => attraction.attraction_id);
//   let promises = [];
//   attractionIds.forEach((id) => {
//     promises.push(retrieveAttraction(id));
//   });
//   const executePromises = Promise.all(promises).then((attractions) => {
//     const mapAttractions = attractions.map(attraction => {
//       const typeId = attraction.type_id;
//       return typeId;
//     })
//     return mapAttractions;
//   });
//   return executePromises;
// };

// const filterAttractionTypeData = async (parkId) => {
//   const typeIds = await attractionTypeData(parkId);
//   let promises = [];
//   typeIds.forEach(id => {
//     promises.push(getAttractionType(id));
//   })
//   let typeSet = new Set();
//   Promise.all(promises).then(types => {
//     types.map(type => {
//       const name = type.name;
//       typeSet.add(name)
//     })
//   })
//   return typeSet;
// };

// const formatAttractionTypes = async (parkId) => {
//   const filteredData = await filterAttractionTypeData(parkId);
//   const typeAdjList = new Map();
//   filteredData.forEach(type => {
//     typeAdjList.set(type, []);
//   });
//   const fetchParkAttractions = await getParkAttractions(parkId);
//   console.log(fetchParkAttractions)
//   fetchParkAttractions.forEach(attraction => {
//     const type = attraction.attraction.type.name
//     console.log("TYPE", type)
//     const name = attraction.attraction.name;
//     console.log("NAME", name)

//   })
// }

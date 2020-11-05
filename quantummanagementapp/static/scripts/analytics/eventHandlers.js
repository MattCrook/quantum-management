// const attractionsButton = document.getElementById("attr_btn");
// const waitTimesButton = document.getElementById("waitTimesButton");

// const waitTimesContainer = document.getElementById("wait_time_table_container");
// const attractionVisitorsChartContainer = document.getElementById("attraction_visitors_chart_container");
// const parkAttendanceContainer = document.querySelector(".container_2_charts");

var attractionVisitorsChartContainer = document.getElementById("attraction_visitors_chart_div");
var parkAttendanceContainer = document.getElementById("curve_chart");
var waitTimesContainer = document.getElementById("wait_time_table_container");

parkAttendanceContainer.style.display = "none";
waitTimesContainer.style.display = "none";

// const toggleParkAttendance = () => {
//     const parkAttendanceButton = document.getElementById("park_attendance_btn");

//     parkAttendanceButton.addEventListener("click", () => {
//         parkAttendanceContainer.style.display = "block";
//         attractionVisitorsChartContainer.style.display = "none";
//         waitTimesContainer.style.display = "none";
//     })
// }

// const toggleAttractionsByMonth = () => {
//     const attractionsButton = document.getElementById("attr_btn");

//     attractionsButton.addEventListener("click", () => {
//         attractionVisitorsChartContainer.style.display = 'block';
//         parkAttendanceContainer.style.display = "none";
//         waitTimesContainer.style.display = "none";

//     })
// }

// const toggleWaitTimes = () => {
//     const waitTimesButton = document.getElementById("ride_wait_time_btn");

//     waitTimesButton.addEventListener("click", () => {
//         attractionVisitorsChartContainer.style.display = 'none';
//         parkAttendanceContainer.style.display = "none";
//         waitTimesContainer.style.display = "block";

//     })
// }

// toggleParkAttendance();
// toggleAttractionsByMonth()
// toggleWaitTimes()

const openDropdown = () => {
  const selectYearOptions = document.querySelector(".select_year_options");
  const selectYearButton = document.querySelector(".year_select_label");
  selectYearButton.addEventListener("click", () => {
    const display = selectYearOptions.style.display;
    display === "none" ? (selectYearOptions.style.display = "block") : (selectYearOptions.style.display = "none");
  });
};

const showDropdownAttractions = () => {
  const attractionsButton = document.getElementById("attr_btn");
  const selectYearContainer = document.querySelector(".select_year_container");
  const chartTitlesContainer = document.querySelector(".chart_titles_container");
  const attractionVisitorChartContainer = document.getElementById("attraction_visitors_chart_container");
  const chartTitles = document.querySelector(".chart_titles_container");
  const chartTitlesAttendance = document.querySelector(".chart_titles_attendance_container");
  const waitTimeTitles = document.querySelector(".chart_titles_waittimes_container");

  attractionsButton.addEventListener("click", () => {
    selectYearContainer.style.display = "block";
    chartTitlesContainer.style.display = "block";
    attractionVisitorChartContainer.style.border = "1px solid rgb(189, 189, 189)";
    chartTitlesAttendance.style.display = "none";
    waitTimeTitles.style.display = "none";
    chartTitles.style.display = "block";
  });
};

const showDropdownParkAttendance = () => {
  const parkAttendanceButton = document.getElementById("park_attendance_btn");
  const selectYearContainer = document.querySelector(".select_year_container");
  const chartTitlesContainer = document.querySelector(".chart_titles_container");
  const attractionVisitorChartContainer = document.getElementById("attraction_visitors_chart_container");
  const chartTitlesAttendance = document.querySelector(".chart_titles_attendance_container");
  const chartTitlesAttrVisitors = document.querySelector(".chart_titles_container");
  const waitTimeTitles = document.querySelector(".chart_titles_waittimes_container");

  parkAttendanceButton.addEventListener("click", () => {
    selectYearContainer.style.display = "block";
    chartTitlesContainer.style.display = "block";
    attractionVisitorChartContainer.style.border = "1px solid rgb(189, 189, 189)";
    chartTitlesAttrVisitors.style.display = "none";
    waitTimeTitles.style.display = "none";
    chartTitlesAttendance.style.display = "block";
  });
};

const hideDropdownsAndShowWaitTimeTitles = () => {
  const waitTimesButton = document.getElementById("ride_wait_time_btn");
  const selectYearContainer = document.querySelector(".select_year_container");
  const chartTitlesContainer = document.querySelector(".chart_titles_container");
  const chartTitlesAttendance = document.querySelector(".chart_titles_attendance_container");
  const attractionVisitorChartContainer = document.getElementById("attraction_visitors_chart_container");
  const waitTimeTitles = document.querySelector(".chart_titles_waittimes_container");

  waitTimesButton.addEventListener("click", () => {
    selectYearContainer.style.display = "none";
    chartTitlesContainer.style.display = "none";
    attractionVisitorChartContainer.style.border = "none";
    chartTitlesAttendance.style.display = "none";
    waitTimeTitles.style.display = "block";
  });
};

const initEvenHandlers = () => {
  openDropdown();
  showDropdownAttractions();
  showDropdownParkAttendance();
  hideDropdownsAndShowWaitTimeTitles();
};

initEvenHandlers();

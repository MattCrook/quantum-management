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

const initEvenHandlers = () => {
  openDropdown();
};

initEvenHandlers();

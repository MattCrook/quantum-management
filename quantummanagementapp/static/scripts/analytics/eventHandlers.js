import { getAttractionVisitors, getAttractions } from "../services.js";

var parkAttendanceContainer = document.getElementById("curve_chart");
var waitTimesContainer = document.getElementById("wait_time_table_container");

parkAttendanceContainer.style.display = "none";
waitTimesContainer.style.display = "none";

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

const getYearsForDropdownData = async (parkId) => {
  try {
    const attractions = await getAttractions(parkId);
    let promises = [];
    const attractionIds = attractions.map((attraction) => {
      const id = attraction.id;
      return id;
    });
    attractionIds.forEach((id) => {
      promises.push(getAttractionVisitors(id));
    });
    const all_attraction_visitors = await Promise.all(promises);

    const timestamps = [];
    const timestamp_local_strings = [];
    const month_numbers = [];
    const month_names = [];
    const monthNames = new Set();
    const all_years = [];
    const years = new Set();
    all_attraction_visitors.forEach((attraction_array) => {
      attraction_array.forEach((attraction) => {
        const datetime = attraction.visit_timestamp;
        timestamps.push(datetime);

        const readable_datetime = new Date(datetime);
        const timestamp = readable_datetime.getMonth();
        month_numbers.push(timestamp);

        const localStrings = readable_datetime.toLocaleString();
        timestamp_local_strings.push(localStrings);

        const datetimeLocalString = new Date(datetime).toLocaleString("default", { month: "long" });
        month_names.push(datetimeLocalString);
        monthNames.add(datetimeLocalString);

        const yearLocalString = new Date(datetime).toLocaleString("default", { year: "numeric" });
        all_years.push(yearLocalString);
        years.add(yearLocalString);
      });
    });

    const data = {
      timestamps: timestamps,
      localStrings: timestamp_local_strings,
      monthNames: month_names,
      monthNumbers: month_numbers,
      monthNameSet: monthNames,
      allYears: all_years,
      years: years,
    };
    return data;
  } catch (err) {
    console.log({ err });
  }
};

const populateYearsDropdown = async (parkId) => {
  try {
    const dateData = await getYearsForDropdownData(parkId);
    const yearsWithData = dateData.years;
    const years = [...yearsWithData];
    const yearOption = document.getElementById("dynamic_years_with_data");
    yearOption.innerHTML = "";
    years.forEach((year) => {
      const option = renderYearOption(year);
      yearOption.innerHTML += option;
    });
  } catch (err) {
    console.log({ err });
  }
};

function renderYearOption(year) {
  return `
  <div class="year_option">${year}</div>
  `;
}

const initEvenHandlers = () => {
  openDropdown();
  showDropdownAttractions();
  showDropdownParkAttendance();
  hideDropdownsAndShowWaitTimeTitles();
};

initEvenHandlers();

export { populateYearsDropdown };

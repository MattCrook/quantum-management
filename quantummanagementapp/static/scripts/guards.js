const isSalary = document.getElementById("is_salary");
const isHourly = document.getElementById("is_hourly");
const startDate = document.getElementById("start_date");
const updateEmployeeButton = document.getElementById("update_employee_btn");

if (updateEmployeeButton && isHourly && isSalary) {
    console.log("called")
  updateEmployeeButton.addEventListener("click", () => {
    if (isSalary === "" || isHourly === "") {
      window.alert("Please select a pay rate.");
    }
  });
}

if (updateEmployeeButton) {
    updateEmployeeButton.addEventListener("click", () => {
      console.log("updatebtnclick")
    if (startDate === "") {
      window.alert("Please select a start date.");
    }
  });
}

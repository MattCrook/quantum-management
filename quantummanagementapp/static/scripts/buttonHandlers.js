const deleteEmployeeButton = document.querySelector(".employee_detail_delete_btn");
if (deleteEmployeeButton) {
    deleteEmployeeButton.addEventListener("click", () => {
        window.alert("Are you sure you want to delete this employee?");
    });
};

const createNewParkButton = document.getElementById("create_park_btn");
if (createNewParkButton) {
    createNewParkButton.addEventListener("click", () => {
        window.alert("Click OK to confirm creation of New Theme Park.")
    });
};

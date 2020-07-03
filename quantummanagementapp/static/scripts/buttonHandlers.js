const deleteEmployeeButton = document.querySelector(".employee_detail_delete_btn");
if (deleteEmployeeButton) {
  deleteEmployeeButton.addEventListener("click", () => {
    window.confirm("Are you sure you want to delete this employee?");
  });
}

const createNewParkButton = document.getElementById("create_park_btn");
if (createNewParkButton) {
  createNewParkButton.addEventListener("click", () => {
    window.confirm("Click OK to confirm creation of New Theme Park.");
  });
}

const deleteParkButton = document.querySelectorAll(".delete_park_btn");
if (deleteParkButton) {
  deleteParkButton.forEach((deleteButton) => {
    deleteButton.addEventListener("click", () => {
      window.confirm("Click OK to confirm deletion of this park");
    });
  });
}

// const editParkButton = document.querySelectorAll(".park_edit_btn");
// if (editParkButton) {
//   editParkButton.forEach((editButton) => {
//     editButton.addEventListener("click", () => {
//       window.alert("clicked");
//     });
//   });
// }

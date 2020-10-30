const createNoneAssigned = () => {
  return `
    <div class="employee_on_ride_list_title">
    <li class="park_detail_list_item_btn">None currently assigned</li>
    </div>
    `;
};

const renderEntry = (htmlTemplate) => {
  const renderContainer = document.querySelector(".render_if_none_container");
  renderContainer.innerHTML += htmlTemplate;
};

// const analyticsBtn = document.getElementById("analytics");
// function analyticsListener(element) {
//   element.addEventListener("click", (e) => {
//     const origin = window.location.origin;
//     const path = window.location.pathname;
//     const parkId = path.split("/")[2];
//     window.location.href = origin + `/parks/${parkId}/analytics`;
//   });
// };

// analyticsListener(analyticsBtn);

// const checkForList = () => {
//     let parkAttractionsListContainer = document.querySelectorAll(".park_attractions_container");
//     let employee_on_ride_list_title = document.querySelector(".employee_on_ride_list_title");

//   for (let i = 0; i < parkAttractionsListContainer.length; i++) {
//       let element = parkAttractionsListContainer[i];
//       console.log(element)
//     //   let node = element.contains(employee_on_ride_list_title)
//     //   console.log(node)
//     if (!element.contains(employee_on_ride_list_title)) {
//       console.log("not have it");
//       renderEntry(createNoneAssigned());
//     }
//   }
// };

// document.onload = checkForList()
